# Model, output and charged resources

The task is to implement a random-unitary channel whose unitaries form an unknown representation of a known finite group. The group supplies exact algebraic relations. It does not supply matrices for the unknown representation. The distinction makes it possible to compress a known random word while retaining a meaningful oracle lower bound.

The main theorem in [Group quantiles](group-quantiles.md) applies to any known probability law on the group. A continuous-time random walk supplies the law in the [wreath-product application](wreath-product.md).

## A known group and an unknown representation

Let $`G`$ be a finite group with identity $`e`$, and let $`S\subseteq G\setminus\{e\}`$ be a known, finite, inverse-closed generating set. Elements of $`S`$ label the permitted primitive queries. Define the word length

```math
\ell(g)=|g|_S
 =\min\{k\geq 0:g=s_k\cdots s_1,\ s_i\in S\}.
```

The minimum for the identity is zero. Inverse closure makes the associated Cayley-graph metric undirected. In particular, for every $`s\in S`$ and $`g\in G`$,

```math
|\ell(sg)-\ell(g)|\leq 1.
```

The input is a finite-dimensional unitary representation

```math
\pi:G\longrightarrow\mathrm U(\mathcal H),
\qquad
\pi(gh)=\pi(g)\pi(h),\quad \pi(e)=I.
```

The representation is unknown except through its supplied generator oracles. It may be reducible or unfaithful. The representation promise is exact and includes all relations in $`G`$. A family satisfying additional relations remains an admissible instance.

A group table, a word-length algorithm, a classical description of a reference regular representation, or another representation-independent construction may be used in known computation. None of these supplies the unknown $`\pi(g)`$. In particular, the model supplies no free change of basis that reveals the unknown representation and no free implementation of an arbitrary long group element.

## The strongest permitted primitive

The query model permits a coherent selection of generators,

```math
\operatorname{SELECT}_{\pi}
 =\sum_{s\in S}|s\rangle\!\langle s|\otimes\pi(s),
```

its inverse, and externally controlled versions. Each selected invocation costs one serial query. A basis-state selection is a permitted special case. Since $`S`$ is inverse closed, an inverse can also be described by the known relabelling $`s\mapsto s^{-1}`$.

Ancillas, randomness, adaptive measurements, coherent controls, resets, and other known quantum operations are permitted. They must be independent of the unknown representation except through oracle queries. Queries applied in parallel count separately in the serial query total. Coherently choosing among several primitives counts as one SELECT query, so the lower theorem is proved for this stronger access convention.

This is an oracle model for unitary generators. It supplies neither a block encoding of an unspecified logarithm of a generator nor arbitrary real powers at unit cost. If a richer primitive is supplied, its cost and the relevant word metric must be reconsidered.

## The channel to be implemented

Let $`\mu`$ be a known probability distribution on $`G`$. The target channel is

```math
\Phi_{\pi,\mu}(\rho)
 =\sum_{g\in G}\mu(g)\,\pi(g)\rho\pi(g)^{\dagger}.
```

The algorithm receives an arbitrary state on $`\mathcal H`$ and implements a completely positive, trace-preserving map on that system. The approximation must hold on every input, including one entangled with an untouched reference system. An implementation may discard its own internal records, but it cannot postselect and renormalize a successful branch without accounting for failure in the delivered channel.

Throughout this repository the error is the **unhalved diamond norm**:

```math
\|\widetilde\Phi_{\pi}-\Phi_{\pi,\mu}\|_{\diamond}
 \leq \varepsilon.
```

The maximum distance between channels in this convention is two. For any input state, any reference, and any final measurement event, this norm bound changes that event's probability by at most $`\varepsilon/2`$. Indeed, the output-state difference is Hermitian with trace zero, so its largest measurement bias is half its trace norm.

The quantile theorem is stated for $`0\leq\varepsilon<1`$. Exact simulation is included by setting $`\varepsilon=0`$. The strict inequality in the lower theorem's escape condition is material at a quantile boundary.

## Worst-case query cost and its dimension quantifier

Write $`Q_G(\mu,\varepsilon)`$ for the smallest integer $`q`$ with the following property: for each finite target dimension there is an algorithm, chosen using that dimension and the known data $`G,S,\mu,\varepsilon`$, that uses at most $`q`$ supplied-generator queries on every branch and satisfies the diamond-error bound for every representation of that dimension.

