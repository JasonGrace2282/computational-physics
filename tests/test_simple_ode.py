"""Solve dv/dt = g"""

import pytest

from computations import ode

g = 10
v0 = 0

T = 2
N = 100


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
    assert ode.euler(f, v0, T, N) - g * t < 1e-10
    assert ode.runge_kutta(f, v0, T, N) - g * t < 1e-10
