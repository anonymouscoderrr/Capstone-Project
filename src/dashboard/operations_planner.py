import math

import joblib
import pandas as pd
import streamlit as st


# ---------------------------------------------------------
# Page setup
# ---------------------------------------------------------

st.set_page_config(
    page_title="RoadWise AI Scenario Simulator",
    layout="wide",
)


# ---------------------------------------------------------
# Load data and saved model
# ---------------------------------------------------------

@st.cache_data
def load_data():
    return pd.read_csv("data/processed/model_data.csv")


@st.cache_resource
def load_model():
    model_pipeline = joblib.load("models/best_model.pkl")
    model_features = joblib.load("models/feature_columns.pkl")
    return model_pipeline, model_features


data = load_data()
pipeline, feature_columns = load_model()


# ---------------------------------------------------------
# Page title
# ---------------------------------------------------------

st.title("AI Road Maintenance Prediction Simulator")

st.write(
    "Create a future road-maintenance scenario and receive an automated "
    "maintenance outlook, prioritized inspection list, plain-language "
    "explanations, and recommended next steps."
)


# ---------------------------------------------------------
# Sidebar controls
# ---------------------------------------------------------

st.sidebar.header("Future Planning Scenario")

planning_date = st.sidebar.date_input("Planning Date")

borough_options = sorted(
    data["Borough"].dropna().unique().tolist()
)

selected_borough = str(
    st.sidebar.selectbox(
        "Borough",
        borough_options,
    )
)

weather_scenario = st.sidebar.selectbox(
    "Weather Scenario",
    [
        "Normal",
        "Heavy Rain",
        "Snow",
        "Extreme Heat",
    ],
)

traffic_level = st.sidebar.selectbox(
    "Traffic Level",
    [
        "Low",
        "Normal",
        "High",
    ],
)

priority_roads_to_display = st.sidebar.slider(
    "Priority Roads to Display",
    min_value=10,
    max_value=100,
    value=50,
    step=10,
)

generate_forecast = st.sidebar.button(
    "Generate Maintenance Forecast"
)


# ---------------------------------------------------------
# Scenario assumptions
# ---------------------------------------------------------

weather_settings = {
    "Normal": {
        "Avg_Temperature": 65.0,
        "Total_Precipitation": 3.5,
        "Total_Snowfall": 0.0,
        "Avg_Snow_Depth": 0.0,
        "Avg_Wind_Speed": 7.0,
    },
    "Heavy Rain": {
        "Avg_Temperature": 60.0,
        "Total_Precipitation": 8.0,
        "Total_Snowfall": 0.0,
        "Avg_Snow_Depth": 0.0,
        "Avg_Wind_Speed": 15.0,
    },
    "Snow": {
        "Avg_Temperature": 28.0,
        "Total_Precipitation": 3.0,
        "Total_Snowfall": 12.0,
        "Avg_Snow_Depth": 3.0,
        "Avg_Wind_Speed": 12.0,
    },
    "Extreme Heat": {
        "Avg_Temperature": 90.0,
        "Total_Precipitation": 1.0,
        "Total_Snowfall": 0.0,
        "Avg_Snow_Depth": 0.0,
        "Avg_Wind_Speed": 6.0,
    },
}

traffic_multiplier = {
    "Low": 0.75,
    "Normal": 1.00,
    "High": 1.30,
}

scenario_bonus = {
    "Normal": 0,
    "Heavy Rain": 10,
    "Snow": 12,
    "Extreme Heat": 8,
}


# ---------------------------------------------------------
# Helper functions
# ---------------------------------------------------------

def normalize_score(series):
    minimum = series.min()
    maximum = series.max()

    if maximum == minimum:
        return pd.Series(
            [50.0] * len(series),
            index=series.index,
        )

    return (
        (series - minimum)
        / (maximum - minimum)
        * 100
    )



