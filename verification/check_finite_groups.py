#!/usr/bin/env python3
"""Finite group/gauge/compiler checks and floating channel diagnostics.

Run from any directory: python verification/check_finite_groups.py
The JSON report is reproducible. Exact permutation equalities are exhaustive on
the stated finite instances; floating diagnostics are not diamond certificates
or proofs of the infinite-family escape exponent.
"""

from __future__ import annotations

import collections
import itertools
import json
import math
from fractions import Fraction

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import expm_multiply
from scipy.stats import poisson


class Cyclic:
    def __init__(self, order: int):
        self.order = order
        self.name = f"C{order}"
        self.states = list(range(order))
        self.identity = 0
        self.generators = [1, order - 1]
        self.inverse_labels = [1, 0]

    def mul(self, a, b):
        return (a + b) % self.order

    def defining_relations(self, supplied):
        unit = np.arange(len(supplied[0]))
        assert np.array_equal(power(supplied[0], self.order), unit)
        return 1


class Dihedral:
    def __init__(self, rotation_order: int):
        self.rotation_order = rotation_order
        self.name = f"D{rotation_order} (order {2 * rotation_order})"
        self.states = list(itertools.product(range(rotation_order), range(2)))
        self.identity = (0, 0)
        self.generators = [(1, 0), (rotation_order - 1, 0), (0, 1)]
        self.inverse_labels = [1, 0, 2]

    def mul(self, a, b):
        r, f = a
        s, h = b
        return ((r + (-1 if f else 1) * s) % self.rotation_order, f ^ h)

    def defining_relations(self, supplied):
        unit = np.arange(len(supplied[0]))
        r, rinv, flip = supplied
        assert np.array_equal(power(r, self.rotation_order), unit)
        assert np.array_equal(compose(flip, flip), unit)
        assert np.array_equal(compose(flip, compose(r, flip)), rinv)
        return 3


class Wreath:
    def __init__(self, lamp_order: int, cycle_length: int):
        self.M, self.L = lamp_order, cycle_length
        self.name = f"C{lamp_order} wr C{cycle_length}"
        zero = (0,) * self.L
        one = (1,) + (0,) * (self.L - 1)
        minus = (self.M - 1,) + (0,) * (self.L - 1)
        self.states = [(p, a) for p in range(self.L)
                       for a in itertools.product(range(self.M), repeat=self.L)]
        self.identity = (0, zero)
        self.generators = [(1, zero), (self.L - 1, zero), (0, one), (0, minus)]
        self.inverse_labels = [1, 0, 3, 2]

    def mul(self, a, b):
        p, eta = a
        q, xi = b
        return ((p + q) % self.L,
                tuple((eta[j] + xi[(j - p) % self.L]) % self.M
                      for j in range(self.L)))

    def defining_relations(self, supplied):
        unit = np.arange(len(supplied[0]))
        shift, shiftinv, lamp, _ = supplied
        assert np.array_equal(power(shift, self.L), unit)
        assert np.array_equal(power(lamp, self.M), unit)
        translated = [compose(power(shift, j), compose(lamp, power(shiftinv, j)))
                      for j in range(self.L)]
        for a in translated:
            for b in translated:
                assert np.array_equal(compose(a, b), compose(b, a))
        return 2 + self.L * self.L

    def cycle_word(self, endpoint):
        """Exact geodesic, independently checked against BFS below.

        Word labels are multiplied algebraically from left to right. This is a
        right-multiplication cursor construction, not the left regular action.
        """
        final, lamps = endpoint
        required = {0, final} | {j for j, a in enumerate(lamps) if a}
        candidates = []
        for cut in range(self.L):
            origin = (cut + 1) % self.L
            coordinates = {j: (j - origin) % self.L for j in required}
            start, end = coordinates[0], coordinates[final]
            low, high = min(coordinates.values()), max(coordinates.values())
            for waypoints in ((low, high, end), (high, low, end)):
                route = [0]
                pos = start
                for target in waypoints:
                    step = 1 if target > pos else -1
                    while pos != target:
                        pos += step
                        route.append((origin + pos) % self.L)
                candidates.append(route)
        route = [j % self.L for j in range(self.L + 1)]
        direction = 1 if final <= self.L / 2 else -1
        pos = 0
        while pos != final:
            pos = (pos + direction) % self.L
            route.append(pos)
        candidates.append(route)
        route = min(candidates, key=len)
        word, visited = [], set()

        def set_lamp(pos):
            if pos in visited:
                return
            visited.add(pos)
            amount = lamps[pos]
            signed = amount if amount <= self.M / 2 else amount - self.M
            word.extend([2 if signed >= 0 else 3] * abs(signed))

        set_lamp(0)
        for before, after in zip(route, route[1:]):
            assert (after - before) % self.L in (1, self.L - 1)
            word.append(0 if (after - before) % self.L == 1 else 1)
            set_lamp(after)
        reached = self.identity
        for label in word:
            reached = self.mul(reached, self.generators[label])
        assert reached == endpoint
        return word


