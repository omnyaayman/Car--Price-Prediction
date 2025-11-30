🚗 Used Car Price Prediction 
A simple Machine Learning model that predicts the price of a used car based on its specifications (year, mileage, engine size, transmission, fuel type, and brand).

This project is perfect for beginners learning:

Data preprocessing

Label encoding

Random Forest Regression

Saving and loading ML models

Making real predictions

💡Features

Predict used car prices based on real attributes

Fully working ML pipeline

Encodes categorical features

Saves model & encoders for future predictions

Simple and clean project structure

**Project Structure
car-price-prediction
│
├── used_cars.csv        # sample dataset
├── train_model.py       # trains ML model + saves model.pkl
├── prediction.py        # load model + predict prices
├── model.pkl            # trained model (auto generated)
├── encoders.pkl         # label encoders (auto generated)
└── README.md            # documentation

🧠 How It Works

📝 1. Dataset (used_cars.csv)

Contains car details:

year

km mileage

engine size

transmission

fuel type

brand

price


🤖 2. Model Training (train_model.py)

Reads CSV

Encodes categorical columns

Trains RandomForestRegressor

Displays accuracy (R² score)

Saves:

model.pkl

encoders.pkl



🔮 3. Price Prediction (prediction.py)

Loads the saved model and predicts price based on input values.


---

▶ How to Run

1️⃣ Install dependencies:

pip install pandas numpy scikit-learn joblib

2️⃣ Train the model:

python train_model.py

3️⃣ Make predictions:

python prediction.py


---

🎯 Purpose of This Project

This simple ML project was created to:

Practice Machine Learning fundamentals

Build a clean GitHub portfolio

Improve Python usage in GitHub stats

Understand model training & prediction pipeline
