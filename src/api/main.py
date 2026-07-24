import time

from fastapi import FastAPI, Request
from src.utils.logging_config import logger

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
    title="RoadWise AI Maintenance Risk Prediction API",
    description=(
        "REST API for predicting next-month road maintenance risk "
        "using the final trained Logistic Regression pipeline."
    ),
    version="2.0.0",
)

# Let us know when the API starts
logger.info("Road Maintenance API started successfully.")

# Track every API request and how long it takes
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()

    try:
        response = await call_next(request)

        response_time = round(time.time() - start_time, 4)

        logger.info(
            f"{request.method} {request.url.path} | "
            f"Status: {response.status_code} | "
            f"Time: {response_time} seconds"
        )

        return response

    except Exception as error:
        response_time = round(time.time() - start_time, 4)

        logger.error(
            f"{request.method} {request.url.path} failed after "
            f"{response_time} seconds. Error: {error}"
        )

        raise

@app.get("/health")
def health():
    # Record every health check request
    logger.info("Health endpoint accessed.")
    return {
    "status": "ok",
    "model": "Logistic Regression",
    "version": "2.0.0"
}

# Predict maintenance risk for one road record
@app.post("/predict", response_model=PredictionResponse)
def predict(input_data: PredictionInput):

    # Record when a prediction request is received
    logger.info("Prediction request received.")

    result = make_prediction(input_data)

    # Record the final prediction
    logger.info(
        f"Prediction completed. Label: {result['risk_label']}, Score: {result['risk_score']}"
    )

    return result


# Predict maintenance risk for multiple road records
@app.post("/batch_predict", response_model=BatchPredictionResponse)
def batch_predict(batch_data: BatchPredictionInput):

    # Record when a batch prediction starts
    logger.info(f"Batch prediction started for {len(batch_data.records)} records.")

    results = []

    for record in batch_data.records:
        prediction = make_prediction(record)
        results.append(prediction)

    # Record when the batch prediction finishes
    logger.info("Batch prediction completed.")

    return {
        "predictions": results
    }