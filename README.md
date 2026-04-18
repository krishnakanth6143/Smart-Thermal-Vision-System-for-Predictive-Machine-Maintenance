# 🔥 Smart Thermal Vision System for Predictive Machine Maintenance

An AI-powered thermal imaging system that detects machine faults and abnormalities using deep learning. This system analyzes thermal images to predict equipment failures before they occur, enabling proactive maintenance.

## Features

- **Real-time Thermal Analysis**: Analyzes thermal images to detect equipment faults
- **Deep Learning Model**: ResNet18-based CNN trained on thermal motor images
- **11 Fault Classes**: Detects various motor conditions including:
  - Normal operation (No-load)
  - Single-phase faults (A10, A30, A50)
  - Bearing faults (A_B50)
  - Cooling system faults (A_C10, A_C30)
  - Combined faults (A_C_B10, A_C_B30)
  - Fan-related issues
  - Rotor problems (Rotor-0)
- **Web-based Interface**: User-friendly dashboard with drag-and-drop image upload
- **Prediction Confidence**: Shows confidence score for each prediction
- **Actionable Insights**: Provides possible causes and recommended actions

## Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, Tailwind CSS
- **Deep Learning**: PyTorch, TorchVision
- **Image Processing**: Pillow (PIL)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/Smart-Thermal-Vision-System.git
cd Smart-Thermal-Vision-System
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install flask torch torchvision pillow
```

4. Download the pre-trained model:
- Download `best_thermal_motor_model.pth` from [releases](https://github.com/your-username/Smart-Thermal-Vision-System/releases)
- Place it in the project root directory

## Usage

1. Start the Flask application:
```bash
python app.py
```

2. Open your browser and navigate to:
```
http://localhost:5000
```

3. Upload a thermal image (JPG, PNG, or WebP)

4. Click "ANALYZE WITH AI" to get predictions and recommendations

## Project Structure

```
├── app.py                      # Flask backend application
├── index.html                  # Frontend interface
├── best_thermal_motor_model.pth # Pre-trained ResNet18 model
├── Smart_Thermal_Vision_System_for_Predictive_Machine_Maintenance.ipynb
├── thermal_dataset/            # Training dataset (not included)
├── screenshots/                # Demo screenshots
└── README.md                   # This file
```

## Screenshots

### Initial Interface
The clean, modern interface ready for thermal image analysis:
<img width="1920" height="1920" alt="image" src="https://github.com/user-attachments/assets/b2705df5-9109-4c49-86fc-9210910de8ce" />


### Analysis Results
Real-time AI analysis showing fault detection with confidence score:
<img width="1920" height="3500" alt="image" src="https://github.com/user-attachments/assets/2cd9222e-7047-4512-aea6-268b8b50b339" />


## Model Information

- **Architecture**: ResNet18
- **Input Size**: 224×224 pixels
- **Number of Classes**: 11 (different motor fault conditions)
- **Training Data**: Thermal images of electric motors with various conditions

## Performance

The model achieves high accuracy in detecting motor faults and abnormal thermal patterns, enabling early detection of potential equipment failures.

## Features

### Web Interface
- **Drag-and-drop upload**: Easily upload thermal images
- **Real-time preview**: See uploaded image before analysis
- **Detailed results**: View predictions with confidence scores
- **Actionable recommendations**: Get maintenance guidance
- **Print reports**: Generate analysis reports

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Authors

Created for Predictive Maintenance in Manufacturing, Maritime, and Aviation Industries

## Acknowledgments

- PyTorch team for the excellent deep learning framework
- Tailwind CSS for the modern UI framework
- Flask community for the lightweight web framework

## Support

For issues, questions, or suggestions, please open an issue on GitHub.

---

**Note**: The pre-trained model and thermal dataset are large files and are not included in the repository. They can be downloaded from the releases section.
