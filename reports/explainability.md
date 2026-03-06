# 📈 Explainability Report – Feature Importance

## 1. Method Used

- Model: `RandomForestRegressor`
- Feature importance method: `.feature_importances_` from scikit-learn

## 2. Ranked Feature Importances

| Feature                | Importance Score |
|------------------------|------------------|
| Distance_km            | 0.683048         |
| Preparation_Time_min   | 0.137682         |
| Vehicle_Type           | 0.068628         |
| Traffic_Level          | 0.030935         |
| Courier_Experience_yrs | 0.029522         |
| Weather                | 0.026105         |
| Time_of_Day            | 0.014577         |

> **Note:** An earlier version of this report listed `Order_ID` as the 3rd feature.
> That was incorrect — `Order_ID` is dropped in `preprocess.py` before training and
> therefore cannot appear in the model. `Vehicle_Type` is the correct 3rd feature.
> Regenerate this table by running `train_model.py` and calling
> `model.feature_importances_` against `X_train.columns` after training.


## 3. Observations

- `Distance_km` and `Preparation_Time_min` likely have the highest impact on delivery time.
- Traffic and weather conditions also contribute significantly.
- Courier experience has a moderate effect.

## 4. Visualization


