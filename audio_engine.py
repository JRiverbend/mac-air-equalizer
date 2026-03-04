import sounddevice as sd
import numpy as np

class AudioEngine:
    def __init__(self):
        self.fs = 44100
        self.bands = [31, 63, 125, 250, 500, 1000, 2000, 4000, 8000, 16000]
        self.gains = [0.0] * 10
        self.stream = None

    def process_audio(self, indata, outdata, frames, time, status):
        # Если процессор не успевает, выводим ошибку в терминал
        if status:
            print(f"Статус: {status}")
        
        # Переходим в частотную область (FFT) — это в разы быстрее для 10 полос
        spectrum = np.fft.rfft(indata, axis=0)
        frequencies = np.fft.rfftfreq(frames, 1/self.fs)
        
        # Создаем маску усиления
        gain_mask = np.ones(len(frequencies), dtype=np.float32)
        
        for i, freq_center in enumerate(self.bands):
            if self.gains[i] != 0:
                # Находим частоты, попадающие в диапазон полосы
                dist = np.abs(np.log2(frequencies + 1) - np.log2(freq_center + 1))
                # Создаем плавный подъем/спад (колокол)
                band_gain = 10 ** (self.gains[i] / 20)
                influence = np.exp(-dist**2 / (2 * 0.3**2))
                gain_mask *= (1 + (band_gain - 1) * influence)

        # Применяем усиление и возвращаемся в обычный звук
        spectrum *= gain_mask[:, np.newaxis]
        processed = np.fft.irfft(spectrum, axis=0)
        
        # Лимитер, чтобы не хрипело
        outdata[:] = np.clip(processed, -0.9, 0.9)

    def start(self):
        input_id = 2
        output_id = 1
        print(f"Запуск облегченного движка: {input_id} -> {output_id}")
        
        try:
            self.stream = sd.Stream(
                device=(input_id, output_id),
                channels=2,
                callback=self.process_audio,
                samplerate=self.fs,
                blocksize=8192 # Большой буфер = легкая работа для CPU
            )
            self.stream.start()
            print("ГОТОВО! Окно должно открыться.")
        except Exception as e:
            print(f"Ошибка: {e}")

    def stop(self):
        if self.stream:
            self.stream.stop()