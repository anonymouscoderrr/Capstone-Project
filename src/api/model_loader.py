import joblib
import pandas as pd

# Load the final saved model pipeline
pipeline = joblib.load("models/best_model.pkl")

# Load the exact feature order used during training
feature_columns = joblib.load("models/feature_columns.pkl")


def make_prediction(input_data):
    input_dict = input_data.model_dump()

    row = {
        "Year": input_dict["Year"],
        "Month": input_dict["Month"],
        "Latitude": input_dict["Latitude"],
        "Longitude": input_dict["Longitude"],
        "Avg_Temperature": input_dict["Avg_Temperature"],
        "Total_Precipitation": input_dict["Total_Precipitation"],
        "Total_Snowfall": input_dict["Total_Snowfall"],
        "Avg_Snow_Depth": input_dict["Avg_Snow_Depth"],
        "Avg_Wind_Speed": input_dict["Avg_Wind_Speed"],
        "Avg_Daily_Traffic": input_dict["Avg_Daily_Traffic"],
        "Traffic_Observation_Days": input_dict[
            "Traffic_Observation_Days"
        ],
        "Traffic_Data_Available": input_dict[
            "Traffic_Data_Available"
        ],
        "Previous_Month_Complaints": input_dict[
            "Previous_Month_Complaints"
        ],
        "Complaints_Last_3_Months": input_dict[
            "Complaints_Last_3_Months"
        ],
        "Average_Complaints_Last_3_Months": input_dict[
            "Average_Complaints_Last_3_Months"
        ],
        "Complaints_Last_6_Months": input_dict[
            "Complaints_Last_6_Months"
        ],
        "Borough": input_dict["Borough"]
    }

    data = pd.DataFrame([row])

    # Enforce the same feature order used during training
    data = data[feature_columns]

    prediction = pipeline.predict(data)[0]
    probability = pipeline.predict_proba(data)[0][1]

    risk_score = round(float(probability) * 100, 2)

    risk_label = (
        "High Maintenance Risk"
        if prediction == 1
        else "Low Maintenance Risk"
    )

    return {
        "prediction": int(prediction),
        "risk_label": risk_label,
        "risk_score": risk_score
    }