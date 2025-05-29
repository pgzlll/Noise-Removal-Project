import numpy as np
import soundfile as sf
import scipy.signal as signal
from scipy.ndimage import median_filter, gaussian_filter

def ses_temizle(girdi_dosyasi="veriler/Kayit.wav", cikti_dosyasi="veriler/temiz.wav"):
    # 1. Dosyayı oku ve mono yap
    y, sr = sf.read(girdi_dosyasi)
    if y.ndim > 1:
        y = np.mean(y, axis=1)
    print(f"Giriş sesi max değer: {np.max(np.abs(y))}")

    # 2. STFT parametreleri
    n_fft = 2048
    hop_length = 512
    window = 'hann'

    frequencies, times, Zxx = signal.stft(
        y,
        fs=sr,
        window=window,
        nperseg=n_fft,
        noverlap=n_fft - hop_length,
        return_onesided=True,
        padded=True,
        boundary='zeros'
    )

    # 3. Genlik, güç hesabı
    magnitude = np.abs(Zxx)
    power = magnitude ** 2
    n_frames = power.shape[1]
    freqs = np.linspace(0, sr / 2, power.shape[0])

    # 4. Gürültü profili
    init_frames = 30
    noise_profile = np.percentile(power[:, :init_frames], 10, axis=1)
    adaptive_noise_memory = noise_profile.copy()

    # 5. EMA ve temiz güç matrisi
    ema_alpha = 0.95
    power_clean = np.zeros_like(power)

    # 6. Gürültü azaltma döngüsü
    for t in range(n_frames):
        frame_power = power[:, t]
        adaptive_noise_memory = ema_alpha * adaptive_noise_memory + (1 - ema_alpha) * frame_power
        adaptive_noise = adaptive_noise_memory

        for f in range(len(freqs)):
            signal_pwr = frame_power[f]
            noise_pwr = adaptive_noise[f] + 1e-8
            ratio = np.clip(signal_pwr / noise_pwr, 1e-3, 1e3)
            snr = 10 * np.log10(ratio)

            if freqs[f] < 300:
                alpha = 0.1 * np.exp(-snr / 20)
            elif freqs[f] > 5000:
                alpha = 0.5 * np.exp(-snr / 20)
            elif 300 <= freqs[f] <= 3400:
                alpha = 0.4 * np.exp(-snr / 15)
            else:
                alpha = 0.5 * np.exp(-snr / 15)

            alpha = np.clip(alpha, 0.1, 0.9)
            suppression = alpha * noise_pwr
            cleaned_power = signal_pwr - 0.3 * suppression
            min_ratio = 0.03 if 300 <= freqs[f] <= 3400 else 0.01
            cleaned_power = max(cleaned_power, min_ratio * signal_pwr)

            if snr < 0:
                power_clean[f, t] = 1e-10
            else:
                power_clean[f, t] = cleaned_power

            power_clean[f, t] = cleaned_power

    # 7. Median filtre ile yumuşatma
    power_clean_smooth = median_filter(power_clean, size=(3, 3))

    # 8. Gaussian filtre ile yumuşatma
    power_clean_smooth = gaussian_filter(power_clean_smooth, sigma=0.3)

    # 9. Genlik matrisi
    magnitude_clean = np.sqrt(power_clean_smooth)

    # 10. Orijinal fazı kullanarak kompleks spektrum oluştur
    Zxx_clean = magnitude_clean * np.exp(1j * np.angle(Zxx))
    Zxx_clean_real = np.real(Zxx_clean)
    Zxx_clean_imag = np.imag(Zxx_clean)
    Zxx_clean_real_smooth = signal.wiener(Zxx_clean_real, 5)
    Zxx_clean_imag_smooth = signal.wiener(Zxx_clean_imag, 5)
    Zxx_clean = Zxx_clean_real_smooth + 1j * Zxx_clean_imag_smooth

    # 11. Fazı koruyarak ISTFT ile sinyali yeniden oluştur
    _, y_clean = signal.istft(
        Zxx_clean,
        fs=sr,
        window=window,
        nperseg=n_fft,
        noverlap=n_fft - hop_length,
        input_onesided=True,
        boundary=True
    )

    # 12. Normalizasyon
    peak_orig = np.max(np.abs(y))
    peak_clean = np.max(np.abs(y_clean))
    if peak_clean > 1e-9:
        y_clean = y_clean * (peak_orig / peak_clean)

    # 13. Klip
    y_clean = np.clip(y_clean, -1.0, 1.0)

    # 14. Kaydet
    sf.write(cikti_dosyasi, y_clean, sr)

    print("Orijinal RMS:", np.sqrt(np.mean(y**2)))
    print("Temiz RMS   :", np.sqrt(np.mean(y_clean**2)))
    print(f"İşlem tamamlandı, '{cikti_dosyasi}' dosyası oluşturuldu.")

    return y, y_clean, sr  # Grafik için döndür
