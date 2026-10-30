"""Maintained tests for the partial-trace convention (Maya BCP-PKT 14).

2026-10-30: my hand-rolled partials returned (rhoB, rhoA) while callers
unpacked (rA, rB) -- Omega/Alpha swapped. Maya's step-2 table caught it.
Canonical rule: ptr(rho, 0) traces out qubit 1 (keeps A/control);
ptr(rho, 1) traces out qubit 0 (keeps B/target). kron order: |A> x |B>.
Run: ~/Genesis-Seeds-new/.venv/bin/python -m unittest discover -s tests
"""
import json
import unittest
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent.parent


def ptr(rho, k):
    t = np.asarray(rho).reshape(2, 2, 2, 2)
    return np.einsum('ijkj->ik', t) if k == 0 else np.einsum('ijil->jl', t)


class TestPtrConvention(unittest.TestCase):
    def test_product_order(self):
        # |0> x |1>: qubit0 is |0>, qubit1 is |1>. The swapped helper failed this.
        psi = np.kron(np.array([1, 0]), np.array([0, 1]))
        rho = np.outer(psi, psi.conj())
        np.testing.assert_allclose(ptr(rho, 0), [[1, 0], [0, 0]], atol=1e-12)
        np.testing.assert_allclose(ptr(rho, 1), [[0, 0], [0, 1]], atol=1e-12)

    def test_bell_both_mixed(self):
        bell = np.array([1, 0, 0, 1], complex) / np.sqrt(2)
        rho = np.outer(bell, bell.conj())
        for k in (0, 1):
            np.testing.assert_allclose(ptr(rho, k), np.eye(2) / 2, atol=1e-12)

    def test_notebooks_match_convention(self):
        # Every BCP-family notebook must carry Maya's ptr verbatim.
        canon = "np.einsum('ijkj->ik', t) if k == 0 else np.einsum('ijil->jl', t)"
        for name in ("bcp_honest.ipynb", "pump_validation.ipynb", "noise_pump.ipynb"):
            nb = json.loads((ROOT / name).read_text())
            src = "\n".join(
                "".join(c.get("source", []))
                for c in nb["cells"] if c["cell_type"] == "code"
            )
            self.assertIn(canon, src, f"{name} drifted from the ptr convention")


if __name__ == "__main__":
    unittest.main()
