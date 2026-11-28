# Quantum Group Escape

**How do algebraic cancellations determine the cost of simulating quantum noise?**

A random-unitary evolution can contain a long sequence of jumps while its endpoint has a much shorter group-word description. This project relates that endpoint geometry to the optimal number of calls to unknown unitary generators. The group and its relations are known; its unitary representation is supplied through charged oracle calls.

## Principal results

For a known finite group, let $`D`$ be the shortest-word distance of an endpoint sampled from a known law. Define its upper escape quantile by

```math
R_\eta=\min\{r\in\mathbb Z_{\ge0}:\Pr(D>r)\le\eta\}.
```

With at most $`q`$ generator calls on each branch, the exact worst-case unhalved diamond error is $`2\Pr(D>q)`$. The minimum hard cap at error $`\varepsilon`$ is therefore

```math
Q_G(\mu,\varepsilon)=R_{\varepsilon/2}.
```

With classical stopping, the minimum worst-case expected number of calls is

```math
\sum_{q\ge0}\max\{\Pr(D>q)-\varepsilon/2,0\}.
```

One sampler attains the optimal probability of exceeding every budget $`q`$ at once. It replaces the farthest $`\varepsilon/2`$ of endpoint probability with the identity and applies a shortest word for every retained endpoint. At exact accuracy the expected cost is $`\mathbb E[D]`$. A finite-precision sampler uses a separate error allowance.

The converse permits coherent controls, inverse calls, ancillas, and adaptive measurements. It preserves all group relations while assigning independent signs to copies of the regular representation. Coherence between two copies at distance $`D`$ requires sign degree $`2D`$. A $`q`$-call circuit can supply degree at most $`2q`$. See the [exact theorem and proof](science/group-quantiles.md).

A nonabelian example uses four equal-rate unitary jumps: a cursor shift and its inverse, and an integer-lamp update and its inverse. Known relations make updates at translated lamp sites commute. Along explicitly specified growing finite quotients, the optimal fixed-error query cost is

```math
Q(t,\varepsilon)=\Theta_\varepsilon(t^{3/4})
\qquad(t\longrightarrow\infty),
\qquad0\lt \varepsilon\le1/100\text{ fixed}.
```

The [occupation-time proof](science/wreath-product.md) establishes the required escape quantiles, and the [finite-quotient proof](science/finite-quotients.md) supplies finite groups, metric preservation and dimension bounds. The classical escape exponent and the existence of intermediate Lindblad simulation exponents are established antecedents; [related work](references/related-work.md) identifies the added oracle-level statement.

## Run endpoint compression

1. **Sample the endpoint on a classical computer.** Use the known endpoint law. For the continuous-time walk, draw the [capped Poisson event count](science/algorithms-and-resources.md#capped-poisson-trajectory-sampling), draw that many generator labels, and multiply them in the known group. Return the input on overflow.
2. **Choose which endpoint to apply.** For a [hard call cap](science/algorithms-and-resources.md#a-hard-query-cap), compute a shortest word or use a certified short-word routine with its own length bound. Return the input when the chosen word exceeds the cap. For [optimal expected cost](science/algorithms-and-resources.md#trimming-for-the-exact-expected-cost), use shortest words and redirect the allowed farthest endpoint mass to the identity. Use a classical random draw if the cutoff splits a distance shell. Reserve error for finite probabilities, time rounding, and gate implementation.
3. **Apply the retained word to the supplied quantum input.** For an algebraic product in a left representation, apply the supplied generator or inverse gates from the rightmost factor to the leftmost. Use the classical draws to control the gates and return the quantum register. Averaging this output over the draws gives the simulated evolution.

Charge the classical sampling, word computation, and storage alongside the implementation of each invoked generator. The [error budget](science/algorithms-and-resources.md#finite-precision-and-the-full-error-budget) gives one finite allocation.

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

## Learn the argument

The educational anchor is Andrew M. Childs, [*Lecture Notes on Quantum Algorithms*](https://www.cs.umd.edu/~amchilds/qa/), **17 April 2025**. The [learning route](learning/README.md) connects its reversible computation, representations and query lower bounds to this project. Begin with the [four-element worked example and source bridge](learning/childs-bridge.md), then follow the [thirty milestones](learning/milestones.md) through the complete proof and its resource limits.

## Implementation and scope

The sublinear resource is serial calls to unknown generators. The direct sampler still processes order $`t`$ classical events; its work can be performed before receiving the quantum input. This account establishes oracle-call fast forwarding, with an explicit classical cost. A total-runtime or hardware advantage is not established.

The exact minimax statements are uniform over finite target dimensions. The converse also gives explicit finite-dimension bounds. The wreath example uses groups and finite target widths that grow with time. A sufficient hard-instance width is $`O_\varepsilon(t\log(t+2))`$ qubits. The model supplies exact algebraic relations, inverse and controlled generator access, and charges every invoked controlled query. The expected-cost statement uses a classically recorded stopping time.

Known group arithmetic, word finding, classical storage, probability evaluation and physical realization of each generator are charged separately in the [resource account](science/algorithms-and-resources.md). The construction uses ordinary classical sampling and control, without a QRAM or a free loader for unknown classical data.

## Reproduce the finite checks

From the repository root:

```bash
python3 verification/check_finite_groups.py
```

The [verification guide](verification/README.md) documents dependencies, exact finite checks and floating diagnostics. These checks test representation conventions, relation preservation and finite implementations. The universal and asymptotic statements rest on the analytical proofs.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
