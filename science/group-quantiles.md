# Error-shifted quantile bounds for group-twirl simulation

A known group law lets a simulator replace a sampled word by a shortest representative of the same group element. The following theorem identifies a matching obstruction to arbitrary coherent query algorithms: an unknown change of basis can encode parity in the distance reached by the known group walk while preserving every group relation.

The result concerns the full quantum channel and the [supplied-generator model](model.md). The endpoint law need not come from a random walk.

## The finite-group theorem

Fix a finite group $`G`$, a known inverse-closed generating set $`S`$, and a known probability law $`\mu`$ on $`G`$. Let

```math
D=\ell(g),\qquad g\sim\mu,
```

and define its upper-tail radius at tolerance $`0\leq\eta<1`$ by

```math
R_{\eta}(\mu)
 =\min\bigl\{r\in\mathbb Z_{\geq0}:
                 \Pr[D>r]\leq\eta\bigr\}.
```

This radius is finite because $`G`$ is finite. The convention includes $`R_0`$, the largest length having positive probability. The event uses a strict inequality $`D>r`$; that convention fixes the integer endpoint in the lower proof.

**Theorem 1.** For every $`0\leq\varepsilon<1`$, the worst-case query cost, uniform over all finite-dimensional unknown representations, satisfies

```math
\frac14 R_{\varepsilon}(\mu)
 \ \leq\ Q_G(\mu,\varepsilon)
 \ \leq\ R_{\varepsilon/2}(\mu).
```

The error is the unhalved diamond norm. More explicitly:

- If $`r\geq0`$ is an integer with $`\Pr[D>r]\leq\varepsilon/2`$, there is a trace-preserving implementation using at most $`r`$ generator queries on every branch.
- If $`m\geq1`$ is an integer with $`\Pr[D\geq m]>\varepsilon`$, every such worst-case simulator uses at least $`m/4`$ queries. Since the query count is an integer, the lower bound can be rounded up.

The lower bound allows coherent SELECT, its inverse, external control, arbitrary ancillas, and adaptive known processing. It does not assume that the simulator follows a trajectory or returns a sampled group endpoint.

The two bounds use different tail-error levels. Without assumptions on the law, their radii can differ substantially. The theorem is therefore an error-shifted quantile bracket, rather than a same-error identity or an unrestricted expectation law.

## A capped geodesic implementation

For each $`g\in G`$, fix a known geodesic word

```math
 g=s_{\ell(g)}\cdots s_1.
```

Sample $`g\sim\mu`$. If $`\ell(g)\leq r`$, apply the corresponding generator queries in order. Otherwise apply the identity. The output map is

```math
\widetilde\Phi^{(r)}_{\pi,\mu}
 =\sum_{\ell(g)\leq r}\mu(g)\mathrm{Ad}_{\pi(g)}
   +\beta_r\mathrm{Id},
\qquad
\beta_r=\Pr[D>r].
```

It is a convex combination of channels, so every branch is part of a completely positive, trace-preserving implementation. The discarded event does not become postselection. Every retained word uses at most $`r`$ queries. By the triangle inequality and the fact that a channel has diamond norm one,

```math
\begin{aligned}
\|\Phi_{\pi,\mu}-\widetilde\Phi^{(r)}_{\pi,\mu}\|_{\diamond}
&=\left\|
  \sum_{\ell(g)>r}\mu(g)
       \bigl(\mathrm{Ad}_{\pi(g)}-\mathrm{Id}\bigr)
  \right\|_{\diamond} \\
&\leq 2\beta_r.
\end{aligned}
```

The estimate is independent of the representation, the target dimension, the input state, and any reference entanglement. Choosing $`r=R_{\varepsilon/2}(\mu)`$ proves the upper bound.

This construction establishes an upper bound on oracle calls. Sampling $`\mu`$ and obtaining a geodesic are known computations whose time and storage are separate resources. Their existence on a finite group does not establish that they are efficient.

## A representation that encodes distance parity

Fix an integer $`m\geq1`$ and an unknown Boolean string $`x=(x_1,\ldots,x_m)`$. Define the capped prefix parity

```math
 F_x(k)=\bigoplus_{i=1}^{\min\{k,m\}}x_i,
\qquad F_x(0)=0.
```

On a group register and an answer qubit, define

```math
 T_x|g,b\rangle
   =|g,b\oplus F_x(\ell(g))\rangle.
```

The operator $`T_x`$ is unitary and self-inverse. Let $`L_g`$ denote the known left regular representation, $`L_g|h\rangle=|gh\rangle`$, and supply the representation

```math
 \pi_x(g)=T_x(L_g\otimes I)T_x.
```

It obeys all group relations exactly:

```math
\begin{aligned}
\pi_x(g)\pi_x(h)
 &=T_x(L_g\otimes I)T_x^2(L_h\otimes I)T_x \\
 &=T_x(L_{gh}\otimes I)T_x
 =\pi_x(gh).
\end{aligned}
```

