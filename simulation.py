import matplotlib.pyplot as plt

# constants
mass = 0.5 #kg
spring_constant = 1 #N/m
current_time = 0.0
time_step = 0.01 # seconds

# initial variables
v_o = 0 # m/s
x_o = -1.0 # m

# state lists
position = [x_o]
velocity = [v_o]
time = [0]

def Acceleration_equation(x):
    return (-spring_constant/mass)*x


while(current_time < 100):
    # Calculate current acceleration, velocity, and position
    a = Acceleration_equation(position[-1])
    v = velocity[-1] + time_step * a
    x = position[-1] + time_step * velocity[-1]
    current_time += time_step

    # add values to the list
    position.append(x)
    velocity.append(v)
    time.append(current_time)

fig, ax = plt.subplots(1,2, layout="constrained")
ax[0].plot(time, position)
ax[0].set_title("position with respect to time")

ax[1].plot(time, velocity)
ax[1].set_title("velocity with respect to time")

plt.show()