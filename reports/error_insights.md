# ❌ Error Insights – Model Weakness Analysis

---

## 1. Performance Summary

- Final model: `RandomForestRegressor`
- Evaluation metric: **MAE = 7.05 minutes**
- Most predictions fall within ±10 minutes of the true delivery time.

---

## 2. Largest Error Cases

### 🔍 Patterns in high-error predictions:

| Condition                     | Impact                    | Notes                            |
|------------------------------|----------------------------|----------------------------------|
| 🚦 High Traffic_Level         | Underestimates delivery    | Delays compound beyond expected  |
| ⛅ Certain Weather patterns    | Slight underestimation     | e.g., fog or storms not frequent |
| 🕒 Time_of_Day (late evening) | More variance in error     | Possibly tied to driver fatigue  |
| 🚗 Vehicle_Type = bicycle     | Outliers in urban sprawl   | More delays on long distances    |

---

## 3. Distribution of Residuals

Most residuals are centered around 0, but the **right tail (underestimates)** is heavier.

> Run this to confirm:

```python
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt

errors = model.predict(X_test) - y_test
plt.hist(errors, bins=30)
plt.title("Residual Distribution")
plt.xlabel("Prediction Error (min)")
plt.ylabel("Frequency")
plt.axvline(0, color='red', linestyle='--')
plt.show()