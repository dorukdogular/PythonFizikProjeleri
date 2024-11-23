import numpy as np
import matplotlib.pyplot as plt

# Parametreler
num_particles = 10
num_steps = 100
x = np.zeros((num_particles, num_steps))
y = np.zeros((num_particles, num_steps))

# Rastgele hareket
for i in range(num_particles):
    for j in range(1, num_steps):
        x[i, j] = x[i, j - 1] + np.random.normal(0, 0.1)
        y[i, j] = y[i, j - 1] + np.random.normal(0, 0.1)

# Görselleştirme
plt.figure(figsize=(8, 8))
for i in range(num_particles):
    plt.plot(x[i], y[i])
plt.title("Brownian Motion (Rastgele Hareket)")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
plt.show()