# Thirty milestones for understanding group-escape simulation

This map follows one scientific story: a known random word can have a short endpoint description, and coherence across independently signed representations makes that endpoint distance an unavoidable quantum-query cost. The final example connects the theorem to the occupation times of a cursor-and-lamps walk.

The first **12 milestones are background/preliminaries**. They assemble the state, algebra, oracle, probability and error notions needed to state the task. The remaining **18 milestones are narrative/innovation**. They establish the exact hard and expected costs, then build the finite nonabelian example and assess its complete resource scope. Each phase proceeds from individual objects to an integrated account. The map covers the load-bearing scientific ideas, rather than every calculation or neighboring subject.

The single educational anchor is Andrew M. Childs, [*Lecture Notes on Quantum Algorithms*](https://www.cs.umd.edu/~amchilds/qa/), **17 April 2025**. Start with the [source bridge](childs-bridge.md) for the notation translation and worked finite-group example. Section numbers below refer to that version; page numbers are the notes' printed pages. Childs supplies the circuit, representation, query, polynomial and Hamiltonian-simulation foundations. Density-operator channels, diamond error, the Poisson group law, escape quantiles, occupation-time estimates and the exact group-quantile and expected-cost proofs are supplied in this repository. A source pointer to a nearby Childs topic does not attribute those project-specific extensions to the notes.

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

**Source pointers:** Childs §11.1, printed pp. 47–48; [Model: unknown representation](../science/model.md#a-known-group-and-an-unknown-representation) and [Group quantiles: hard representation](../science/group-quantiles.md#radial-signs-in-an-exact-representation).

### M05 — The oracle interface defines the counted resource

**Central question:** Which operations cost a query, and which known operations may occur between queries?

**Understanding target:** Describe generator, inverse, controlled and coherent SELECT access. Distinguish a hard maximum on serial calls from expected calls, parallel depth, known gate count and arbitrary-power access.

**Dependencies and story role:** Requires M01 and M04. It fixes the interface before an upper or lower bound is interpreted.

**Conceptual connection:** A lower bound must survive all permitted known controls; an upper-query saving alone does not measure total runtime.

**Source pointers:** Childs §§21.1–21.2, printed pp. 97–98, and §28.3 for SELECT; [Model: primitives](../science/model.md#the-strongest-permitted-primitive) and [query quantifiers](../science/model.md#worst-case-query-cost-and-its-dimension-quantifier).

### M06 — Known routing and coherent control

**Central question:** Which operations can a circuit perform on a generator's address without learning the unknown representation?

**Understanding target:** Explain coherent address selection, known relabelling for inverse calls and restoring temporary arithmetic registers. Distinguish the known routing operations from the charged invocation of the selected generator.

**Dependencies and story role:** Requires M01 and M05. It prepares the controlled-generator model used in the lower bound.

**Conceptual connection:** A control branch may invoke the identity while other branches apply an unknown represented generator. These fixed control labels do not add dependence on the hidden signs.

**Source pointers:** Childs §1.4, printed pp. 2–3, and §21.2; [Model: primitives](../science/model.md#the-strongest-permitted-primitive) and [signed representation](../science/group-quantiles.md#radial-signs-in-an-exact-representation).

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

### M10 — Query degree and products of independent signs

**Central question:** Why can a low-degree polynomial have no correlation with a product of more independent signs than its degree?

**Understanding target:** Explain polynomial degree growth under an oracle query and orthogonality of the products of independent uniform signs. Reduce repeated signs using their squared value of one.

**Dependencies and story role:** Requires M05 and M06. It supplies the lower-bound tool before the project embeds signs into a group representation.

**Conceptual connection:** The proof compares the degree of an individual output density-matrix entry with the degree required for matching coherence between two independently signed blocks.

**Source pointers:** Childs §§21.2–21.3 and §21.5, printed pp. 98–100; [Group quantiles: coherence witness](../science/group-quantiles.md#a-measurement-of-distant-coherence).

### M11 — Conditional randomness and useful moment bounds

**Central question:** How can conditioning reveal independent variables when the unconditioned process is correlated?

**Understanding target:** Explain conditional expectation and variance, first/second/fourth moments, and the distinct jobs of Markov, Cauchy–Schwarz, Paley–Zygmund and Chebyshev bounds. Recognize that a mean does not by itself specify a fixed lower quantile.

**Dependencies and story role:** Requires M07 and M09. It prepares the probability tools needed to turn cursor occupation into a query-scale statement.

**Conceptual connection:** The lamps become independent after the entire cursor path is fixed, making both an upper tail and a strong lower tail accessible.

**Source pointers:** Childs §17.3 supplies nearby one-dimensional walk context only; [Wreath product: conditional lamp law](../science/wreath-product.md#3-conditional-lamp-law), [upper quantile](../science/wreath-product.md#4-an-upper-escape-quantile), and [lower quantile](../science/wreath-product.md#5-a-high-lower-escape-quantile). These probability tools and derivations are supplied locally.

### M12 — The complete simulation question

**Central question:** What precisely is being optimized before any group-escape result is used?

**Understanding target:** State the known group and law, unknown represented primitives, arbitrary-input channel output, unhalved error, hard serial-query cap, classical stopping and uniformity over representations and finite dimensions. Identify classical work as an additional resource.

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

### M16 — Independent radial signs preserve every group relation

**Central question:** How can unknown signs be assigned to an entire representation while preserving cycles and commutation relations?

**Understanding target:** Take several independent copies of the regular action. In each block, assign the basis state at distance $`\ell`$ the product of that block's first $`\ell`$ signs, and conjugate every generator by the resulting diagonal unitary.

**Dependencies and story role:** Requires M03, M04, M10 and M12. It constructs hard instances of the same exact group representation promised to the simulator.

**Conceptual connection:** The local change of distance controls each generator entry. The whole-prefix product remains visible in the effect of a distant group element on the identity.

**Source pointers:** Childs §11.1; [Group quantiles: radial signs](../science/group-quantiles.md#radial-signs-in-an-exact-representation).

### M17 — Each supplied call adds at most two degrees to the output

**Central question:** How does a one-step distance change constrain the sign dependence of a simulator that uses many coherent calls?

**Understanding target:** Show that a generator entry contains at most one sign. Apply the same argument to inverse and controlled generators, then track how a matrix factor on each side of a density operator adds at most two degrees per call.

**Dependencies and story role:** Requires M03, M05, M06, M10 and M16. It gives a bound that uses the supplied oracle calls directly.

**Conceptual connection:** Sign-independent interleavings act linearly on density matrices. They preserve the polynomial bound even when they use ancillas or store measurement outcomes.

**Source pointers:** Childs §§21.2–21.3; [Group quantiles: radial signs](../science/group-quantiles.md#radial-signs-in-an-exact-representation) and [coherence measurement](../science/group-quantiles.md#a-measurement-of-distant-coherence).

### M18 — A distant endpoint carries coherence across blocks

**Central question:** What changes in the ideal output after a long group element acts on a superposition of block identities?

**Understanding target:** Calculate an off-diagonal entry between two different blocks at endpoint $`g`$. Identify its product of $`2\ell(g)`$ independent signs. Explain how a projection onto the ideal signed state, with its diagonal part subtracted, measures just this coherence.

**Dependencies and story role:** Requires M08, M10, M16 and M17. It converts the degree bound into a channel error witness.

**Conceptual connection:** A correct classical endpoint histogram can preserve every diagonal probability while missing every long-distance coherence tested by the witness.

**Source pointers:** Childs §§21.3 and 21.5; [Group quantiles: coherence measurement](../science/group-quantiles.md#a-measurement-of-distant-coherence).

### M19 — Tail probability sets the minimum channel error for a hard cap

**Central question:** Why does a $`q`$-call simulator face diamond error at least twice the probability that the ideal endpoint has distance greater than $`q`$?

**Understanding target:** Use the range-one score to convert cross-block coherence into an error lower bound. Explain how the finite-case factor $`1-1/K`$ approaches one across admissible finite target dimensions.

**Dependencies and story role:** Requires M05, M08, M10, M17 and M18. It completes the converse without assuming a particular internal simulation strategy.

**Conceptual connection:** The cap is uniform over finite representation dimensions. The witness can therefore use enough independent blocks to make the invisible coherence account for essentially all distant endpoint mass.

**Source pointers:** Childs §§21.3–21.5; [Group quantiles: coherence witness](../science/group-quantiles.md#a-measurement-of-distant-coherence).

### M20 — The exact hard escape quantile

**Central question:** When does the trace-preserving geodesic cap meet the best possible error?

**Understanding target:** Combine the upper and lower proofs to obtain $`Q_G(\mu,\varepsilon)=R_{\varepsilon/2}(\mu)`$. Check the equality boundary, the zero-radius case, integer word lengths and the uniform dimension quantifier.

**Dependencies and story role:** Requires M09, M12, M14, M15 and M19. It completes the general finite-group result under a hard query budget.

**Conceptual connection:** The same overflow probability determines the geodesic scheme's error allowance and the coherence any simulator with that cap must miss.

**Source pointers:** Childs §§21.1–21.5 for the lower-bound tools; [Group quantiles: exact theorem](../science/group-quantiles.md#the-finite-group-theorem). The quantile equality is project-specific.

### M21 — The exact expected cost with classical stopping

**Central question:** What is the smallest worst-case average query count if branches may stop at different times?

**Understanding target:** Explain how truncating the simulator at each cutoff bounds the probability of needing more calls. Sum these bounds and derive the mean distance after removing the farthest $`\varepsilon/2`$ of probability mass, with partial replacement of a distance atom when needed.

**Dependencies and story role:** Requires M09, M11, M14 and M20. It extends the hard result to classically observed stopping and shows why a rare long endpoint can affect the untrimmed mean without forcing a larger cap.

**Conceptual connection:** The optimizer uses the same overflow error allowance for the hard and expected costs. The hard problem asks how far the retained distribution reaches, and the expected problem adds its remaining tail probabilities.

**Source pointers:** Childs §§21.2–21.3 and §27.2 for query and accuracy context; [Group quantiles: exact expected cost](../science/group-quantiles.md#classical-stopping-and-the-exact-mean). The stopping and trimming arguments are supplied locally.

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

**Dependencies and story role:** Requires M11, M20, M24 and M25. It resolves the decisive lower-tail issue before invoking the quantum converse.

**Conceptual connection:** Conditioning first controls the environment of the independent lamps; concentration afterward turns a large conditional mean into a useful escape quantile.

**Source pointers:** Childs §17.3 supplies context only; [Wreath product: high lower escape quantile](../science/wreath-product.md#5-a-high-lower-escape-quantile). The heat-kernel, occupation and concentration estimates are developed locally.

### M27 — A finite quotient must preserve short geodesics

**Central question:** How can an infinite-group calculation become a statement about a finite-dimensional quantum instance?

**Understanding target:** Describe finite cursor and lamp cycles, the quotient homomorphism, and the kernel argument proving injectivity and exact word-length preservation in a chosen ball. Explain why merely observing no wrapping is not sufficient to rule out a shorter quotient word.

**Dependencies and story role:** Requires M03, M04, M22 and M23. It makes the infinite probability reference compatible with the finite-group theorem's input promise.

**Conceptual connection:** Preserving short distances keeps both the compressed words and the tail tested by the finite hard representation.

**Source pointers:** Childs §11.1; [Finite quotients: group family](../science/finite-quotients.md#1-a-quotient-chosen-for-each-requested-time) and [metric-preservation proof](../science/finite-quotients.md#2-injectivity-and-exact-metric-preservation). The word-ball construction is supplied locally.

### M28 — Coupling transfers the exponent and exposes its width

**Central question:** Which parameters vary when the finite-group query theorem is applied at a growing requested time?

**Understanding target:** Connect the Poisson event cap, equality of coupled endpoint distances, transferred tail margins and regular-register dimension. State the three-quarter query law for each fixed $`0\lt \varepsilon\leq1/100`$ along its specified family of finite groups, with the growing target width visible.

**Dependencies and story role:** Requires M15, M20, M25, M26 and M27. It assembles the complete finite nonabelian consequence.

**Conceptual connection:** A controlled finite-window approximation transfers the probability law without exchanging a growing-time limit with a fixed-dimension limit.

**Source pointers:** Childs §11.1, §21.1 and §27.2; [Finite quotients: walk coupling](../science/finite-quotients.md#3-coupling-the-two-walks), [query transfer](../science/finite-quotients.md#4-transfer-to-the-query-theorem), and [dimension](../science/finite-quotients.md#6-dimension-and-counted-workspace).

### M29 — Identify the saved resource and the inherited ingredients

**Central question:** What does the completed result establish after classical work, access assumptions and closest prior mechanisms are counted?

**Understanding target:** Distinguish sublinear unknown-generator calls from the direct sampler's linear classical event overhead and from a hardware advantage. Attribute the random-walk exponent and query-polynomial method, and identify the exact cost formulas supplied by this project.

**Dependencies and story role:** Requires M05, M15, M20, M21 and M28. It places the assembled theorem and example in their actual computational and scientific scope.

**Conceptual connection:** Known group geometry supplies the compression, while the gauge proves its worst-case oracle significance; neither removes the remaining implementation costs automatically.

**Source pointers:** Childs §27.2 and §§28.1–28.3, printed pp. 139–142; [Resources: counted acceleration](../science/algorithms-and-resources.md#what-is-and-is-not-fast-forwarded), [Interpretation: boundaries](../science/interpretation.md#resource-boundaries), and [Related work](../references/related-work.md).

### M30 — The complete escape-to-simulation argument

**Central question:** How do the channel, quantile theorem and finite wreath example form one connected scientific account?

**Understanding target:** Explain the full chain from a known endpoint law to a short trace-preserving implementation, from independently signed regular actions to hard and expected query lower bounds, and from finite escape quantiles to the declared three-quarter law. Retain the exact representation promise, error normalization, dimension growth, output requirements and total-resource limits in that explanation.

**Dependencies and story role:** Requires M12, M20, M21, M28 and M29. This is the narrative phase's global synthesis, rather than another independent technical ingredient.

**Conceptual connection:** The same group distance governs a constructive algorithm and a worst-case information obstruction, provided the actual probability tails and oracle interface justify the transfer.

**Source pointers:** Childs §11.1, §§21.1–21.5 and §§27.2, 28.1–28.3; [Scientific reading route](../science/README.md), [Group quantiles](../science/group-quantiles.md), [Wreath product](../science/wreath-product.md), [Finite quotients](../science/finite-quotients.md), and [Interpretation](../science/interpretation.md).

[Return to the scientific reading route](../science/README.md)
