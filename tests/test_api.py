# Import the FastAPI test client
from fastapi.testclient import TestClient

# Import the API app
from src.api.main import app


# Create a test client so we can test the API without opening the browser
client = TestClient(app)


# Sample road data used in the prediction tests
sample_record = {
    "Year": 2024,
    "Month": 6,
    "Latitude": 40.7128,
    "Longitude": -74.0060,
    "Avg_Temperature": 75.0,
    "Total_Precipitation": 0.20,
    "Total_Snowfall": 0.0,
    "Avg_Snow_Depth": 0.0,
    "Avg_Wind_Speed": 8.0,
    "Avg_Daily_Traffic": 12000,
    "Traffic_Observation_Days": 30,
    "Traffic_Data_Available": 1,
    "Previous_Month_Complaints": 2,
    "Complaints_Last_3_Months": 6,
    "Average_Complaints_Last_3_Months": 2.0,
    "Complaints_Last_6_Months": 11,
    "Borough": "MANHATTAN"
}


# Check that the health endpoint is working
def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200

    result = response.json()

    assert result["status"] == "ok"
    assert result["model"] == "Logistic Regression"
    assert result["version"] == "2.0.0"


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