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

Its hard family starts with the regular representation and conjugates every generator by the same unknown prefix-parity gauge. A step changes distance from the identity by at most one, so its answer update requires at most one Boolean input bit. A distant endpoint contains the parity of many bits. One common conjugation preserves every group relation, including relations around cycles. The construction therefore stays inside the representation promise while importing the quantum parity lower bound.

This makes the lower bound a statement about the unknown representation interface. It is not a restriction to algorithms that explicitly generate trajectories or compile geodesics.

## Quantiles, rather than an unrestricted mean law

Write $`D=|g|_S`$ for the word distance of $`g\sim\mu`$. With unhalved diamond error $`\varepsilon`$, the exact-law bounds are

```math
\Pr(D>r)\le\varepsilon/2
\quad\Longrightarrow\quad Q\le r,
```

```math
\Pr(D\ge m)>\varepsilon
\quad\Longrightarrow\quad Q\ge m/4.
```

Sampling and compilation inaccuracies consume a separately reserved part of the error budget. The query cap is a maximum on every branch. The two bounds compare tail thresholds at different error levels; they do not assert equality of those thresholds for an arbitrary distribution.

An expected distance alone need not describe the optimum. For example, a law can put probability at most $`\varepsilon/2`$ on a very distant element and all remaining probability on the identity. Returning the identity channel already meets the error target, even though the mean distance can grow along a family of groups. A mean escape law becomes an optimal query law only after the needed upper-tail and lower-tail estimates are proved.

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

The asymptotic example uses finite groups and finite-dimensional targets whose sizes increase with $`t`$. For a fixed finite group, word distance is bounded by its diameter, so the displayed power law cannot describe unrestricted long-time growth at that fixed group. The theorem also supplies no geometric locality guarantee for the unknown representation matrices and no optimal joint time-and-precision law.

The target is the reduced quantum channel. Retaining a specified coherent bath, an emission record, or a particular physical dilation is a different output requirement. Endpoint compression need not preserve such extra outputs. Exact group relations are part of the input promise; an approximate-relation model needs an additional error analysis before the same compilation can be used.

[Back to the scientific model](model.md) · [Read the proof](group-quantiles.md) · [Compare prior work](../references/related-work.md)
