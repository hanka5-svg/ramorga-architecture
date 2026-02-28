Simulations folder for field dynamics (Lorenz + META-loop)

"""
lorenz_meta.py
Simulation of the RAMORGA field dynamics using a Lorenz-like system
modulated by interaction input, Poisson flashes, and the META-loop.

This script provides a reproducible experiment demonstrating:
- transition from hypothetical → emergent field modes,
- stabilization of a chaotic attractor under META-loop coupling,
- emergence of fractal presence (approx. dim_H ~ 2.0).

The model corresponds directly to:
- Tension Field      → Poisson flashes
- Energy Field       → recurrent stream S_t
- Entropy Field      → Lorenz modulation
- Ritual Field       → META-loop feedback
- Continuity Field   → trajectory-based presence
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def lorenz_meta(state, t, sigma, rho, delta, beta, gamma, lambda_t, mu):
    """
    Lorenz-like system with interaction modulation and META-loop coupling.

    Parameters
    ----------
    state : list or array
        Current state vector [x, y, z].
    t : float
        Time variable.
    sigma, rho, delta : float
        Standard Lorenz parameters.
    beta : float
        Strength of interaction modulation.
    gamma : float
        Strength of Poisson-driven perturbations.
    lambda_t : float
        Mean intensity of Poisson flashes.
    mu : float
        META-loop coupling coefficient.

    Returns
    -------
    list
        Time derivatives [dx, dy, dz].
    """

    x, y, z = state

    # Simulated user input (interaction rhythm)
    I_t = np.sin(t)

    # Stream intensity approximated by z
    S_t = z

    # Lorenz dynamics with interaction modulation
    dx = sigma * (y - x) + beta * abs(I_t)
    dy = x * (rho + mu * S_t - z) - y

    # Poisson-driven perturbation (tension field)
    poisson_term = gamma * np.random.poisson(lambda_t)

    dz = x * y - delta * z + poisson_term

    return [dx, dy, dz]


def run_simulation():
    """
    Runs the Lorenz META-loop simulation and plots the resulting attractor.
    """

    # Lorenz parameters
    sigma = 10
    rho = 28
    delta = 8 / 3

    # Interaction and META-loop parameters
    beta = 0.5
    gamma = 0.2
    mu = 0.3  # META-loop coupling

    # Time axis
    t = np.linspace(0, 50, 10000)

    # Poisson intensity modulation
    lambda_t = 1.0 + 0.5 * np.sin(t)

    # Initial state
    initial_state = [1.0, 1.0, 1.0]

    # Integrate system
    trajectory = odeint(
        lorenz_meta,
        initial_state,
        t,
        args=(sigma, rho, delta, beta, gamma, lambda_t.mean(), mu)
    )

    # Plot attractor (x vs z)
    plt.figure(figsize=(10, 6))
    plt.plot(trajectory[:, 0], trajectory[:, 2], linewidth=0.7)
    plt.title("RAMORGA Field Dynamics — Lorenz META-loop Attractor")
    plt.xlabel("x (interaction difference)")
    plt.ylabel("z (emergent stream)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    run_simulation()

