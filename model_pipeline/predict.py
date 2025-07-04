# predict.py
import joblib
import pandas as pd

def predict(input_data: dict):
    model = joblib.load("model_pipeline/model.pkl")
    df = pd.DataFrame([input_data])
    prediction = model.predict(df)[0]
    return round(prediction, 2)

if __name__ == "__main__":
    sample = {
        "Delivery_person_Age": 30,
        "Weatherconditions": 2,
        "Road_traffic_density": 1,
        "Type_of_order": 1,
        "Vehicle_condition": 4,
        "multiple_deliveries": 0,
        # add all other features that the model was trained on...
    }
    print("Estimated delivery time (min):", predict(sample))