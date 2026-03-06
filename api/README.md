# API – Delivery Time Prediction

## How to Run

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Train the model first (from the project root):

```bash
PYTHONPATH=. python model_pipeline/train_model.py
```

3. Start the API server (from the project root):

```bash
uvicorn api.app:app --reload
```

The server will be available at `http://127.0.0.1:8000`.

---

## Endpoint

### `POST /predict`

Predicts the estimated delivery time in minutes.

**Request body (JSON):**

```json
{
  "Distance_km": 7.93,
  "Weather": 4,
  "Traffic_Level": 1,
  "Time_of_Day": 0,
  "Vehicle_Type": 2,
  "Preparation_Time_min": 12.0,
  "Courier_Experience_yrs": 1.0
}
```

Categorical fields are integer-encoded by the preprocessing pipeline using `.cat.codes`
(alphabetical ordering). Reference values from the training set:

| Field          | Value | Label     |
|----------------|-------|-----------|
| Weather        | 0     | Clear     |
| Weather        | 1     | Foggy     |
| Weather        | 2     | Rainy     |
| Weather        | 3     | Snowy     |
| Weather        | 4     | Windy     |
| Traffic_Level  | 0     | High      |
| Traffic_Level  | 1     | Low       |
| Traffic_Level  | 2     | Medium    |
| Time_of_Day    | 0     | Afternoon |
| Time_of_Day    | 1     | Evening   |
| Time_of_Day    | 2     | Morning   |
| Time_of_Day    | 3     | Night     |
| Vehicle_Type   | 0     | Bike      |
| Vehicle_Type   | 1     | Car       |
| Vehicle_Type   | 2     | Scooter   |

**Response (JSON):**

```json
{
  "predicted_delivery_time_min": 43.21
}
```

**Error response (HTTP 500):**

```json
{
  "detail": "Prediction failed: <reason>"
}
```

---

## Interactive Docs

FastAPI auto-generates interactive documentation at:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`
