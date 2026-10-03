import pennylane as qml
from pennylane import numpy as np
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
def circuit(theta):
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
print(circuit(np.pi))

import matplotlib.pyplot as plt
thetas = np.arange(-np.pi, np.pi, 0.01)
measurements = np.zeros(len(thetas))

for i, theta in enumerate(thetas):
    measurements[i]=circuit(theta)

for i, theta in enumerate(thetas):
    measurements[i]=circuit(theta)

plt.plot(thetas, measurements)
plt.show()