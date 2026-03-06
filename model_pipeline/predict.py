# predict.py
import joblib
import pandas as pd

# Load the model once at module level to avoid reloading on every call
_model = joblib.load("model_pipeline/model.pkl")

FEATURE_ORDER = [
    'Distance_km',
    'Weather',
    'Traffic_Level',
    'Time_of_Day',
    'Vehicle_Type',
    'Preparation_Time_min',
    'Courier_Experience_yrs',
]

def predict(input_data: dict):
    df = pd.DataFrame([input_data])[FEATURE_ORDER]
    prediction = _model.predict(df)[0]
    return round(prediction, 2)

if __name__ == "__main__":
    # Categorical columns are integer-encoded by preprocess.py using .cat.codes.
    # Codes are assigned alphabetically. Example values from the training set:
    #   Weather:       Clear=0, Foggy=1, Rainy=2, Snowy=3, Windy=4
    #   Traffic_Level: High=0, Low=1, Medium=2
    #   Time_of_Day:   Afternoon=0, Evening=1, Morning=2, Night=3
    #   Vehicle_Type:  Bike=0, Car=1, Scooter=2
    sample = {
        "Distance_km": 7.93,
        "Weather": 4,              # Windy
        "Traffic_Level": 1,        # Low
        "Time_of_Day": 0,          # Afternoon
        "Vehicle_Type": 2,         # Scooter
        "Preparation_Time_min": 12.0,
        "Courier_Experience_yrs": 1.0,
    }
    print("Estimated delivery time (min):", predict(sample))
