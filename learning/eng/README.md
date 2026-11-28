# Learning: quantum computing fundamentals

A short course on the fundamentals, in the language of linear algebra. States are vectors in ℂ^(2ⁿ), gates are unitary matrices, and Dirac notation appears only as labels (that is how PennyLane and Qiskit report results).

Each lesson is a notebook with theory, NumPy code, figures and exercises. Boxes marked "This was tricky" collect the places where it is easiest to get confused.

| Lesson | Topic |
|---|---|
| [01_qubit_state](01_qubit_state.ipynb) | two-level system, transmon, cooling, the state as a vector in ℂ², qubit vs state vs outcome |
| [02_measurement_born_rule](02_measurement_born_rule.ipynb) | Born rule, shots, 1/√N error, collapse, measurement is not a readout |
| [03_bases_and_phase](03_bases_and_phase.ipynb) | Dirac → linear algebra dictionary, measuring in any basis, global and relative phase, interference |
| [04_bloch_sphere](04_bloch_sphere.ipynb) | parametrisation (θ, φ), axes as bases, measurement as projection, α and β via angles |
| [05_gates_and_circuits](05_gates_and_circuits.ipynb) | unitarity, X, Z, H, rotations, a circuit as a product of matrices, the physics of pulses |
| [06_many_qubits_and_superposition](06_many_qubits_and_superposition.ipynb) | ℂ^(2ⁿ) and the Kronecker product, bit-string indexing, definition of superposition |
| [07_entanglement_and_bell_state](07_entanglement_and_bell_state.ipynb) | the Bell state step by step, determinant test, correlations in every basis, the ibm_fez result |
| [08_bell_in_numpy](08_bell_in_numpy.ipynb) | exercise: the Bell state built by hand from matrices, and 1000 shots |
| [09_grovers_algorithm](09_grovers_algorithm.ipynb) | the oracle as a diagonal matrix and from gates, phase kickback, diffusion as reflection about the mean, rotation by 2θ, where √N comes from, results from ibm_marrakesh |

## Big picture

We cool a physical system so that it is superconducting and starts in its ground state e₀ ⊗ … ⊗ e₀. Microwave pulses rotate its state, which mathematically is multiplying the state vector by unitary matrices. At the end we measure and get one bit string, drawn according to the Born rule. We repeat everything many times to learn the distribution. A quantum algorithm is a choice of rotations that concentrates the distribution on the right answer.

## Dictionary

| Dirac | Linear algebra |
|---|---|
| \|0⟩, \|1⟩ | e₀ = (1, 0), e₁ = (0, 1) |
| \|ab⟩ | e_a ⊗ e_b = e_(2a+b), e.g. \|10⟩ = e₂ |
| ⟨φ\|ψ⟩ | inner product u*v |
| \|ψ⟩⟨ψ\| | matrix v v* (projection) |
| U\|ψ⟩ | Uv |

## Running

The notebooks only need NumPy and matplotlib (both in the project environment: `uv sync`). Cell outputs are saved in the files, so you can read them without running anything, including on GitHub.

Possible next topics: quantum kernels (Demo 2) and noise on real hardware.
