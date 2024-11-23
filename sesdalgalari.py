import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft

# Ses kaydı
fs = 44100  # Örnekleme frekansı
duration = 2  # Kayıt süresi (saniye)
print("Ses kaydediliyor...")
audio = sd.rec(int(fs * duration), samplerate=fs, channels=1)
sd.wait()
print("Kayıt tamamlandı.")

# Fourier dönüşümü
N = len(audio)
yf = fft(audio[:, 0])
xf = np.linspace(0.0, fs / 2, N // 2)

# Görselleştirme
plt.figure(figsize=(12, 6))
plt.plot(xf, 2.0 / N * np.abs(yf[:N // 2]))
plt.title("Ses Dalgası Frekans Analizi")
plt.xlabel("Frekans (Hz)")
plt.ylabel("Genlik")
plt.grid()
plt.show()