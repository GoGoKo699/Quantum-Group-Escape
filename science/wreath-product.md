# A bounded-jump example with three-quarter query scaling

The [group-quantile theorem](group-quantiles.md) turns a classical escape estimate into a statement about simulating an unknown quantum channel. This page supplies an explicit nonabelian example: a cursor moves along an integer line, and each visited site carries an integer counter. Diffusion spreads the cursor over order $`\sqrt t`$ sites. The counters accumulated on those sites require order $`t^{3/4}`$ elementary updates after cancellations. The resulting exponent is inherited classical probability; the quantum conclusion uses the representation-preserving lower bound.

## 1. The group and the channel

Write an element of the restricted wreath product $`\mathbb Z\wr\mathbb Z`$ as $`g=(k,\eta)`$, where $`k\in\mathbb Z`$ and $`\eta:\mathbb Z\to\mathbb Z`$ has finite support. The generators $`a`$ and $`b`$ move the cursor one site to the right and increment the lamp at its current site, respectively. Their inverses reverse these actions. This is the standard cursor-and-lamps description of the right Cayley walk. Reversing the multiplication convention gives the same distance law for this symmetric walk.

Let $`S=\{a,a^{-1},b,b^{-1}\}`$. The lamp translations commute:

```math
[a^x b a^{-x},a^y b a^{-y}]=e
\qquad(x,y\in\mathbb Z).
```

For an unknown supplied unitary representation, write $`A=U_a`$ and $`B=U_b`$. The target generator is

```math
\mathcal L_U
=\frac14\left(
\operatorname{Ad}_{A}+\operatorname{Ad}_{A^{-1}}
+\operatorname{Ad}_{B}+\operatorname{Ad}_{B^{-1}}
\right)-\operatorname{Id}.
```

It has four bounded unitary jump terms, total jump rate one, no Hamiltonian term, and is self-adjoint in the Hilbert–Schmidt inner product. The supplied unitaries need not be Hermitian involutions. The [query model](model.md) includes selected inverse and controlled access; it does not provide their unknown matrices as classical input.

The infinite group is a probability and algebraic reference. The actual finite-dimensional hard instances are the explicitly chosen finite quotients in [Finite quotients](finite-quotients.md). Their size grows with the requested time.

## 2. Word length separates lamp work from cursor travel

For $`g=(k,\eta)`$, define

```math
W(g)=\sum_{x\in\mathbb Z}|\eta(x)|,
\qquad
u=\min\bigl(\{0,k\}\cup\operatorname{supp}\eta\bigr),
\qquad
v=\max\bigl(\{0,k\}\cup\operatorname{supp}\eta\bigr).
```

Its exact word length for $`S`$ is

```math
|g|_S=W(g)+2(v-u)-|k|.
\tag{1}
```

Every word must perform at least $`|\eta(x)|`$ updates at each lamp. Its cursor path must start at zero, visit both extreme required sites, and finish at $`k`$. Visiting the left extreme first costs $`2(v-u)-k`$ movement steps; visiting the right extreme first costs $`2(v-u)+k`$. Their minimum gives the travel term in (1). Conversely, perform the necessary signed lamp updates along a minimizing route. This attains the lower bound and proves the formula.

If $`R_t`$ is the number of sites visited by the entire cursor path up to time $`t`$, then its endpoint $`G_t`$ satisfies

```math
W(G_t)\le |G_t|_S\le W(G_t)+2(R_t-1).
\tag{2}
```

Thus a classical endpoint and its word can be obtained by recording net lamp counts and two cursor extremes. This compression reduces the number of supplied-unitary calls; generating the complete random trajectory still takes expected order $`t`$ classical steps.

## 3. Conditional lamp law

The rate-one Poisson walk chooses each element of $`S`$ with probability $`1/4`$. Poisson thinning makes the cursor a continuous-time simple symmetric walk $`X_s`$ of jump rate $`1/2`$. Conditional on its entire path, define occupation times

