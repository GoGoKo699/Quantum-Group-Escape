# From Childs's algorithm notes to group-escape simulation

Use Andrew M. Childs's [*Lecture Notes on Quantum Algorithms*](https://www.cs.umd.edu/~amchilds/qa/), **17 April 2025**, as the single educational anchor. The page numbers below are the printed numbers in that version. The notes introduce the relevant representations, reversible oracles, query bounds, and simulation perspective. This bridge supplies the additional channel and probability ideas used by the project.

The task begins with a register in an arbitrary quantum state. A controller can call certain unknown unitary operations. Their multiplication rules are known: some sequences cancel or give the same operation. The controller must reproduce a specified random mixture of these operations on the register, including its correlations with any untouched external register. Returning one classical endpoint or preparing one convenient output state would be a different task.

## 1. A complete four-element example

Take the cyclic group $`C_4=\{e,a,a^2,a^3\}`$ with $`a^4=e`$ and generators $`a,a^{-1}`$. The supplied unitary $`U=\pi(a)`$ is unknown but obeys $`U^4=I`$. Its inverse is a supplied primitive. Choose the known uniform law on these four elements. This is an example of the arbitrary-law theorem, rather than an assertion about a particular continuous-time walk.

| Sampled exponent $`j`$ | Probability | Short word | Unknown-generator calls |
|---:|---:|---|---:|
| 0 | $`1/4`$ | identity | 0 |
| 1 | $`1/4`$ | $`U`$ | 1 |
| 2 | $`1/4`$ | $`UU`$ | 2 |
| 3 | $`1/4`$ | $`U^{-1}`$ | 1 |

Two fair classical bits choose the row. Apply its word to the supplied input and discard the classical choice. The resulting channel is exactly

```math
\Phi(\rho)=\frac14\left(
\rho+U\rho U^\dagger
+U^2\rho(U^2)^\dagger
+U^{-1}\rho(U^{-1})^\dagger
\right).
```

The maximum call count is two. There is no success condition or postselection, and the implementation works when the input is entangled with a reference.

Now impose a one-call cap. Replace the $`j=2`$ row by the identity and keep the other rows. This changes a set of classical choices of probability $`1/4`$. In the unhalved diamond convention used here,

```math
\lVert \widetilde\Phi-\Phi\rVert _\diamond
=\frac14\lVert \mathrm{Id}-\mathrm{Ad}_{U^2}\rVert _\diamond
\le\frac12.
```

Thus the one-call cap certifies error at most $`1/2`$; it does not certify error $`1/100`$. The factor of two arises because two quantum channels can have diamond distance two. The cap retains every run as a valid output channel. It does not discard and renormalize the unwanted row.

### The same example can carry hidden parity

The upper construction does not prove optimality. To see the lower-bound mechanism, use a particular admissible representation on a four-state group register and one answer qubit. Let $`x_1,x_2`$ be unknown bits and assign these capped distance parities:

| Group label $`j`$ | Distance from 0 | $`F_x(\ell(j))`$ | Answer flip on $`j\mapsto j+1\pmod4`$ |
|---:|---:|---|---|
| 0 | 0 | 0 | $`x_1`$ |
| 1 | 1 | $`x_1`$ | $`x_2`$ |
| 2 | 2 | $`x_1\oplus x_2`$ | $`x_2`$ |
| 3 | 1 | $`x_1`$ | $`x_1`$ |

The gauged generator shifts the group label and performs the indicated answer flip. Around the complete cycle each input bit is flipped twice, so the fourth power is still exactly the identity. Equivalently, this generator is a common conjugation of the ordinary cyclic shift. The unknown bits have changed the representation without breaking its group relation.

Starting from group label zero and answer zero, the ideal channel outputs the full parity $`x_1\oplus x_2`$ at label two. That label occurs with probability $`1/4`$. Measure the group label and answer; use the answer at label two and an independent fair bit elsewhere. The parity success probability is $`1/2+(1/4)/2=5/8`$ on every input string. A channel approximation of unhalved diamond error $`1/100`$ retains success at least $`0.62`$.

Each controlled gauged-generator call can be compiled using two ordinary input-bit queries: compute which bit is needed, query it into a buffer, conditionally flip the answer, and query again to erase the buffer. Childs's reversible-computation and query-polynomial sections explain the ingredients. The general proof gives a lower bound of one supplied-generator call after integer rounding in this toy example; it does not claim that this small example attains every constant in the general bracket. Its purpose is to exhibit the operation, cost, delivered channel, error convention, and measured parity flag in one setting.

## 2. The source sections that lead into the project