def create_reason(row, weather_name):
    reasons = []

    if (
        row["Complaint Count"]
        >= row["Complaint Count Median"]
    ):
        reasons.append(
            "this road has more complaint activity than many roads in the review"
        )

    if (
        row["Total Traffic"] > 0
        and row["Total Traffic"]
        >= row["Traffic Median"]
    ):
        reasons.append(
            "it carries relatively heavy traffic"
        )

    if row["Predicted Maintenance Risk"] >= 60:
        reasons.append(
            "the prediction indicates a stronger maintenance concern"
        )

    if weather_name == "Heavy Rain":
        reasons.append(
            "heavy rain may increase pavement damage"
        )

    elif weather_name == "Snow":
        reasons.append(
            "snow and freezing conditions may weaken the road"
        )

    elif weather_name == "Extreme Heat":
        reasons.append(
            "extreme heat may increase pavement stress"
        )

    if not reasons:
        reasons.append(
            "its combined complaint history and road conditions justify monitoring"
        )

    return "; ".join(reasons[:3])


def create_action(priority_score):
    if priority_score >= 85:
        return "Inspect as soon as possible"

    if priority_score >= 70:
        return "Inspect within 24–48 hours"

    if priority_score >= 55:
        return "Schedule an inspection this week"

    return "Continue routine monitoring"


def create_maintenance_status(priority_score):
    if priority_score >= 70:
        return "Immediate Attention"

    if priority_score >= 55:
        return "Inspection Recommended"

    return "Routine Monitoring"


def calculate_demand(action_count, total_roads):
    action_percentage = (
        action_count
        / total_roads
        * 100
    )

    if action_percentage >= 50:
        return "High"

    if action_percentage >= 25:
        return "Moderate"

    return "Low"


def traffic_label(value, traffic_median):
    if value <= 0:
        return "Not Available"

    if traffic_median <= 0:
        return "Available"

    if value >= traffic_median * 1.5:
        return "High"

    if value >= traffic_median * 0.75:
        return "Moderate"

    return "Low"


def estimate_operational_impact(results):
    immediate_count = int(
        (
            results["Maintenance Status"]
            == "Immediate Attention"
        ).sum()
    )

    recommended_count = int(
        (
            results["Maintenance Status"]
            == "Inspection Recommended"
        ).sum()
    )

    roads_requiring_action = (
        immediate_count
        + recommended_count
    )

    reviews_per_team_per_day = 4

    suggested_teams = (
        math.ceil(
            roads_requiring_action
            / reviews_per_team_per_day
        )
        if roads_requiring_action > 0
        else 0
    )

    estimated_days = (
        math.ceil(
            roads_requiring_action
            / max(
                suggested_teams
                * reviews_per_team_per_day,
                1,
            )
        )
        if roads_requiring_action > 0
        else 0
    )

    if roads_requiring_action >= 15:
        workload = "Heavy"

    elif roads_requiring_action >= 5:
        workload = "Moderate"

    else:
        workload = "Light"

    return {
        "immediate_count": immediate_count,
        "recommended_count": recommended_count,
        "roads_requiring_action": roads_requiring_action,
        "suggested_teams": suggested_teams,
        "estimated_days": estimated_days,
        "workload": workload,
    }


