from fastapi import FastAPI

# Import the request and response formats
from src.api.schemas import (
    PredictionInput,
    PredictionResponse,
    BatchPredictionInput,
    BatchPredictionResponse,
)

# Import the prediction helper
from src.api.model_loader import make_prediction


# Create the API app
app = FastAPI(
    title="Road Maintenance Risk Prediction API",
    description="API for predicting road maintenance risk using a trained machine learning pipeline.",
    version="1.0.0",
)


# Simple endpoint to check if the API is running
@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "message": "API is running"
    }


# Predict maintenance risk for one road record
@app.post("/predict", response_model=PredictionResponse)
def predict(input_data: PredictionInput):
    result = make_prediction(input_data)
    return result


# Predict maintenance risk for multiple road records
@app.post("/batch_predict", response_model=BatchPredictionResponse)
def batch_predict(batch_data: BatchPredictionInput):
    results = []

    for record in batch_data.records:
        prediction = make_prediction(record)
        results.append(prediction)

    return {
        "predictions": results
    }