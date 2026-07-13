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


```json
{
  "Street_Name": "Broadway",
  "Borough": "Manhattan",
  "Year": 2024,
  "Month": 7,
  "Latitude": 40.7128,
  "Longitude": -74.006,
  "temperature_2m_F": 82.4,
  "precipitation_inch": 0.15,
  "snowfall_inch": 0.0,
  "snow_depth_ft": 0.0,
  "weather_code_wmo_code": 3,
  "wind_speed_10m_mph": 7.2,
  "Total_Traffic": 15843
}
```



```
POST /batch_predict
```


```json
{
  "records": [
    {
      "Street_Name": "Broadway",
      "Borough": "Manhattan",
      "Year": 2024,
      "Month": 7,
      "Latitude": 40.7128,
      "Longitude": -74.006,
      "temperature_2m_F": 82.4,
      "precipitation_inch": 0.15,
      "snowfall_inch": 0.0,
      "snow_depth_ft": 0.0,
      "weather_code_wmo_code": 3,
      "wind_speed_10m_mph": 7.2,
      "Total_Traffic": 15843
    },
    {
      "Street_Name": "Queens Boulevard",
      "Borough": "Queens",
      "Year": 2024,
      "Month": 1,
      "Latitude": 40.7282,
      "Longitude": -73.7949,
      "temperature_2m_F": 34.6,
      "precipitation_inch": 0.75,
      "snowfall_inch": 2.4,
      "snow_depth_ft": 0.4,
      "weather_code_wmo_code": 71,
      "wind_speed_10m_mph": 12.8,
      "Total_Traffic": 9231
    }
  ]
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