import numpy as np
import matplotlib.pyplot as plt

# Simulate a vehicle path
path_length = 100 # number of steps in path
step_size = 0.1 # distance between steps

# Simulate a path (a simple sine wave)
t = np.linspace(0,4 * np.pi, path_length)
x_path = t
y_path = np.sin(t)

# Plot the path
plt.plot(x_path, y_path, label="Vehicle Path")
plt.xlabel("x")
plt.ylabel("Y")
plt.legend()
plt.title("Simulated Vehicle Path")
plt.show()

# Simulate IMU data
# Acceleration, angular velocity, orientation

# Caculate velocities and accelerations
vel_x = np.diff(x_path) / step_size
vel_y = np.diff(y_path) / step_size
acc_x = np.diff(vel_x) / step_size
acc_y = np.diff(vel_y) / step_size

# Add some noise to simulate real IMU data
noise_level = 0.01
acc_x += np.random.normal(0, noise_level, len(acc_x))
acc_y += np.random.normal(0, noise_level, len(acc_y))

# Plot the simulated accelerations
plt.plot(acc_x, label="Acc X")
plt.plot(acc_y, label="Acc Y")
plt.xlabel("Time step")
plt.ylabel("Acceleration")
plt.legend()
plt.title("Simulated IMU Data")
plt.show()

# Cone positions (example positions)
cones = np.array([[2, 1], [3, -1], [4, 2], [5, -2], [6, 0]])

# Function to simulate distance measurements to cones
def simulate_cone_measurements(x, y, cones):
    measurements = []
    for cx, cy in cones:
        distance = np.sqrt((cx - x)**2 + (cy - y)**2)
        angle = np.arctan2(cy - y, cx - x)
        measurements.append((distance, angle))
    return measurements

# Simulate measurements for each path step
all_measurements = []
for x, y in zip(x_path, y_path):
    measurements = simulate_cone_measurements(x, y, cones)
    all_measurements.append(measurements)

# Plot cone positions and path
plt.scatter(cones[:, 0], cones[:, 1], color='red', label="Cones")
plt.plot(x_path, y_path, label="Vehicle Path")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.title("Simulated Cone Positions and Vehicle Path")
plt.show()

