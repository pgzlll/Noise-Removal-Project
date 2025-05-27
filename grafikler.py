import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

def plot_waveform(y, sr, title="Waveform"):
    times = np.arange(len(y)) / sr
    plt.figure(figsize=(10, 4))
    plt.plot(times, y)
    plt.title(title)
    plt.xlabel("Zaman (s)")
    plt.ylabel("Genlik")
    plt.tight_layout()
    plt.show()

def plot_spectrogram(y, sr, title="Spektrogram"):
    f, t, Sxx = signal.spectrogram(y, fs=sr)
    plt.figure(figsize=(10, 4))
    plt.pcolormesh(t, f, 10 * np.log10(Sxx + 1e-8), shading='gouraud')
    plt.title(title)
    plt.ylabel('Frekans [Hz]')
    plt.xlabel('Zaman [s]')
    plt.colorbar(label='Güç [dB]')
    plt.tight_layout()
    plt.show()

def plot_overlay_waveform(y1, y2, sr, title="Üst Üste Ses Dalgaları"):
    times = np.arange(len(y1)) / sr
    plt.figure(figsize=(10, 4))
    plt.plot(times, y1, label="Orijinal")
    plt.plot(times, y2, label="Temizlenmiş", alpha=0.7)
    plt.title(title)
    plt.xlabel("Zaman (s)")
    plt.ylabel("Genlik")
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_side_by_side_spectrograms(y1, y2, sr, title1="Orijinal", title2="Temizlenmiş"):
    f1, t1, Sxx1 = signal.spectrogram(y1, fs=sr)
    f2, t2, Sxx2 = signal.spectrogram(y2, fs=sr)

    plt.figure(figsize=(14, 5))

    plt.subplot(1, 2, 1)
    plt.pcolormesh(t1, f1, 10 * np.log10(Sxx1 + 1e-8), shading='gouraud')
    plt.title(title1)
    plt.xlabel("Zaman [s]")
    plt.ylabel("Frekans [Hz]")
    plt.colorbar(label="Güç [dB]")

    plt.subplot(1, 2, 2)
    plt.pcolormesh(t2, f2, 10 * np.log10(Sxx2 + 1e-8), shading='gouraud')
    plt.title(title2)
    plt.xlabel("Zaman [s]")
    plt.ylabel("Frekans [Hz]")
    plt.colorbar(label="Güç [dB]")

    plt.tight_layout()
    plt.show()

def plot_difference_waveform(y1, y2, sr, title="Dalga Farkı"):
    diff = y1 - y2
    times = np.arange(len(diff)) / sr
    plt.figure(figsize=(10, 4))
    plt.plot(times, diff)
    plt.title(title)
    plt.xlabel("Zaman (s)")
    plt.ylabel("Fark (Genlik)")
    plt.tight_layout()
    plt.show()

def plot_spectrogram_difference(y1, y2, sr, title="Spektrogram Farkı"):
    f, t, Sxx1 = signal.spectrogram(y1, fs=sr)
    _, _, Sxx2 = signal.spectrogram(y2, fs=sr)
    Sxx_diff = np.abs(Sxx1 - Sxx2)

    plt.figure(figsize=(10, 4))
    plt.pcolormesh(t, f, 10 * np.log10(Sxx_diff + 1e-8), shading='gouraud')
    plt.title(title)
    plt.xlabel("Zaman [s]")
    plt.ylabel("Frekans [Hz]")
    plt.colorbar(label="Güç Farkı [dB]")
    plt.tight_layout()
    plt.show()
