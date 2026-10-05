import pennylane as qml
from pennylane import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Image Folder
try:
    IMAGES = Path(__file__).parent / "images"   # run as a script: images/ next to this file
except NameError:
    IMAGES = Path.cwd() / "images"              # Jupyter has no __file__: images/ next to the notebook

# A qubit is referred to as a wire
dev = qml.device('default.qubit', wires=2)

# dictionary to map gate to qml function
PAULI_GATE_MAPPING = { "paulix" : qml.PauliX, "pauliy" : qml.PauliY, "pauliz" : qml.PauliZ}
ROTATE_GATE_MAPPING = { "rx" : qml.RX, "ry" : qml.RY, "rz" : qml.RZ}

def general_circuit(theta, pauli_axis="paulix", rotate_axis="ry"):
    # 1. Extract the single-letter axis (e.g., 'x', 'y')
    axis_1 = pauli_axis.lower()[-1]
    axis_2 = rotate_axis.lower()[-1]

    # 2. Raise an error if both gates use the same axis
    if axis_1 == axis_2:
        raise ValueError(f"{pauli_axis} and {rotate_axis} should be different from each other")

    # 3. Measure along the remaining axis, e.g. x and y leave z -> "pauliz"
    avail_axes = {"x", "y", "z"}
    used_axes = {axis_1, axis_2}
    third_axis = "pauli" + list(avail_axes - used_axes)[0]

    # 4. Execute circuit
    return pennylane_circuit(theta, pauli_axis=pauli_axis, rotate_axis=rotate_axis, exp_axis=third_axis)
    
# positional arguments passed to a @qml.qnode are automatically treated as differentiable quantum parameters.
# PennyLane expects numerical or array-like values for its positional arguments to compute quantum gradients.
# We should pass non-differentiable arguments as keyword arguments.
@qml.qnode(dev)
def pennylane_circuit(theta, pauli_axis="paulix", rotate_axis="ry", exp_axis="pauliz"):
    # Quantum operations
    # All qubits start in the |0> state.
    # 1. Apply the chosen Pauli gate (X, Y or Z) to the second qubit (wires=1).
    #   PauliX and PauliY flip it from |0> to |1> (PauliY also adds a phase of i).
    #   PauliZ leaves |0> unchanged.
    pauli_gate = PAULI_GATE_MAPPING[pauli_axis.lower()]
    pauli_gate(wires=1)
        
    # CNOT : Controlled-NOT logic gate
    # 2. Apply a CNOT gate where the 2nd qbit (wires=1) is the control,
    #   and the first qubit (wires=0) is the target.
    #   If the 2nd qubit is |1>, this flips the 1st qubit (wires=0) from |0> to |1>.
    #   If it is still |0> (the PauliZ case), nothing happens.
    qml.CNOT(wires=[1,0])

    # 3. Rotate the 1st qubit (wires=0) by theta around the chosen axis
    #    (RX, RY or RZ) of the Bloch sphere
    rotate_gate = ROTATE_GATE_MAPPING[rotate_axis.lower()]
    rotate_gate(theta, wires=0)
        
    # 4. Measure and return the expectation value 
    #    The avg measurement outcome of the Pauli operator along exp_axis on the 1st qubit (wires=0)
    #    The result will be a single scalar value between -1.0 and +1.0
    #    (for Pauli-Z: -1.0 means |1>, +1.0 means |0>)
    expval_gate = PAULI_GATE_MAPPING[exp_axis.lower()]
    return qml.expval(expval_gate(wires=0))

thetas = np.arange(-np.pi, np.pi, 0.01)
measurements_px_ry = np.zeros(len(thetas))
measurements_py_rx = np.zeros(len(thetas))
measurements_pz_ry = np.zeros(len(thetas))

for i, theta in enumerate(thetas):
    measurements_px_ry[i] = general_circuit(theta, pauli_axis="paulix", rotate_axis="ry")
    measurements_py_rx[i] = general_circuit(theta, pauli_axis="pauliy", rotate_axis="rx")
    measurements_pz_ry[i] = general_circuit(theta, pauli_axis="pauliz", rotate_axis="ry")

# Setups 1 and 2 both give -cos(theta), so their curves overlap; setup 3 gives sin(theta)
plt.plot(thetas, measurements_px_ry, color="red", 
    linestyle="-",          # Solid line
    marker="o",             # Circle markers
    markersize=8,           # Size of circles
    label="Setup 1")

plt.plot(thetas, measurements_py_rx, color="blue" , 
    linestyle="--",         # Dashed line
    marker="s",             # Square markers
    markersize=4,           # Size of squares
    label="Setup 2")

plt.plot(thetas, measurements_pz_ry, color="darkgreen", 
    linestyle="--",         # Dashed line
    marker="*",             # star markers
    markersize=1,           # Size of stars
    label="Setup 3")

plt.legend(loc="best")

# Safety check: Create the folder if it doesn't exist yet
IMAGES.mkdir(parents=True, exist_ok=True)
plt.savefig(IMAGES / "01b_axis_sweep.png", dpi=300, bbox_inches="tight")

plt.show()