import pandas as pd
import joblib

# import the ml model

model = joblib.load("model/rfmodel.pkl")

#MLflow 
MODEL_VERSION = "1.0.0"