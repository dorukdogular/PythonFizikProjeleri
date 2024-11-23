import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parametreler
g = 9.8  # Yerçekimi ivmesi
l = 1.0  # İp uzunluğu (metre)
theta0 = np.radians(30)  # Başlangıç açısı (dereceyi radyana çeviriyoruz)
dt = 0.02  # Zaman adımı

# Başlangıç durumları
theta = theta0
omega = 0.0

# Hareket listeleri
angles = []

# Sarkacın hareketini hesapla
for i in range(500):
    alpha = -(g / l) * np.sin(theta)
    omega += alpha * dt
    theta += omega * dt
    angles.append(theta)

# Görselleştirme
fig, ax = plt.subplots()
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
line, = ax.plot([], [], lw=2)

def update(frame):
    x = l * np.sin(angles[frame])
    y = -l * np.cos(angles[frame])
    line.set_data([0, x], [0, y])
    return line,

ani = FuncAnimation(fig, update, frames=len(angles), interval=dt*1000)
plt.show()