In particular, inverse and commutation promises remain valid. This is an admissible representation of dimension $`2|G|`$. A qubit implementation can pad it by a trivial representation if a power-of-two target dimension is required.

The lower argument does not assume a free implementation of $`T_x`$. It implements only the supplied generators by the following local compiler.

## Two ordinary bit queries implement a controlled generator

Use the standard Boolean oracle

```math
 O_x|i,z\rangle=|i,z\oplus x_i\rangle,
\qquad i\in\{1,\ldots,m\}.
```

Consider a generator label $`s`$, a group state $`g`$, and an external control bit $`c`$, all of which may occur coherently. Put

```math
 h=\begin{cases}sg,&c=1,\\g,&c=0,\end{cases}
\qquad d=\ell(g),\quad d'=\ell(h).
```

The metric inequality gives $`|d-d'|\leq1`$. Consequently

```math
F_x(d)\oplus F_x(d')
 =\begin{cases}
 x_{\max\{d,d'\}},&d\neq d'\text{ and }\max\{d,d'\}\leq m,\\
 0,&\text{otherwise}.
 \end{cases}
```

Known reversible group and metric arithmetic computes an active flag $`a`$ for the first case and its address $`i=\max\{d,d'\}`$. On inactive branches choose the valid dummy address $`i=1`$. This is possible because $`m\geq1`$; no additional oracle address with a promised zero bit is needed.

The circuit performs the following sequence:

1. Compute $`a`$ and $`i`$ into clean known work registers, retaining $`c,s,g`$.
2. Query $`O_x`$ into a clean buffer bit $`z`$.
3. Flip the answer qubit by $`z`$ controlled on $`a=1`$.
4. Query $`O_x`$ again to erase $`z`$.
5. Uncompute the address, flag, and known arithmetic, then apply the known group shift $`g\mapsto h`$ controlled on $`c`$.

The resulting action is exactly the externally controlled $`\pi_x(s)`$. Inactive branches may query an unknown dummy bit, but the two calls erase it and perform no answer flip. All work is restored. The argument is linear on superpositions, so it implements coherent selection over $`s`$ as well as a fixed generator. Replacing $`s`$ by $`s^{-1}`$ covers inverse calls and SELECT inverses with the same two-query cost.

There is no free controlled Boolean-oracle assumption in this compiler. Both oracle invocations are ordinary $`O_x`$ calls; the conditional action is supplied by known reversible computation between them. Thus every permitted supplied-generator query of a simulator can be replaced by at most two Boolean queries, including in an adaptive algorithm.

## The channel reveals full parity above a known radius

Use the input $`|e,0\rangle`$, which is independent of $`x`$. Since $`T_x|e,0\rangle=|e,0\rangle`$,

```math
 \pi_x(g)|e,0\rangle
   =|g,F_x(\ell(g))\rangle.
```

The ideal channel output is therefore

```math
 \Phi_{\pi_x,\mu}(|e,0\rangle\!\langle e,0|)
 =\sum_{g\in G}\mu(g)
  |g,F_x(\ell(g))\rangle\!\langle g,F_x(\ell(g))|.
```

Measure the group register and answer bit. If $`\ell(g)\geq m`$, return the answer; otherwise return an independent fair bit. Writing

```math
 p_m=\Pr[D\geq m],
```

the exact procedure returns the full parity $`\bigoplus_{i=1}^m x_i`$ with success probability

```math
 \frac12+\frac{p_m}{2}
```

on every Boolean input. The group-measurement flag is known and its distribution does not depend on $`x`$.

Now replace the ideal channel by any simulator satisfying the uniform diamond guarantee. Its parity success probability is at least

```math
 \frac12+\frac{p_m-\varepsilon}{2}.
```

This follows from the measurement-probability bound for the unhalved diamond convention. It does not require that the simulator expose its internal trajectory or that its output have the ideal block-diagonal form. If $`p_m>\varepsilon`$, the success bias is strictly positive on every input.

## Positive bias suffices for the parity obstruction

