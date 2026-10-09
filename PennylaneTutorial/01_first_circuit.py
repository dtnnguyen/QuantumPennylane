import pennylane as qml
from pennylane import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

try:
    IMAGES = Path(__file__).parent / "images"   # run as a script: images/ next to this file
except NameError:
    IMAGES = Path.cwd() / "images"              # Jupyter has no __file__: images/ next to the notebook

# A qubit is referred to as a wire
dev = qml.device('default.qubit', wires=2)

# The circuit lives in qcircuits/circuits.py so the tests can check it too.
# make_circuit_Px_Ry builds it on this device; it is used exactly as before.
from qcircuits.circuits import make_circuit_Px_Ry
circuit_Px_Ry = make_circuit_Px_Ry(dev)

# Quick check: at theta = pi, RY turns |1> back into |0>, so this prints 1.0
print(circuit_Px_Ry(np.pi))

thetas = np.arange(-np.pi, np.pi, 0.01)
measurementsPxRy = np.zeros(len(thetas))

for i, theta in enumerate(thetas):
    measurementsPxRy[i]=circuit_Px_Ry(theta)

plt.plot(thetas, measurementsPxRy)
IMAGES.mkdir(parents=True, exist_ok=True)
plt.savefig(IMAGES / "01_first_circuit.png", dpi=300, bbox_inches="tight")
plt.show()
