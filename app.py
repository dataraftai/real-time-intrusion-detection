from fastapi import FastAPI
from schema.user_input_pydantic import UserInput
from schema.prediction_responce import predictionResponce
from fastapi.responses import JSONResponse
from model.predict import MODEL_VERSION,model
import pandas as pd

app = FastAPI()

@app.get("/")
def home():
    return{"project_name": "Real-Time Intrusion Detection System",
           "message" : ("A machine learning–based system to detect malicious network traffic "
            "in real time using supervised learning. Designed to handle highly "
            "imbalanced data and deployed as a production-ready FastAPI service.")
        }

@app.get("/health")
def health_check():
    return{
        "status":"ok",
        "version":MODEL_VERSION,
        "model_loaded" : model is not None
    }

@app.post("/predict",response_model=predictionResponce)
def predict_attack(data:UserInput):

    # Convert input to DataFrame
    input_df = pd.DataFrame([data.model_dump()])

    # Ensure categorical columns are strings (VERY IMPORTANT)
    for col in ["proto", "state", "flgs"]:
        input_df[col] = input_df[col].astype(str)

    # Prediction
    prediction = int(model.predict(input_df)[0])
    probabllity = float(model.predict_proba(input_df)[0][1])

    return {
        "predicted_category":prediction,
        "confidence" : round(probabllity,4)
    }