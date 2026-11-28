# Quantum computing: next big thing?

Live demos and learning materials from the talk *"Quantum computing: next big thing?"* by Dawid Hanrahan and Jakub Okrzesa (Addepto), DataScience Summit, November 2026.

Two short demos, each placed right after the slides it illustrates. Everything runs on a laptop simulator; the Grover circuit (and a Bell state) also runs on a real IBM quantum processor.

## Demos

| Notebook | When | What you see |
| --- | --- | --- |
| `notebooks/00_ibm.ipynb` | start of the talk | Sends the Bell and Grover circuits to a real IBM QPU and saves the counts |
| `notebooks/01_grover.ipynb` | Demo 1 | Grover on 3 qubits: ≈ 95% after 2 iterations, why more iterations make it worse, and the real-hardware result |
| `notebooks/02_qsvm_moons.ipynb` | Demo 2 | A quantum kernel SVM vs a classical RBF SVM on two moons (0.89 vs 0.99) |
| `notebooks/extra_entanglement.ipynb` | extra | A fair coin, two independent coins, then one CNOT: the Bell state (a demo cut after the dry run) |

Run `00_ibm` at the start of the talk, and once in the morning as a backup. If the IBM queue is slow, the demos use the last saved `ibm_results.json`.

## Learning

`learning/` is a short course on the fundamentals in the language of linear algebra: qubit states, the Born rule, bases and phase, the Bloch sphere, gates and circuits, many qubits, entanglement, and Grover's algorithm. Each lesson is a notebook with NumPy code, figures and exercises, with outputs saved so they read well on GitHub.

- [English](learning/eng/README.md)
- [Polski](learning/pl/README.md)

## Results on real hardware

`notebooks/ibm_results.json` holds the latest counts saved by `00_ibm.ipynb` (1,000 shots per circuit). The notebook picks the least busy IBM processor, so the backend and the exact numbers change between runs. In the saved run (`ibm_marrakesh`, IBM Heron, 27 November 2026):

- Bell state: 00 or 11 in 949 of 1,000 shots; 01 and 10 are noise.
- Grover, one circuit for each of the 8 possible secrets: the secret comes up in 758 to 820 of 1,000 shots (783 for 101), against 95% on a noiseless simulator.

## Setup

Requires Python 3.12 and [uv](https://docs.astral.sh/uv/).

```bash
uv sync
```

For the IBM notebook, create a free account at [quantum.cloud.ibm.com](https://quantum.cloud.ibm.com) and put your API key in `.env`:

```
IBM_QUANTUM_PLATFORM_API_KEY=your-key
```

The demos and the learning notebooks run without an IBM account; only the last cell of each demo, which plots the real-hardware counts, needs `ibm_results.json` (included).

Built with [PennyLane](https://pennylane.ai), [Qiskit](https://www.ibm.com/quantum/qiskit) and scikit-learn.
