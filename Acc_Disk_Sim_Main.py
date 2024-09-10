import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')


# Constants
G = 6.67430e-11 
while True:
    try:
        m = int(input("What is the mass of the black hole, in Solar Masses? "))
        num_particles = int(input("How many particles are in the accretion disk? ")) # Number of particles in the accretion disk
        break
    except ValueError:
        pass

M = 1.989e30 * m # Converts from solar masses to kg

time_step = 1e5
# Initialize particle positions in a circular disk
radii = np.random.uniform(3e10, 1e12, num_particles)  # Random radii
angles = np.random.uniform(0, 2 * np.pi, num_particles)  # Random angles

# Particle positions (x, y)
x = radii * np.cos(angles)
y = radii * np.sin(angles)

# Particle velocities (circular orbit velocity)
velocities = np.sqrt(G * M / radii)
vx = -velocities * np.sin(angles)
vy = velocities * np.cos(angles)

# Simulation loop
for _ in range(1000):  # Run for 1000 time steps
    # Calculate distances to the black hole
    distances = np.sqrt(x ** 2 + y ** 2)

    # Calculate gravitational acceleration
    accel = G * M / distances ** 2
    ax = -accel * x / distances
    ay = -accel * y / distances

    vx += ax * time_step
    vy += ay * time_step

    x += vx * time_step
    y += vy * time_step

    plt.clf()
    plt.scatter(x, y, s=1)
    plt.xlim(-1e12, 1e12)
    plt.ylim(-1e12, 1e12)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.pause(0.01)

plt.show()