def compose(a, b):
    """Permutation matrices A B act as a[b[i]]."""
    return a[b]


def power(a, exponent):
    result = np.arange(len(a))
    for _ in range(exponent):
        result = a[result]
    return result


def bfs(group):
    distance = {group.identity: 0}
    queue = collections.deque([group.identity])
    while queue:
        g = queue.popleft()
        for s in group.generators:
            h = group.mul(s, g)
            if h not in distance:
                distance[h] = distance[g] + 1
                queue.append(h)
    assert len(distance) == len(group.states)
    return distance


def sparse_permutation(permutation):
    n = len(permutation)
    return sparse.csr_matrix((np.ones(n), (permutation, np.arange(n))), shape=(n, n))


def dyadic_round(law, bits):
    scale = 1 << bits
    exact = np.maximum(law, 0) * scale
    counts = np.floor(exact).astype(np.int64)
    remaining = scale - int(counts.sum())
    assert 0 <= remaining <= len(law)
    order = np.argsort(-(exact - counts), kind="stable")
    counts[order[:remaining]] += 1
    assert int(counts.sum()) == scale and np.all(counts >= 0)
    return counts / scale


def verify_signed_witness(group, seed, copies=3):
    """Average the finite signed-copy test against known interquery operations."""
    rng = np.random.default_rng(seed)
    index = {g: i for i, g in enumerate(group.states)}
    distances = bfs(group)
    metric = np.array([distances[g] for g in group.states])
    diameter = int(metric.max())
    shape = (1 + len(group.generators), copies, len(group.states))
    dimension = math.prod(shape)
    state = np.zeros(shape, dtype=complex)
    state[0, :, index[group.identity]] = 1 / math.sqrt(copies)

    def known_gate():
        matrix = rng.normal(size=(dimension, dimension))
        matrix = matrix + 1j * rng.normal(size=matrix.shape)
        return np.linalg.qr(matrix)[0]

    state = (known_gate() @ state.ravel()).reshape(shape)
    # Keep both measurement branches with their original weights. Their forward
    # and inverse SELECT choices alternate; selector zero bypasses the query.
    branches = [state.copy(), state.copy()]
    branches[0][1:] = 0
    branches[1][0] = 0
    interleavings = [[known_gate() for _ in range(diameter)] for _ in branches]
    forward = [np.arange(len(group.states))] + [
        np.array([index[group.mul(s, h)] for h in group.states])
        for s in group.generators
    ]
    inverse = [np.argsort(p) for p in forward]
    endpoint_weights = np.arange(1, len(group.states) + 1, dtype=float)
    endpoint_weights /= endpoint_weights.sum()
    acceptances = np.zeros(diameter + 1)
    ideal_acceptances = np.zeros_like(acceptances)
    assignments = 2 ** (copies * diameter)

    for signs in itertools.product((-1, 1), repeat=copies * diameter):
        increments = np.reshape(signs, (copies, diameter))
        prefixes = np.column_stack((np.ones(copies, dtype=int),
                                    np.cumprod(increments, axis=1)))
        gauge = prefixes[:, metric]
        ideal = gauge / math.sqrt(copies)
        current = branches
        for q in range(diameter + 1):
            far = metric > q
            for branch in current:
                near_weight = np.sum(np.abs(branch[:, :, ~far]) ** 2)
                far_overlap = np.sum(branch[:, :, far] * gauge[None, :, far], axis=1)
                acceptances[q] += (near_weight + np.sum(np.abs(far_overlap) ** 2)) / copies
            overlaps = np.sum(ideal[:, far] * gauge[:, far], axis=0) / math.sqrt(copies)
            ideal_acceptances[q] += (np.sum(endpoint_weights[~far]) / copies
                                     + endpoint_weights[far] @ np.abs(overlaps) ** 2)
            if q == diameter:
                break
            updated = []
            for b, branch in enumerate(current):
                output = np.empty_like(branch)
                permutations = inverse if (b + q) % 2 else forward
                for selector, permutation in enumerate(permutations):
                    next_metric = metric[permutation]
                    assert np.all(np.abs(next_metric - metric) <= 1)
                    address = np.maximum(np.maximum(next_metric, metric) - 1, 0)
                    radial_phase = np.where(next_metric == metric, 1, increments[:, address])
                    phase = gauge * gauge[:, permutation]
                    assert np.array_equal(phase, radial_phase)
                    output[selector][:, permutation] = branch[selector] * phase
                updated.append((interleavings[b][q] @ output.ravel()).reshape(shape))
            current = updated

    acceptances /= assignments
    ideal_acceptances /= assignments
    gaps = ideal_acceptances - acceptances
    predicted = [(1 - 1 / copies) * endpoint_weights[metric > q].sum()
                 for q in range(diameter + 1)]
    residual = float(np.max(np.abs(acceptances - 1 / copies)))
    assert residual < 1e-12
    assert np.max(np.abs(gaps - predicted)) < 1e-12
    return {"group": group.name, "copies": copies, "sign_assignments": assignments,
            "max_acceptance_residual": residual, "ideal_minus_test_acceptance": gaps.tolist()}


