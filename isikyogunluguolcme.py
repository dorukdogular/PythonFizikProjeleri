import numpy as np
import matplotlib.pyplot as plt

# Işık yoğunluğu simülasyonu
time = np.linspace(0, 10, 100)
intensity = np.sin(time) ** 2  # Yoğunluk değişimi (sinüs dalgası)

# Grafik
plt.plot(time, intensity, label="Işık Yoğunluğu")
plt.title("Işık Yoğunluğu Değişimi")
plt.xlabel("Zaman (saniye)")
plt.ylabel("Yoğunluk")
plt.legend()
plt.grid()
plt.show()