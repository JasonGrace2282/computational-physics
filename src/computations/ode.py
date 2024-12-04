"""Solving linear ordinary differential equations."""

from collections.abc import Callable


def euler(f: Callable[[float, float], float], v0: float, t: float, n: int) -> float:
    """Calculate the solution of dv/dt = f(t, v) with v(0) = v0 at t using n steps.

    This uses the modified explicit Eulers method.
    """
    h = t / n
    v = v0
    for i in range(n):
        t_n = i * h
        v += h * f(t_n + h / 2, v + h / 2 * f(t_n, v))
    return v
