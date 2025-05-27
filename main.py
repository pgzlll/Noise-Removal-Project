import soundfile as sf
from grafikler import (
    plot_waveform,
    plot_overlay_waveform,
    plot_side_by_side_spectrograms,
    plot_difference_waveform,
    plot_spectrogram_difference,
    plot_spectrogram
)
from frekans_analizi import ses_temizle

# 1. Temizleme işlemi yap
y_orig, y_clean, sr = ses_temizle()

# 2. Grafiksel analiz
# Orijinal ses
plot_waveform(y_orig, sr, "Orijinal Ses")
plot_spectrogram(y_orig, sr, "Orijinal Ses")

# Temizlenmiş ses
plot_waveform(y_clean, sr, "Temizlenmiş Ses")
plot_spectrogram(y_clean, sr, "Temizlenmiş Ses")

# Karşılaştırmalı grafikler
plot_overlay_waveform(y_orig, y_clean, sr)
plot_side_by_side_spectrograms(y_orig, y_clean, sr)
plot_difference_waveform(y_orig, y_clean, sr)
plot_spectrogram_difference(y_orig, y_clean, sr)
