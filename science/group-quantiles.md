# Exact query laws for group-twirl simulation

A known group law lets a simulator replace a sampled word by a shortest word for its endpoint. The theorem below identifies exactly how much error can buy shorter words or fewer calls on average. The target is the full quantum channel in the [supplied-generator model](model.md). The endpoint law may be any known law on the finite group.

## The finite-group theorem

Let $`G`$ be a finite group with a known inverse-closed generating set $`S`$. For an endpoint $`g\sim\mu`$, write $`D=\ell(g)`$ for its shortest-word distance and $`d=\max_{g\in G}\ell(g)`$ for the diameter. Define

```math
\beta_q=\Pr[D>q],
\qquad
R_\eta=\min\{q\in\mathbb Z_{\ge0}:\beta_q\le\eta\},
\qquad 0\le\eta\le1.
```

**Theorem.** With a hard cap of $`q`$ supplied-generator calls, the dimension-uniform minimax unhalved diamond error is $`2\beta_q`$. Thus the smallest hard cap for error $`0\le\varepsilon\le2`$ is

```math
Q_G(\mu,\varepsilon)=R_{\varepsilon/2}.
```

If the number of calls $`N`$ is determined by a classically recorded stopping time, the smallest uniformly guaranteed expected number of calls at the same error is

```math
Q_G^{\mathrm{mean}}(\mu,\varepsilon)
=\sum_{q=0}^{d-1}\bigl(\beta_q-\varepsilon/2\bigr)_+,
\qquad (x)_+=\max\{x,0\}.
```

The same sampler attains every tail in this sum. Both statements allow coherent SELECT, its inverse, external control, ancillas and adaptive known processing. The algorithm can depend on the target dimension, and must work for every representation of that dimension. The upper guarantees are uniform over inputs, including states entangled with an untouched reference.

## A capped geodesic implementation

Sample $`g\sim\mu`$ and apply a shortest representing word if $`\ell(g)\le q`$. Otherwise return the input by applying the identity. The implemented channel is

```math
\widetilde\Phi^{(q)}_{\pi,\mu}
=\sum_{\ell(g)\le q}\mu(g)\mathrm{Ad}_{\pi(g)}+\beta_q\mathrm{Id}.
```

Every branch belongs to the delivered trace-preserving map, and every retained word uses at most $`q`$ queries. Each difference $`\mathrm{Ad}_{\pi(g)}-\mathrm{Id}`$ has diamond norm at most two, so this implementation has error at most $`2\beta_q`$.

## Radial signs in an exact representation

For an integer $`K\ge2`$, use $`K`$ copies of the left regular representation. For each copy $`j`$ and depth $`h=1,\ldots,d`$, choose an independent uniform sign $`x_{j,h}`$. Let

```math
a_j(g)=\prod_{h=1}^{\ell(g)}x_{j,h},
\qquad
T_x|j,g\rangle=a_j(g)|j,g\rangle,
\qquad
\pi_x(g)=T_x(I_K\otimes L_g)T_x,
```

where $`L_g|u\rangle=|gu\rangle`$ and an empty product is one. The same conjugation applies to every element and $`T_x^2=I`$, so each $`\pi_x`$ obeys all relations in $`G`$ exactly. One generator step changes $`\ell(u)`$ by at most one. Therefore every nonzero matrix entry of a controlled SELECT call, forward or inverse, is one or a single sign. If the distance stays the same, the two prefixes cancel completely. If it changes by one, precisely the sign at the larger depth remains.

After at most $`q`$ calls, each entry of the simulator's output density matrix on a fixed input is a polynomial of degree at most $`2q`$ in the signs. Conjugating by an oracle adds at most one degree on each side of the density matrix, and known operations are linear in its entries. For adaptive processing, the same count applies to unnormalized branches and their sum. Equivalently, a circuit can keep measurement outcomes coherently and pad terminal branches with the identity using controlled SELECT. Replacing $`x_{j,h}^2`$ by one makes the polynomials multilinear without increasing their degree. Distinct products of signs are orthogonal under the uniform sign law. This is the polynomial-method degree argument, applied directly to the supplied representation instead of compiling each query into a separate bit oracle.

## A measurement of distant coherence

Use the same input for every sign assignment,

```math
|\psi_{\rm in}\rangle=\frac1{\sqrt K}\sum_{j=1}^K|j,e\rangle.
```

The ideal channel produces a mixture of states with one pure state for each endpoint,

```math
|\psi_g(x)\rangle=\frac1{\sqrt K}\sum_{j=1}^K a_j(g)|j,g\rangle,
\qquad
\rho_x^{\rm ideal}=\sum_{g\in G}\mu(g)|\psi_g(x)\rangle\langle\psi_g(x)|.
```

Let $`\Pi_g`$ project onto the $`K`$-dimensional subspace spanned by the copies of $`g`$. For a given budget $`q`$, use the effect

```math
E_{x,q}
=\sum_{\ell(g)>q}|\psi_g(x)\rangle\langle\psi_g(x)|
+\frac1K\sum_{\ell(g)\le q}\Pi_g.
```

The endpoint subspaces are orthogonal, so the operator lies between zero and the identity. Its ideal acceptance is $`\beta_q+(1-\beta_q)/K`$. In a far endpoint block, the diagonal coefficients of the effect are $`1/K`$. The coefficient between distinct copies $`j`$ and $`k`$ is proportional to $`a_j(g)a_k(g)`$, a product of $`2\ell(g)>2q`$ independent signs. Its correlation with each $`q`$-query output entry vanishes by orthogonality. The near blocks already contribute their diagonal trace divided by $`K`$. Consequently the acceptance on any $`q`$-query simulator, averaged over the sign assignments, is exactly $`1/K`$.

