import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')


G = 6.67430e-11
while True:
    try:
        m = int(input("What is the mass of the black hole, in Solar Masses? "))
        num_particles = int(input("How many particles are in the accretion disk? "))  # Number of particles in the accretion disk
        break
    except ValueError:
        pass

M = 1.989e30 * m  
time_step = 1e5

# Initialize particle positions in a circular disk
radii = np.random.uniform(3e10, 1e12, num_particles)  # Random radii
angles = np.random.uniform(0, 2 * np.pi, num_particles)  # Random angles


x = radii * np.cos(angles)
y = radii * np.sin(angles)

# circular orbit velocity
velocities = np.sqrt(G * M / radii)
vx = -velocities * np.sin(angles)
vy = velocities * np.cos(angles)


fig, ax = plt.subplots()

black_hole = plt.Circle((0, 0), 1e11, color='black')  # Adjust radius to match your scale
ax.add_artist(black_hole)


ax.set_xlim(-1e12, 1e12)
ax.set_ylim(-1e12, 1e12)
ax.set_aspect('equal', adjustable='box')


scatter = ax.scatter(x, y, s=1)

# Simulation loop
for _ in range(1000):  # Run for 1000 time steps
    # Calculate distances to the black hole
    distances = np.sqrt(x ** 2 + y ** 2)

    # Calculate gravitational acceleration
    accel = G * M / distances ** 2
    ax_accel = -accel * x / distances
    ay_accel = -accel * y / distances

    # Update velocities and positions
    vx += ax_accel * time_step
    vy += ay_accel * time_step
    x += vx * time_step
    y += vy * time_step

    # Update scatter plot data
    scatter.set_offsets(np.c_[x, y])

    # Pause to create animation effect
    plt.pause(0.01)

plt.show()
