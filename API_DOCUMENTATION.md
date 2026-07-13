# API Documentation

## Overview

The Predictive Road Maintenance API provides machine learning predictions for road maintenance risk. It is built using FastAPI and serves as the backend for the dashboard and future integrations.

---

# Base URL

When running locally:

```
http://127.0.0.1:8000
```


# Endpoints

## GET /health

Checks whether the API is running.

### Request

```
GET /health
```

### Successful Response

```json
{
    "status": "healthy"
}
```

Status Code

```
200 OK
```


## POST /predict

Predicts whether a road record is considered Low Risk or High Risk.

### Request

```
POST /predict
```

Example Request

```json
{
    "Complaint Count": 18,
    "temperature_2m (°F)": 76.5,
    "precipitation (inch)": 0.10,
    "snowfall (inch)": 0.0,
    "wind_speed_10m (mp/h)": 8.4,
    "Total Traffic": 2150
}
```


### Successful Response

```json
{
    "maintenance_risk": "High Risk"
}
```

Status Code

```
200 OK
```


# Error Responses

If invalid input is provided, the API returns an error message.

Example

```json
{
    "detail": "Validation Error"
}
```

Status Code

```
422 Unprocessable Entity
```


# Machine Learning Model

Model Used

- Decision Tree Classifier

Input Features

- Complaint Count
- Temperature
- Precipitation
- Snowfall
- Wind Speed
- Traffic Volume

Output

- Low Risk
- High Risk



# Running the API

Start the API using:

```bash
uvicorn src.api.main:app --reload
```

After the server starts, open:

```
http://127.0.0.1:8000/docs

```

to access the automatically generated Swagger UI documentation.


# Testing

Run the API tests using:

```bash
python -m pytest tests/test_api.py
```

All API tests should pass before deploying the application.