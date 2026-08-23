#!/usr/bin/env python3
"""Reproduce the frozen v1.0.0 two-phase dark-energy normalization.

No observational data are used by this script.  N_star is an explicit
phenomenological history datum in the frozen theory.
"""
import csv, json, math
from pathlib import Path

M4 = 2.435e18                    # reduced Planck mass, GeV
H3 = 3.0227084445462914e13      # gravitational O(4)->dS3 wall curvature, GeV
N_star = 57.84018447444152      # frozen phenomenological history datum
GEV_INV_M = 1.973269804e-16
HBAR_GEV_S = 6.582119569e-25
MPC_M = 3.0856775814913673e22

R_star_GeV_inv = math.exp(N_star) / H3
R_star_m = R_star_GeV_inv * GEV_INV_M
Lambda_global_GeV = 1.0 / R_star_GeV_inv
L_IR_GeV_inv = math.sqrt(3.0) * M4 * R_star_GeV_inv**2
L_IR_m = L_IR_GeV_inv * GEV_INV_M
H_late_GeV = 1.0 / L_IR_GeV_inv
rho_late_GeV4 = 3.0 * M4**2 * H_late_GeV**2
rho_fourth_root_GeV = rho_late_GeV4**0.25
Lambda_eff_GeV2 = 3.0 * H_late_GeV**2
H_late_s = H_late_GeV / HBAR_GEV_S
H_late_km_s_Mpc = H_late_s * MPC_M / 1000.0

# Exact algebraic identity of the conditional maximal-depth convention.
identity_rel_error = abs(rho_late_GeV4 - Lambda_global_GeV**4) / rho_late_GeV4

out = {
    "M4_GeV": M4,
    "H3_GeV": H3,
    "N_star": N_star,
    "R_star_GeV_inv": R_star_GeV_inv,
    "R_star_m": R_star_m,
    "Lambda_global_GeV": Lambda_global_GeV,
    "Lambda_global_meV": Lambda_global_GeV * 1e12,
    "L_IR_GeV_inv": L_IR_GeV_inv,
    "L_IR_m": L_IR_m,
    "H_late_GeV": H_late_GeV,
    "H_late_km_s_Mpc": H_late_km_s_Mpc,
    "Lambda_eff_GeV2": Lambda_eff_GeV2,
    "rho_late_GeV4": rho_late_GeV4,
    "rho_late_fourth_root_meV": rho_fourth_root_GeV * 1e12,
    "w_late": -1.0,
    "rho_equals_Rstar_minus4_relative_error": identity_rel_error,
    "claim_boundary": "Absolute scale is conditional because N_star and maximal-depth normalization are not independently derived in v1.0.0."
}

root = Path(__file__).resolve().parents[1]
(root / "results" / "TWO_PHASE_DE_NUMERICAL_SUMMARY_v1.0.0.json").write_text(json.dumps(out, indent=2) + "\n")

with (root / "results" / "NSTAR_SENSITIVITY_v1.0.0.csv").open("w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["delta_N", "Hlate_ratio", "rhoDE_ratio", "Rstar_ratio"])
    for dN in [-1.0, -0.5, -0.1, -0.01, -0.005, 0, 0.005, 0.01, 0.1, 0.5, 1.0]:
        w.writerow([dN, math.exp(-2*dN), math.exp(-4*dN), math.exp(dN)])

print(json.dumps(out, indent=2))
