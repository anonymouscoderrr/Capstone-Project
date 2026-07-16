# RoadWise AI API Documentation

## Overview

The RoadWise AI API provides the machine learning prediction service that powers the RoadWise AI Maintenance Scenario Simulator.

The API loads the trained Decision Tree model, validates incoming requests, generates maintenance predictions, and supports both single-road and batch prediction workflows.

Although the Streamlit dashboard is the primary user interface, the API serves as the prediction engine responsible for evaluating road profiles and returning maintenance predictions.

The API supports:

- Health monitoring
- Single-road prediction
- Batch prediction
- JSON-based communication
- Integration with the Streamlit Maintenance Scenario Simulator

The dashboard uses the batch prediction workflow to evaluate every available street profile within the selected borough, rank the results by inspection priority, and generate operational planning recommendations.

---

# Technology Stack

- Python 3.12+
- FastAPI
- Uvicorn
- Pydantic
- Scikit-learn
- Joblib
- Pandas
- NumPy

---

# Project Structure

```
src/
│
├── api/
│   ├── main.py
│   ├── model_loader.py
│   ├── schemas.py
│   └── __init__.py
│
├── dashboard/
│   ├── operations_planner.py
│   ├── app.py
│   └── __init__.py
│
├── forecasting/
├── analytics/
├── llm/
└── models/
```

---

# Starting the API

From the project root, run:

```bash
uvicorn src.api.main:app --reload
```

The API starts on:

```
http://127.0.0.1:8000
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

ReDoc:

```
http://127.0.0.1:8000/redoc
```

---

# Available Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| /health | GET | Verify the API is running |
| /predict | POST | Predict maintenance for one road profile |
| /batch_predict | POST | Predict maintenance for multiple road profiles |

---

# Health Endpoint

## Request

```http
GET /health
```

## Example Response

```json
{
    "status": "healthy"
}
```

This endpoint is used by automated monitoring systems to verify that the API is available.

---

# Prediction Endpoint

## Request

```http
POST /predict
```

The endpoint accepts one road profile and returns a maintenance prediction.

Example request:

```json
{
    "borough": "Bronx",
    "complaint_count": 52,
    "traffic_volume": 420.5,
    "temperature": 82,
    "precipitation": 0,
    "snowfall": 0,
    "month": 7
}
```

Example response:

```json
{
    "prediction": 1
}
```

Prediction values:

| Value | Meaning |
|------:|---------|
| 0 | Lower maintenance concern |
| 1 | Higher maintenance concern |

---

# Batch Prediction Endpoint

## Request

```http
POST /batch_predict
```

This endpoint accepts multiple road profiles within a single request.

Batch prediction is significantly faster than sending individual prediction requests.

The Streamlit dashboard uses this endpoint internally to evaluate every available street profile in the selected borough before ranking roads by inspection priority.

Example response:

```json
{
    "predictions": [1,0,1,1,0]
}
```

---

# Request Validation

All incoming requests are validated using Pydantic.

Validation checks include:

- Required fields
- Numeric data types
- Missing values
- Invalid JSON format

Invalid requests automatically return descriptive error messages.

---

# Model Loading

The API loads the trained Decision Tree model during startup.

Artifacts loaded:

```
models/
│
├── decision_tree_model.pkl
└── feature_columns.pkl
```

Loading the model once during startup minimizes prediction latency.

---

# Prediction Workflow

```
Client Request
       │
       ▼
Pydantic Validation
       │
       ▼
Feature Preparation
       │
       ▼
Decision Tree Model
       │
       ▼
Prediction
       │
       ▼
JSON Response
```

For batch predictions, this workflow is repeated efficiently across all submitted road profiles.

---

# Integration with the Dashboard

The Streamlit Maintenance Scenario Simulator uses the prediction model to evaluate every available street profile in the selected borough.

The workflow is:

```
Select Borough
        │
        ▼
Aggregate Historical Records
        │
        ▼
Build One Profile Per Street
        │
        ▼
Generate Batch Predictions
        │
        ▼
Calculate Inspection Priority
        │
        ▼
Rank Roads
        │
        ▼
Display Highest-Priority Results
```

The API provides the prediction capability, while the dashboard performs scenario simulation, ranking, explanation generation, and operational planning.

---

# Error Responses

Invalid requests return standard HTTP status codes.

Common responses include:

| Code | Meaning |
|------|---------|
| 200 | Successful prediction |
| 400 | Invalid request |
| 422 | Validation error |
| 500 | Internal server error |

---

# Performance

The API is designed for low-latency inference.

Typical operations include:

- Loading the trained Decision Tree model.
- Predicting a single road profile.
- Processing batch prediction requests.
- Returning structured JSON responses.

Batch prediction significantly improves performance when evaluating hundreds or thousands of road profiles.

---

# Security Notes

This project is an academic prototype.

Authentication and authorization are not currently implemented.

A production deployment should include:

- API authentication
- HTTPS
- Rate limiting
- Logging
- Request monitoring
- User authorization

---

# Future Improvements

Possible enhancements include:

- Real-time weather integration
- Live traffic feeds
- Automated retraining pipeline
- Database-backed prediction history
- GIS integration
- Cloud deployment
- Role-based authentication
- LLM-generated maintenance summaries

---

# Summary

The RoadWise AI API serves as the prediction engine for the RoadWise AI Maintenance Scenario Simulator.

It provides reliable machine learning inference through a lightweight FastAPI service, enabling both individual and batch predictions. By supporting the dashboard's full-borough evaluation workflow, the API allows historical road data to be transformed into ranked inspection priorities, operational workload estimates, and explainable maintenance recommendations.