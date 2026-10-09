# Checks circuit_Px_Ry from 01_first_circuit.py (defined in qcircuits/circuits.py).
# Run from the repository root:  pytest -v

import pytest
from pennylane import numpy as np

from conftest import ATOL
from qcircuits.circuits import make_circuit_Px_Ry


def test_pi_gives_one(dev2):
    """At theta = pi, RY turns |1> back into |0>, so <Z> is +1."""
    circuit_Px_Ry = make_circuit_Px_Ry(dev2)
    assert circuit_Px_Ry(np.pi) == pytest.approx(1.0, abs=ATOL)
