import joblib
import pandas as pd

# Load the saved model pipeline
pipeline = joblib.load("models/decision_tree_model.pkl")


# Load the feature columns from training
feature_columns = joblib.load("models/feature_columns.pkl")


# Turn one request into a DataFrame for the model
def make_prediction(input_data):
    input_dict = input_data.dict()

    row = {
        "Street Name": input_dict["Street_Name"],
        "Borough": input_dict["Borough"],
        "Year": input_dict["Year"],
        "Month": input_dict["Month"],
        "Latitude": input_dict["Latitude"],
        "Longitude": input_dict["Longitude"],
        "temperature_2m (°F)": input_dict["temperature_2m_F"],
        "precipitation (inch)": input_dict["precipitation_inch"],
        "snowfall (inch)": input_dict["snowfall_inch"],
        "snow_depth (ft)": input_dict["snow_depth_ft"],
        "weather_code (wmo code)": input_dict["weather_code_wmo_code"],
        "wind_speed_10m (mp/h)": input_dict["wind_speed_10m_mph"],
        "Total Traffic": input_dict["Total_Traffic"]
    }

    data = pd.DataFrame([row])

    data = data[feature_columns]

    prediction = pipeline.predict(data)[0]

    probability = pipeline.predict_proba(data)[0][1]

    risk_score = round(probability * 100, 2)

    risk_label = "High Risk" if prediction == 1 else "Low Risk"

    return {
        "prediction": int(prediction),
        "risk_label": risk_label,
        "risk_score": risk_score
    }