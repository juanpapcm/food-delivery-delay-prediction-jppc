from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd

# Load the trained model once at startup; fail early with a clear message
try:
    model = joblib.load("model_pipeline/model.pkl")
except FileNotFoundError:
    raise RuntimeError(
        "model_pipeline/model.pkl not found. "
        "Run `PYTHONPATH=. python model_pipeline/train_model.py` first."
    )

# Initialize FastAPI app
app = FastAPI(title="Delivery Time Prediction API")

# Feature order must match the order used during training
COLUMN_ORDER = [
    'Distance_km',
    'Weather',
    'Traffic_Level',
    'Time_of_Day',
    'Vehicle_Type',
    'Preparation_Time_min',
    'Courier_Experience_yrs',
]

# Define the expected input data schema
class DeliveryInput(BaseModel):
    Distance_km: float
    Weather: int
    Traffic_Level: int
    Time_of_Day: int
    Vehicle_Type: int
    Preparation_Time_min: float
    Courier_Experience_yrs: float

@app.post("/predict")
def predict_delivery_time(data: DeliveryInput):
    input_df = pd.DataFrame([data.model_dump()])[COLUMN_ORDER]
    try:
        prediction = model.predict(input_df)[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {e}")
    return {"predicted_delivery_time_min": round(float(prediction), 2)}
