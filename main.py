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

#  Temizleme işlemi
y_orig, y_clean, sr = ses_temizle()

# Grafikler
# Orijinal ses için
plot_waveform(y_orig, sr, "Orijinal Ses")
plot_spectrogram(y_orig, sr, "Orijinal Ses")

# Temiz ses için
plot_waveform(y_clean, sr, "Temizlenmiş Ses")
plot_spectrogram(y_clean, sr, "Temizlenmiş Ses")

# Karşılaştırma
plot_overlay_waveform(y_orig, y_clean, sr)
plot_side_by_side_spectrograms(y_orig, y_clean, sr)
plot_difference_waveform(y_orig, y_clean, sr)
plot_spectrogram_difference(y_orig, y_clean, sr)
