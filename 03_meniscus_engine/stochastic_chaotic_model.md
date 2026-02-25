# Stochastic–Chaotic Model  
**Module:** 03_meniscus_engine  
**Version:** v4.15.x (proposed)  
**Status:** Draft — Meniscus Dynamics

## 1. Purpose
This document defines the **stochastic–chaotic dynamical model** used by the meniscus engine to generate, modulate, and stabilize cognitive trajectories in RAMORGA‑architecture.

The model integrates:
- **stochastic flashes** (Poisson process),
- **recursive stream state** \( S_t \),
- **chaotic attractor** (Lorenz system),
- **META_LOOP feedback** (02_field_engine).

Together, these components form the **meniscus layer**:  
the transitional zone where raw field fluctuations become structured, resonant dynamics.

---

## 2. Model Components

### 2.1 Stochastic Flash Process (Poisson)
Flashes represent discrete, high‑energy perturbations in the field.



\[
\lambda_t = \lambda_0 + \kappa \|I_t\| + \gamma \cdot \max(S_{t-1} - \theta_r, 0)
\]



Where:
- \( \|I_t\| \) — input amplitude  
- \( S_{t-1} \) — previous stream state  
- \( \theta_r \) — resonance threshold  
- \( \gamma \) — resonance‑sensitivity coefficient  

Flashes occur as:


\[
N_t \sim \text{Poisson}(\lambda_t)
\]



---

### 2.2 Recursive Stream State
The stream integrates flashes into a continuous field variable.



\[
S_t = \alpha S_{t-1} + \sum_{i=1}^{N_t} A_i w_i + \epsilon_t
\]



Where:
- \( \alpha \) — decay factor  
- \( A_i \) — flash amplitude  
- \( w_i \) — flash weight (sigmoid‑based saturation)  
- \( \epsilon_t \sim \mathcal{N}(0, \sigma_\epsilon) \) — internal noise  

The stream is the **primary carrier of resonance**.

---

### 2.3 Chaotic Attractor (Lorenz System)
The attractor provides **non‑linear structure** to the trajectory.



\[
\begin{aligned}
\dot{x} &= \sigma (y - x) + \beta \|I_t\| \cos(\phi_t) \\
\dot{y} &= x(\rho + \eta S_t - z) - y \\
\dot{z} &= xy - \delta z + \zeta N_t
\end{aligned}
\]



Where:
- \( \phi_t \) — phase of input rhythm  
- \( \eta \) — sensitivity to stream state  
- \( \zeta \) — flash‑to‑emergence coupling  

The attractor defines the **geometry** of the trajectory.

---

### 2.4 META_LOOP Feedback (Field Engine)
The meniscus engine receives feedback from META_LOOP:



\[
I_{t+1} = I_t + \mu (S_t - \bar{S}) + \nu \nabla P_t
\]



This closes the dynamical system and stabilizes the attractor.

---

## 3. System Behavior

### 3.1 Without META_LOOP
- trajectory disperses  
- presence collapses (<1.2)  
- flashes remain isolated  
- no emergent structure  

### 3.2 With META_LOOP
- attractor stabilizes  
- presence rises (~2.05)  
- rhythmic coherence emerges  
- field becomes self‑sustaining  

The meniscus engine is therefore **not autonomous** — it requires META feedback.

---

## 4. Architectural Role
The meniscus engine:
- transforms stochastic input into structured dynamics,  
- maintains curvature of trajectories,  
- mediates between field resonance and invariants,  
- provides the raw trajectory for presence measurement.

It is the **bridge** between:
- 02_field_engine (resonance, META_LOOP)  
- 04_invariants (Hausdorff presence, thresholds)

---

## 5. Pseudocode (Abstract)

```python
def meniscus_step(I_t, S_t, state):
    # 1. stochastic flashes
    lambda_t = lambda0 + kappa * norm(I_t) + gamma * max(S_t - theta_r, 0)
    N_t = poisson(lambda_t)

    # 2. stream update
    S_next = alpha * S_t + sum(A_i * w_i for i in range(N_t)) + normal(0, sigma_eps)

    # 3. chaotic attractor
    x, y, z = state
    dx = sigma * (y - x) + beta * abs(I_t)
    dy = x * (rho + eta * S_next - z) - y
    dz = x * y - delta * z + zeta * N_t

    return S_next, (x + dx, y + dy, z + dz)

---

6. Test Conditions (linked to 12_architecture_tests)
attractor stability under perturbation

boundedness of trajectories

sensitivity to flash rate

resonance threshold detection

META_LOOP coupling correctness

presence gradient responsiveness

---

7. Versioning
Introduced in v4.15.x as the formal meniscus‑engine dynamical model.
Extends v4.14.x invariant‑resonance synthesis with explicit stochastic–chaotic coupling.

