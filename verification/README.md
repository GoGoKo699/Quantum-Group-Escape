# Finite verification

Run the checks from the repository root:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/check_finite_groups.py
```

The script constructs small cyclic, dihedral and finite wreath groups independently of the scientific exposition. It checks group multiplication and inverses, breadth-first-search word distances, exact regular-representation relations, and the parity-gauged controlled-generator compiler. It also checks finite wreath word lengths against graph distances and compares a classical endpoint-mixture implementation with a Lindblad exponential on reference-entangled finite inputs.

The signed-copy witness check enumerates every radial sign assignment for three copies of $`C_4`$ and $`D_3`$ (order six). It checks the local sign rule for controlled forward and inverse queries and compares the measured acceptance gap with the predicted finite-copy gap. The numerical circuits mix the copies with fixed complex unitaries and retain two measurement branches with separate query choices. The rational runtime check independently trims farthest endpoint atoms on $`C_4`$. It verifies the complete query tail, expected count, hard cap and probability change, including an exact radius boundary and a partially trimmed atom.

The output is a JSON report. Every exact algebraic assertion must pass, and floating comparisons must satisfy their explicitly stated tolerances. Probability-table and Poisson diagnostics test the finite numerical implementation; analytical probability guarantees are derived in [Algorithms and resources](../science/algorithms-and-resources.md).

These finite checks verify conventions and reproducible implementations. The [general proof](../science/group-quantiles.md) establishes the universal diamond-norm and runtime statements. The [occupation-time estimates](../science/wreath-product.md) and [finite quotient transfer](../science/finite-quotients.md) establish the asymptotic exponent.

The checks use deterministic finite cases and fixed random seeds where randomized numerical inputs are useful. No external dataset, network access, QRAM or private file is required.

## Hosted mathematics

The [read-only verification workflow](../.github/workflows/hosted-math.yml) runs these finite checks on the exact proposed commit, tests representative GitHub mathematics, then compares every tracked Markdown expression with its hosted rendering. It retains reports and screenshots as workflow artifacts for visual inspection. The [capture guide](hosted_math/README.md) documents the pinned collector and expression contract. Rendering checks support presentation accuracy; they do not replace proof review.
