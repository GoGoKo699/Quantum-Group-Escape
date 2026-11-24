# Learning the group-escape argument

The central question is operational: **when unknown quantum operations obey known group relations, how many calls are needed to reproduce a prescribed random mixture of those operations?** A long sampled history can cancel to a short word. The converse asks whether an arbitrary coherent algorithm can do better than that compression.

The single educational anchor is Andrew M. Childs, [*Lecture Notes on Quantum Algorithms*](https://www.cs.umd.edu/~amchilds/qa/), version dated **17 April 2025**. The selected source supplies the algorithmic language; the repository supplies its channel model, geometric converse, and probability arguments.

| Route | Purpose |
|---|---|
| [Childs bridge](childs-bridge.md) | Compare hard and expected query costs in a four-element example, translate the notation, and find the relevant source sections. |
| [Thirty milestones](milestones.md) | Follow the common project map from prerequisites to the complete contribution and its limits. |
| [Scientific reading route](../science/README.md) | Read the canonical definitions, theorem, proofs, implementation account, and interpretation directly. |
| [Finite verification](../verification/README.md) | Inspect the small-group checks and distinguish finite diagnostics from the analytical results. |

The bridge does not require reading the entire source first. Its principal source stops are reversible computation (§1.4), group representations (§11.1), query polynomials and parity (§§21.1–21.3, 21.5), and the simulation lower-bound example (§28.1). The bridge gives printed-page locators and explains the project-specific material that those sections do not supply.

The learning map has two phases: background/preliminaries and narrative/innovation. It is a common map of the science, independent of any reader's study history. Each milestone points to the selected anchor and to the actual project account.

The exact hard cost is the distance quantile at half the unhalved diamond error. With classical stopping, the exact worst-case expected cost is the mean distance after redirecting up to that much probability mass from the farthest endpoints to the identity. Both results concern the full reduced channel for an unknown representation. The three-quarter example uses growing finite quotients and a direct sampler with linear expected classical trajectory work.

[Repository overview](../README.md) · [Begin the bridge](childs-bridge.md) · [Open the map](milestones.md)
