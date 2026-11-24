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

Now impose a one-call cap. Replace the $`j=2`$ row by the identity and keep the other rows. This changes a set of classical choices of probability $`1/4`$. In the unhalved diamond convention,

```math
\lVert \widetilde\Phi-\Phi\rVert _\diamond
=\frac14\lVert \mathrm{Id}-\mathrm{Ad}_{U^2}\rVert _\diamond
\le\frac12.
```

The one-call cap gives error at most $`1/2`$. The factor of two comes from the maximum diamond distance between two channels. Every run delivers a channel, including those with the replacement.

### Why a one-call cap cannot improve this error

Use $`K`$ four-state group blocks. In block $`i`$, assign independent unknown signs $`x_{i,1},x_{i,2}\in\{-1,1\}`$ to the first and second outward steps. The basis signs, in the order $`e,a,a^2,a^3`$, are $`1,x_{i,1},x_{i,1}x_{i,2},x_{i,1}`$. Conjugation of the cyclic shift by this diagonal sign change preserves $`U^4=I`$. Each generator matrix entry uses at most one sign because a step changes word length by at most one.

Start in an equal superposition of the identity labels across the blocks. If the endpoint is $`a^2`$, the ideal state is an equal superposition of the $`a^2`$ labels, with phase $`x_{i,1}x_{i,2}`$ in block $`i`$. Between two different blocks the corresponding density-matrix entry carries a product of four independent signs. After one call each density-matrix entry has degree at most two in the signs, even after known operations. Orthogonality of products of independent signs therefore makes the average matching coherence vanish for any one-call simulator.

To read that coherence, the proof measures the projection onto the ideal signed superposition and subtracts $`1/K`$ times the probability of the $`a^2`$ label. The subtraction removes the part due to diagonal probabilities alone. The average simulator score is zero, while the ideal score is $`(1-1/K)/4`$. The score has spectral range of length one, so an unhalved diamond error $`\varepsilon`$ allows a score change of at most $`\varepsilon/2`$. Representations of arbitrarily large finite $`K`$ then force $`\varepsilon\ge1/2`$ for any uniform one-call procedure.

### The expected cost can be lower than the cap

