# Template: copy this file to tests/test_<topic>.py, rename the tests and
# replace each pytest.skip(...) with your own check. Files and functions must
# start with "test_" for pytest to find them.
#
# A good test pins down physics you can work out by hand: a known input state,
# a known gate, and the expectation value or probabilities it must give.

import pytest
from pennylane import numpy as np

from conftest import ATOL
# from qcircuits.circuits import <your_function>


def test_single_known_case(dev1):
    """One input whose answer you know exactly."""
    pytest.skip("TODO: call your circuit and assert the expected value")
    # result = <your_function>(dev1, ...)
    # assert result == pytest.approx(<expected>, abs=ATOL)


@pytest.mark.parametrize("theta", np.linspace(0, 2 * np.pi, 5))
def test_matches_formula_over_a_range(dev1, theta):
    """The same check over many inputs: compare against a closed-form formula."""
    pytest.skip("TODO: compare the circuit output with the formula you derived")
    # assert <your_function>(dev1, theta) == pytest.approx(<formula(theta)>, abs=ATOL)


def test_two_qubit_behaviour(dev2):
    """A property that involves more than one qubit, e.g. correlated outcomes."""
    pytest.skip("TODO: check probabilities or correlations across both wires")