def verify_runtime_profiles():
    """Check exact tail subtraction and partial-atom trimming on a cyclic group."""
    group = Cyclic(4)
    distances = bfs(group)
    lengths = [distances[g] for g in group.states]
    law = tuple(Fraction(weight, 8) for weight in (1, 2, 3, 2))
    diameter = max(lengths)
    identity = group.states.index(group.identity)

    def tails(weights):
        return [sum(mass for length, mass in zip(lengths, weights) if length > q)
                for q in range(diameter + 1)]

    results = []
    for budget in map(Fraction, (0, "1/8", "3/8", "1/2", "7/8", 1)):
        trimmed = list(law)
        remaining = budget
        for i in sorted(range(len(law)), key=lengths.__getitem__, reverse=True):
            if i == identity or remaining == 0:
                break
            removed = min(remaining, trimmed[i])
            trimmed[i] -= removed
            trimmed[identity] += removed
            remaining -= removed
        expected_tails = [max(0, tail - budget) for tail in tails(law)]
        actual_tails = tails(trimmed)
        assert actual_tails == expected_tails
        assert sum(trimmed) == 1
        assert sum(abs(a - b) for a, b in zip(law, trimmed)) == 2 * (budget - remaining)
        mean = sum(length * weight for length, weight in zip(lengths, trimmed))
        cap = max(length for length, weight in zip(lengths, trimmed) if weight)
        assert mean == sum(actual_tails)
        assert cap == actual_tails.index(0)
        results.append({"half_error_budget": str(budget), "hard_cap": cap,
                        "expected_queries": str(mean), "tails": list(map(str, actual_tails))})
    return results


