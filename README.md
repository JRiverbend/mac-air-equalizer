# macOS System-Wide Equalizer (Lite)

A lightweight 10-band audio equalizer designed specifically for older Macs (like the MacBook Air 2017). It uses **FFT (Fast Fourier Transform)** processing to ensure high-quality sound manipulation with minimal CPU overhead.

## 🚀 Key Features
* **10-Band Control:** Fine-tune frequencies from 31Hz to 16kHz.
* **Optimized for Performance:** Uses FFT-based filtering to prevent system lag on older hardware.
* **Soft Limiter:** Built-in protection to prevent audio clipping and distortion.
* **Simple GUI:** Responsive interface built with PyQt5.

---

## 🛠 Prerequisites

To route system audio through this equalizer, you need a virtual audio driver:
1. **Install [BlackHole 2ch](https://existential.audio/blackhole/)** (Free & Open Source).
2. Go to **System Preferences > Sound > Output** and select **BlackHole 2ch**.

---

## 📦 Installation & Launch

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/JRiverbend/mac-air-equalizer.git](https://github.com/JRiverbend/mac-air-equalizer.git)
   cd mac-air-equalizer
Set up a virtual environment:

Bash
python3 -m venv venv
source venv/bin/activate
Install dependencies:

Bash
pip install numpy scipy PyQt5 sounddevice
Run the application:

Bash
python3 equalizer.py
⚡️ Easy Launch (macOS Application)
Instead of using the terminal, you can create a native macOS shortcut:

Open Script Editor (Spotlight search: "Script Editor").

Paste the following code (replace YOUR_PATH with your actual folder path):

AppleScript
tell application "Terminal"
    do script "cd /Users/YOUR_USER/YOUR_PATH && source venv/bin/activate && python3 equalizer.py"
    activate
end tell
Go to File > Export, select File Format: Application, and save it as "Equalizer".

Now you can launch it with a simple double-click from your Desktop or Dock!

🧬 Technical Stack
Language: Python 3.x

DSP: NumPy & SciPy

GUI: PyQt5

Audio I/O: SoundDevice (PortAudio)

License
MIT License - Feel free to use and modify!

