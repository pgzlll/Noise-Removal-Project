import os
import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np

def ses_kaydi_al():
    # Klasör varsa geç, yoksa oluştur
    if not os.path.exists("veriler"):
        os.mkdir("veriler")

    print("Kayıt ismi: (örn: ornek.wav): ", end="")
    dosya_adi = input().strip()
    if not dosya_adi.endswith(".wav"):
        dosya_adi += ".wav"
    dosya_yolu = os.path.join("veriler", dosya_adi)

    sure = 30  # saniye
    print("Kaydediliyor...")
    recording = sd.rec(int(sure * 44100), samplerate=44100, channels=1)
    sd.wait()
    write(dosya_yolu, 44100, np.int16(recording * 32767))
    print(f"Kayıt alındı: {dosya_yolu}")

    return dosya_yolu