A quantum algorithm using at most $`k`$ ordinary Boolean-oracle queries has an acceptance probability given on Boolean inputs by a multilinear polynomial of degree at most $`2k`$. This is the polynomial method of [Beals, Buhrman, Cleve, Mosca and de Wolf](https://arxiv.org/abs/quant-ph/9802049).

Here the compiled simulator uses at most $`2q`$ Boolean queries. If $`P(x)`$ is its final probability of returning one, then $`H(x)=1-2P(x)`$ has degree at most $`4q`$. Let

```math
 \chi(x)=(-1)^{x_1+\cdots+x_m}.
```

Strictly positive parity bias gives

```math
 \chi(x)H(x)\geq p_m-\varepsilon>0
 \quad\text{for every }x.
```

Every multilinear polynomial of degree less than $`m`$ is orthogonal to $`\chi`$ under the uniform Boolean law: each monomial omits a variable whose signed average is zero. If $`4q<m`$, it would follow that

```math
 2^{-m}\sum_x\chi(x)H(x)=0,
```

contradicting the strict positive lower bound. Hence $`4q\geq m`$.

This proof needs no amplification and no bias bounded away from zero as parameters vary. The assumption $`p_m>\varepsilon`$ is therefore sufficient even near a quantile boundary. The polynomial bound applies to adaptive measurements and randomness by deferring measurements, or equivalently by the usual acceptance-probability argument for a maximum-query algorithm. It does not apply to free postselection or replace the maximum-query convention by an expected-query convention.

Finally, if $`R_{\varepsilon}(\mu)>0`$, minimality of that radius gives

```math
 \Pr[D\geq R_{\varepsilon}(\mu)]
 =\Pr[D>R_{\varepsilon}(\mu)-1]>\varepsilon.
```

Take $`m=R_{\varepsilon}(\mu)`$. If that radius is zero, the lower bound is trivial. This completes Theorem 1, including the integer and exact-error cases.

## Numerical laws and reserved error

For any two endpoint laws,

```math
 \|\Phi_{\pi,\mu}-\Phi_{\pi,\widehat\mu}\|_{\diamond}
 \leq\sum_g|\mu(g)-\widehat\mu(g)|
 =2\|\mu-\widehat\mu\|_{\mathrm{TV}}.
```

Let $`C_r(g)`$ retain $`g`$ when $`\ell(g)\leq r`$ and otherwise replace it by $`e`$. If the implemented sampler has total-variation error at most $`\delta`$, its capped pushforward differs from the ideal capped pushforward by at most $`\delta`$. The implemented channel therefore satisfies

```math
 \|\Phi_{\pi,\mu}-\widetilde\Phi_{\pi}\|_{\diamond}
 \leq 2\Pr[D>r]+2\delta.
```

This establishes a concrete finite-precision version of the upper bound whenever the sampler and its total-variation certificate are supplied. Approximate tail evaluation must leave a proved margin in this inequality. The exact-law theorem does not certify a numerical sampler or charge its execution time. The lower theorem concerns the exact target law; if a different law is chosen as the target, its tail probabilities must be used instead.

## Turning the bracket into an escape-rate law

For a family of laws $`\mu_t`$ and a positive scale $`a_t`$, the quantile bracket yields $`Q_G(\mu_t,\varepsilon)=\Theta(a_t)`$ at a fixed error when there are constants $`c,C>0`$ for which

```math
 \Pr[D_t\geq c a_t]>\varepsilon,
 \qquad
 \Pr[D_t>C a_t]\leq\varepsilon/2,
```

with harmless integer rounding for sufficiently large $`a_t`$. Those are properties of the actual law; a claim about the mean alone does not supply them.

A useful sufficient condition at sufficiently small fixed error is a two-moment comparison,

```math
 \mathbb E D_t\geq c_0a_t,
 \qquad
 \mathbb E D_t^2\leq C_0a_t^2.
```

Paley-Zygmund gives

```math
 \Pr[D_t\geq \tfrac12\mathbb E D_t]
 \geq\frac{(\mathbb E D_t)^2}{4\mathbb E D_t^2}
 \geq\frac{c_0^2}{4C_0},
```

while Markov gives an upper fixed quantile using $`\mathbb E D_t\leq\sqrt{C_0}a_t`$. Thus these moment assumptions prove a matching law for each fixed $`\varepsilon<c_0^2/(4C_0)`$. A claim at larger fixed error needs a stronger lower-quantile estimate. The [wreath-product analysis](wreath-product.md) supplies the estimates used for its own error regime, and the [finite-quotient analysis](finite-quotients.md) accounts for their transfer to finite groups.

The need for quantiles is substantive. For example, let $`\mu=(1-\alpha)\delta_e+\alpha\delta_g`$, where $`\ell(g)=L`$ and $`0<\alpha\leq\varepsilon/2`$. Returning the identity uses zero queries and has diamond error at most $`2\alpha\leq\varepsilon`$, even though

```math
 \mathbb E D=\alpha L
```

can grow without bound in a family of groups. Therefore $`Q=\Theta(\mathbb E D)`$ is false for arbitrary laws at fixed positive error.

## Relation to earlier mechanisms

The stochastic expansion of a random-unitary generator, algebraic word cancellation, and the parity query lower bound are inherited ingredients. A tree-based radial parity implementation appears in [Quantum-Dephasing-Threshold](https://github.com/GoGoKo699/Quantum-Dephasing-Threshold), including its [lower-bound account](https://github.com/GoGoKo699/Quantum-Dephasing-Threshold/blob/main/science/lower-bounds.md).

The global conjugation above makes the hard oracles a representation of the entire finite group. It therefore preserves relations involving cycles and commuting translated generators while still supporting arbitrary coherent known controls. This is the step used to pass from a tree-specialized cancellation argument to the finite-group, arbitrary-law, error-quantile theorem. The [related-work comparison](../references/related-work.md) distinguishes this statement from other notions of random-walk and Lindbladian fast forwarding.
