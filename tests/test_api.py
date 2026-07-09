# Import the FastAPI test client
from fastapi.testclient import TestClient

# Import the API app
from src.api.main import app


# Create a test client so we can test the API without opening the browser
client = TestClient(app)


# Sample road data used in the prediction tests
sample_record = {
    "Street_Name": "Broadway",
    "Borough": "Manhattan",
    "Year": 2024,
    "Month": 6,
    "Latitude": 40.7128,
    "Longitude": -74.006,
    "temperature_2m_F": 75,
    "precipitation_inch": 0.2,
    "snowfall_inch": 0,
    "snow_depth_ft": 0,
    "weather_code_wmo_code": 3,
    "wind_speed_10m_mph": 8,
    "Total_Traffic": 12000
}


# Check that the health endpoint is working
def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


# Check that one prediction works
def test_predict_endpoint():
    response = client.post("/predict", json=sample_record)

    assert response.status_code == 200

    result = response.json()

    assert "prediction" in result
    assert "risk_label" in result
    assert "risk_score" in result


# Check that batch prediction works
def test_batch_predict_endpoint():
    response = client.post(
        "/batch_predict",
        json={
            "records": [
                sample_record,
                sample_record
            ]
        }
    )

    assert response.status_code == 200

    result = response.json()

    assert "predictions" in result
    assert len(result["predictions"]) == 2