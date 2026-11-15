# Algorithms and resources

The simulation theorem counts **serial calls to unknown represented generators**. The upper algorithm also performs classical random-walk sampling and word computation. Those operations remain charged when assessing runtime.

Throughout, the channel error is the unhalved diamond norm. For probability laws $`\mu,\nu`$ on a known finite group and any unitary representation $`\pi`$,

```math
\left\|\sum_g(\mu(g)-\nu(g))\mathrm{Ad}_{\pi(g)}\right\|_\diamond
\leq \sum_g|\mu(g)-\nu(g)|
=2\mathrm{TV}(\mu,\nu).
```

The inequality is uniform over representation dimension and reference-entangled inputs. It converts errors of a classical sampler into errors of the resulting quantum channel.

## A hard query cap

For a known endpoint law $`\mu`$, choose a deterministic word $`w(g)`$ representing each endpoint. A shortest word gives the general escape-distance upper bound; any explicitly computable short word also gives a valid algorithm. Fix an integer query cap $`q`$.

1. Sample an endpoint by classical computation.
2. Compute its representing word.
3. If its length exceeds $`q`$, apply the identity channel. Otherwise apply the represented word in the representation's product convention.

Every branch uses at most $`q`$ unknown-generator calls. Replacing a set of samples of probability $`\delta_{\rm word}`$ by the identity changes the channel by at most $`2\delta_{\rm word}`$. This is a trace-preserving replacement, with no postselection or conditional success convention.

Known group multiplication and word computation are classical tasks. A generic finite group specified by its multiplication table admits a breadth-first-search word table using $`O(|G||S|)`$ table operations and $`O(|G|)`$ stored vertices. That can be exponential in the number of bits naming a group element. The query theorem does not assert efficient generic geodesic computation.

## Capped Poisson trajectory sampling

For the rate-one continuous-time walk, sample $`J\sim\mathrm{Pois}(t)`$, then independently sample $`J`$ generator labels with distribution $`p`$ and multiply them classically. The endpoint law is the convolution-semigroup law used in the theorem.

To make the classical event count bounded as well, choose $`0<\delta_{\rm P}<1`$ and

```math
B=\left\lceil2t+2\ln(1/\delta_{\rm P})\right\rceil.
```

The Poisson Chernoff bound at parameter $`\ln2`$ gives

```math
\Pr[J>B]\leq\Pr[J\geq B]
\leq e^{t-B\ln2}\leq\delta_{\rm P}.
```

The last inequality follows from $`2\ln2>1`$. At $`t=0`$, return the identity directly. Sample from the finite law consisting of $`J=0,\ldots,B`$ and one overflow outcome. On overflow, return the identity channel. On other outcomes, simulate the generator labels and then apply the word-cap rule above. The total channel error from these two replacements is at most

```math
2\Pr[J>B]+2\Pr[J\leq B,\ |w(X_t)|>q].
```

The direct sampler performs $`O(t)`$ classical events in expectation and at most $`B=O(t+\ln(1/\delta_{\rm P}))`$ events on every branch. These events do not become sublinear merely because the resulting quantum word is short.

The algorithm uses classical random bits, arithmetic and ordinary classical control of the sampled gate sequence. It uses no QRAM or coherent lookup of a classical endpoint table.

## Finite precision and the full error budget

The scalar probabilities and time parameter must have computable descriptions. If a particular known distribution has no supplied efficient sampler, the query theorem does not provide one.

For a finite law with $`K`$ outcomes, nonnegative dyadic probabilities summing to one can approximate it to total variation $`\delta`$ using $`O(\log(K/\delta))`$ bits per probability, in addition to the work needed to evaluate those probabilities to certified accuracy. One construction evaluates the probabilities with a total absolute-error budget, projects them to a probability vector, then rounds by a largest-remainder rule. The sum of the evaluation and rounding errors must be bounded; floating-point normalization alone is not an error certificate.

For the capped Poisson law, $`K=B+2`$. A finite probability table therefore uses $`O(B\log(B/\delta))`$ bits. Interval evaluation of $`e^{-t}t^j/j!`$ or another certified Poisson sampler can supply the required finite scalar law. Generating it is classical preprocessing. A finite-precision uniform draw from its dyadic cumulative probabilities then uses a finite number of random bits.

If generator-label sampling has per-event total-variation error at most $`\eta`$, coupling over at most $`B`$ events bounds its cumulative contribution by $`B\eta`$. The wreath-product application chooses each of four labels with probability $`1/4`$, so these draws require exactly two fair bits and no probability rounding.

If the represented time is $`\widetilde t`$, couple the two Poisson processes to obtain

```math
\mathrm{TV}(\mu_t,\mu_{\widetilde t})
\leq 1-e^{-|t-\widetilde t|}\leq |t-\widetilde t|.
```

Time rounding can therefore be included in the scalar sampling budget. For a nonunit total jump rate, rescale time before using this bound.

A concrete allocation for target error $`0<\epsilon<1`$ is

| Contribution | Required bound | Diamond contribution |
|---|---:|---:|
| Poisson overflow | $`\Pr[J>B]\leq\epsilon/8`$ | $`\epsilon/4`$ |
| Long compiled word, without overflow | $`\Pr[J\leq B,\ |w(X_t)|>q]\leq\epsilon/8`$ | $`\epsilon/4`$ |
| All scalar sampling and time errors together | total variation at most $`\epsilon/8`$ | $`\epsilon/4`$ |
| Implemented generator words | total channel error at most $`\epsilon/4`$ | $`\epsilon/4`$ |

