# Quantum Group Escape

**How do algebraic cancellations determine the cost of simulating quantum noise?**

A random-unitary evolution can contain a long sequence of jumps while its endpoint has a much shorter group-word description. This project relates that endpoint geometry to the optimal number of calls to unknown unitary generators. The group and its relations are known; its unitary representation is supplied through charged oracle calls.

## Principal results

For a known finite group, let $`D`$ be the shortest-word distance of an endpoint sampled from a known law. Define its upper escape quantile by

```math
R_\eta=\min\{r\in\mathbb Z_{\ge0}:\Pr(D>r)\le\eta\}.
```

The worst-case cost of implementing the full random-unitary channel, uniformly over all unknown finite-dimensional representations, obeys

```math
\frac14 R_\varepsilon
\le Q_G(\mu,\varepsilon)
\le R_{\varepsilon/2}.
```

Here $`\varepsilon`$ is the **unhalved diamond error**, and queries are bounded on every execution branch. The two quantiles need not be comparable for an arbitrary endpoint law. Sampling precision uses a separate error allowance.

The upper algorithm samples an endpoint and applies a short representing word. The lower bound permits arbitrary coherent controls, ancillas and adaptive measurements. It conjugates an entire regular representation by one unknown parity gauge, preserving every group relation while turning escape into a quantum parity task. See the [exact theorem and proof](science/group-quantiles.md).

A nonabelian example uses four equal-rate unitary jumps: a cursor shift and its inverse, and an integer-lamp update and its inverse. Known relations make updates at translated lamp sites commute. Along explicitly specified growing finite quotients, the optimal fixed-error query cost is

```math
Q(t,\varepsilon)=\Theta_\varepsilon(t^{3/4})
\qquad(t\longrightarrow\infty),
\qquad0<\varepsilon\le1/100\text{ fixed}.
```

The [occupation-time proof](science/wreath-product.md) establishes the required escape quantiles, and the [finite-quotient proof](science/finite-quotients.md) supplies finite groups, metric preservation and dimension bounds. The classical escape exponent and the existence of intermediate Lindblad simulation exponents are established antecedents; [related work](references/related-work.md) identifies the added oracle-level statement.

## Read the account

| Reader's question | Authoritative route |
|---|---|
| What is known, what is unknown, and what counts as a query? | [Model](science/model.md) |
| Why is endpoint compression optimal against general quantum algorithms? | [Group quantiles](science/group-quantiles.md) |
| Where does the three-quarter power come from? | [Wreath-product escape](science/wreath-product.md) |
| How does the infinite probability example become a finite quantum instance? | [Finite quotients](science/finite-quotients.md) |
| What does the algorithm actually cost? | [Algorithms and resources](science/algorithms-and-resources.md) |
| What is the scientific consequence and its scope? | [Interpretation](science/interpretation.md) |
| Which ingredients and earlier results are inherited? | [Related work](references/related-work.md) |

The [science entrypoint](science/README.md) gives a connected reading order. The [retrieval guide](llms.txt) maps specific questions to their proof sources.

## Implementation and scope

The sublinear resource is serial calls to unknown generators. The direct sampler still processes order $`t`$ classical events; its work can be performed before receiving the quantum input. This account establishes oracle-call fast forwarding, with an explicit classical cost. A total-runtime or hardware advantage is not established.

The lower bound ranges over representations and dimensions; it does not apply to every individual representation. The wreath example uses groups and finite target widths that grow with time. A sufficient hard-instance width is $`O_\varepsilon(t\log(t+2))`$ qubits. Exact algebraic relations, inverse/controlled generator access, full-channel output, and a hard query cap are material assumptions. No geometric locality or optimal joint time-and-precision claim is made.

Known group arithmetic, word finding, classical storage, probability evaluation and physical realization of each generator are charged separately in the [resource account](science/algorithms-and-resources.md). The construction uses ordinary classical sampling and control, without a QRAM or a free loader for unknown classical data.

## Reproduce the finite checks

From the repository root:

```bash
python3 verification/check_finite_groups.py
```

The [verification guide](verification/README.md) documents dependencies, exact finite checks and floating diagnostics. These checks test representation conventions, relation preservation and finite implementations. The universal and asymptotic statements rest on the analytical proofs.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
