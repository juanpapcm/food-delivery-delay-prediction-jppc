import pandas as pd
from sklearn.model_selection import train_test_split

REQUIRED_COLUMNS = [
    'Distance_km', 'Weather', 'Traffic_Level',
    'Time_of_Day', 'Vehicle_Type', 'Preparation_Time_min',
    'Courier_Experience_yrs', 'Delivery_Time_min'
]

def load_data(path):
    print("📂 Loading data from:", path)
    return pd.read_csv(path)

def preprocess(df):
    print("🔍 Preprocessing data...")

    missing_cols = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing required columns: {missing_cols}")

    df = df.dropna(subset=REQUIRED_COLUMNS)

    df['Weather'] = df['Weather'].astype('category').cat.codes
    df['Traffic_Level'] = df['Traffic_Level'].astype('category').cat.codes
    df['Time_of_Day'] = df['Time_of_Day'].astype('category').cat.codes
    df['Vehicle_Type'] = df['Vehicle_Type'].astype('category').cat.codes

    df = df.drop(columns=["Order_ID"])
    return df

def split_data(df, target_column='Delivery_Time_min'):
    features = df.drop(columns=[target_column])
    target = df[target_column]
    return train_test_split(features, target, test_size=0.2, random_state=42)