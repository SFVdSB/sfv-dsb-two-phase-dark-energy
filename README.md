# SFV/dSB Two-Phase Holographic Dark-Energy Cosmology — v1.0.0

This repository accompanies the manuscript:

> **Two-Phase Holographic Cosmology from a Gravitational O(4) Wall: Conditional Reconstruction of the Late Dark-Energy Scale**

Author: Steven Hoffmann  
Version: v1.0.0  
Date: 2026-08-23  
Zenodo DOI: **10.5281/zenodo.22071079**

GitHub repository: `SFVdSB/sfv-dsb-two-phase-dark-energy`

## Core result

The published gravitational O(4) wall provides an early literal `dS3` phase with

`H3 = 3.0227084445e13 GeV`.

The frozen cosmology retains one phenomenological handoff-history datum,

`N_star = 57.8401844744`,

which fixes the global handoff radius

`R_star = H3^-1 exp(N_star) = 85.993 micrometers`.

The finite nonlocal reconstruction sector is assigned the global ruler

`Lambda_global = 1/R_star = 2.294686 meV`.

Under the discrete maximal-depth reconstruction convention,

`L_IR = sqrt(3) Mbar_4 R_star^2`,

which gives

- `L_IR = 1.580518e26 m = 16.7061 Gly`,
- `H_late = 1.248496e-42 GeV`,
- `rho_DE = 2.772638e-47 GeV^4`,
- `rho_DE^(1/4) = 2.294686 meV`,
- exact conditional `w = -1`.

The algebraic identity

`rho_DE = R_star^-4 = Lambda_global^4`

is exact within the frozen maximal-depth convention.

## Claim boundary

This is a **frozen conditional cosmology**, not a first-principles prediction of every observable.

The absolute late dark-energy normalization is conditional because:

1. `N_star` is a phenomenological continuous history datum rather than an action-derived transition criterion;
2. maximal-depth screen-to-bulk saturation and its current order-one ruler convention remain discrete holographic assumptions.

The exact `w=-1` result is geometric once the constant-curvature `dS4` reconstruction is granted.

The primordial scalar state parameters `{A_s, n_s}` are also phenomenological in v1.0.0 after explicit current-action no-go audits. No tensor-to-scalar ratio is frozen as a prediction.

## Required ownership rules

The end-to-end background passes only with the following explicit rules:

- reconstruct the hot `3+1` universe from a local flat `dS3` causal patch; do not turn the global wall `S2` radius into conserved FRW `k=+1` curvature;
- use the inherited true-Minkowski gravitational reference for reconstructed vacuum energy;
- do not double count wall pressure/tension, excitation/Brown–York energy, and late extrinsic curvature as additive copies of one source;
- treat the dimensional handoff as delocalizing but non-destructive so the microscopic holographic screen persists.

## Repository structure

- `paper/` — LaTeX manuscript source. The compiled PDF is distributed with the Zenodo release.
- `freeze/` — frozen theory specification, final falsification audit, and final claim ledger.
- `derivation/` — late-DE and primordial-interface checkpoints leading to the freeze.
- `scripts/` — reproduction scripts, including a lightweight standalone late-scale calculator.
- `results/` — machine-readable numerical summaries and stress-weight controls.
- `reference/` — links to separately published O(4)/CDL and flavor foundations.
- `CLAIM_BOUNDARY.md` — publication claim classes.
- `REPRODUCIBILITY.md` — minimal reproduction instructions.
- `CITATION.cff` and `.zenodo.json` — publication metadata.

## Upstream published foundations

**Gravitational O(4)/CDL foundation**  
DOI: `10.5281/zenodo.22070942`  
GitHub: https://github.com/SFVdSB/sfv-dsb-gravitational-cdl

**Phase B2 flavor**  
DOI: `10.5281/zenodo.22059294`

## Future derivation priorities

The architecture is frozen. Future work should attempt to derive, rather than retune:

1. the handoff value `N_star`, preferably from a symmetry-compatible material/reconstruction flow;
2. the exact screen-scale -> IR-depth theorem and order-one normalization;
3. the primordial `{A_s,n_s}` state from the constrained holographic/material-flow response;
4. channel-resolved handoff/reheating and flavor transport.

The static wall is not assumed to rotate. Possible 4D/5D substrate flow is retained only as a future microscopic derivation program.
