from flask import Flask, render_template, request, jsonify, send_from_directory
import torch
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image
import io
import os

# Initialize Flask app
app = Flask(__name__, static_folder='.', template_folder='.')

# Device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# Load model
model = models.resnet18(weights=None)
num_classes = 11
model.fc = torch.nn.Linear(model.fc.in_features, num_classes)
model.load_state_dict(torch.load('best_thermal_motor_model.pth', map_location=device))
model = model.to(device)
model.eval()
print("✅ Model loaded successfully!")

# Transform
inference_transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# Class names based on thermal_dataset folder structure
class_names = [
    'Noload',           # 0
    'A10',              # 1
    'A30',              # 2
    'A50',              # 3
    'A_B50',            # 4
    'A_C10',            # 5
    'A_C30',            # 6
    'A_C_B10',          # 7
    'A_C_B30',          # 8
    'Fan',              # 9
    'Rotor-0'           # 10
]

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Check if image file is present
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        # Read and process image
        image = Image.open(io.BytesIO(file.read())).convert('RGB')
        
        # Transform and predict
        input_tensor = inference_transform(image).unsqueeze(0).to(device)
        
        with torch.no_grad():
            output = model(input_tensor)
            probs = torch.nn.functional.softmax(output[0], dim=0)
            pred_idx = torch.argmax(probs).item()
            confidence = probs[pred_idx].item() * 100
        
        predicted_class = class_names[pred_idx]
        
        # Generate maintenance recommendation
        if predicted_class.lower() in ['noload', 'healthy']:
            recommendation = "✅ NORMAL OPERATION - No abnormal heat detected. Continue regular monitoring."
        else:
            recommendation = f"⚠️ FAULT DETECTED: {predicted_class}\nRecommendation: Schedule immediate inspection of motor windings / bearings / cooling system. Prevent unexpected downtime."
        
        return jsonify({
            'predicted_class': predicted_class,
            'confidence': round(confidence, 1),
            'recommendation': recommendation
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    print("🔥 Smart Thermal Vision System Starting...")
    app.run(host='127.0.0.1', port=5000, debug=False)