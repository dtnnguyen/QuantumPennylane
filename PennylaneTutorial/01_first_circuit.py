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

# Mathematically, the circuit initializes the system.
# It flips both qubits to |1> state using PauliX and CNOT gates,
# then rotates the first qubit (wires=0) by theta before measuring it.
# wire 0: |0> ---------(+)---- R_y(theta) --- <Z>
#                       |
# wire 1: |0> ---X------*----------------------
# (+) is the CNOT target and * is its control.
# This quantum function circuit_Px_Ry() contains instructions for the device to perform
# A Quantum Node = Quantum computation unit
# A Quantum Node encapsulate: device and function
@qml.qnode(dev)
def circuit_Px_Ry(theta):
    # Quantum operations
    # All qubits start in the |0> state.
    # 1. Apply a Pauli-X gate (quantum NOT gate) to second qubit(wires=1).
    #   The system starts in the default |0> state, flips the 2nd qubit to |1> state
    qml.PauliX(wires=1)
    # CNOT : Controlled-NOT logic gate
    # 2. Apply a CNOT gate where the 2nd qbit (wires=1) is the control,
    #   and the first qubit (wires=0) is the target.
    #   Because the 2nd qubit (wires=1) was flipped earlier, 
    # this gate will flip 1st qubit (wires=0) from |0> to |1>   
    qml.CNOT(wires=[1,0])
    # 3. Rotate the 1st qubit (wires=0) by theta around the Y axis of the Bloch sphere
    qml.RY(theta, wires=0)
    # 4. Measure and return the expectation value 
    #    The avg measurement outcome of the Pauli-Z operator on the 1st qubit(wires=0)
    #    The result will be a single scalar value between -1.0 (|1>) and +1.0(|0>)
    return qml.expval(qml.PauliZ(wires=0))

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
