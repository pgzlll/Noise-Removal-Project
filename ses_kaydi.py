import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np

def ses_kaydi_al(dosya_adi, sure, fs=44100):
    print("Kaydediliyor...")
    recording = sd.rec(int(sure*fs), samplerate = fs, channels=1)
    sd.wait()
    write(dosya_adi, fs, np.int16(recording * 32767))

    print("kayıt alındı.")

kayit_adi = "kayit.wav"

sure = 30
ses_kaydi_al(kayit_adi, sure)