The circuit and all its nonoracle operations are uniform over the unknown representations in its target dimension. The bound $`q`$ is uniform over all finite dimensions. A single hard representation of dimension $`2|G|`$ therefore suffices for the general lower bound. This is not a statement about every individual representation, a chosen irreducible representation, or one fixed small physical system as time tends to infinity.

The cost is a worst-case bound on the number of oracle calls, rather than an expected stopping time. A random word of unbounded length must be capped before it yields such a bound. Conversely, a maximum-query lower bound does not by itself establish the same statement for arbitrary expected-query algorithms.

The finite group and the law may vary with a problem parameter. The [finite-quotient construction](finite-quotients.md) states the resulting size and target-width costs when a growing group is used to represent a finite window of an infinite random walk.

## Continuous-time laws

For a known probability distribution $`\nu`$ on $`S`$, let $`N_t`$ be Poisson with mean $`t`$. Starting at the identity, take $`N_t`$ independent left increments with distribution $`\nu`$. Their endpoint law is

```math
\mu_t
 =e^{-t}\sum_{k=0}^{\infty}\frac{t^k}{k!}\,\nu^{*k},
\qquad \nu^{*0}=\delta_e.
```

No symmetry of $`\nu`$ is required for the general theorem. Symmetry is imposed in the wreath-product application. The corresponding random-unitary generator is

```math
\mathcal L_{\pi,\nu}
 =\sum_{s\in S}\nu(s)
   \bigl(\operatorname{Ad}_{\pi(s)}-\operatorname{Id}\bigr),
\qquad
\operatorname{Ad}_{U}(\rho)=U\rho U^{\dagger},
```

and the Poisson expansion gives the exact identity

```math
 e^{t\mathcal L_{\pi,\nu}}=\Phi_{\pi,\mu_t}.
```

Thus the endpoint is known classical randomness, while applying its represented group element is the unknown quantum operation. Removing algebraic cancellations concerns the latter cost. It does not automatically accelerate the classical process used to obtain the endpoint.

## Probability precision and implementation precision

The information-theoretic query theorem first treats $`\mu`$ as an exact mathematical law and permits exact known classical randomization. A finite classical description can instead specify a law $`\widehat\mu`$ with a certified total-variation error

```math
\|\widehat\mu-\mu\|_{\mathrm{TV}}
 =\frac12\sum_{g\in G}|\widehat\mu(g)-\mu(g)|\leq\delta.
```

This changes the random-unitary channel by at most $`2\delta`$ in unhalved diamond norm. The same bound holds after any deterministic cap on the sampled endpoint because total variation contracts under postprocessing. In particular, a cap at length $`r`$ has total error at most

```math
2\Pr_{g\sim\mu}[\ell(g)>r]+2\delta.
```

The probability tail and the sampling error therefore require separate portions of the requested error budget. A truncated Poisson sampler, approximated transition probabilities, or finite random-bit implementation must supply its actual total-variation guarantee. A floating-point estimate of a tail probability is not itself such a guarantee. For an arbitrary known law, the query theorem does not assert a polynomial-time sampler.

The primitive oracles and algebraic relations are exact in the theorem. Approximate relations are not interchangeable with this promise: shortening a word using an inaccurate relation can produce an error that depends on the original trajectory. Known gate-synthesis errors and deviations of supplied oracles from an exact representation require their own error bounds. No robustness conclusion for approximate group relations is inferred from the exact theorem.

## Resources beyond oracle calls

Classical endpoint sampling, multiplication and reduction of words, geodesic computation, classical memory, target width, ancillary space, known reversible arithmetic, gate synthesis, and measurement are separate resources. The upper theorem allows arbitrary representation-independent computation; it does not bound all of those costs.

For a finite group, one may in principle precompute geodesics by breadth-first search of its Cayley graph. That proves existence of an upper-query procedure and can be computationally expensive in $`|G|`$. In the wreath-product application the normal form gives a more direct representation-independent implementation, but the straightforward sampler still processes a number of Poisson events linear in $`t`$ on average. The [algorithm and resource account](algorithms-and-resources.md) keeps that classical work separate from the sublinear generator-query count.

There is no data-dependent QRAM or free unknown-input state-loading oracle. The target input is supplied once, and the simulator implements a channel on it. The demonstrated acceleration concerns the number of calls to unknown unitary primitives under the stated exact relations. A total-runtime or hardware advantage would require additional evidence.
