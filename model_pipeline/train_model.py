# train_model.py
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from model_pipeline.preprocess import load_data, preprocess, split_data
def train():
    print("🔄 Loading data...")
    df = load_data("data/train.csv")

    print("🧹 Preprocessing...")
    df = preprocess(df)

    print("📊 Splitting data...")
    X_train, X_test, y_train, y_test = split_data(df)

    print("🎯 Training model...")
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    mae = mean_absolute_error(y_test, preds)
    print(f"✅ Model trained. MAE: {round(mae, 2)}")

    print("💾 Saving model...")
    joblib.dump(model, "model_pipeline/model.pkl")
    print("✅ Model saved at model_pipeline/model.pkl")

if __name__ == "__main__":
    train()
