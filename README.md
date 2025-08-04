# 🖐️ Real-Time Finger Counter

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/W7W61I0YBJ)

A real-time finger counting application using computer vision and machine learning. Count fingers with your webcam in an interactive web interface!

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.8.1-green.svg)
![MediaPipe](https://img.shields.io/badge/MediaPipe-0.10.7-orange.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.29.0-red.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## 🎯 Features

- 🔴 **Real-time detection** - Instant finger counting through your webcam
- ✋ **Multi-hand support** - Detect up to 2 hands simultaneously (10 fingers max)
- 🎨 **Modern web interface** - Clean and intuitive Streamlit UI
- ⚙️ **Adjustable settings** - Customize detection sensitivity
- 📊 **Live metrics** - Real-time display of finger count and hand detection
- 🚀 **High performance** - Optimized for smooth real-time processing

## 🛠️ Technologies

- **Python 3.8+** - Core programming language
- **OpenCV** - Computer vision and image processing
- **MediaPipe** - Google's hand tracking ML solution
- **Streamlit** - Web application framework
- **NumPy** - Numerical computations

## 📋 Prerequisites

- Python 3.8 or higher
- Webcam (built-in or external)
- Modern web browser

## 🚀 Quick Start

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/finger-counter.git
   cd finger-counter
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Launch the Application

**Option 1: Interactive launcher**
```bash
python run.py
```

**Option 2: Direct launch**
```bash
streamlit run app.py
```

**Option 3: Using Python module**
```bash
python -m streamlit run app.py
```

The application will open automatically in your browser at `http://localhost:8501`

## 🎮 How to Use

1. **Start the webcam** by clicking the checkbox
2. **Position your hands** in front of the camera
3. **Raise your fingers** - the app counts them in real-time
4. **Adjust settings** in the sidebar for better detection

### 💡 Tips for Better Detection

- Ensure good lighting conditions
- Use a plain background when possible
- Keep hands clearly visible in the camera frame
- Avoid rapid hand movements

## 📱 Interface Overview

The application features a clean two-column layout:

- **Left Column**: Live webcam feed with visual overlays
- **Right Column**: Real-time metrics and detection results
- **Sidebar**: Adjustable parameters and settings

## 🔧 Configuration

Customize the detection behavior by adjusting:

- **Confidence Threshold**: Sensitivity of hand detection (0.1 - 1.0)
- **Display Options**: Show/hide various UI elements

## 📁 Project Structure

```
finger-counter/
├── app.py              # Main Streamlit application
├── app_yolo.py         # Advanced version with YOLO integration
├── requirements.txt    # Python dependencies
├── config.py          # Configuration settings
├── demo.py            # Standalone demo without Streamlit
├── run.py             # Interactive launcher script
├── install.py         # Automated installation script
├── README.md          # This file
├── INSTALL.md         # Detailed installation guide
└── .gitignore         # Git ignore file
```

## 🧪 Demo Mode

Test the application without Streamlit:

```bash
python demo.py
```

This provides a basic OpenCV window for testing the finger counting functionality.

## ⚡ Performance

- **Lightweight**: Runs smoothly on most modern computers
- **CPU optimized**: No GPU required
- **Real-time**: 30 FPS processing capability
- **Low latency**: Minimal detection delay

## 🐛 Troubleshooting

### Webcam Issues
- Ensure webcam is connected and not used by other applications
- Check camera permissions in your browser/system
- Try restarting the application

### Installation Problems
- Verify Python 3.8+ is installed: `python --version`
- Update pip: `pip install --upgrade pip`
- Install dependencies individually if batch install fails

### Detection Issues
- Improve lighting conditions
- Ensure hands are clearly visible
- Adjust confidence threshold in settings
- Use a plain background

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Google MediaPipe team for the excellent hand tracking solution
- OpenCV community for computer vision tools
- Streamlit team for the amazing web app framework

## 📞 Support

If you encounter any issues or have questions:

1. Check the [troubleshooting section](#-troubleshooting)
2. Review the [installation guide](INSTALL.md)
3. Open an issue on GitHub

---

**Made with ❤️ using Python and Computer Vision**