```math
\ell_x=\int_0^t\mathbf 1_{\{X_s=x\}}\,ds,
\qquad
\lambda_x=\frac{\ell_x}{2},
\qquad
\sum_x\lambda_x=\frac t2.
```

The final lamps $`Z_x=\eta_t(x)`$ are conditionally independent. Each is the difference of two independent Poisson variables of mean $`\ell_x/4`$. In particular,

```math
\mathbb E[Z_x\mid X]=0,
\qquad
\mathbb E[Z_x^2\mid X]=\lambda_x,
\qquad
\mathbb E[Z_x^4\mid X]=3\lambda_x^2+\lambda_x.
\tag{3}
```

All independence assertions in this page are conditional on the cursor path. The occupation times themselves are correlated.

## 4. An upper escape quantile

The cursor is a martingale with $`\mathbb E X_t^2=t/2`$. Doob's inequality and $`R_t\le2\sup_{s\le t}|X_s|+1`$ give, for $`t\ge1`$,

```math
\mathbb E R_t\le 2\sqrt{2t}+1\le4\sqrt t.
\tag{4}
```

Put $`W_t=\sum_x|Z_x|`$. Conditional Cauchy–Schwarz gives

```math
\mathbb E[W_t^2\mid X]
\le R_t\sum_x\mathbb E[Z_x^2\mid X]
=\frac t2R_t.
```

Consequently,

```math
\mathbb E W_t^2\le2t^{3/2},
\qquad
\mathbb E|G_t|_S
\le\sqrt2\,t^{3/4}+8\sqrt t
\le10t^{3/4}.
\tag{5}
```

For every $`0<\alpha<1`$, Markov's inequality therefore supplies the explicit upper quantile

```math
\Pr\!\left\{|G_t|_S>\frac{10}{\alpha}t^{3/4}\right\}
\le\alpha
\qquad(t\ge1).
\tag{6}
```

This is a bounded-query cap after replacing the tail by an ordinary output channel. It does not use postselection.

## 5. A high lower escape quantile

An expectation lower bound alone would not establish the required fixed-error quantum lower bound. We prove a high-probability statement, using the independence of the lamps after conditioning.

### Occupation-time self-intersection

Let $`I_t=\sum_x\lambda_x^2`$. For $`u>0`$, the cursor heat kernel has the Fourier formula

```math
\Pr\{X_u=0\}
=\frac1{2\pi}\int_{-\pi}^{\pi}
\exp\!\left[-\frac u2(1-\cos\theta)\right]\,d\theta
\le\frac{2}{\sqrt u}.
```

The bound follows, for example, from $`1-\cos\theta\ge2\theta^2/\pi^2`$ on this interval and a Gaussian integral. Stationary independent increments then imply

```math
\begin{aligned}
\mathbb E I_t
&=\frac14\int_0^t\int_0^t
\Pr\{X_s=X_u\}\,ds\,du\\
&=\frac12\int_0^t(t-u)\Pr\{X_u=0\}\,du
\le\frac43t^{3/2}.
\end{aligned}
\tag{7}
```

Fix $`0<\delta<1/3`$. Equations (4) and (7) imply that, with probability at least $`1-2\delta`$ over the cursor,

```math
I_t\le\frac{4}{3\delta}t^{3/2},
\qquad
R_t\le\frac4\delta\sqrt t.
\tag{8}
```

### Conditional mean and variance

Hölder's inequality yields

```math
\sum_x\sqrt{\lambda_x}
\ge\frac{(\sum_x\lambda_x)^{3/2}}
{\sqrt{\sum_x\lambda_x^2}}.
\tag{9}
```

On the cursor event (8), its right side is at least $`a_\delta t^{3/4}`$, where

```math
a_\delta=\frac{\sqrt{3\delta}}{4\sqrt2},
\qquad b_\delta=\frac4\delta.
```

For a signed Poisson difference $`Z`$ of variance $`\lambda\ge1`$, (3) and Paley–Zygmund give

```math
\Pr\{Z^2\ge\lambda/2\}
\ge\frac{\lambda^2}{4(3\lambda^2+\lambda)}
\ge\frac1{16}.
```

