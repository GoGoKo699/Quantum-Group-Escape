# Finite quotients and the size of the hard instances

The [integer-lamp walk](wreath-product.md) is most easily analyzed on an infinite group. Quantum query lower bounds here use finite-dimensional representations. This page gives the finite groups, an exact word-ball comparison, and the resulting dimension bound.

## 1. A quotient chosen for each requested time

Fix $`t\ge1`$ and $`0\lt \epsilon\le1/100`$. Put

```math
\delta=\frac{\epsilon}{8},
\qquad
B_t=\left\lceil4t+\log\frac1\delta\right\rceil,
\qquad
L_t=M_t=2B_t+1,
```

where $`\log`$ is natural. Use the finite wreath product

```math
G_t=\mathbb Z_{M_t}\wr\mathbb Z_{L_t}.
\qquad (1)
```

An element is a cursor $`k\in\mathbb Z_{L_t}`$ and one $`\mathbb Z_{M_t}`$ lamp at every cursor site. The four generators again move the cursor by one step or change its current lamp by one unit. The group has

```math
|G_t|=L_tM_t^{L_t}
\qquad (2)
```

elements. The quotient map from $`\mathbb Z\wr\mathbb Z`$ reduces the cursor modulo $`L_t`$ and sums all lamps at congruent sites modulo $`M_t`$. It is a group homomorphism and maps each named generator to its finite counterpart.

The word metric is always measured using these four named generators. Their finite orders and all translated-lamp commutation relations are part of the known group promise.

## 2. Injectivity and exact metric preservation

We first give a deterministic statement. Let $`L,M>2B`$ and let $`\pi:\mathbb Z\wr\mathbb Z\to\mathbb Z_M\wr\mathbb Z_L`$ be the quotient map. No nonidentity element represented by a word of length at most $`2B`$ lies in its kernel.

To prove this, follow such a word. The cursor visits an integer interval of diameter at most $`2B\lt L`$, so distinct visited sites have distinct residues modulo $`L`$. Its final integer cursor position has absolute value at most $`2B`$; if it is zero modulo $`L`$, it is zero as an integer. At each visited site the net lamp value has absolute value at most $`2B\lt M`$. If that value is zero modulo $`M`$, it too is zero as an integer. Since different visited sites do not merge under the quotient, a trivial quotient endpoint forces the original endpoint to be the identity.

It follows that $`\pi`$ is injective on the word ball of radius $`B`$: equality of two images would put their quotient difference, of word length at most $`2B`$, in the kernel. More strongly,

```math
|\pi(g)|_{S_{L,M}}=|g|_S
\qquad\text{whenever }|g|_S\le B.
\qquad (3)
```

Indeed the quotient cannot increase word length. If a strictly shorter quotient word represented $`\pi(g)`$, lift that word to the infinite group. Its difference from $`g`$ has length at most $`2B`$, so the kernel statement forces the lift to equal $`g`$, contradicting minimality of $`|g|_S`$. This proves a geodesic comparison; absence of visible cursor wrapping alone would not have been enough.

## 3. Coupling the two walks

Couple the finite and infinite walks using the same rate-one Poisson event count $`N_t`$ and the same four-letter increment word. On $`N_t\le B_t`$, the infinite endpoint has word length at most $`B_t`$, so (3) gives exact equality of the two endpoint distances.

The exponential moment of a Poisson variable is

```math
\mathbb E e^{N_t}=\exp[(e-1)t].
```

Since $`e-1\lt 4`$, the chosen cap gives

```math
\Pr\{N_t>B_t\}
\le\exp[(e-1)t-B_t]
\le\delta.
\qquad (4)
```

Write $`D_t`$ for infinite-group distance and $`\overline D_t`$ for finite-group distance. For every integer threshold $`m`$,

```math
\left|\Pr\{\overline D_t\ge m\}-\Pr\{D_t\ge m\}\right|
\le\delta.
\qquad (5)
```

The same bound holds for strict-tail events. This comparison is uniform in the threshold, and requires no exchange of a time limit with a fixed quotient limit. Each requested time has its own explicitly specified finite group.

## 4. Transfer to the query theorem

