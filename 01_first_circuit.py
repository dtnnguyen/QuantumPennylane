import pennylane as qml
from pennylane import numpy as np
import matplotlib.pyplot as plt

# qubit is referred as wire
dev=qml.device('default.qubit', wires=2)

# Mathematically, the circuit initializes the system.
# It flips both qubits to |1> state using PauliX and CNOT gates,
# then rotate the first qubit (wires=0) by theta before measuring it.
# |0> ---------- R_y(theta) ------- <Z> 
#                 |
# |0> -------X---------------------
# This quantum function circuit() contains instructions for the device to perform
# A Quantum Node = Quantum computation unit
# A Quantum Node encapsulate: device and function
@qml.qnode(dev)
def circuit_Px_Ry(theta):
    # Quantum operations
    # by default, all qubit is default at 0-state
    # 1. Apply a Pauli-X gate (quantum NOT gate) to second qubit(wires=1).
    #   The system starts in the default |0> state, flips the 2nd qubit to |1> state
    qml.PauliX(wires=1)
    # CNOT : Controlled-NOT logic gate
    # 2. Apply a CNOT gate where the 2nd qbit (wires=1) is the control,
    #   and the first qubit (wires=0) is the target.
    #   Because the 2nd qubit (wires=1) was flipped earlier, 
    # this gate will flip 1st qubit (wires=0) from |0> to |1>   
    qml.CNOT(wires=[1,0])
    # 3. Apply a parameterized Y-axis rotation around Y-axis with Bloch sphere
    #    by theta angle 
    qml.RY(theta, wires=0)
    # 4. Measure and return the expectation value 
    #    The avg measurement outcome of the Pauli-Z operator on the 1st qubit(wires=0)
    #    The result will be a single scalar value between -1.0 (|1>) and +1.0(|0>)
    return qml.expval(qml.PauliZ(wires=0))

# Test the function
print(circuit_Px_Ry(np.pi))

thetas = np.arange(-np.pi, np.pi, 0.01)
measurementsPxRy = np.zeros(len(thetas))

for i, theta in enumerate(thetas):
    measurementsPxRy[i]=circuit_Px_Ry(theta)

plt.plot(thetas, measurementsPxRy)
plt.show()


###########################
def general_ciruit(theta, pauli_axis="paulix", rotate_axis="ry"):
    # 1. Extract the single-letter axis (e.g., 'x', 'y')
    axis_1 = pauli_axis.lower()[-1]
    axis_2 = rotate_axis.lower()[-1]

    # 2. Return if axes are the same
    if axis_1 == axis_2:
        print("{pauliAxis} and {rotateAxis} should be different from each other")
        return

    # 3. Deduce expected axis
    avail_axes = {"x", "y", "z"}
    used_axes = {axis_1, axis_2}
    # Extract third axis
    third_axis = list(avail_axes - used_axes)
    # print(f"third_axis {third_axis} ")

    # 4. Execute circuit
    return pennylane_circuit(theta, pauli_axis="paulix", rotate_axis="ry", exp_axis="z")
    
# positional arguments passed to a @qml.qnode are automatically treated as differentiable quantum parameters.
# PennyLane expects numerical or array-like values for its positional arguments to compute quantum gradients.
# We should pass non-differentiable arguments as keyword arguments.
@qml.qnode(dev)
def pennylane_circuit(theta, pauli_axis="paulix", rotate_axis="ry", exp_axis="z"):   
    # Quantum operations
    # by default, all qubit is default at 0-state
    # 1. Apply a Pauli-X gate (quantum NOT gate) to second qubit(wires=1).
    #   The system starts in the default |0> state, flips the 2nd qubit to |1> state
    if pauli_axis.lower() == "paulix":
        qml.PauliX(wires=1)
    elif pauli_axis.lower() == "pauliy":
        qml.PauliY(wires=1)
    else:
        qml.PauliZ(wires=1)
        
    # CNOT : Controlled-NOT logic gate
    # 2. Apply a CNOT gate where the 2nd qbit (wires=1) is the control,
    #   and the first qubit (wires=0) is the target.
    #   Because the 2nd qubit (wires=1) was flipped earlier, 
    # this gate will flip 1st qubit (wires=0) from |0> to |1>   
    qml.CNOT(wires=[1,0])

    # 3. Apply a parameterized Y-axis rotation around Y-axis with Bloch sphere
    #    by theta angle 
    if rotate_axis.lower() == "ry":
        qml.RY(theta, wires=0)
    elif rotate_axis.lower() == "rx":
        qml.RX(theta, wires=0)
    else:
        qml.RZ(theta, wires=0)
        
    # 4. Measure and return the expectation value 
    #    The avg measurement outcome of the Pauli-Z operator on the 1st qubit(wires=0)
    #    The result will be a single scalar value between -1.0 (|1>) and +1.0(|0>)
    #if exp_axis.lower() == "x":
    #    return qml.expval(qml.PauliX(wires=0))
    #elif exp_axis.lower() == "y":
    #    return qml.expval(qml.PauliY(wires=0))
    #else:
    return qml.expval(qml.PauliZ(wires=0))

thetas = np.arange(-np.pi, np.pi, 0.01)
measurements_PtRt = np.zeros(len(thetas))
for i, theta in enumerate(thetas):
    measurements_PtRt[i]=general_ciruit(theta, pauli_axis="paulix", rotate_axis="ry")

plt.plot(thetas, measurements_PtRt)
plt.show()