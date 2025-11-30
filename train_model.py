# train_model.py
# Simple Used Car Price Prediction Model

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
import joblib

# Load dataset
df = pd.read_csv("used_cars.csv")

# Encode categorical columns
label_cols = ["transmission", "fuel", "brand"]
encoders = {}

for col in label_cols:
    encoders[col] = LabelEncoder()
    df[col] = encoders[col].fit_transform(df[col])

# Features & target
X = df[["year", "km", "engine", "transmission", "fuel", "brand"]]
y = df["price"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = RandomForestRegressor(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# Predict & evaluate
y_pred = model.predict(X_test)
score = r2_score(y_test, y_pred)

print("Model trained successfully!")
print("R2 Score:", round(score, 3))

# Save model
joblib.dump(model, "model.pkl")
print("Model saved as model.pkl")

# Save encoders
joblib.dump(encoders, "encoders.pkl")
print("Encoders saved as encoders.pkl")
