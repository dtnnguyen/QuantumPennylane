# QuantumPennylane

[![Run scripts](https://github.com/dtnnguyen/QuantumPennylane/actions/workflows/run-scripts.yml/badge.svg)](https://github.com/dtnnguyen/QuantumPennylane/actions/workflows/run-scripts.yml)

Learning quantum computing with [PennyLane](https://pennylane.ai), Xanadu's quantum programming library, alongside the [PennyLane Codebook](https://pennylane.ai/codebook) and Xanadu's YouTube playlists.

## Playlists

| Playlist | What it covers | Code |
|---|---|---|
| [PennyLane Tutorials - Playlist](https://www.youtube.com/playlist?list=PL_hJxz_HrXxsY23iiLZTxiPctXKYI6tNV) | Installing PennyLane, first circuits, devices, optimization, VQE, QAOA, Grover, the parameter-shift rule | [`PennylaneTutorial/`](PennylaneTutorial/) |
| [PennyLane Code Camp - Playlist](https://www.youtube.com/playlist?list=PL_hJxz_HrXxueNNX4CVerdIXVPle0JpAX) | Signing up, forming a team and a walkthrough of the Code Camp platform, plus the Munich, Sydney and Toronto meetups | — |
| [Xanadu Cloud Tutorials - Playlist](https://www.youtube.com/playlist?list=PL_hJxz_HrXxugF8aKVyk5t-j-58Aj9awp) | Running jobs on Xanadu's photonic hardware: Borealis and the X-series devices | — |

Install: `pip install -r requirements.txt` (Python 3.11). Jupyter notebook start-up steps: [`PennylaneJupyterNotebook.md`](PennylaneJupyterNotebook.md).

---

## Saving plots

To save a script's figure for its folder's README, call `savefig` before `plt.show()`:

```python
plt.legend()
plt.savefig(Path(__file__).parent / "images" / "<script-name>.png", dpi=300, bbox_inches="tight")
plt.show()   # after savefig: closing the window clears the figure
```
