# Reproducibility

## Minimal late-scale calculation

The core numerical relation is reproduced with only the Python standard library:

```bash
python scripts/reproduce_two_phase_dark_energy.py
```

The script writes:

- `results/TWO_PHASE_DE_NUMERICAL_SUMMARY_v1.0.0.json`
- `results/NSTAR_SENSITIVITY_v1.0.0.csv`

Frozen inputs used by that script:

- reduced Planck mass: `Mbar_4 = 2.435e18 GeV`;
- published gravitational wall curvature: `H3 = 3.0227084445462914e13 GeV`;
- phenomenological history datum: `N_star = 57.84018447444152`;
- conversion: `1 GeV^-1 = 1.973269804e-16 m`.

It evaluates

`R_star = exp(N_star)/H3`,

`Lambda_global = 1/R_star`,

`L_IR = sqrt(3) Mbar_4 R_star^2`,

`H_late = 1/L_IR`,

`rho_DE = 3 Mbar_4^2 H_late^2`.

The script also verifies numerically that

`rho_DE = Lambda_global^4 = R_star^-4`

within floating-point precision.

## Full derivation record

The `derivation/` directory contains the checkpoints that establish:

- exhaustion of local/global action-derived handoff clocks before introducing `N_star`;
- end-to-end background, metric-ownership, thermal, and late-Friedmann hostile tests;
- screen-scale ownership and controlled visible-loading interface;
- current-action primordial perturbation no-go sequence.

The final frozen interpretation is authoritative in `freeze/TWO_PHASE_THEORY_FREEZE_v1.0.0.md` and `freeze/TWO_PHASE_FINAL_FALSIFICATION_AUDIT_v1.0.0.md`.

## Upstream dependencies

The full gravitational O(4)/CDL derivation is separately archived at DOI `10.5281/zenodo.22070942`; the Phase-B2 flavor derivation is separately archived at DOI `10.5281/zenodo.22059294`. They are referenced rather than duplicated here.