For a word of at most $`q>0`$ unitary calls, operator-norm error at most $`\epsilon/(8q)`$ per implemented unitary suffices for the last row: each induced unitary channel differs by at most twice that error in unhalved diamond norm, and a telescoping bound adds the errors. If a physical oracle comes with a different accuracy guarantee, use its actual channel-error bound. The ideal black-box theorem itself assumes exact supplied calls.

## A computable short word for the wreath family

Write an endpoint of $`\mathbb Z\wr\mathbb Z`$ as a cursor $`k\in\mathbb Z`$ and finitely supported integer lamps $`\eta_j`$. During the capped classical trajectory, retain the lifted integer cursor and the net signed update of each visited lamp. This takes at most $`O(B)`$ records, each with $`O(\log(B+2))`$ bits.

Set

```math
W=\sum_j|\eta_j|,\qquad
a=\min\bigl(\{0,k\}\cup\mathrm{supp}\eta\bigr),\qquad
b=\max\bigl(\{0,k\}\cup\mathrm{supp}\eta\bigr).
```

Visit the two extreme sites in the cheaper order, ending at $`k`$. On the first visit to each nonzero lamp, apply its net update using $`|\eta_j|`$ lamp generators or their inverses. The resulting word has length

```math
C(k,\eta)=W+
\min\{\,|a|+(b-a)+|b-k|,\ |b|+(b-a)+|a-k|\,\}.
```

This is the exact line word length. The lower bound follows because every required lamp must receive its net number of updates, and every cursor route must visit both extreme required sites. The two displayed routes attain it. Sorting the stored lamp sites and emitting such a route takes polynomial time and $`O(B\log(B+2))`$ bits of classical storage; even a dictionary-based implementation has only polynomial classical overhead.

Reduce the same word modulo $`L`$ and $`M`$ to obtain a valid word in $`C_M\wr C_L`$. It remains valid even when the sampled lifted path wraps in the quotient. For the algorithmic upper bound, no assertion that it is the shortest quotient word is needed. The moment bound for $`C(X_t)`$ gives an admissible fixed-error cap of order $`(t+1)^{3/4}`$.

If an exact finite-cycle geodesic is desired, it is also computable in polynomial time. The lamp cost is $`\sum_j\min(\eta_j,M-\eta_j)`$. For cursor travel, minimize over each possible omitted cycle edge: cutting that edge leaves a line, where the two-extreme-site formula applies. Also include a complete cycle followed by a shortest path to the final cursor. Any route either omits an edge or traverses every edge, so these cases exhaust the optimum. A direct implementation examines $`L`$ cuts and scans the required sites for each cut. This is a classical computation, with its cost stated separately from oracle calls.

For a word written algebraically as $`g=s_1\cdots s_r`$, a left representation satisfies $`\pi(g)=\pi(s_1)\cdots\pi(s_r)`$. Its gates act on a state from right to left. A cursor implementation that builds an endpoint by successive **right** multiplication must account for this execution order; it is not silently identified with the left regular action used in the lower-bound construction.

## What is and is not fast-forwarded

At fixed sufficiently small error, the wreath family has a hard quantum-query cap of order $`t^{3/4}`$, with a matching representation-uniform lower order. A convenient finite quotient has regular-representation width $`O(t\log(t+2))`$ qubits; that is a sufficient growing-width lower-bound realization, not an optimal memory claim or a fixed-system long-time limit.

The direct algorithm still samples $`O(t)`$ classical events. It therefore establishes sublinear **unknown-generator query count**, while leaving an explicit linear classical event overhead. It establishes no end-to-end runtime speedup or hardware crossover.

If one physical call costs $`C_{\rm gen}(n,\zeta)`$ gates at system width $`n`$ and required precision $`\zeta`$, the quantum gate cost includes up to $`q C_{\rm gen}(n,\zeta)`$, plus the actual known control costs. Unequal generator costs should be summed along the sampled word. Classical sampling, word computation, storage and probability evaluation must then be added. An unknown unitary is not assumed to have a free gate decomposition merely because its invocation is one query.

The generic upper algorithm stores only classical endpoint/word information beyond the represented input and the supplied oracle interface. It does not require the regular representation. The large regular representation appears in the lower-bound hard instance. The proof is uniform over allowed finite representations and includes arbitrary reference systems; it does not turn the lower-bound group's encoding into an uncharged implementation for a different physical device.

## Finite verification

[The finite verifier](../verification/check_finite_groups.py) checks cyclic, dihedral and wreath groups. It independently constructs group multiplication, the left regular representation and breadth-first-search distances; verifies the parity gauge and the two-bit-query compiler as exact permutations; checks representative defining relations and finite-cycle word lengths; and compares endpoint mixtures with a sparse Lindblad exponential on reference-entangled inputs.

It also checks Poisson overflow and dyadic-law error diagnostics. These finite tests verify conventions and implementations. The general diamond bound, group-relation guarantee, quantile lower bound and wreath escape exponent remain analytical statements with the scope given in their proof accounts. No asymptotic exponent is inferred from the small finite examples.
