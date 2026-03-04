import sys
import threading
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QSlider, QLabel
from PyQt5.QtCore import Qt
from audio_engine import AudioEngine

class EqualizerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        # 1. Инициализируем движок
        self.engine = AudioEngine()
        
        # 2. Запускаем обработку звука в отдельном потоке
        # daemon=True значит, что при закрытии окна звук тоже выключится
        self.audio_thread = threading.Thread(target=self.engine.start, daemon=True)
        self.audio_thread.start()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Saturn System EQ - 10 Bands")
        self.setGeometry(100, 100, 800, 400)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QHBoxLayout(central_widget)

        # Частоты для подписей
        freq_labels = ["31Hz", "63Hz", "125Hz", "250Hz", "500Hz", "1kHz", "2kHz", "4kHz", "8kHz", "16kHz"]
        
        for i in range(10):
            v_box = QVBoxLayout()
            
            # Слайдер
            slider = QSlider(Qt.Vertical)
            slider.setRange(-15, 15)  # От -15 до +15 децибел
            slider.setValue(0)
            slider.setTickPosition(QSlider.TicksBothSides)
            
            # Привязываем движение слайдера к движку
            # Мы передаем индекс слайдера (i), чтобы движок знал, какую частоту менять
            slider.valueChanged.connect(lambda val, idx=i: self.update_gain(idx, val))
            
            label = QLabel(freq_labels[i])
            label.setAlignment(Qt.AlignCenter)
            
            v_box.addWidget(slider)
            v_box.addWidget(label)
            layout.addLayout(v_box)

    def update_gain(self, index, value):
        # Обновляем усиление в реальном времени
        self.engine.gains[index] = value

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = EqualizerApp()
    ex.show()
    sys.exit(app.exec_())