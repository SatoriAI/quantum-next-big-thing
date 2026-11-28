"""Small helpers for the DSS demos: plots in the deck's colours and IBM result files."""
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

GREEN = "#1A8A1F"
LIGHT = "#96E199"
GREY = "#BDBDBD"
TEXT = "#242424"
RESULTS = Path(__file__).with_name("ibm_results.json")

plt.rcParams.update({
    "figure.dpi": 120,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.edgecolor": GREY,
    "axes.titlesize": 14,
    "axes.labelsize": 12,
    "font.size": 12,
})


def plot_counts(counts, title="", highlight=None):
    """Bar chart of measurement counts. Shows every bitstring, also the ones that never came up."""
    counts = {str(k): int(v) for k, v in counts.items()}
    n = len(next(iter(counts)))
    labels = [format(i, f"0{n}b") for i in range(2 ** n)]
    values = [counts.get(b, 0) for b in labels]
    colors = [GREEN if (highlight is None or b == highlight) else LIGHT for b in labels]
    fig, ax = plt.subplots(figsize=(max(4, 0.8 * len(labels)), 3.2))
    bars = ax.bar(labels, values, color=colors)
    ax.bar_label(bars, padding=3)
    ax.set_xlabel("measurement outcome")
    ax.set_ylabel("shots")
    ax.set_ylim(0, max(values) * 1.18 + 1)
    ax.set_title(title, color=TEXT)
    plt.show()


def plot_probs(probs, title="", highlight=None):
    """Bar chart of exact probabilities from qml.probs."""
    n = int(np.log2(len(probs)))
    labels = [format(i, f"0{n}b") for i in range(2 ** n)]
    colors = [GREEN if (highlight is None or b == highlight) else LIGHT for b in labels]
    fig, ax = plt.subplots(figsize=(max(4, 0.8 * len(labels)), 3.2))
    bars = ax.bar(labels, probs, color=colors)
    ax.bar_label(bars, labels=[f"{p:.2f}" for p in probs], padding=3)
    ax.set_xlabel("measurement outcome")
    ax.set_ylabel("probability")
    ax.set_ylim(0, 1.1)
    ax.set_title(title, color=TEXT)
    plt.show()


def load_ibm(name):
    """Counts saved by 00_ibm.ipynb, plus backend name and date."""
    data = json.loads(RESULTS.read_text())
    return data[name]["counts"], data[name]["backend"], data[name]["date"]


def load_grover(secret):
    """Grover counts for the given secret, plus backend, date and the secret actually run (as bits).
    Results files from before the 8-secret run contain only secret 5."""
    data = json.loads(RESULTS.read_text())
    key = f"grover_{secret}" if f"grover_{secret}" in data else "grover"
    bits = format(secret, "03b") if key != "grover" else "101"
    return data[key]["counts"], data[key]["backend"], data[key]["date"], bits
