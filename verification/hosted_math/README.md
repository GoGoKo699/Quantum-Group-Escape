# Hosted mathematical comparison

The read-only pull-request workflow checks exact proposed source, runs the finite scientific verifier, tests the hosted README, and captures every tracked Markdown page at desktop and narrow widths. It compares actual GitHub MathML with the pinned source and retains HTML, screenshots and structural reports as workflow artifacts. A successful automated report still requires visual inspection of the captured claims, proofs and learning route.

The three unmodified collector/checker/probe helpers are public snapshots from [Quantum Learning Batch Threshold, revision 94b7809](https://github.com/GoGoKo699/Quantum-Learning-Batch-Threshold/tree/94b78092702ecb691822739fd961dc57fcd42c32/verification/hosted_math). Their Git blob identities are:

| Helper | Git blob |
|---|---|
| `capture_hosted_math.cjs` | `6f36ee03223a82d0075da2fe903f21bc5a45a75b` |
| `check_rendered_math.py` | `1d3bf9810d0dfadb844a48b354af80f9b66924bc` |
| `probe_hosted_math.cjs` | `f83ea9da799bee0b53bd5c57315ae2b4b2d9de43` |

Dependencies are installed into the runner's temporary directory. The job uses `contents: read`, does not persist checkout credentials, and runs only for pull requests whose head belongs to this same repository. It does not modify source or require secrets.

`math-contract.json` adds explicit visible-text checks for principal formulas; it cannot skip structural checks. Workflow artifacts have finite retention, so a badge alone is not a permanent observation or a proof certificate. The [scientific verification guide](../README.md) separates finite diagnostics from the analytical claims.
