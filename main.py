# main.py

import os
from frekans_analizi import ses_temizle
from grafikler import (
    plot_waveform,
    plot_overlay_waveform,
    plot_side_by_side_spectrograms,
    plot_difference_waveform,
    plot_spectrogram_difference,
    plot_spectrogram
)

def ana_program():
    print("Yeni ses kaydı oluşturmak ister misiniz (e/h): ", end="")
    cevap = input().strip().lower()

    if cevap == "e":
        from ses_kaydi import ses_kaydi_al
        dosya_yolu = ses_kaydi_al()
    else:
        print("KAYITLI DOSYALARDAN BİRİNİ GİRİN(örn: Kayit.wav): ", end="")
        dosya_adi = input().strip()
        if not dosya_adi.endswith(".wav"):
            dosya_adi += ".wav"
        dosya_yolu = os.path.join("veriler", dosya_adi)

    # Dosya var mı kontrol et
    if not os.path.exists(dosya_yolu):
        print(f"Hata: '{dosya_yolu}' bulunamadı.")
        return
    
    y_orig, y_clean, sr = ses_temizle(dosya_yolu, "veriler/temiz.wav")


    # Grafikler
    plot_waveform(y_orig, sr, "Orijinal Ses")
    plot_spectrogram(y_orig, sr, "Orijinal Ses")

    plot_waveform(y_clean, sr, "Temizlenmiş Ses")
    plot_spectrogram(y_clean, sr, "Temizlenmiş Ses")

    plot_overlay_waveform(y_orig, y_clean, sr)
    plot_side_by_side_spectrograms(y_orig, y_clean, sr)
    plot_difference_waveform(y_orig, y_clean, sr)
    plot_spectrogram_difference(y_orig, y_clean, sr)


if __name__ == "__main__":
    ana_program()
