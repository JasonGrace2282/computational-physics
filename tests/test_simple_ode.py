"""Solve dv/dt = g"""

from computations import ode

g = 10
v0 = 0

T = 2
N = 100

def f(t, v):
    """f(t, v) = g"""
    return g


def test_euler():
    assert ode.euler(f, v0, T, N) - g * T < 1e-10
