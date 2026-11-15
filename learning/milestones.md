# Thirty milestones for understanding group-escape simulation

This map follows one scientific story: a known random word can have a short endpoint description, and a representation-preserving parity construction can make that endpoint distance an unavoidable quantum-query cost. The final example connects the theorem to the occupation times of a cursor-and-lamps walk.

The first **12 milestones are background/preliminaries**. They assemble the state, algebra, oracle, probability and error notions needed to state the task. The remaining **18 milestones are narrative/innovation**. They connect the upper and lower mechanisms, then build the finite nonabelian example and assess its complete resource scope. Each phase proceeds from individual objects to an integrated account. The map covers the load-bearing scientific ideas, rather than every calculation or neighboring subject.

The single educational anchor is Andrew M. Childs, [*Lecture Notes on Quantum Algorithms*](https://www.cs.umd.edu/~amchilds/qa/), **17 April 2025**. Start with the [source bridge](childs-bridge.md) for the notation translation and worked finite-group example. Section numbers below refer to that version; page numbers are the notes' printed pages. Childs supplies the circuit, representation, query, polynomial and Hamiltonian-simulation foundations. Density-operator channels, diamond error, the Poisson group law, escape quantiles, occupation-time estimates and the new group-quantile proof are supplied in this repository. A source pointer to a nearby Childs topic does not attribute those project-specific extensions to the notes.

## Background/preliminaries — M01–M12

### M01 — Registers, unitary actions and an untouched reference

**Central question:** What does it mean to apply an operation to one quantum register while leaving another register untouched?

**Understanding target:** Explain basis labels, superposition, tensor products, unitary action and computational-basis measurement. Identify the represented system and a possible reference, including an entangled input.

**Dependencies and story role:** No earlier milestone is required. This supplies the individual quantum objects that the channel guarantee must eventually cover.

**Conceptual connection:** A group label can be stored in a quantum register, but its label and the unknown physical unitary representing it are different objects.

**Source pointers:** Childs §§1.1–1.2, printed p. 1; [Model: the channel](../science/model.md#the-channel-to-be-implemented) and [the known group](../science/model.md#a-known-group-and-an-unknown-representation). The reference-system channel guarantee is developed locally.

### M02 — A mixture of operations is a channel

**Central question:** What output is produced when a classical random choice selects a unitary and its choice record is discarded?

**Understanding target:** Interpret the density operator as the state used to predict measurement probabilities, and explain a convex mixture of unitary channels. Distinguish that delivered channel from a coherent sum of unitaries or a specified retained environment.

**Dependencies and story role:** Requires M01. It changes the task from following one state vector to implementing one map on arbitrary states.

**Conceptual connection:** Several jump histories may be replaced without preserving their records if the resulting reduced system channel remains the same.

**Source pointers:** Childs §§1.1–1.2 for unitary circuit foundations and §28.3, printed pp. 140–142, for the distinct coherent linear-combination construction; [Model: target channel](../science/model.md#the-channel-to-be-implemented) and [Interpretation: output scope](../science/interpretation.md#resource-boundaries). The channel formalism is project-supplied.

### M03 — Group elements, words and distance

**Central question:** How can a long sequence of named moves describe the same endpoint as a shorter sequence?

**Understanding target:** Explain identity, inverse, multiplication, generating set, relations and shortest-word length. Use the fact that a generator changes distance from the identity by at most one.

**Dependencies and story role:** Requires M01 for group-register labels. It supplies the local geometric quantity whose distribution later controls query cost.

**Conceptual connection:** Algebraic equality of endpoints allows exact removal of work; word length measures that work using the actual permitted primitive alphabet.

**Source pointers:** Childs §11.1, printed pp. 47–48, for the group-representation setting; [Model: group and word length](../science/model.md#a-known-group-and-an-unknown-representation). The word metric and its resource meaning are developed locally.

### M04 — A known group can have an unknown representation

**Central question:** What is known when all algebraic relations are specified but the unitaries implementing the generators remain unknown?

**Understanding target:** Explain a unitary representation, the left regular representation, and a simultaneous change of basis. Distinguish knowing group multiplication from possessing a free implementation of the supplied representation.

**Dependencies and story role:** Requires M01 and M03. It joins abstract group geometry to the physical operations that the simulator must call.

**Conceptual connection:** Simultaneous conjugation preserves every relation and can conceal information in the implementation without changing the known group.

**Source pointers:** Childs §11.1, printed pp. 47–48; [Model: unknown representation](../science/model.md#a-known-group-and-an-unknown-representation) and [Group quantiles: hard representation](../science/group-quantiles.md#a-representation-that-encodes-distance-parity).

### M05 — The oracle interface defines the counted resource

**Central question:** Which operations cost a query, and which known operations may occur between queries?

**Understanding target:** Describe generator, inverse, controlled and coherent SELECT access. Distinguish a hard maximum on serial calls from expected calls, parallel depth, known gate count and arbitrary-power access.

**Dependencies and story role:** Requires M01 and M04. It fixes the interface before an upper or lower bound is interpreted.

**Conceptual connection:** A lower bound must survive all permitted known controls; an upper-query saving alone does not measure total runtime.

**Source pointers:** Childs §§21.1–21.2, printed pp. 97–98, and §28.3 for SELECT; [Model: primitives](../science/model.md#the-strongest-permitted-primitive) and [query quantifiers](../science/model.md#worst-case-query-cost-and-its-dimension-quantifier).

### M06 — Reversible arithmetic and clean uncomputation

**Central question:** How can a quantum circuit compute an address, use an unknown bit and restore its temporary work coherently?

**Understanding target:** Explain compute, conditional copy and uncompute without measuring a superposed address. Track the distinction between known reversible calculations and calls to unknown data.

**Dependencies and story role:** Requires M01 and M05. It provides the circuit mechanism needed by the lower-bound oracle compiler.

**Conceptual connection:** A costly global unknown transformation may have a locally cheap conjugated generator; temporary known arithmetic does not supply that unknown transformation for free.

**Source pointers:** Childs §1.4, printed p. 2, and §21.2; [Group quantiles: two-query compiler](../science/group-quantiles.md#two-ordinary-bit-queries-implement-a-controlled-generator).

### M07 — Random histories and their endpoint law

**Central question:** How does a Poisson number of classical generator jumps define a continuous-time random-unitary channel?

**Understanding target:** Interpret the event count, independent generator labels, group endpoint and convolution law. Explain why averaging the represented endpoint gives the exponential of the jump generator.

**Dependencies and story role:** Requires M02–M04. It connects one random trajectory to the complete law used by the simulation task.

**Conceptual connection:** The probability distribution is known classical input, while applying its represented endpoint remains an unknown quantum operation.

**Source pointers:** Childs §§17.1 and 17.3, printed pp. 73–75, for classical/quantum walk context; [Model: continuous-time laws](../science/model.md#continuous-time-laws). The Poisson expansion and random-unitary semigroup are supplied locally.

### M08 — One error guarantee for every quantum input

**Central question:** What must remain accurate when the simulator acts on an unknown state entangled with another system?

**Understanding target:** Explain the operational role of the unhalved diamond norm, its measurement-probability consequence and the factor of two between these conventions. Distinguish a channel guarantee from accuracy on one chosen state.

**Dependencies and story role:** Requires M01, M02 and M05. It fixes the error notion shared by both directions of the theorem.

**Conceptual connection:** Replacing a small probability of unitary branches changes the full channel by a controlled amount, including on reference-entangled inputs.

**Source pointers:** Childs §2.1, printed p. 7, for composing circuit errors and §27.2, printed p. 133, for simulation accuracy; [Model: channel error](../science/model.md#the-channel-to-be-implemented). Diamond norm and its normalization are project-supplied.

### M09 — Tail probabilities, quantiles and approximation budgets

**Central question:** Why does a hard query cap depend on a tail probability rather than only on an average length?

**Understanding target:** Interpret strict and non-strict distance tails, an integer upper-tail radius, and total-variation error of a classical law. Explain why an overflow event and a sampler's numerical error consume separate parts of the channel-error budget.

**Dependencies and story role:** Requires M03, M07 and M08. It supplies the probability language that makes a maximum-query theorem possible.

**Conceptual connection:** Approximation permits rare long endpoints to be replaced by an ordinary output channel, so the requested accuracy determines which distances matter.

**Source pointers:** Childs §27.2 for the accuracy/resource setting; [Group quantiles: theorem definitions](../science/group-quantiles.md#the-finite-group-theorem) and [numerical laws](../science/group-quantiles.md#numerical-laws-and-reserved-error). Tail and total-variation arguments are supplied locally.

### M10 — Parity as a query obstruction

**Central question:** Why does even a very small positive advantage in predicting all input-bit parity require many Boolean queries?

**Understanding target:** Connect a query algorithm to a low-degree acceptance polynomial and explain why parity cannot correlate positively with a polynomial missing its full degree. Keep the maximum-query convention visible.

**Dependencies and story role:** Requires M05 and M06. It introduces the general lower-bound tool before the project embeds it in a representation.

**Conceptual connection:** A simulator can be ruled out by turning its output into a parity prediction; the bias need not be large or amplified.

**Source pointers:** Childs §§21.2–21.3 and §21.5, printed pp. 98–100; [Group quantiles: positive-bias argument](../science/group-quantiles.md#positive-bias-suffices-for-the-parity-obstruction).

### M11 — Conditional randomness and useful moment bounds

**Central question:** How can conditioning reveal independent variables when the unconditioned process is correlated?

**Understanding target:** Explain conditional expectation and variance, first/second/fourth moments, and the distinct jobs of Markov, Cauchy–Schwarz, Paley–Zygmund and Chebyshev bounds. Recognize that a mean does not by itself specify a fixed lower quantile.

**Dependencies and story role:** Requires M07 and M09. It prepares the probability tools needed to turn cursor occupation into a query-scale statement.

**Conceptual connection:** The lamps become independent after the entire cursor path is fixed, making both an upper tail and a strong lower tail accessible.

**Source pointers:** Childs §17.3 supplies nearby one-dimensional walk context only; [Wreath product: conditional lamp law](../science/wreath-product.md#3-conditional-lamp-law), [upper quantile](../science/wreath-product.md#4-an-upper-escape-quantile), and [lower quantile](../science/wreath-product.md#5-a-high-lower-escape-quantile). These probability tools and derivations are supplied locally.

### M12 — The complete simulation question

**Central question:** What precisely is being optimized before any group-escape result is used?

**Understanding target:** State the known group and law, unknown represented primitives, arbitrary-input channel output, unhalved error, hard serial-query cap and uniformity over representations and finite dimensions. Identify classical work as an additional resource.

**Dependencies and story role:** Requires M01–M11. This closes the background phase by assembling its local notions into the full operational task.

**Conceptual connection:** The same specification determines whether an algorithm is admissible, whether a lower-bound witness belongs to the model, and what a claimed acceleration means.

**Source pointers:** Childs §11.1, §§21.1–21.2, §27.2 and §28.1, printed p. 139; [Model](../science/model.md) and [Interpretation](../science/interpretation.md).

## Narrative/innovation — M13–M30

### M13 — Compressing a random word preserves its channel

**Central question:** Why can a chronological jump history be replaced by a geodesic for its endpoint?

**Understanding target:** Explain that a representation assigns the same unitary to equal group words, and connect this equality to the averaged channel on any input. Track gate execution order when a classical cursor convention uses right multiplication.

**Dependencies and story role:** Requires M03, M04, M07 and M12. It isolates the upper algorithm's exact algebraic mechanism.

**Conceptual connection:** The endpoint law supplies randomness; group relations remove redundant unknown-generator calls without requiring the representation matrices.

**Source pointers:** Childs §11.1 and §27.3, printed pp. 134–135, as context for products of operators; [Group quantiles: capped geodesics](../science/group-quantiles.md#a-capped-geodesic-implementation) and [Resources: word implementation](../science/algorithms-and-resources.md#a-computable-short-word-for-the-wreath-family).

### M14 — A long-word replacement is a trace-preserving cap

**Central question:** How does the geodesic procedure obtain a hard query bound while remaining a valid quantum channel?

**Understanding target:** Explain identity fallback on long endpoints and derive the factor-two tail bound in the unhalved convention. Distinguish replacement of a branch from discarding unsuccessful runs and renormalizing.

**Dependencies and story role:** Requires M08, M09 and M13. It converts an exact but variable-length operation into the theorem's bounded-query upper algorithm.

**Conceptual connection:** Probability tails become operational channel errors, which is why an upper quantile determines the cap.

**Source pointers:** Childs §27.2 and §28.3 for simulation/error and postselection context; [Group quantiles: upper proof](../science/group-quantiles.md#a-capped-geodesic-implementation) and [Resources: hard cap](../science/algorithms-and-resources.md#a-hard-query-cap).

### M15 — Scalar probability error belongs in the same budget

**Central question:** What changes when the endpoint law and time are implemented with finite classical precision?

**Understanding target:** Connect total-variation error, Poisson overflow, long compiled words and implemented-unitary error to the complete diamond-error budget. Explain why a floating-point normalization is not a certificate of that budget.

**Dependencies and story role:** Requires M08, M09 and M14. It completes the upper mechanism's implementable accuracy account before the lower construction begins.

**Conceptual connection:** The mathematical law, its numerical sampler and the physical primitive precision are different approximations whose errors must be reconciled.

**Source pointers:** Childs §2.1 and §27.2; [Group quantiles: numerical laws](../science/group-quantiles.md#numerical-laws-and-reserved-error) and [Resources: full error budget](../science/algorithms-and-resources.md#finite-precision-and-the-full-error-budget).

### M16 — One global gauge preserves every relation

**Central question:** How can unknown parity be hidden in a family of generators without violating cycles or commutation promises?

**Understanding target:** Explain the capped prefix-parity transformation, its action on a regular register and answer qubit, and simultaneous conjugation of all generators. Show why this produces a genuine representation of the entire known group.

**Dependencies and story role:** Requires M04, M10 and M12. It introduces the hard family that makes the converse apply beyond tree-like relations.

**Conceptual connection:** Algebraic structure helps the upper algorithm and also constrains its adversarial input; the common conjugation keeps that input inside the same promise.

**Source pointers:** Childs §11.1; [Group quantiles: hard representation](../science/group-quantiles.md#a-representation-that-encodes-distance-parity).

### M17 — A global unknown gauge has a local two-query compiler

**Central question:** Why does applying one gauged generator need only two ordinary input-bit queries rather than the full unknown prefix parity?

**Understanding target:** Use the one-step distance inequality to identify a single active bit. Track the valid dummy address, clean buffer, conditional copy, uncomputation, inverse and coherent SELECT branches.

**Dependencies and story role:** Requires M03, M05, M06 and M16. It supplies the load-bearing reduction between the physical primitive interface and the Boolean oracle model.

**Conceptual connection:** The hard representation is not free to apply, but its individual generators have an exact low-query compiler independent of the unknown bits.

**Source pointers:** Childs §1.4 and §21.2; [Group quantiles: controlled two-query compiler](../science/group-quantiles.md#two-ordinary-bit-queries-implement-a-controlled-generator).

### M18 — A distant endpoint reveals complete parity

**Central question:** What measurable information does the ideal channel carry when its endpoint passes the chosen radius?

**Understanding target:** Follow the representation on the fixed input at the identity, recognize the known distance flag, and explain the fair-bit fallback below the threshold. Derive how channel error reduces the parity advantage.

**Dependencies and story role:** Requires M08, M10, M16 and M17. It connects the hard oracle construction to an observable computational consequence.

**Conceptual connection:** The flag is measured on the delivered output, so the argument does not assume access to the simulator's internal trajectory.

**Source pointers:** Childs §§21.2 and 21.5; [Group quantiles: parity above a radius](../science/group-quantiles.md#the-channel-reveals-full-parity-above-a-known-radius).

### M19 — The converse defeats arbitrary coherent algorithms

**Central question:** Why does the parity reduction rule out a simulator that uses a completely different coherent strategy?

**Understanding target:** Combine the two-query compiler with the acceptance-polynomial degree bound and the strictly positive parity bias. Account for arbitrary known interleavings, ancillas and adaptive measurements without assuming classical trajectory following.

**Dependencies and story role:** Requires M05, M10, M17 and M18. It completes the lower mechanism at its actual oracle strength.

**Conceptual connection:** The simulator is used as a subroutine of an ordinary Boolean-query algorithm, making the established parity obstruction applicable to every permitted strategy.

**Source pointers:** Childs §§21.3–21.5; [Group quantiles: positive-bias lower proof](../science/group-quantiles.md#positive-bias-suffices-for-the-parity-obstruction).

### M20 — Assembling the error-shifted quantile bracket

**Central question:** Which upper and lower tail thresholds follow from the two completed mechanisms?

**Understanding target:** State $`R_{\varepsilon}/4\leq Q\leq R_{\varepsilon/2}`$ with the unhalved convention, strict lower-tail condition, zero-radius case, integer rounding and uniform representation/dimension quantifiers. Explain why the different error levels are part of the statement.

**Dependencies and story role:** Requires M09, M12, M14, M15 and M19. It integrates the first part of the narrative into the general finite-group theorem.

**Conceptual connection:** A short endpoint is sufficient to simulate, and enough probability on distant endpoints is sufficient to force many queries.

**Source pointers:** Childs §§21.1–21.5 for query lower-bound foundations; [Group quantiles: Theorem 1](../science/group-quantiles.md#the-finite-group-theorem) and [its lower-proof conclusion](../science/group-quantiles.md#positive-bias-suffices-for-the-parity-obstruction). The quantile theorem is project-specific.

### M21 — A mean escape distance can give the wrong answer

**Central question:** When can a tiny probability of a very distant endpoint inflate the mean without forcing queries at the requested error?

**Understanding target:** Explain the rare-long-endpoint counterexample and identify the upper/lower quantile conditions needed for a matching asymptotic law. Distinguish a two-moment small-error argument from a high-probability lower-escape estimate.

**Dependencies and story role:** Requires M09, M11 and M20. It establishes the additional evidence needed before an escape exponent is promoted to a query exponent.

**Conceptual connection:** The application must prove the tails relevant to its declared error, rather than insert an expected-distance formula into the theorem.

**Source pointers:** Childs §27.2 for accuracy-dependent simulation as context; [Group quantiles: escape-rate conditions and counterexample](../science/group-quantiles.md#turning-the-bracket-into-an-escape-rate-law). The probability comparison is supplied locally.

### M22 — A cursor with integer lamps gives a nonabelian example

**Central question:** Which relations hold when a cursor can move and update an integer counter at its current site?

**Understanding target:** Describe an element of the integer-lamp wreath product, its four symmetric jump types, and commutation of lamps translated to distinct sites. Explain why cursor motion and a lamp update generally do not commute.

**Dependencies and story role:** Requires M03, M04, M07 and M20. It opens the application with explicit local operations and a fixed bounded alphabet.

**Conceptual connection:** The example retains useful algebraic compression while moving beyond jumps generated along one common commuting Hamiltonian orbit.

**Source pointers:** Childs §11.1 and §17.3 for group and line-walk foundations; [Wreath product: group and channel](../science/wreath-product.md#1-the-group-and-the-channel). Wreath-product relations are supplied locally.

### M23 — Word length is lamp work plus cursor travel

**Central question:** What must any word do to realize a specified lamp configuration and final cursor position?

**Understanding target:** Explain the lower requirements from net lamp updates and visiting the two extreme required sites, then describe a route attaining them. Separate the endpoint's minimal work from the chronological number of jumps.

**Dependencies and story role:** Requires M13 and M22. It turns the application's algebraic normal form into a computable query cost.

**Conceptual connection:** The exact word-length formula joins independent lamp contributions to a global route-planning constraint on the cursor.

**Source pointers:** Childs §11.1 for represented products; [Wreath product: exact word length](../science/wreath-product.md#2-word-length-separates-lamp-work-from-cursor-travel) and [Resources: computable word](../science/algorithms-and-resources.md#a-computable-short-word-for-the-wreath-family). The metric formula is project-supplied.

### M24 — Occupation time determines each lamp's random displacement

**Central question:** Why do the final lamps become independent signed Poisson differences after the cursor path is fixed?

**Understanding target:** Explain Poisson thinning, a site's occupation time, conditional lamp variance and fourth moment. Keep conditional independence distinct from independence of the correlated occupation times.

**Dependencies and story role:** Requires M07, M11 and M22. It supplies the local probabilistic mechanism behind the fractional scale.

**Conceptual connection:** Time spent at a site determines how much canceled lamp motion remains there; summing over the visited region creates the endpoint work.

**Source pointers:** Childs §17.3 gives one-dimensional walk context; [Wreath product: conditional lamp law](../science/wreath-product.md#3-conditional-lamp-law). Thinning, occupation times and the conditional formulas are supplied locally.

### M25 — Diffusive range produces an upper three-quarter quantile

**Central question:** How do cursor range and conditional lamp variance combine to bound total endpoint work?

**Understanding target:** Join the diffusive cursor-range estimate with Cauchy–Schwarz and the word-length formula, then convert the expectation bound into a hard upper quantile. Explain why this supplies an admissible query cap.

**Dependencies and story role:** Requires M11, M14, M23 and M24. It moves from local lamp statistics to a complete application-level upper bound.

**Conceptual connection:** About square-root-many visited sites share the available lamp-update time; their remaining fluctuations accumulate on the three-quarter scale.

**Source pointers:** Childs §17.3 for the classical line-walk setting and §27.2 for simulation-resource context; [Wreath product: upper escape quantile](../science/wreath-product.md#4-an-upper-escape-quantile). The moment and tail proof is supplied locally.

### M26 — A high lower quantile needs more than an expectation

**Central question:** Why is endpoint work of the same order present with sufficiently high probability?

**Understanding target:** Explain the role of occupation-time self-intersection, the interpolation bound on square roots of occupation times, and the conditional mean/variance argument. Identify the fixed error and finite threshold covered by the resulting tail statement.

**Dependencies and story role:** Requires M11, M21, M24 and M25. It resolves the decisive lower-tail issue before invoking the quantum converse.

**Conceptual connection:** Conditioning first controls the environment of the independent lamps; concentration afterward turns a large conditional mean into a useful escape quantile.

**Source pointers:** Childs §17.3 supplies context only; [Wreath product: high lower escape quantile](../science/wreath-product.md#5-a-high-lower-escape-quantile). The heat-kernel, occupation and concentration estimates are developed locally.

### M27 — A finite quotient must preserve short geodesics

**Central question:** How can an infinite-group calculation become a statement about a finite-dimensional quantum instance?

**Understanding target:** Describe finite cursor and lamp cycles, the quotient homomorphism, and the kernel argument proving injectivity and exact word-length preservation in a chosen ball. Explain why merely observing no wrapping is not sufficient to rule out a shorter quotient word.

**Dependencies and story role:** Requires M03, M04, M22 and M23. It makes the infinite probability reference compatible with the finite-group theorem's input promise.

**Conceptual connection:** Preserving all short relations and distances protects both the compressed upper and the parity radius in the finite hard representation.

**Source pointers:** Childs §11.1; [Finite quotients: group family](../science/finite-quotients.md#1-a-quotient-chosen-for-each-requested-time) and [metric-preservation proof](../science/finite-quotients.md#2-injectivity-and-exact-metric-preservation). The word-ball construction is supplied locally.

### M28 — Coupling transfers the exponent and exposes its width

**Central question:** Which parameters vary when the finite-group query theorem is applied at a growing requested time?

**Understanding target:** Connect the Poisson event cap, equality of coupled endpoint distances, transferred tail margins and regular-register dimension. State the three-quarter query law for each fixed $`0\lt \varepsilon\leq1/100`$ along its specified family of finite groups, with the growing target width visible.

**Dependencies and story role:** Requires M15, M20, M25, M26 and M27. It assembles the complete finite nonabelian consequence.

**Conceptual connection:** A controlled finite-window approximation transfers the probability law without exchanging a growing-time limit with a fixed-dimension limit.

**Source pointers:** Childs §11.1, §21.1 and §27.2; [Finite quotients: walk coupling](../science/finite-quotients.md#3-coupling-the-two-walks), [query transfer](../science/finite-quotients.md#4-transfer-to-the-query-theorem), and [dimension](../science/finite-quotients.md#6-dimension-and-counted-workspace).

### M29 — Identify the saved resource and the inherited ingredients

**Central question:** What does the completed result establish after classical work, access assumptions and closest prior mechanisms are counted?

**Understanding target:** Distinguish sublinear unknown-generator calls from the direct sampler's linear classical event overhead and from a hardware advantage. Separate inherited random-walk exponents, parity machinery and other intermediate simulation exponents from the representation-uniform group-quantile contribution.

**Dependencies and story role:** Requires M05, M15, M20, M21 and M28. It places the assembled theorem and example in their actual computational and scientific scope.

**Conceptual connection:** Known group geometry supplies the compression, while the gauge proves its worst-case oracle significance; neither removes the remaining implementation costs automatically.

**Source pointers:** Childs §27.2 and §§28.1–28.3, printed pp. 139–142; [Resources: counted acceleration](../science/algorithms-and-resources.md#what-is-and-is-not-fast-forwarded), [Interpretation: boundaries](../science/interpretation.md#resource-boundaries), and [Related work](../references/related-work.md).

### M30 — The complete escape-to-simulation argument

**Central question:** How do the channel, quantile theorem and finite wreath example form one connected scientific account?

**Understanding target:** Explain the full chain from a known endpoint law to a short trace-preserving implementation, from the global gauge to an unrestricted query lower bound, and from finite escape quantiles to the declared three-quarter law. Retain the exact representation promise, error normalization, dimension growth, output requirements and total-resource limits in that explanation.

**Dependencies and story role:** Requires M12, M20, M21, M28 and M29. This is the narrative phase's global synthesis, rather than another independent technical ingredient.

**Conceptual connection:** The same group distance governs a constructive algorithm and a worst-case information obstruction, provided the actual probability tails and oracle interface justify the transfer.

**Source pointers:** Childs §11.1, §§21.1–21.5 and §§27.2, 28.1–28.3; [Scientific reading route](../science/README.md), [Group quantiles](../science/group-quantiles.md), [Wreath product](../science/wreath-product.md), [Finite quotients](../science/finite-quotients.md), and [Interpretation](../science/interpretation.md).

[Return to the scientific reading route](../science/README.md)
