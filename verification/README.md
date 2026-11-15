# Finite verification

Run the checks from the repository root:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/check_finite_groups.py
```

The script constructs small cyclic, dihedral and finite wreath groups independently of the scientific exposition. It checks group multiplication and inverses, breadth-first-search word distances, exact regular-representation relations, and the parity-gauged controlled-generator compiler. It also checks finite wreath word lengths against graph distances and compares a classical endpoint-mixture implementation with a Lindblad exponential on reference-entangled finite inputs.

The output is a JSON report. Every exact algebraic assertion must pass, and floating comparisons must satisfy their explicitly stated tolerances. Probability-table and Poisson diagnostics test the finite numerical implementation; analytical probability guarantees are derived in [Algorithms and resources](../science/algorithms-and-resources.md).

These finite checks verify conventions and reproducible implementations. They do not certify an asymptotic exponent, a universal diamond-norm theorem, a mathematical prior-work claim or a physical hardware crossover. The [general proof](../science/group-quantiles.md), [occupation-time estimates](../science/wreath-product.md), and [finite quotient transfer](../science/finite-quotients.md) are the authoritative analytical accounts.

The checks use deterministic finite cases and fixed random seeds where randomized numerical inputs are useful. No external dataset, network access, QRAM or private file is required.
