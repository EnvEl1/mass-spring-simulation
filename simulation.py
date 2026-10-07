import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# constants
mass = 0.5 #kg
spring_constant = 1 #N/m
time_int = (0,100)
time_span = np.linspace(0,100,1000)

# initial variables
initial_state = (-1.0, 0)

# state lists


def state_derivatives(t, state):
    x = state[0]
    v = state[1]
    return (v, -(spring_constant/mass)*x)

solution = solve_ivp(state_derivatives, time_int, initial_state, t_eval=time_span)

fig, ax = plt.subplots(2,1, layout="constrained")
ax[0].plot(solution.t, solution.y[0])
ax[0].set_title("position with respect to time")

ax[1].plot(solution.t, solution.y[1])
ax[1].set_title("velocity with respect to time")

plt.show()