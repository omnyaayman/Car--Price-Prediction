# prediction.py
# Predict used car prices using the trained model

import joblib
import numpy as np

# Load model & encoders
model = joblib.load("model.pkl")
encoders = joblib.load("encoders.pkl")

def predict_price(year, km, engine, transmission, fuel, brand):
    # Encode categorical values
    transmission = encoders["transmission"].transform([transmission])[0]
    fuel = encoders["fuel"].transform([fuel])[0]
    brand = encoders["brand"].transform([brand])[0]

    # Prepare input
    features = np.array([[year, km, engine, transmission, fuel, brand]])

    # Predict
    predicted_price = model.predict(features)[0]

    return round(predicted_price, 2)


# Example
if _name_ == "_main_":
    price = predict_price(
        year=2017,
        km=90000,
        engine=1600,
        transmission="Automatic",
        fuel="Gasoline",
        brand="Kia"
    )

    print("Predicted Car Price:", price, "EGP")
