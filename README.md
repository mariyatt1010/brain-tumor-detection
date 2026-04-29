 Brain Tumor Detection using MRI Images

Description
This project uses deep learning to classify brain MRI images into:
- Glioma Tumor
- Meningioma Tumor
- Pituitary Tumor
- No Tumor

The model is built using MobileNetV2 and deployed using a Flask API for real-time predictions.
 Tech Stack
- Python
- TensorFlow / Keras
- Flask
- NumPy
- PIL
  
 How it Works
1. Upload an MRI image
2. Image is preprocessed (resize, normalize)
3. Model predicts tumor type
4. Result is returned via API

 Run the Project

```bash
python app.py

 API Endpoint
POST /predict
Upload an image file and get prediction.

Model Info
Model: MobileNetV2 (Transfer Learning)
Input Size: 150x150
Accuracy: ~68%

⚠️ Note
This project is for educational purposes only and not for medical use.

 Author
Mariya Thomas
