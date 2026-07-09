from pydantic import BaseModel
from typing import List, Optional

# Information for predicting one road
class PredictionInput(BaseModel):
    Street_Name: str
    Borough: str
    Year: int
    Month: int
    Latitude: Optional[float] = None
    Longitude: Optional[float] = None
    temperature_2m_F: float
    precipitation_inch: float
    snowfall_inch: float
    snow_depth_ft: float
    weather_code_wmo_code: int
    wind_speed_10m_mph: float
    Total_Traffic: float


# Information returned after making one prediction
class PredictionResponse(BaseModel):
    prediction: int
    risk_label: str
    risk_score: float


# Allow multiple roads to be predicted at once
class BatchPredictionInput(BaseModel):
    records: List[PredictionInput]


# Return the predictions for all roads
class BatchPredictionResponse(BaseModel):
    predictions: List[PredictionResponse]