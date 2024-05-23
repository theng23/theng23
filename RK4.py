import math

def rk4(f, t0, y0, h, num_steps):
    t_values = [t0]
    y_values = [y0]

    for _ in range(num_steps):
        t = t_values[-1]
        y = y_values[-1]

        k1 =  f(t, y)
        k2 =  f(t + 0.5 * h, y + 0.5 * h * k1)
        k3 =  f(t + 0.5 * h, y + 0.5 * h * k2)
        k4 =  f(t + h, y + h * k3)

        # Print the values of k1, k2, k3, k4
        print(f"Step {_ + 1}: k1 = {k1}, k2 = {k2}, k3 = {k3}, k4 = {k4}")
        #
        y_next = y + h*(k1 + 2 * k2 + 2 * k3 + k4) / 6.0
        t_next = t + h

        t_values.append(t_next)
        y_values.append(y_next)

    return t_values, y_values

# Given ODE: dy/dt = ...
def example_ode(t, y):
    return math.exp(t-y)

# Initial conditions
initial_t = 0.0
initial_y = 1
step_size = 0.25
num_steps = int((1 - initial_t) / step_size)  # Adjust the number of steps based on the interval and step size

# Run RK4 method
t_values, y_values = rk4(example_ode, initial_t, initial_y, step_size, num_steps)

# Print the results or visualize as needed
for t, y in zip(t_values, y_values):
    print(f"t = {t:.2f}, y = {y:.6f}")