The test may depend on $`x`$ because it witnesses the trace distance on the representation chosen for the lower bound. No access to that test is required of the simulator. A difference in acceptance is at most half the trace norm of the output difference. Thus in dimension $`K|G|`$, some represented channel has unhalved diamond error at least

```math
2\beta_q(1-1/K)
```

for every candidate simulator. Taking the supremum over finite dimensions yields $`2\beta_q`$. The capped sampler attains this uniform error bound. In particular, equality at $`\beta_q=\varepsilon/2`$ qualifies for the stated query cap. At a prescribed finite dimension, the construction gives the displayed finite-$`K`$ bound whenever that many copies fit. Extra dimensions may carry a trivial representation, with the measurement effect set to the identity divided by the number of copies on that block.

## Classical stopping and the exact mean

Consider an $`\varepsilon`$-accurate simulator with a classical record of whether it will make another call. Its query count is $`N`$. For each $`q`$, form a capped version that aborts just before call $`q+1`$ and returns a fixed valid state on those histories. Outputs on histories with $`N\le q`$ are identical. For any effect, the acceptance difference between the capped and original simulator is therefore at most $`\Pr_x(N>q)`$ on the fixed input above. The subscript denotes the representation, with probability over the simulator's recorded histories.

For the effect $`E_{x,q}`$, accuracy bounds the original acceptance below by the ideal acceptance minus $`\varepsilon/2`$. The capped simulator has average acceptance $`1/K`$ by the hard-cap proof. Therefore

```math
\mathbb E_x\Pr_x(N>q)
\ge\bigl[(1-1/K)\beta_q-\varepsilon/2\bigr]_+.
```

All these inequalities use the same dimension, sign ensemble and input, so their sum bounds the ensemble average of the expected query count. Indeed, $`\mathbb E_x\mathbb E[N\mid x]`$ is at least the sum of the left sides for $`q=0,\ldots,d-1`$. The uniformly guaranteed expected budget must be at least that average. Taking $`K`$ arbitrarily large gives the lower bound for $`Q_G^{\mathrm{mean}}`$.

For achievability, remove mass $`m=\min\{\varepsilon/2,\beta_0\}`$ from the farthest nonidentity distances, and redirect it to the identity. If a distance shell straddles the cutoff, thin it with a known probability chosen to remove the required fraction. Sample from the resulting law and apply a shortest word. The change in each branch redirected to the identity has diamond cost at most two per unit mass, so the error is at most $`2m\le\varepsilon`$. The original shell union $`\{D>q\}`$ loses exactly $`\min\{m,\beta_q\}`$ of its mass. Thus the actual query count of this sampler satisfies

```math
\Pr(N>q)=\beta_q-\min\{m,\beta_q\}
=(\beta_q-\varepsilon/2)_+
\qquad(q\ge0).
```

The tail-sum formula proves the exact mean. The trimming rule uses the known endpoint law to determine the cutoff and tie probability. Exact classical sampling of the designated law is part of the oracle-cost model.

## Numerical laws and reserved error

For two laws $`\mu`$ and $`\widehat\mu`$, their random-unitary channels differ in diamond norm by at most $`2\mathrm{TV}(\mu,\widehat\mu)`$. In particular, if a numerical sampler approximates the designated trimmed law to total-variation error at most $`\delta`$, the error bound is $`2m+2\delta`$ plus any gate error. The same reasoning gives $`2\beta_q+2\delta`$ for a hard cap when the sampled law is pushed through the exact cutoff. Certified approximate sampling and gate synthesis need a reserved portion of the error budget. See [Algorithms and resources](algorithms-and-resources.md) for a finite-bit implementation account.

## From the tail law to escape rates

For a family of endpoint distances $`D_t`$ and a scale $`a_t`$, the hard-cap formula gives $`\Theta(a_t)`$ queries at fixed error when $`\Pr(D_t\ge ca_t)>\varepsilon/2`$ and $`\Pr(D_t>Ca_t)\le\varepsilon/2`$ for suitable constants $`c,C>0`$, with integer rounding. A lower bound on $`\mathbb E D_t`$ together with a matching upper bound on $`\mathbb E D_t^2`$ gives the required lower-tail estimate for sufficiently small fixed error by Paley–Zygmund. An upper bound on $`\mathbb E D_t`$ gives the upper quantile by Markov. The [wreath-product analysis](wreath-product.md) instead proves its required upper and lower quantiles directly and [transfers them to finite groups](finite-quotients.md).

For a law that puts probability $`b`$ on one endpoint of length $`L>0`$ and the remainder on the identity, the optimal hard cap is zero for $`b\le\varepsilon/2`$ and $`L`$ for $`b>\varepsilon/2`$. The optimal mean is $`L(b-\varepsilon/2)_+`$. The raw mean escape $`bL`$ can be large below the cutoff. The location of the tail relative to the error budget determines the operational cost.

The [related-work comparison](../references/related-work.md) credits the inherited group twirl, word cancellation and polynomial method, and compares the coherence witness with the earlier parity argument.

[Model](model.md) · [Algorithms and resources](algorithms-and-resources.md) · [Interpretation](interpretation.md)
