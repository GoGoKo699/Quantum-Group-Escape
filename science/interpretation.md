# What escape geometry tells us about simulation

The same random-unitary evolution can be described by its entire jump history or by the group element reached at the end. The history usually contains order $`t`$ elementary jumps. Its endpoint can have a much shorter representative because the supplied operators satisfy known algebraic relations. This project identifies when that shorter endpoint description also captures the optimal number of calls to unknown unitary generators.

The formal statements are in [the model](model.md) and [the quantile theorem](group-quantiles.md). The [wreath-product example](wreath-product.md) and [finite quotient construction](finite-quotients.md) give a noncommutative application.

## The endpoint is the quantum operation

Let $`\pi`$ be an unknown unitary representation of a known finite group $`G`$, and let $`\mu`$ be a known probability law on $`G`$. The target channel is

```math
\Phi_{\pi,\mu}(\rho)
=\sum_{g\in G}\mu(g)\,\pi(g)\rho\pi(g)^\dagger.
```

For a continuous-time random walk, $`\mu=\mu_t`$ is the endpoint law of the Poisson jump process. All chronological words reaching the same $`g`$ apply exactly the same represented unitary. Sampling an endpoint and applying a geodesic word therefore implements the same quantum channel. This statement holds on arbitrary inputs, including inputs entangled with an untouched reference; it does not rely on a classical initial state.

The group and its relations are known. The representation matrices are available through charged generator queries. No oracle giving an arbitrary group element, an arbitrary power, or the representation's matrix entries is supplied. Computing an endpoint or finding a geodesic is a separate classical task.

## Why a different quantum algorithm cannot always do better

Compressing words gives an algorithm, but by itself does not rule out a faster coherent procedure. The converse addresses every algorithm in the declared oracle model, including algorithms with protected ancillas, measurements, adaptive control, and arbitrary known interleavings.

The hard family assigns independent radial signs to several copies of the regular representation. One conjugation preserves all group relations. The simulator gains at most one sign per oracle call on each side of a density-matrix entry. At a distant endpoint, the ideal output has coherence between different copies. Matching that coherence requires the product of both sign strings, of degree twice the endpoint distance. Averaging the corresponding output test over the unknown signs gives the exact distance-tail obstruction.

## The effect of the error budget

Write $`\beta_q=\Pr(D>q)`$ for the tail of the endpoint word distance. At a hard cap $`q`$, the optimum unhalved diamond error is $`2\beta_q`$. The smallest allowable cap uses the first radius with $`\beta_q\le\varepsilon/2`$. If the simulator can stop at a classically recorded query count, the optimum mean is $`\sum_q(\beta_q-\varepsilon/2)_+`$. One geodesic sampler achieves it by spending the error allowance on the farthest draws.

For example, suppose a distance-$`L`$ endpoint has probability $`b`$ and the identity gets the rest. The hard cap jumps from zero to $`L`$ as $`b`$ crosses $`\varepsilon/2`$. The expected cost instead rises as $`L(b-\varepsilon/2)_+`$. This is why the raw mean distance can be large even when an identity channel already attains the target accuracy. Sampling and compilation inaccuracies require a separate share of the error budget.

## Four bounded jumps and a three-quarter power

The explicit example has a cursor on a line and integer-valued lamps. The cursor shift $`S`$ and lamp increment $`A`$ do not commute, while the translated lamps $`S^jAS^{-j}`$ commute with one another. Each of $`S,S^{-1},A,A^{-1}`$ occurs at rate $`1/4`$. Thus the total jump rate is one, with a fixed finite alphabet of norm-one unitary operations.

After time $`t`$, the cursor explores order $`\sqrt t`$ sites. Repeated positive and negative lamp updates partly cancel at each site, but they leave accumulated lamp work over the whole visited region. The local-time analysis gives endpoint length of order $`t^{3/4}`$ at the quantiles needed by the theorem. Along the specified growing finite quotients, the optimal generator-query count at the declared fixed error $`\varepsilon=1/100`$ is consequently

```math
Q(t,1/100)=\Theta(t^{3/4})
\qquad (t\longrightarrow\infty).
```

The classical escape behavior is established random-walk mathematics. The added quantum statement is that this geometry determines the worst-case simulation cost over the supplied representations, even for an unrestricted quantum simulator. The fractional exponent comes from noncommuting finite-generator geometry with bounded jump rates. It is not inserted through a heavy-tailed distribution of Hamiltonian evolution times. [Related work](../references/related-work.md) explains why intermediate Lindblad simulation exponents themselves are already known.

## Resource boundaries

The result reduces serial calls to the unknown generators. The direct sampler still processes order $`t`$ classical jump events, and normal-form arithmetic and finite-bit sampling have their own costs. Thus this implementation establishes oracle-call fast forwarding; it does not establish a reduction of total runtime, energy, or hardware cost. There is no QRAM assumption or free loader for an arbitrary classical table.

The asymptotic example uses finite groups and finite-dimensional targets whose sizes increase with $`t`$. For a fixed finite group, word distance is bounded by its diameter, so the displayed power law cannot describe unrestricted long-time growth at that fixed group. The exact query formulas apply to every endpoint law along the family. Obtaining an explicit joint dependence on time and precision requires quantitative escape tails for that law.

The target is the reduced quantum channel. Retaining a specified coherent bath, an emission record, or a particular physical dilation is a different output requirement. Endpoint compression need not preserve such extra outputs. Exact group relations are part of the input promise; an approximate-relation model needs an additional error analysis before the same compilation can be used.

[Back to the scientific model](model.md) · [Read the proof](group-quantiles.md) · [Compare prior work](../references/related-work.md)
