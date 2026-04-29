from flask import Flask, flash, request, jsonify, redirect, url_for
import tensorflow as tf
import numpy as np
from flask_cors import CORS
from PIL import Image
import io

app = Flask(__name__)
CORS(app)

# Load model once
model = tf.keras.models.load_model("brain_tumor_model-2.h5")
CLASS_NAMES = ['glioma_tumor', 'meningioma_tumor', 'no_tumor', 'pituitary_tumor']


@app.route("/predict", methods=["POST"])
async def predict():
    # data = request.json["input"]

    file = request.files['file']
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        flash('No selected file')
        return jsonify({
            "status": False,
            "message": "No selected file"
        })
    
    
    image_bytes = file.read()
    image = Image.open(io.BytesIO(image_bytes))
    # Ensure image has 3 channels (RGB)
    if image.mode != 'RGB':
        image = image.convert('RGB')

    # Resize to model input
    image = image.resize((150, 150))

    # Convert to numpy array and normalize
    image = np.array(image) / 255.0

    # Add batch dimension
    image = np.expand_dims(image, axis=0)  # shape: (1, 150, 150, 3)

    print("start model prediction")
    prediction = model.predict(image)
    print("end model prediction")
    # print(prediction)
    class_idx = np.argmax(prediction)
    print("class_idx", class_idx)
    class_labels = ['glioma_tumor', 'meningioma_tumor', 'no_tumor', 'pituitary_tumor']
    result = class_labels[class_idx]
        

    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run(port=5001)