# 🤖 Model Notes – Food Delivery Time Prediction

## 1. Objective

Predict the **delivery time in minutes** for food orders based on variables such as:
- weather
- traffic
- distance
- order type
- delivery person's info

---

## 2. Target Variable

- **`delivery_time_min`**: engineered from timestamps  
(`Time_Order_picked - Time_Orderd`) in minutes.

---

## 3. Data Processing

- Dropped rows with null critical values
- Encoded categorical variables:
  - Weatherconditions
  - Road_traffic_density
  - Type_of_order
- Converted time columns to datetime
- Created feature: `delivery_time_min`

---

## 4. Model Selection

### ✅ Tried:
| Model               | MAE (approx) | Notes                        |
|---------------------|--------------|------------------------------|
| Linear Regression   | ~14.0        | Underfit, poor with outliers |
| Random Forest       | ~8.2         | Best performer overall       |
| XGBoost             | ~8.0         | Slightly better, slower      |

**Final choice:** `RandomForestRegressor`  
- Easy to interpret
- Robust to outliers
- No heavy tuning required

---

## 5. Features Used

- `Delivery_person_Age`
- `Vehicle_condition`
- `multiple_deliveries`
- `Weatherconditions` (encoded)
- `Road_traffic_density` (encoded)
- `Type_of_order` (encoded)

---

## 6. Metric Chosen

- **Mean Absolute Error (MAE)**  
  Reason: delivery time should be **accurate**, but tolerates small off-by-x errors.

---

## 7. Tuning Notes

- RandomForest with:
  - `n_estimators=100`
  - `max_depth=None` (default)
  - `random_state=42`
- Minimal tuning due to small dataset size

---

## 8. Saving the Model

Saved using `joblib`:

```python
joblib.dump(model, "model_pipeline/model.pkl")