| Childs locator | Use here | Project source |
|---|---|---|
| §§1.1–1.2, pp. 1–2; §1.4, pp. 2–3 | Registers, unitary gates, and restoring temporary work | [Model](../science/model.md); [two-query compiler](../science/group-quantiles.md#two-ordinary-bit-queries-implement-a-controlled-generator) |
| §2.1, p. 7 | Tracking errors through a composition | [Implementation error budget](../science/algorithms-and-resources.md#finite-precision-and-the-full-error-budget) |
| §11.1, pp. 47–48 | Representations, regular actions, and common changes of basis | [Representation-preserving gauge](../science/group-quantiles.md#a-representation-that-encodes-distance-parity) |
| §§17.1, 17.3, pp. 73, 75 | Distinguishing classical and coherent walk dynamics | [Continuous-time endpoint laws](../science/model.md#continuous-time-laws) |
| §§21.1–21.3, pp. 97–99; §21.5, pp. 99–100 | Oracle cost, acceptance-polynomial degree, and parity | [Positive-bias converse](../science/group-quantiles.md#positive-bias-suffices-for-the-parity-obstruction) |
| §§27.1–27.2, p. 133; §28.1, pp. 139–140 | Simulation tasks and a parity-based obstruction | [Full theorem](../science/group-quantiles.md); [interpretation](../science/interpretation.md) |

The algebraic route does not require implementing a group Fourier transform. The query route does not require a search algorithm. Read the indicated sections for the objects and proof tools that enter this argument, then return to the linked project statements.

## 3. Translate the notation and the access promise

| Object | This repository's notation | Meaning in the task |
|---|---|---|
| Known finite group | $`G`$, generators $`S`$, identity $`e`$ | A classical algebraic specification |
| Representation (written $`\sigma`$ in Childs §11.1) | $`\pi(g)`$ | Unknown unitary matrices respecting all group products |
| Known left regular action | $`L_g\lvert h\rangle=\lvert gh\rangle`$ | A reference construction used in the converse |
| Oracle input in the parity reduction | $`x=(x_1,\ldots,x_m)`$ | Hidden bits used to instantiate a hard representation |
| One supplied query | controlled $`\mathrm{SELECT}_\pi`$ or its inverse | One charged call, including coherent generator selection |
| Known endpoint law | $`\mu(g)`$ | Classical randomness, not an unknown-data loader |
| Output channel | $`\Phi_{\pi,\mu}`$ | The transformation on every input and reference |
| Word length | $`\ell(g)=\lvert g\rvert_S`$ | The fewest supplied generators needed to spell $`g`$ |

A known multiplication table does not reveal the unknown matrices. Likewise, the mathematical existence of a basis change relating two representations does not make that change of basis a free gate. The lower bound exploits precisely this distinction: its common parity conjugation exists, but is not supplied to the simulator.

The output is

```math
\Phi_{\pi,\mu}(\rho)
=\sum_{g\in G}\mu(g)\pi(g)\rho\pi(g)^\dagger.
```

There is no requirement that the simulator return its internally sampled endpoint. In the lower proof, the group label is part of the deliberately chosen **target representation**, so it can be measured after any valid simulator, regardless of that simulator's internal method.

## 4. The additional channel and probability steps

The selected source is an algorithms anchor. The following statements are supplied locally and should not be assumed merely from its Hamiltonian-simulation chapters.

**Full-channel error.** A density operator $`\rho`$ describes the input state, including classical mixtures. The diamond error tests the implemented map even when that state is correlated with an untouched reference. In the unhalved convention, error $`\varepsilon`$ changes a final event probability by at most $`\varepsilon/2`$. This is the bridge between a simulator guarantee and the parity success calculation. See [the output definition](../science/model.md#the-channel-to-be-implemented).

**Tail replacement.** If endpoint choices of total probability $`\beta`$ are replaced by the identity, convexity gives diamond error at most $`2\beta`$. If the classical endpoint sampler itself has total-variation error $`\delta`$, it contributes another $`2\delta`$. These are separately budgeted errors, as in [the resource account](../science/algorithms-and-resources.md).

**Escape quantiles.** Let $`D=\ell(g)`$ for $`g\sim\mu`$. The quantity

```math
R_\eta(\mu)=\min\{r\in\mathbb Z_{\ge0}:\Pr(D>r)\le\eta\}
```

is the smallest integer radius outside which at most probability $`\eta`$ remains. The theorem is

```math
\frac14R_\varepsilon(\mu)
\le Q_G(\mu,\varepsilon)
\le R_{\varepsilon/2}(\mu).
```

Its two sides use different error levels. An expectation alone cannot replace these radii: a rare, very distant endpoint may be discarded within the allowed error while contributing greatly to the mean distance. The general statement and its integer boundary cases are in [Group quantiles](../science/group-quantiles.md).

**Positive parity bias.** Childs §21.5 explains why parity still needs half as many ordinary bit queries as input bits when the permitted error is any amount below one half. Here a group-distance event of probability $`p_m>\varepsilon`$ leaves a strictly positive bias after simulation error. The repository's common-conjugation construction shows that this parity instance obeys every known group relation. The factor $`1/4`$ combines the ordinary parity bound with two ordinary bit queries per supplied-generator query.

## 5. From one cyclic example to the nonabelian application

In the wreath-product application, a cursor moves along a line and each site has an integer lamp. The cursor move and lamp update do not commute. Updates translated to different sites do commute, which permits compression into final lamp values plus a cursor route.

Conditional on the cursor path, its occupation time $`\ell_x`$ is the total time spent at site $`x`$. The lamp's net signed update has variance $`\lambda_x=\ell_x/2`$. These lamps are conditionally independent. Summing their residual update magnitudes yields the three-quarter distance scale. The project supplies the needed moment, self-intersection, and high-quantile derivations in [Wreath-product escape](../science/wreath-product.md); they are additional probability arguments rather than prerequisite chapters silently added to the anchor.

An infinite walk is used to derive those estimates. [Finite quotients](../science/finite-quotients.md) then proves exact metric preservation in a chosen finite ball, bounds the probability of leaving that ball, and gives finite-dimensional hard representations. The final power law is along a family whose group and target width grow with time.

The direct implementation still generates order $`t`$ classical events on average. Its optimal $`t^{3/4}`$ law concerns calls to unknown represented generators. It does not establish the same scaling for total runtime, preserve a specified coherent bath, or cover approximate group relations without further analysis.

## 6. Continue through the common map

The [thirty milestones](milestones.md) connect these pieces in dependency order. Use the [scientific route](../science/README.md) for the canonical statements and proofs, and [verification](../verification/README.md) for finite implementation checks. Primary research citations remain in [Related work](../references/related-work.md); they provide attribution and comparison, while Childs remains the single educational anchor.

[Learning overview](README.md) · [Milestone map](milestones.md) · [Repository overview](../README.md)
