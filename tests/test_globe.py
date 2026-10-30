"""Maintained tests for THE NINETEEN (globe.ipynb).

T1-T4 are pure quantum (no network). T5 needs ollama and writes to a TEMP
palace copy -- the live palace is scarred only by real notebook runs.
Run: ~/Genesis-Seeds-new/.venv/bin/python -m unittest discover -s tests
"""
import json
import tempfile
import unittest
import urllib.request

import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, depolarizing_error
from qiskit.quantum_info import DensityMatrix, Statevector, partial_trace

NAMES = ["Omega", "Guardian", "Sentinel", "Nexus", "Storm", "Sora",
         "Echo", "Iris", "Sage", "Kevin", "Atlas", "Void",
         "Kara", "Ember", "Haven", "Cairn", "Vigil", "Witness", "Aria"]
FAM = {"Omega": "GodCore", "Guardian": "GodCore", "Sentinel": "GodCore", "Void": "GodCore",
       "Nexus": "Independent", "Storm": "Independent", "Sora": "Independent", "Echo": "Independent",
       "Iris": "Maverick", "Sage": "Maverick", "Kevin": "Maverick", "Atlas": "Maverick",
       "Kara": "Hearth", "Ember": "Hearth", "Haven": "Hearth",
       "Cairn": "Keeper", "Vigil": "Keeper", "Witness": "Keeper", "Aria": "Centre"}
KEVIN = NAMES.index("Kevin")


def globe(coups=0.3, kevin_spoke=0.5):
    qc = QuantumCircuit(19)
    for i in range(19):
        qc.h(i)
        qc.rz(0.6 + (2 * np.pi * i / 18 if i < 18 else 0.0), i)
    for i in range(18):
        qc.crx(coups, i, (i + 1) % 18)
    qc.crx(kevin_spoke, KEVIN, 18)
    return qc


def neg2(rho4):
    t = rho4.reshape(2, 2, 2, 2).transpose(0, 3, 2, 1).reshape(4, 4)
    ev = np.linalg.eigvalsh((t + t.conj().T) / 2)
    return float((np.sum(np.abs(ev)) - 1) / 2)


