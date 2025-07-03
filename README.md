# 🚚 Food Delivery Delay Prediction – DS Technical Assessment

This project addresses a real-world issue in urban logistics: unpredictable food delivery delays.  
The objective is to build a system that predicts delivery time based on operational features such as distance, traffic, weather, and courier attributes. The insights and model help the Operations team respond more intelligently to delivery delays.

---

## 📁 Repository Structure

```
food-delivery-delay-prediction/
├── data/                      # Raw dataset (not uploaded to GitHub)
├── model_pipeline/           # Scripts for preprocessing, training, prediction
├── reports/                  # EDA, model notes, explainability, error insights
├── sql/                      # SQL queries and insights
├── strategy/                 # Strategic business reflections
└── README.md                 # Project overview and setup
```

---

## ✅ Deliverables

| Area        | Description                                                                 |
|-------------|-----------------------------------------------------------------------------|
| SQL         | Queries to extract delay patterns, delivery person trends, and top areas   |
| Modeling    | RandomForestRegressor predicting `Delivery_Time_min`                       |
| Explainability | Feature importance analysis using `.feature_importances_`                |
| Error Analysis | Residual distribution and failure case insights                           |
| Strategy    | Production plan, transferability, GenAI use, and signature insight         |

---

## 📊 Features Used

- `Distance_km`
- `Weather`, `Traffic_Level`, `Time_of_Day`, `Vehicle_Type` (categorical)
- `Preparation_Time_min`
- `Courier_Experience_yrs`

---

## 🔁 How to Run

1. **Install dependencies**:

```bash
pip install -r requirements.txt
```

2. **Train the model**:

```bash
PYTHONPATH=. python model_pipeline/train_model.py
```

3. **Run explainability analysis**:

```bash
jupyter notebook eda_for_mds.ipynb
```

4. **(Optional)** Predict on new data with `predict.py`.

---

## ⚙️ Tools Used

- Python (pandas, scikit-learn, matplotlib, seaborn)
- SQL
- Jupyter Notebook
- Git / GitHub

---

## 💡 Author Note

This project was executed with the support of GenAI tools (ChatGPT) for formatting the markdown files and some of the troubleshooting. All code was human input made by Juan Pablo Perez-Cerda. See `strategy/strategic_reflections.md` for strategic reflections and deployment plan.

---

## 📬 Contact

Feel free to reach out via GitHub or LinkedIn with any questions.

👉 Local Swagger UI: http://127.0.0.1:8000/docs