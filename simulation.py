# constants
mass = 0.5 #kg
spring_constant = 1 #N/m
current_time = 0.0
time_step = 0.1 # seconds

# initial variables
v_o = 0 # m/s
x_o = -1.0 # m

# state lists
position = [x_o]
velocity = [v_o]
time = []

def Acceleration_equation(x):
    return (-spring_constant/mass)*x


while(current_time < 10):
    # Calculate current acceleration, velocity, and position
    a = Acceleration_equation(position[-1])
    v = velocity[-1] + time_step * a
    x = position[-1] + time_step * velocity[-1]
    current_time += time_step

    # add values to the list
    position.append(x)
    velocity.append(v)
    time.append(current_time)

print(time)
print(position)
print(velocity)