def verify_group(group, seed):
    rng = np.random.default_rng(seed)
    states, identity = group.states, group.identity
    n = len(states)
    index = {g: i for i, g in enumerate(states)}
    unit = np.arange(n)
    for g in states:
        assert group.mul(g, identity) == group.mul(identity, g) == g
    triples = (itertools.product(states, repeat=3) if n <= 12 else
               ((states[int(i)], states[int(j)], states[int(k)])
                for i, j, k in rng.integers(n, size=(2000, 3))))
    associative_tests = 0
    for g, h, k in triples:
        assert group.mul(group.mul(g, h), k) == group.mul(g, group.mul(h, k))
        associative_tests += 1
    regular = [np.array([index[group.mul(g, h)] for h in states]) for g in states]
    # Exhaustive representation law on all group pairs, independently of relations.
    for g in states:
        for h in states:
            assert np.array_equal(compose(regular[index[g]], regular[index[h]]),
                                  regular[index[group.mul(g, h)]])
    distance = bfs(group)
    metric = np.array([distance[g] for g in states])
    generators = [regular[index[s]] for s in group.generators]
    edge_count = n * len(generators)
    for s, inverse in enumerate(group.inverse_labels):
        assert np.array_equal(compose(generators[s], generators[inverse]), unit)
        assert np.max(np.abs(metric[generators[s]] - metric)) <= 1
    m = min(4, int(metric.max()))
    gauge_tests = compiler_basis_tests = relation_tests = 0
    selected_supplied = None
    for bits in itertools.product((0, 1), repeat=m):
        prefix = np.concatenate(([0], np.bitwise_xor.accumulate(bits)))
        value = prefix[np.minimum(metric, m)]
        gauge = np.array([2 * i + (b ^ int(value[i])) for i in range(n) for b in (0, 1)])
        lifted = [np.array([2 * int(p[i]) + b for i in range(n) for b in (0, 1)])
                  for p in generators]
        supplied = [gauge[p[gauge]] for p in lifted]
        # Equality of basis permutations also verifies coherent superpositions.
        for selector in range(-1, len(generators)):
            for control in (0, 1):
                for i, g in enumerate(states):
                    for answer in (0, 1):
                        active = selector >= 0 and control == 1
                        h_index = int(generators[selector][i]) if active else i
                        d, e = int(metric[i]), int(metric[h_index])
                        changes = active and d != e and max(d, e) <= m
                        address = max(d, e) - 1 if changes else 0
                        # Two ordinary queries use a valid dummy address too.
                        buffer = 0
                        buffer ^= bits[address]
                        result = answer ^ (buffer if changes else 0)
                        buffer ^= bits[address]
                        assert buffer == 0
                        actual = 2 * h_index + result
                        expected = (int(supplied[selector][2 * i + answer])
                                    if active else 2 * i + answer)
                        assert actual == expected
                        compiler_basis_tests += 1
        for s, inverse in enumerate(group.inverse_labels):
            assert np.array_equal(compose(supplied[s], supplied[inverse]), np.arange(2 * n))
        relation_tests += group.defining_relations(supplied)
        selected_supplied = supplied
        gauge_tests += 1

    geodesic_tests = 0
    if isinstance(group, Wreath):
        for g in states:
            assert len(group.cycle_word(g)) == distance[g]
            geodesic_tests += 1

    transition = sum((sparse_permutation(p) for p in generators),
                     sparse.csr_matrix((n, n))) / len(generators)
    classical_generator = transition - sparse.eye(n)
    source = np.zeros(n)
    source[index[identity]] = 1
    endpoint_rows = []
    for t in (0.5, 2.0, 8.0):
        law = expm_multiply(t * classical_generator, source)
        assert abs(float(law.sum()) - 1) < 5e-13
        assert float(law.min()) > -5e-14
        q = max(0, int(metric.max()) // 2)
        bad = metric > q
        tail = float(law[bad].sum())
        capped = law.copy()
        capped[bad] = 0
        capped[index[identity]] += tail
        l1 = float(np.abs(law - capped).sum())
        assert abs(l1 - 2 * tail) < 1e-12
        rounded = dyadic_round(law, 20)
        tv = float(np.abs(law - rounded).sum() / 2)
        assert tv <= n / (2 ** 20)
        endpoint_rows.append({"time": t, "radius_cap": q,
                              "mean_distance": float(law @ metric),
                              "tail_probability": tail,
                              "regular_input_unhalved_trace_error": l1,
                              "dyadic_20_bit_tv": tv})

    # A genuine reference-entangled input, including coherences and off-diagonals.
    supplied = selected_supplied
    d = 2 * n
    reference_dim = 2
    total_d = d * reference_dim
    full_psi = rng.normal(size=total_d) + 1j * rng.normal(size=total_d)
    full_psi /= np.linalg.norm(full_psi)
    full_rho = np.outer(full_psi, full_psi.conj())
    operators = [sparse.kron(sparse_permutation(p), sparse.eye(reference_dim), format="csr")
                 for p in supplied]
    superoperator = (sum((sparse.kron(u.conjugate(), u, format="csr") for u in operators),
                         sparse.csr_matrix((total_d ** 2, total_d ** 2))) / len(operators)
                     - sparse.eye(total_d ** 2))
    t = 1.25
    direct = expm_multiply(t * superoperator, full_rho.reshape(-1, order="F")).reshape(
        (total_d, total_d), order="F")
    law = expm_multiply(t * classical_generator, source)
    bits = tuple([1] * m)
    prefix = np.concatenate(([0], np.bitwise_xor.accumulate(bits)))
    value = prefix[np.minimum(metric, m)]
    gauge = np.array([2 * i + (b ^ int(value[i])) for i in range(n) for b in (0, 1)])
    mixture = np.zeros_like(full_rho)
    truncated_mixture = np.zeros_like(full_rho)
    rounded_mixture = np.zeros_like(full_rho)
    rounded_law = dyadic_round(law, 20)
    radius_cap = max(0, int(metric.max()) // 2)
    word_tail = float(law[metric > radius_cap].sum())
    for i, p in enumerate(regular):
        lift = np.array([2 * int(p[j]) + b for j in range(n) for b in (0, 1)])
        gauged = gauge[lift[gauge]]
        full_permutation = np.array([reference_dim * int(gauged[j]) + r
                                     for j in range(d) for r in range(reference_dim)])
        inverse = np.argsort(full_permutation)
        branch = full_rho[np.ix_(inverse, inverse)]
        mixture += law[i] * branch
        rounded_mixture += rounded_law[i] * branch
        if metric[i] <= radius_cap:
            truncated_mixture += law[i] * branch
    truncated_mixture += word_tail * full_rho
    channel_residual = float(np.linalg.norm(direct - mixture, "fro"))
    assert channel_residual < 2e-12
    assert abs(float(np.trace(direct).real) - 1) < 1e-12
    truncation_trace_error = float(np.abs(np.linalg.eigvalsh(mixture - truncated_mixture)).sum())
    rounding_trace_error = float(np.abs(np.linalg.eigvalsh(mixture - rounded_mixture)).sum())
    assert truncation_trace_error <= 2 * word_tail + 2e-12
    assert rounding_trace_error <= float(np.abs(law - rounded_law).sum()) + 2e-12

    # Independent Poisson-series endpoint reconstruction with identity overflow.
    B = 5
    t = 2.0
    step_law = source.copy()
    poisson_law = np.zeros(n)
    for j in range(B + 1):
        poisson_law += poisson.pmf(j, t) * step_law
        step_law = transition @ step_law
    overflow = float(poisson.sf(B, t))
    poisson_law[index[identity]] += overflow
    exact_law = expm_multiply(t * classical_generator, source)
    poisson_error = float(np.abs(poisson_law - exact_law).sum())
    assert poisson_error <= 2 * overflow + 2e-12

    return {"group": group.name, "order": n, "diameter": int(metric.max()),
            "associativity_tests": associative_tests,
            "representation_pair_tests": n * n, "metric_edges": edge_count,
            "gauge_bit_strings": gauge_tests, "compiler_basis_tests": compiler_basis_tests,
            "defining_relation_tests": relation_tests, "exact_cycle_geodesics": geodesic_tests,
            "reference_entangled_channel_frobenius_residual": channel_residual,
            "reference_entangled_word_truncation": {
                "time": 1.25, "radius_cap": radius_cap,
                "unhalved_trace_error": truncation_trace_error,
                "proved_diamond_upper": 2 * word_tail},
            "reference_entangled_probability_rounding": {
                "unhalved_trace_error": rounding_trace_error,
                "proved_diamond_upper": float(np.abs(law - rounded_law).sum())},
            "poisson_cap_diagnostic": {"time": t, "cap": B, "overflow": overflow,
                                       "endpoint_l1_error": poisson_error,
                                       "proved_l1_upper": 2 * overflow},
            "endpoint_diagnostics": endpoint_rows}


def main():
    cutoff_tests = []
    for t in (0.0, 0.1, 1.0, 3.0, 20.0):
        for delta in (0.01, 0.1):
            B = math.ceil(2 * t + 2 * math.log(1 / delta))
            tail = float(poisson.sf(B, t))
            assert tail <= delta
            cutoff_tests.append({"time": t, "delta": delta, "cap": B, "tail": tail})
    groups = [Cyclic(7), Dihedral(5), Wreath(3, 3)]
    results = [verify_group(group, 12000 + i) for i, group in enumerate(groups)]
    # An additional wreath cycle tests the cycle-geodesic formula independently.
    extra = Wreath(3, 4)
    distance = bfs(extra)
    for endpoint in extra.states:
        assert len(extra.cycle_word(endpoint)) == distance[endpoint]
    print(json.dumps({"passed": True, "seed_rule": "12000 + group index",
                      "groups": results,
                      "signed_copy_witnesses": [verify_signed_witness(group, 6617)
                                                 for group in (Cyclic(4), Dihedral(3))],
                      "exact_runtime_profiles": verify_runtime_profiles(),
                      "additional_geodesic_instance": {"group": extra.name,
                                                       "endpoints_checked": len(extra.states)},
                      "poisson_cutoff_tests": cutoff_tests,
                      "limits": ["Finite permutation and compiler tests concern the listed groups only.",
                                 "Floating channel, probability and rounding diagnostics are not interval certificates.",
                                 "The diamond/quantile theorems and asymptotic wreath exponent are analytical claims; no exponent is fitted here."]},
                     indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
