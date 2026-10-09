# Shared pytest setup. Fixtures defined here are available to every test file
# in tests/ without importing them.

import pytest
import pennylane as qml

# Tolerance for comparing expectation values from the simulator.
ATOL = 1e-6


@pytest.fixture
def dev1():
    """A fresh 1-qubit simulator for each test."""
    return qml.device("default.qubit", wires=1)


@pytest.fixture
def dev2():
    """A fresh 2-qubit simulator for each test."""
    return qml.device("default.qubit", wires=2)