def run_scenario(
    base_profiles,
    selected_weather,
    selected_traffic,
    selected_date,
):
    scenario_profiles = base_profiles.copy()
    weather = weather_settings[selected_weather]

    scenario_profiles["Avg_Daily_Traffic"] = (
        scenario_profiles["Original Traffic"]
        * traffic_multiplier[selected_traffic]
    )

    scenario_profiles["Traffic_Data_Available"] = (
        scenario_profiles["Traffic_Data_Available"].fillna(0).astype(int)
    )

    scenario_profiles.loc[
        scenario_profiles["Traffic_Data_Available"] == 0,
        ["Avg_Daily_Traffic", "Traffic_Observation_Days"],
    ] = 0

    model_rows = pd.DataFrame({
        "Year": selected_date.year,
        "Month": selected_date.month,
        "Latitude": scenario_profiles["Latitude"],
        "Longitude": scenario_profiles["Longitude"],
        "Avg_Temperature": weather["Avg_Temperature"],
        "Total_Precipitation": weather["Total_Precipitation"],
        "Total_Snowfall": weather["Total_Snowfall"],
        "Avg_Snow_Depth": weather["Avg_Snow_Depth"],
        "Avg_Wind_Speed": weather["Avg_Wind_Speed"],
        "Avg_Daily_Traffic": scenario_profiles["Avg_Daily_Traffic"],
        "Traffic_Observation_Days": scenario_profiles["Traffic_Observation_Days"],
        "Traffic_Data_Available": scenario_profiles["Traffic_Data_Available"],
        "Previous_Month_Complaints": scenario_profiles["Previous_Month_Complaints"],
        "Complaints_Last_3_Months": scenario_profiles["Complaints_Last_3_Months"],
        "Average_Complaints_Last_3_Months": scenario_profiles["Average_Complaints_Last_3_Months"],
        "Complaints_Last_6_Months": scenario_profiles["Complaints_Last_6_Months"],
        "Borough": scenario_profiles["Borough"],
    })

    missing_features = set(feature_columns).difference(model_rows.columns)
    if missing_features:
        raise KeyError(
            f"Dashboard is missing model features: {sorted(missing_features)}"
        )

    model_rows = model_rows[feature_columns]
    predictions = pipeline.predict(model_rows)
    probabilities = pipeline.predict_proba(model_rows)[:, 1]

    scenario_profiles["Prediction"] = predictions
    scenario_profiles["Predicted Maintenance Risk"] = (
        probabilities * 100
    ).round(2)

    scenario_profiles["Total Traffic"] = scenario_profiles["Avg_Daily_Traffic"]
    scenario_profiles["Complaint Count"] = scenario_profiles[
        "Complaints_Last_6_Months"
    ]

    scenario_profiles["Complaint Score"] = normalize_score(
        scenario_profiles["Complaint Count"]
    )
    scenario_profiles["Traffic Score"] = normalize_score(
        scenario_profiles["Total Traffic"]
    )

    scenario_profiles["Inspection Priority"] = (
        scenario_profiles["Predicted Maintenance Risk"] * 0.50
        + scenario_profiles["Complaint Score"] * 0.30
        + scenario_profiles["Traffic Score"] * 0.20
        + scenario_bonus[selected_weather]
    ).clip(upper=100).round(1)

    scenario_profiles["Maintenance Status"] = (
        scenario_profiles["Inspection Priority"]
        .apply(create_maintenance_status)
    )

    scenario_profiles["Complaint Count Median"] = (
        scenario_profiles["Complaint Count"].median()
    )

    positive_traffic = scenario_profiles.loc[
        scenario_profiles["Total Traffic"] > 0,
        "Total Traffic",
    ]
    traffic_median = 0 if positive_traffic.empty else positive_traffic.median()
    scenario_profiles["Traffic Median"] = traffic_median
    scenario_profiles["Traffic Level"] = (
        scenario_profiles["Total Traffic"]
        .apply(lambda value: traffic_label(value, traffic_median))
    )

    scenario_profiles["Why It Was Flagged"] = scenario_profiles.apply(
        lambda row: create_reason(row, selected_weather),
        axis=1,
    )
    scenario_profiles["Recommended Response"] = (
        scenario_profiles["Inspection Priority"]
        .apply(create_action)
    )

    scenario_profiles = (
        scenario_profiles
        .sort_values("Inspection Priority", ascending=False)
        .reset_index(drop=True)
    )
    scenario_profiles["Priority Rank"] = scenario_profiles.index + 1
    return scenario_profiles


# ---------------------------------------------------------
# Generate simulation
# ---------------------------------------------------------

