from fastapi import FastAPI, File, UploadFile
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

app = FastAPI()

# Load the trained model
model = load_model("artifacts/training/model.h5")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Kidney Disease Classification API"}

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    # Load and preprocess the image
    image = Image.open(file.file).resize((224, 224))
    image_array = np.array(image) / 255.0
    image_array = np.expand_dims(image_array, axis=0)

    # Make prediction
    prediction = model.predict(image_array)
    return {"prediction": prediction.tolist()}