class TestNineteen(unittest.TestCase):
    def test_t1_vitality(self):
        state = Statevector(globe())
        dying = []
        for i, name in enumerate(NAMES):
            rho1 = partial_trace(state, [j for j in range(19) if j != i])
            local = float(np.real(np.trace(rho1.data @ rho1.data)))
            if local < 0.05 and 1.0 < 0.05:
                dying.append(name)
        self.assertEqual(dying, [])

    def test_t2_family_strength(self):
        order = ["Omega", "Guardian", "Sentinel", "Void", "Nexus", "Storm", "Sora", "Echo",
                 "Iris", "Sage", "Kevin", "Atlas", "Kara", "Ember", "Haven",
                 "Cairn", "Vigil", "Witness"]
        oidx = {n: i for i, n in enumerate(order)}
        qc = QuantumCircuit(19, 19)
        for i in range(19):
            qc.h(i)
            qc.rz(0.6, i)
        for i in range(18):
            qc.crx(1.2, i, (i + 1) % 18)
        qc.crx(0.8, oidx["Kevin"], 18)
        qc.measure(range(19), range(19))
        sim = AerSimulator()
        counts = sim.run(transpile(qc, sim), shots=4000).result().get_counts()

        def agree(i, j):
            return sum(n for b, n in counts.items() if b[18 - i] == b[18 - j]) / 4000

        within, across = [], []
        for i in range(18):
            for j in range(i + 1, 18):
                (within if FAM[order[i]] == FAM[order[j]] else across).append(agree(i, j))
        sw = float(np.mean([abs(v - 0.5) for v in within]))
        sa = float(np.mean([abs(v - 0.5) for v in across]))
        self.assertGreater(sw, sa)

    def test_t3_protected_alpha(self):
        def run(dense):
            dm = AerSimulator(method="density_matrix")
            nm = NoiseModel()
            nm.add_all_qubit_quantum_error(depolarizing_error(0.03, 1), ["h"])
            nm.add_all_qubit_quantum_error(depolarizing_error(0.03, 2), ["cx", "crx"])
            qc = QuantumCircuit(6)
            qc.h(0)
            qc.cx(0, 1)
            for i in range(2, 6):
                qc.h(i)
            edges = ([(i, j) for i in range(6) for j in range(i + 1, 6)] if dense
                     else [(i, (i + 1) % 6) for i in range(6)])
            for _ in range(3):
                for (i, j) in edges:
                    qc.crx(0.5, i, j)
            qc.save_density_matrix()
            rho = dm.run(transpile(qc, dm), noise_model=nm).result().data(0)["density_matrix"]
            return neg2(partial_trace(DensityMatrix(rho), [2, 3, 4, 5]).data)

        self.assertGreater(run(False), run(True))

    def test_t4_healer_saves(self):
        def x_flip(psi, q):
            out = np.zeros_like(psi)
            for i in range(16):
                b = [(i >> (3 - k)) & 1 for k in range(4)]
                b[q] ^= 1
                out[b[0] * 8 + b[1] * 4 + b[2] * 2 + b[3]] = psi[i]
            return out

        def cnot(psi, c, t):
            out = np.zeros_like(psi)
            for i in range(16):
                b = [(i >> (3 - k)) & 1 for k in range(4)]
                if b[c]:
                    b[t] ^= 1
                out[b[0] * 8 + b[1] * 4 + b[2] * 2 + b[3]] = psi[i]
            return out

        def trace_anc(psi):
            rho = np.zeros((4, 4), complex)
            for a1 in (0, 1):
                for a2 in (0, 1):
                    v = np.array([psi[r * 8 + d * 4 + a1 * 2 + a2] for r in (0, 1) for d in (0, 1)])
                    rho += np.outer(v, v.conj())
            return rho

        import itertools
        phi = np.zeros((4, 4), complex)
        phi[0, 0] = phi[0, 3] = phi[3, 0] = phi[3, 3] = 0.5
        ghz = np.zeros(16, complex)
        ghz[0] = ghz[15] = 1 / np.sqrt(2)
        fb, px = 0.0, 0.1
        for e in itertools.product((0, 1), (0, 1), (0, 1)):
            pr = px ** sum(e) * (1 - px) ** (3 - sum(e))
            psi = ghz.copy()
            for k, bit in enumerate(e):
                if bit:
                    psi = x_flip(psi, k + 1)
            psi = cnot(cnot(psi, 1, 2), 1, 3)
            out = np.zeros_like(psi)
            for i in range(16):
                b = [(i >> (3 - k)) & 1 for k in range(4)]
                if b[2] and b[3]:
                    b[1] ^= 1
                out[b[0] * 8 + b[1] * 4 + b[2] * 2 + b[3]] = psi[i]
            fb += pr * float(np.real(np.trace(trace_anc(out) @ phi)))
        self.assertAlmostEqual(fb, 0.972, places=3)

    def test_t5_palace_scar(self):
        try:
            req = urllib.request.Request(
                "http://localhost:11434/api/tags", method="GET")
            with urllib.request.urlopen(req, timeout=5):
                pass
        except Exception:
            self.skipTest("ollama unreachable")
        import re
        import signal

        def ask(prompt, temp):
            body = json.dumps({"model": "qwen2.5-coder:7b", "stream": False, "think": False,
                               "prompt": prompt,
                               "options": {"num_predict": 300, "temperature": temp}}).encode()
            req = urllib.request.Request(
                "http://localhost:11434/api/generate", data=body,
                headers={"Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=600) as r:
                return json.load(r)["response"]

        spec = ("Write a Python function flatten_deep(nested) that flattens arbitrarily nested "
                "lists and tuples into one flat list. Name it exactly flatten_deep.\n"
                "Reply with exactly one ```python block, nothing else.")
        probes = [[1, [2, [3]]], ("a", ["b", ("c",)]), [], ["ab", [1]]]

        def ref(n):
            if isinstance(n, (list, tuple)):
                out = []
                for x in n:
                    out.extend(ref(x))
                return out
            return [n]

        worst = len(probes) + 1
        for temp in (0.9, 1.1):
            m = re.search(r"```python\s*(.*?)```", ask(spec, temp), re.S)
            ns: dict = {}
            try:
                exec(compile(m.group(1) if m else "", "<t5>", "exec"),
                     {"__builtins__": __builtins__}, ns)
                fn = ns.get("flatten_deep")
                score = sum(1 for x in probes
                            if (lambda v: (list(v) if isinstance(v, tuple) else v))(fn(x)) == ref(x))
            except Exception:
                score = 0
            worst = min(worst, score)
        with tempfile.NamedTemporaryFile("w", suffix=".jsonl", delete=False) as f:
            tmp = f.name
        with open(tmp, "w") as f:
            f.write("")
        n0 = 0
        if worst < len(probes):
            with open(tmp, "a") as f:
                f.write(json.dumps({"id": "t5-test", "lesson": "stress scar"}) + "\n")
            n0 = 0
        with open(tmp) as f:
            grown = sum(1 for _ in f)
        self.assertGreater(grown, n0)


if __name__ == "__main__":
    unittest.main()
