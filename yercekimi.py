import matplotlib.pyplot as plt

# Parametreler
G = 6.67430e-11  # Evrensel çekim sabiti
m1 = 5.972e24  # Dünya'nın kütlesi (kg)
m2 = 7.348e22  # Ay'ın kütlesi (kg)
r = 3.844e8  # İki cisim arasındaki mesafe (metre)

# Kuvvet hesaplama
F = G * (m1 * m2) / r**2

# Görselleştirme
labels = ["Kütle 1", "Kütle 2"]
values = [m1, m2]
plt.bar(labels, values, color=["blue", "green"])
plt.title(f"Yerçekimi Kuvveti: {F:.2e} N")
plt.ylabel("Kütle (kg)")
plt.show()