The exact sampler uses one call on average. For $`0\le\varepsilon\le1/2`$, replace probability mass $`\varepsilon/2`$ from the two-call row by the identity. This saves $`2(\varepsilon/2)`$ calls on average. The [expected-query theorem](../science/group-quantiles.md#classical-stopping-and-the-exact-mean) proves that $`1-\varepsilon`$ is optimal. For $`\varepsilon\lt1/2`$, the hard cost stays at two even as the optimal expected cost falls.

## 2. The source sections that lead into the project

| Childs locator | Use here | Project source |
|---|---|---|
| §§1.1–1.2, pp. 1–2; §1.4, pp. 2–3 | Registers, unitary gates, and restoring temporary work | [Model](../science/model.md); [representation and generator matrices](../science/group-quantiles.md#radial-signs-in-an-exact-representation) |
| §2.1, p. 7 | Tracking errors through a composition | [Implementation error budget](../science/algorithms-and-resources.md#finite-precision-and-the-full-error-budget) |
| §11.1, pp. 47–48 | Representations, regular actions, and changes of basis | [Radial sign gauge](../science/group-quantiles.md#radial-signs-in-an-exact-representation) |
| §§17.1, 17.3, pp. 73, 75 | Distinguishing classical and coherent walk dynamics | [Continuous-time endpoint laws](../science/model.md#continuous-time-laws) |
| §§21.1–21.3, pp. 97–99; §21.5, pp. 99–100 | Oracle cost, degree growth, and orthogonality of parity characters | [Coherence measurement](../science/group-quantiles.md#a-measurement-of-distant-coherence) |
| §§27.1–27.2, p. 133; §28.1, pp. 139–140 | Simulation tasks and a parity-based obstruction | [Full theorem](../science/group-quantiles.md); [interpretation](../science/interpretation.md) |

The algebraic route does not require implementing a group Fourier transform. The query route does not require a search algorithm. Read the indicated sections for the objects and proof tools that enter this argument, then return to the linked project statements.

## 3. Translate the notation and the access promise

| Object | This repository's notation | Meaning in the task |
|---|---|---|
| Known finite group | $`G`$, generators $`S`$, identity $`e`$ | A classical algebraic specification |
| Representation (written $`\sigma`$ in Childs §11.1) | $`\pi(g)`$ | Unknown unitary matrices respecting all group products |
| Known left regular action | $`L_g\lvert h\rangle=\lvert gh\rangle`$ | A reference construction used in the converse |
| Radial sign variables | $`x_{i,k}\in\{-1,1\}`$ | Independent unknown signs, one for every block and distance step |
| One supplied query | controlled $`\mathrm{SELECT}_\pi`$ or its inverse | One charged call, including coherent generator selection |
| Known endpoint law | $`\mu(g)`$ | Classical randomness, not an unknown-data loader |
| Output channel | $`\Phi_{\pi,\mu}`$ | The transformation on every input and reference |
| Word length | $`\ell(g)=\lvert g\rvert_S`$ | The fewest supplied generators needed to spell $`g`$ |

The group table gives a reference regular action. The radial signs specify a common conjugation of that action for all generators. Only the conjugated generator oracles are supplied to the simulator.

The output is

```math
\Phi_{\pi,\mu}(\rho)
=\sum_{g\in G}\mu(g)\pi(g)\rho\pi(g)^\dagger.
```

There is no requirement that the simulator return its internally sampled endpoint. In the lower proof, the group label is part of the deliberately chosen **target representation**, so it can be measured after any valid simulator, regardless of that simulator's internal method.

## 4. The additional channel and probability steps

The selected source is an algorithms anchor. The following statements are supplied locally and should not be assumed merely from its Hamiltonian-simulation chapters.

**Full-channel error.** A density operator $`\rho`$ describes the input state, including classical mixtures. The diamond error tests the implemented map even when that state is correlated with an untouched reference. In the unhalved convention, error $`\varepsilon`$ changes the expected value of a measurement score with spectral range of length one by at most $`\varepsilon/2`$. See [the output definition](../science/model.md#the-channel-to-be-implemented).

**Tail replacement.** If endpoint choices of total probability $`\beta`$ are replaced by the identity, convexity gives diamond error at most $`2\beta`$. If the classical endpoint sampler itself has total-variation error $`\delta`$, it contributes another $`2\delta`$. These are separately budgeted errors, as in [the resource account](../science/algorithms-and-resources.md).

**Hard query cost.** Let $`D=\ell(g)`$ for $`g\sim\mu`$. The quantity

```math
R_\eta(\mu)=\min\{r\in\mathbb Z_{\ge0}:\Pr(D>r)\le\eta\}
```

is the smallest integer radius outside which at most probability $`\eta`$ remains. The exact hard cost is

```math
Q_G(\mu,\varepsilon)=R_{\varepsilon/2}(\mu).
```

The cap $`q`$ attains the requested error exactly when its overflow mass is at most $`\varepsilon/2`$. See [the finite-group theorem](../science/group-quantiles.md#the-finite-group-theorem).

**Expected cost under classical stopping.** Stop a copy of the simulator at each integer cutoff $`q`$ for analysis. Completed branches have degree at most $`2q`$. The distance-sensitive score then forces enough probability on branches using more than $`q`$ calls. Summing those requirements gives

```math
\sum_{q\ge0}\big(\Pr(D>q)-\varepsilon/2\big)_+.
```

The geodesic procedure attains the sum by redirecting the farthest endpoints to the identity, using a randomized replacement at the boundary distance if needed. At zero error this sum is the original mean distance. See [the expected-query proof](../science/group-quantiles.md#classical-stopping-and-the-exact-mean).

## 5. From one cyclic example to the nonabelian application

In the wreath-product application, a cursor moves along a line and each site has an integer lamp. The cursor move and lamp update do not commute. Updates translated to different sites do commute, which permits compression into final lamp values plus a cursor route.

Conditional on the cursor path, its occupation time $`\ell_x`$ is the total time spent at site $`x`$. The lamp's net signed update has variance $`\lambda_x=\ell_x/2`$. These lamps are conditionally independent. Summing their residual update magnitudes yields the three-quarter distance scale. The project supplies the needed moment, self-intersection, and high-quantile derivations in [Wreath-product escape](../science/wreath-product.md); they are additional probability arguments rather than prerequisite chapters silently added to the anchor.

An infinite walk is used to derive those estimates. [Finite quotients](../science/finite-quotients.md) then proves exact metric preservation in a chosen finite ball, bounds the probability of leaving that ball, and gives finite-dimensional hard representations. The final power law is along a family whose group and target width grow with time.

The direct implementation still generates order $`t`$ classical events on average. Its optimal $`t^{3/4}`$ law concerns calls to unknown represented generators. It does not establish the same scaling for total runtime, preserve a specified coherent bath, or cover approximate group relations without further analysis.

## 6. Continue through the common map

The [thirty milestones](milestones.md) connect these pieces in dependency order. Use the [scientific route](../science/README.md) for the canonical statements and proofs, and [verification](../verification/README.md) for finite implementation checks. Primary research citations remain in [Related work](../references/related-work.md); they provide attribution and comparison, while Childs remains the single educational anchor.

[Learning overview](README.md) · [Milestone map](milestones.md) · [Repository overview](../README.md)
