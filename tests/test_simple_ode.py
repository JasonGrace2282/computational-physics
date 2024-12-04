"""Solve dv/dt = g"""

import pytest

from computations import ode

g = 10
v0 = 0

def f(t, v):
    """f(t, v) = g"""
    return g


@pytest.mark.parametrize(
    ("t", "n"),
    [
        (2, 100),
        (3, 150),
        (4, 200),
    ],
)
def test_euler(t, n):
    assert abs(ode.euler(f, v0, t, n) - g * t) < 1e-10
    assert abs(ode.runge_kutta(f, v0, t, n) - g * t) < 1e-10