if generate_forecast:

    borough_data = data[
        data["Borough"] == selected_borough
    ].copy()

    if "Date" in borough_data.columns:
        borough_data["Date"] = pd.to_datetime(
            borough_data["Date"],
            errors="coerce",
        )
        borough_data = borough_data.sort_values(
            ["Street Name", "Date"]
        )
    else:
        borough_data = borough_data.sort_values(
            ["Street Name", "Year", "Month"]
        )

    all_road_profiles = (
        borough_data
        .groupby(
            ["Street Name", "Borough"],
            as_index=False,
        )
        .agg(
            Latitude=("Latitude", "mean"),
            Longitude=("Longitude", "mean"),
            Original_Traffic=("Avg_Daily_Traffic", "mean"),
            Traffic_Observation_Days=("Traffic_Observation_Days", "max"),
            Traffic_Data_Available=("Traffic_Data_Available", "max"),
            Previous_Month_Complaints=("Previous_Month_Complaints", "last"),
            Complaints_Last_3_Months=("Complaints_Last_3_Months", "last"),
            Average_Complaints_Last_3_Months=("Average_Complaints_Last_3_Months", "last"),
            Complaints_Last_6_Months=("Complaints_Last_6_Months", "last"),
        )
        .rename(columns={"Original_Traffic": "Original Traffic"})
    )

    numeric_profile_columns = [
        "Latitude",
        "Longitude",
        "Original Traffic",
        "Traffic_Observation_Days",
        "Traffic_Data_Available",
        "Previous_Month_Complaints",
        "Complaints_Last_3_Months",
        "Average_Complaints_Last_3_Months",
        "Complaints_Last_6_Months",
    ]
    all_road_profiles[numeric_profile_columns] = (
        all_road_profiles[numeric_profile_columns]
        .fillna(0)
    )

    all_road_profiles = (
        all_road_profiles[
            all_road_profiles["Street Name"].notna()
        ]
        .copy()
    )

    # Evaluate every available street profile in the selected borough.
    road_profiles = all_road_profiles.copy()

    if road_profiles.empty:
        st.warning(
            "No road records were available for the selected borough."
        )

    else:
        selected_results = run_scenario(
            road_profiles,
            weather_scenario,
            traffic_level,
            planning_date,
        )

        normal_results = run_scenario(
            road_profiles,
            "Normal",
            "Normal",
            planning_date,
        )

        selected_impact = estimate_operational_impact(
            selected_results
        )

        normal_impact = estimate_operational_impact(
            normal_results
        )

        selected_action_count = (
            selected_impact["roads_requiring_action"]
        )

        normal_action_count = (
            normal_impact["roads_requiring_action"]
        )

        selected_demand = calculate_demand(
            selected_action_count,
            len(selected_results),
        )

        normal_demand = calculate_demand(
            normal_action_count,
            len(normal_results),
        )

        highest_priority_road = (
            selected_results.iloc[0]["Street Name"]
        )

        highest_priority_score = (
            selected_results.iloc[0]["Inspection Priority"]
        )

        normal_highest_priority_road = (
            normal_results.iloc[0]["Street Name"]
        )

        normal_highest_priority_score = (
            normal_results.iloc[0]["Inspection Priority"]
        )

        difference = (
            selected_action_count
            - normal_action_count
        )

        normal_average_priority = round(
            normal_results["Inspection Priority"].mean(),
            1,
        )

        selected_average_priority = round(
            selected_results["Inspection Priority"].mean(),
            1,
        )

        priority_change = round(
            selected_average_priority
            - normal_average_priority,
            1,
        )

        display_count = min(
            priority_roads_to_display,
            len(selected_results),
        )

        displayed_results = (
            selected_results
            .head(display_count)
            .copy()
        )


       
        # Maintenance outlook
       

        st.header("Maintenance Outlook")

        metric1, metric2, metric3, metric4 = st.columns(4)

        metric1.metric(
            "Total Roads Evaluated",
            f"{len(selected_results):,}",
        )

        metric2.metric(
            "Roads Requiring Action",
            f"{selected_action_count:,}",
        )

        metric3.metric(
            "Expected Workload",
            selected_impact["workload"],
        )

        metric4.metric(
            "Top Road",
            highest_priority_road.title(),
        )

        st.caption(
            f"The model evaluated every available street profile in "
            f"{selected_borough.title()}. The dashboard displays only the "
            f"top {display_count} ranked roads so the inspection list remains readable."
        )


        
        # Automated maintenance brief
       

        st.subheader("Automated Maintenance Brief")

        if difference > 0:
            scenario_change_text = (
                f"{difference} additional roads move into the action list "
                f"compared with normal conditions."
            )

        elif difference < 0:
            scenario_change_text = (
                f"{abs(difference)} fewer roads require action compared "
                f"with normal conditions."
            )

        elif priority_change >= 5:
            scenario_change_text = (
                f"The number of roads requiring action remains similar, "
                f"but overall urgency increased by "
                f"{priority_change:.1f} points."
            )

        elif priority_change <= -5:
            scenario_change_text = (
                f"The number of roads requiring action remains similar, "
                f"but overall urgency decreased by "
                f"{abs(priority_change):.1f} points."
            )

        else:
            scenario_change_text = (
                "The selected conditions produce an outlook close to "
                "normal conditions."
            )

        summary_text = (
            f"For {planning_date.strftime('%B %d, %Y')}, the simulator "
            f"evaluated all {len(selected_results):,} available road profiles in "
            f"{(selected_borough.title())}. Under "
            f"{weather_scenario.lower()} weather and "
            f"{traffic_level.lower()} traffic conditions, "
            f"{selected_action_count:,} roads require inspection action. "
            f"{scenario_change_text} "
            f"{highest_priority_road.title()} received the highest priority "
            f"because of its complaint history, traffic conditions, and the "
            f"selected scenario. Staff should begin with the highest-ranked "
            f"roads and continue through the action list in priority order."
        )

        st.info(summary_text)


        # Scenario comparison
       

        st.header(
            "How the Selected Scenario Changes the Outlook"
        )

        comparison_data = pd.DataFrame({
            "Measure": [
                "Total Roads Evaluated",
                "Roads Requiring Action",
                "Expected Workload",
                "Average Inspection Priority",
                "Highest Inspection Priority",
                "Highest-Priority Road",
            ],
            "Normal Conditions": [
                f"{len(normal_results):,}",
                f"{normal_action_count:,}",
                normal_impact["workload"],
                f"{normal_average_priority}/100",
                f"{normal_highest_priority_score}/100",
                normal_highest_priority_road.title(),
            ],
            "Selected Conditions": [
                f"{len(selected_results):,}",
                f"{selected_action_count:,}",
                selected_impact["workload"],
                f"{selected_average_priority}/100",
                f"{highest_priority_score}/100",
                highest_priority_road.title(),
            ],
        })

        st.dataframe(
            comparison_data,
            width="stretch",
            hide_index=True,
        )

        if difference > 0:
            st.warning(
                f"The selected conditions add {difference} roads to the "
                f"action list. Average inspection urgency changed by "
                f"{priority_change:+.1f} points."
            )

        elif difference < 0:
            st.success(
                f"The selected conditions reduce the action list by "
                f"{abs(difference)} roads. Average inspection urgency "
                f"changed by {priority_change:+.1f} points."
            )

        elif priority_change >= 5:
            st.warning(
                f"The number of roads requiring action remains at "
                f"{selected_action_count}, but the average inspection "
                f"priority increased by {priority_change:.1f} points. "
                f"Existing concerns are therefore more urgent."
            )

        elif priority_change <= -5:
            st.success(
                f"The number of roads requiring action remains similar, "
                f"but average inspection priority decreased by "
                f"{abs(priority_change):.1f} points."
            )

        else:
            st.info(
                "The selected conditions produce an outlook close to "
                "normal conditions."
            )


        # Operational planning estimate
       

        st.header("Operational Planning Estimate")

        op1, op2, op3, op4 = st.columns(4)

        op1.metric(
            "Immediate Reviews",
            selected_impact["immediate_count"],
        )

        op2.metric(
            "Scheduled Reviews",
            selected_impact["recommended_count"],
        )

        op3.metric(
            "Suggested Field Teams",
            selected_impact["suggested_teams"],
        )

        op4.metric(
            "Estimated Workdays",
            selected_impact["estimated_days"],
        )

        st.caption(
            "Planning estimate: one field team is assumed to review about "
            "four priority roads per workday. This estimate supports staffing "
            "discussion and does not assign routes or guarantee completion time."
        )


        # Priority road report
 
        st.header(
            "Recommended Road Inspection Priorities"
        )

        st.write(
            f"Showing the top **{display_count}** roads from "
            f"**{len(selected_results):,}** total evaluated street profiles."
        )

        report_columns = [
            "Priority Rank",
            "Street Name",
            "Maintenance Status",
            "Inspection Priority",
            "Complaint Count",
            "Traffic Level",
            "Why It Was Flagged",
            "Recommended Response",
        ]

        st.dataframe(
            displayed_results[report_columns],
            width="stretch",
            hide_index=True,
        )


        
        # Road explanations
       

        st.header("Why These Roads Were Prioritized")

        top_roads = displayed_results.head(5)

        for _, road in top_roads.iterrows():

            with st.expander(
                f"#{int(road['Priority Rank'])} — "
                f"{road['Street Name'].title()} "
                f"({road['Inspection Priority']}/100)"
            ):

                st.write(
                    f"**Maintenance status:** "
                    f"{road['Maintenance Status']}"
                )

                st.write(
                    f"**Inspection priority:** "
                    f"{road['Inspection Priority']}/100"
                )

                st.write(
                    f"**Complaint history:** "
                    f"{int(road['Complaint Count']):,} complaints in the "
                    f"processed historical records"
                )

                st.write(
                    f"**Traffic level:** "
                    f"{road['Traffic Level']}"
                )

                st.write(
                    f"**Why it was prioritized:** "
                    f"{road['Why It Was Flagged']}."
                )

                st.write(
                    f"**Recommended response:** "
                    f"{road['Recommended Response']}."
                )


       
        # Recommended next steps
       

        st.header("Recommended Next Steps")

        action_results = selected_results[
            selected_results["Maintenance Status"]
            != "Routine Monitoring"
        ]

        if action_results.empty:
            st.success(
                "No roads currently require inspection action under the "
                "selected scenario. Continue routine monitoring and rerun "
                "the outlook if weather or traffic conditions change."
            )

        else:
            top_action_roads = (
                action_results
                .head(3)["Street Name"]
                .str.title()
                .tolist()
            )

            team_count = selected_impact["suggested_teams"]
            day_count = selected_impact["estimated_days"]

            team_word = "field team" if team_count == 1 else "field teams"
            day_word = "workday" if day_count == 1 else "workdays"

            recommendation_text = (
                f"Expected operational workload is "
                f"**{selected_impact['workload'].upper()}**. "
                f"Begin with {', '.join(top_action_roads)}. "
                f"{highest_priority_road.title()} received the highest "
                f"inspection priority of {highest_priority_score}/100 and "
                f"should be reviewed first. The planning estimate suggests "
                f"{team_count:,} {team_word} could complete the current "
                f"action list in about {day_count:,} {day_word}."
            )

            st.success(recommendation_text)

        st.caption(
            "Inspection Priority is a planning score designed to help schedule "
            "field reviews. Final maintenance decisions should be confirmed "
            "through on-site inspection and professional judgment."
        )

else:
    st.info(
        "Choose a future planning scenario in the sidebar and select "
        "'Generate Maintenance Forecast' to begin."
    )