from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Load the trained model
model = joblib.load("model_pipeline/model.pkl")

# Initialize FastAPI app
app = FastAPI(title="Delivery Time Prediction API")

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
    try:
        # Convert to DataFrame
        input_df = pd.DataFrame([data.dict()])

        # Ensure correct column order
        column_order = [
            'Distance_km',
            'Weather',
            'Traffic_Level',
            'Time_of_Day',
            'Vehicle_Type',
            'Preparation_Time_min',
            'Courier_Experience_yrs'
        ]
        input_df = input_df[column_order]

        # Predict
        prediction = model.predict(input_df)[0]
        return {"predicted_delivery_time_min": round(prediction, 2)}
    
    except Exception as e:
        print("❌ Prediction failed:", str(e))
        return {"error": str(e)}