For the upper bound, (6) of [the wreath-product analysis](wreath-product.md#4-an-upper-escape-quantile) gives, after integer rounding,

```math
q_t=\left\lceil\frac{40}{\epsilon}t^{3/4}\right\rceil,
\qquad
\Pr\{D_t>q_t\}\le\frac{\epsilon}{4}.
```

Equations (4)–(5) imply

```math
\Pr\{\overline D_t>q_t\}
\le\frac{\epsilon}{4}+\frac{\epsilon}{8}
\lt \frac{\epsilon}{2}.
```

Thus the [group-quantile upper bound](group-quantiles.md) yields a simulator with at most $`q_t`$ supplied-generator calls and unhalved diamond error at most $`\epsilon`$. As always in that theorem, probability generation and known group computations have their own classical costs.

For the lower bound, fix $`\zeta=1/20`$ in (12) of [the wreath-product analysis](wreath-product.md#5-a-high-lower-escape-quantile). There are absolute constants $`c>0`$ and $`T\lt \infty`$ such that

```math
\Pr\{D_t\ge ct^{3/4}\}\ge\frac{17}{20}
\qquad(t\ge T).
```

Let $`m_t=\lfloor ct^{3/4}\rfloor`$. For $`t\ge T`$ and $`m_t\ge1`$,

```math
\Pr\{\overline D_t\ge m_t\}
\ge\frac{17}{20}-\frac{\epsilon}{8}
>\epsilon.
```

The representation-preserving parity lower bound therefore gives

```math
Q_{G_t}(t,\epsilon)\ge\frac{m_t}{4}.
```

Together with the upper bound, this proves

```math
Q_{G_t}(t,\epsilon)=\Theta_\epsilon(t^{3/4})
\qquad(t\longrightarrow\infty),
\qquad0\lt \epsilon\le\frac1{100}\text{ fixed}.
\qquad (6)
```

The quantile comparisons themselves are finite-time statements. Equation (6) is an asymptotic statement along this time-dependent family of finite groups, and does not require a separate small-time lower-bound convention.

## 5. Exact finite word length is a known computation

For any finite quotient element $`(k,\eta)`$, define its minimal lamp work

```math
W_M(\eta)=\sum_{x\in\mathbb Z_L}
\min\{\eta(x),M-\eta(x)\},
```

using residues $`0\le\eta(x)\lt M`$. Let $`K=\{0,k\}\cup\mathrm{supp}\eta`$. Its word length is exactly

```math
|(k,\eta)|_{S_{L,M}}=W_M(\eta)+\tau_L(K;0,k),
\qquad (7)
```

where $`\tau_L`$ is the length of a shortest cursor walk on the known cycle that starts at zero, visits $`K`$, and ends at $`k`$. The lower bound is immediate from required lamp changes and cursor visits. It is attained by performing a shortest signed lamp update when the chosen route visits each required site.

There is a direct polynomial algorithm for $`\tau_L`$. Enumerate a cycle edge to delete. The remaining graph is a path; order its vertices from $`0`$ to $`L-1`$ in the cut coordinate system. If $`u,v`$ are the extreme required coordinates and $`r,s`$ the coordinates of the start and finish, its minimum visiting length is

```math
\min\{\,|r-u|+(v-u)+|v-s|,
|r-v|+(v-u)+|u-s|\,\}.
```

Take the minimum over all deleted edges and the additional candidate $`L+d_{\mathbb Z_L}(0,k)`$. The additional candidate covers routes that use every cycle edge: such a route must have length at least $`L+d_{\mathbb Z_L}(0,k)`$, and duplicating a shortest zero-to-$`k`$ path in the cycle gives an Euler trail attaining that length. Any route that omits an edge is covered by one of the path cases. This proves the algorithm and formula (7). A straightforward implementation uses $`O(L^2)`$ elementary scans and arithmetic, plus the lamp scan. Faster known bookkeeping is not required by the query lower bound.

These distance calculations depend only on the known group and the computational basis label. In the hard-oracle compiler they can be implemented reversibly, followed by uncomputation. Their gate cost is not an extra call to the unknown input-bit oracle. This distinction is why an unrestricted quantum query lower bound can coexist with substantial known classical or reversible work.

## 6. Dimension and counted workspace

The hard representation in [Group quantiles](group-quantiles.md) acts on

```math
\mathbb C[G_t]\otimes\mathbb C^2,
\qquad
d_t=2L_tM_t^{L_t}.
```

It consists of a regular group register and one answer qubit, conjugated by the unknown parity gauge. All relations of the finite group are preserved exactly. Its target can be embedded into

```math
n_t=\left\lceil\log_2(2L_tM_t^{L_t})\right\rceil
=O_\epsilon\bigl(t\log(t+2)\bigr)
\qquad (8)
```

qubits. Invalid binary basis labels may be given a trivial representation block. This is an explicit sufficient width, not a width optimum. Separate work registers used by a simulator or by the bit-query reduction are not target qubits and are not hidden in (8).

The growing width is essential to the stated result. No linear or three-quarter long-time lower bound at a fixed finite target dimension follows from this family. Conversely, the simulator's upper guarantee applies to every supplied finite-dimensional representation of the chosen finite group, rather than only to the regular representation used in the lower bound.

[Model](model.md) · [Group quantiles](group-quantiles.md) · [Wreath-product escape](wreath-product.md)
