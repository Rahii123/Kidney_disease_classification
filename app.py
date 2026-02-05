from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import os

app = FastAPI()

# Load the trained model
model = load_model("artifacts/training/model.h5")

@app.get("/", response_class=HTMLResponse)
def read_root():
    with open("templates/index.html", "r") as f:
        return f.read()

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    # Load and preprocess the image
    image = Image.open(file.file).convert('RGB').resize((224, 224))
    image_array = np.array(image) / 255.0
    image_array = np.expand_dims(image_array, axis=0)

    # Make prediction
    prediction = model.predict(image_array)
    
    # Class mapping
    classes = ["Normal", "Tumor"]
    predicted_class_index = np.argmax(prediction, axis=1)[0]
    predicted_label = classes[predicted_class_index]
    confidence = float(np.max(prediction))

    return {
        "status": "success",
        "predicted_label": predicted_label,
        "confidence": round(confidence * 100, 2),
        "raw_prediction": prediction.tolist()
    }