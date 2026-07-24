from pydantic import BaseModel, Field


class PredictionInput(BaseModel):
    Year: int = Field(..., ge=2012, le=2100)
    Month: int = Field(..., ge=1, le=12)

    Latitude: float
    Longitude: float

    Avg_Temperature: float
    Total_Precipitation: float = Field(..., ge=0)
    Total_Snowfall: float = Field(..., ge=0)
    Avg_Snow_Depth: float = Field(..., ge=0)
    Avg_Wind_Speed: float = Field(..., ge=0)

    Avg_Daily_Traffic: float = Field(..., ge=0)
    Traffic_Observation_Days: int = Field(..., ge=0)
    Traffic_Data_Available: int = Field(..., ge=0, le=1)

    Previous_Month_Complaints: float = Field(..., ge=0)
    Complaints_Last_3_Months: float = Field(..., ge=0)
    Average_Complaints_Last_3_Months: float = Field(..., ge=0)
    Complaints_Last_6_Months: float = Field(..., ge=0)

    Borough: str

   
from pydantic import BaseModel


class PredictionResponse(BaseModel):
    prediction: int
    risk_label: str
    risk_score: float


class BatchPredictionInput(BaseModel):
    records: list[PredictionInput]


class BatchPredictionResponse(BaseModel):
    predictions: list[PredictionResponse]