With $`c_0=1/(16\sqrt2)`$, it follows for every $`\lambda\ge0`$ that

```math
\mathbb E|Z|\ge c_0\sqrt\lambda-c_0.
```

The subtraction makes the last inequality valid also for $`0\le\lambda<1`$. Hence the conditional mean obeys

```math
\mu(X):=\mathbb E[W_t\mid X]
\ge c_0\bigl(a_\delta t^{3/4}-b_\delta\sqrt t\bigr)
\ge k_\delta t^{3/4},
\qquad
k_\delta=\frac{c_0a_\delta}{2},
\tag{10}
```

provided $`t\ge(2b_\delta/a_\delta)^4`$. Conditional independence and (3) give

```math
\operatorname{Var}(W_t\mid X)
\le\sum_x\mathbb E[Z_x^2\mid X]=\frac t2.
```

Thus, on (8),

```math
\Pr\{W_t<\mu(X)/2\mid X\}
\le\frac{2t}{\mu(X)^2}
\le\frac{2}{k_\delta^2\sqrt t}.
\tag{11}
```

Define the finite, conservative threshold

```math
T_\delta=\max\left\{
1,
\left(\frac{2b_\delta}{a_\delta}\right)^4,
\left(\frac{2}{\delta k_\delta^2}\right)^2
\right\},
\qquad c_\delta=\frac{k_\delta}{2}.
```

Combining (8)–(11) with (2) proves

```math
\Pr\{|G_t|_S\ge c_\delta t^{3/4}\}
\ge1-3\delta
\qquad(t\ge T_\delta).
\tag{12}
```

These constants prove existence of a finite threshold. They are not a numerical estimate of a useful simulation crossover. Equations (6) and (12) establish the fixed upper and lower quantile orders required by the quantum theorem.

## 6. Quantum consequence and resource scope

Choose the finite quotients and coupling error as in [Finite quotients](finite-quotients.md). For every fixed $`0<\epsilon\le1/100`$, the worst-case query complexity over their unknown finite-dimensional representations satisfies

```math
Q_{G_t}(t,\epsilon)=\Theta_\epsilon(t^{3/4})
\qquad(t\longrightarrow\infty).
\tag{13}
```

The upper bound simulates the full trace-preserving channel, including arbitrary reference systems. The lower bound applies to arbitrary coherent and adaptive query algorithms, using a representation on a finite regular-register space and an answer qubit. It is not restricted to algorithms that explicitly follow a trajectory.

The four jump types are fixed; the group, its finite relations and the hard representation dimension depend on time. Equation (13) does not assert long-time hardness at one fixed finite dimension. Its sublinear resource is the number of supplied-unitary calls. Straightforward trajectory generation uses order $`t`$ expected classical updates; the theorem does not establish $`t^{3/4}`$ total runtime or a hardware advantage.

## 7. Attribution

The classical wreath-product escape exponent is prior work, including David Revelle, [*Rate of escape of random walks on wreath products and related groups*](https://doi.org/10.1214/aop/1068646371), *Annals of Probability* **31** (2003), 1917–1934. More general prescribed speed behavior is studied by Gideon Amir and Bálint Virág, [*Speed exponents of random walks on groups*](https://arxiv.org/abs/1203.6226), *International Mathematics Research Notices* **2017**, 2567–2598. Equations (3)–(12) provide the self-contained occupation-time argument needed here; no new classical speed exponent is claimed.

Intermediate quantum simulation exponents also predate this example. Gao, Ji and Liu's [Lévy–Khintchine construction](https://arxiv.org/abs/2511.10253) obtains a continuum of exponents through Hamiltonian twirling. The present application concerns bounded, finitely many nonabelian generator jumps and the unrestricted oracle lower supplied by [Group quantiles](group-quantiles.md). The theorem-level comparison is developed in [Related work](../references/related-work.md).

[Model](model.md) · [Group quantiles](group-quantiles.md) · [Finite quotients](finite-quotients.md)
