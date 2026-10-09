# Circuits as functions, so scripts, notebooks and tests can share them:
#
#   from qcircuits.circuits import <your_function>
#
# Tip: take the device and the parameters (angles, wires) as arguments instead
# of hard-coding them, so a test can call the same circuit with known inputs.

import pennylane as qml


def make_circuit_Px_Ry(dev):
    """Build circuit_Px_Ry on `dev` (2 wires) and return it, ready to call with theta."""
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

    return circuit_Px_Ry
