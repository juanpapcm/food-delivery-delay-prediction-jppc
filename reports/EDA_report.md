# 🧠 EDA Report – Food Delivery Time Prediction

## 1. Dataset Overview

- Total records: ~📦 [insert number after loading data]
- Columns:
  - Delivery distance
  - Weather condition
  - Traffic condition
  - Type of order
  - Time taken (target)

## 2. Data Quality

| Feature               | Issue                            |
|-----------------------|----------------------------------|
| Time_Orderd           | Many missing values              |
| Delivery_person_Age   | Some nulls or invalid entries    |
| Weatherconditions     | Inconsistent strings             |
| Road_traffic_density  | Has "NaN " and spacing issues    |

**Actions:**
- Parsed time fields as datetime
- Imputed or dropped rows with missing critical values
- Encoded categorical variables

---

## 3. Key Patterns

### ⏰ Time Taken Distribution
- Median: XX min
- Long tail over 100+ minutes (outliers)

### ☁️ Weather Conditions vs Time
| Condition     | Avg Delivery Time |
|---------------|-------------------|
| Sunny         | XX                |
| Stormy        | ↑ ↑               |
| Rainy         | ↑↑↑               |

### 🚦 Traffic Impact
- “Jam” and “High” significantly increase delivery time.

### 🛍️ Order Type Impact
- “Snack” and “Drinks” → faster
- “Meal” and “Buffet” →
