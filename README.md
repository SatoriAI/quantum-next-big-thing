# Quantum computing: next big thing?

Live demos from the talk *"Quantum computing: next big thing?"* by Dawid Hanrahan and Jakub Okrzesa (Addepto), DataScience Summit.

Three short demos, each placed right after the slides it illustrates. Everything runs on a laptop simulator; the Bell state and Grover circuits also run on a real IBM quantum processor.

| Notebook | Demo | What you see |
| --- | --- | --- |
| `notebooks/00_ibm.ipynb` | before the talk | Sends the Bell and Grover circuits to a real IBM QPU and saves the counts |
| `notebooks/01_entanglement.ipynb` | Demo 1 | A fair coin, two independent coins, then one CNOT: the Bell state, always 00 or 11 |
| `notebooks/02_grover.ipynb` | Demo 2 | Grover on 3 qubits: ≈ 95% after 2 iterations, and why more iterations make it worse |
| `notebooks/03_qsvm_moons.ipynb` | Demo 3 | A quantum kernel SVM vs a classical RBF SVM on two moons (0.89 vs 0.99) |
| `learning/01_bell.ipynb` | — | The Bell state built by hand from matrices in NumPy |

## Results on real hardware

`notebooks/ibm_results.json` holds the counts from `ibm_fez` (IBM Heron, 24 November 2026, 1,000 shots):

- Bell state: 00 and 11 in 955 of 1,000 shots; 01 and 10 are noise.
- Grover, secret 101: 760 of 1,000 shots, against 95% on a noiseless simulator.

## Setup

Requires Python 3.12 and [uv](https://docs.astral.sh/uv/).

```bash
uv sync
```

For the IBM notebook, create a free account at [quantum.cloud.ibm.com](https://quantum.cloud.ibm.com) and put your API key in `.env`:

```
IBM_QUANTUM_PLATFORM_API_KEY=your-key
```

The demos 1–3 run without an IBM account; only their last cell, which plots the real-hardware counts, needs `ibm_results.json`.

Built with [PennyLane](https://pennylane.ai), [Qiskit](https://www.ibm.com/quantum/qiskit) and scikit-learn.
