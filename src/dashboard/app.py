import joblib
import pandas as pd
import plotly.express as px
import streamlit as st


st.set_page_config(
    page_title="RoadWise AI Dashboard",
    layout="wide",
)


st.title("RoadWise AI Maintenance Planning Dashboard")

st.write(
    "Select a borough, year, and month to identify roads that should be "
    "prioritized for inspection based on the final Logistic Regression model."
)


# ---------------------------------------------------------
# Load data, model, features, and evaluation results
# ---------------------------------------------------------

@st.cache_data
def load_data():
    data = pd.read_csv("data/processed/model_data.csv")

    if "Date" in data.columns:
        data["Date"] = pd.to_datetime(data["Date"])

    return data


@st.cache_resource
def load_model():
    return joblib.load("models/best_model.pkl")


@st.cache_resource
def load_feature_columns():
    return joblib.load("models/feature_columns.pkl")


@st.cache_data
def load_model_results():
    return pd.read_csv("models/model_results.csv")


data = load_data()
model = load_model()
feature_columns = load_feature_columns()
model_results = load_model_results()


# ---------------------------------------------------------
# Dashboard filters
# ---------------------------------------------------------

st.sidebar.header("Planning Filters")

borough_options = ["All"] + sorted(
    data["Borough"].dropna().unique().tolist()
)

selected_borough = st.sidebar.selectbox(
    "Select Borough",
    borough_options,
)

year_options = sorted(
    data["Year"].dropna().astype(int).unique().tolist()
)

selected_year = st.sidebar.selectbox(
    "Select Year",
    year_options,
    index=len(year_options) - 1,
)

available_months = sorted(
    data.loc[
        data["Year"] == selected_year,
        "Month"
    ]
    .dropna()
    .astype(int)
    .unique()
    .tolist()
)

selected_month = st.sidebar.selectbox(
    "Select Month",
    available_months,
    index=len(available_months) - 1,
)


# ---------------------------------------------------------
# Filter the selected planning period
# ---------------------------------------------------------

filtered_data = data[
    (data["Year"] == selected_year)
    & (data["Month"] == selected_month)
].copy()

if selected_borough != "All":
    filtered_data = filtered_data[
        filtered_data["Borough"] == selected_borough
    ].copy()


# ---------------------------------------------------------
# Generate model predictions
# ---------------------------------------------------------

if not filtered_data.empty:
    prediction_data = filtered_data[feature_columns]

    filtered_data["Predicted_Risk"] = model.predict(
        prediction_data
    )

    filtered_data["Risk_Probability"] = (
        model.predict_proba(prediction_data)[:, 1]
    )

    filtered_data["Risk_Score"] = (
        filtered_data["Risk_Probability"] * 100
    ).round(2)

    filtered_data["Risk_Label"] = filtered_data[
        "Predicted_Risk"
    ].map(
        {
            0: "Low Risk",
            1: "High Risk",
        }
    )


# ---------------------------------------------------------
# Planning period heading
# ---------------------------------------------------------

month_name = pd.Timestamp(
    year=selected_year,
    month=selected_month,
    day=1,
).strftime("%B")

st.subheader(
    f"Maintenance Planning for {month_name} {selected_year}"
)


# ---------------------------------------------------------
# Overview metrics
# ---------------------------------------------------------

if filtered_data.empty:
    st.warning(
        "No records are available for the selected filters."
    )
    st.stop()


high_risk_count = int(
    filtered_data["Predicted_Risk"].sum()
)

high_risk_percentage = (
    filtered_data["Predicted_Risk"].mean() * 100
)

average_risk_score = filtered_data[
    "Risk_Score"
].mean()

column1, column2, column3, column4 = st.columns(4)

column1.metric(
    "Road Records Evaluated",
    f"{len(filtered_data):,}",
)

column2.metric(
    "High-Risk Records",
    f"{high_risk_count:,}",
)

column3.metric(
    "High-Risk Percentage",
    f"{high_risk_percentage:.1f}%",
)

column4.metric(
    "Average Risk Score",
    f"{average_risk_score:.1f}%",
)


# ---------------------------------------------------------
# Priority roads for inspection
# ---------------------------------------------------------

st.header("Priority Roads for Inspection")

high_risk_roads = filtered_data[
    filtered_data["Predicted_Risk"] == 1
].copy()

if high_risk_roads.empty:
    st.info(
        "The model did not identify any high-risk roads "
        "for the selected planning period."
    )

else:
    priority_roads = (
        high_risk_roads
        .groupby(
            ["Street Name", "Borough"],
            as_index=False,
        )
        .agg(
            Risk_Score=("Risk_Score", "max"),
            Average_Risk=("Risk_Score", "mean"),
            Current_Complaints=(
                "Complaint_Count",
                "sum",
            ),
            Previous_Month_Complaints=(
                "Previous_Month_Complaints",
                "sum",
            ),
            Complaints_Last_3_Months=(
                "Complaints_Last_3_Months",
                "sum",
            ),
            Average_Daily_Traffic=(
                "Avg_Daily_Traffic",
                "mean",
            ),
            Latitude=("Latitude", "mean"),
            Longitude=("Longitude", "mean"),
        )
        .sort_values(
            by=[
                "Risk_Score",
                "Complaints_Last_3_Months",
            ],
            ascending=False,
        )
        .head(20)
    )

    priority_roads["Inspection_Priority"] = range(
        1,
        len(priority_roads) + 1,
    )

    priority_roads = priority_roads[
        [
            "Inspection_Priority",
            "Street Name",
            "Borough",
            "Risk_Score",
            "Average_Risk",
            "Current_Complaints",
            "Previous_Month_Complaints",
            "Complaints_Last_3_Months",
            "Average_Daily_Traffic",
            "Latitude",
            "Longitude",
        ]
    ]

    priority_roads.columns = [
        "Inspection Priority",
        "Street Name",
        "Borough",
        "Maximum Risk Score",
        "Average Risk Score",
        "Current Complaints",
        "Previous Month Complaints",
        "Complaints in Last 3 Months",
        "Average Daily Traffic",
        "Latitude",
        "Longitude",
    ]

    st.dataframe(
        priority_roads,
        width="stretch",
        hide_index=True,
    )

    priority_chart = px.bar(
        priority_roads.head(10).sort_values(
            "Maximum Risk Score"
        ),
        x="Maximum Risk Score",
        y="Street Name",
        orientation="h",
        title="Top 10 Roads Recommended for Inspection",
        text="Maximum Risk Score",
        hover_data=[
            "Borough",
            "Current Complaints",
            "Complaints in Last 3 Months",
            "Average Daily Traffic",
        ],
    )

    priority_chart.update_traces(
        texttemplate="%{text:.1f}%",
        textposition="outside",
    )

    priority_chart.update_layout(
        xaxis_title="Predicted Maintenance Risk (%)",
        yaxis_title="Road",
        xaxis_range=[0, 100],
    )

    st.plotly_chart(
        priority_chart,
        width="stretch",
    )


# ---------------------------------------------------------
# Map of inspection priorities
# ---------------------------------------------------------

st.header("High-Risk Road Map")

map_data = filtered_data[
    filtered_data["Predicted_Risk"] == 1
].dropna(
    subset=["Latitude", "Longitude"]
).copy()

if map_data.empty:
    st.info(
        "No high-risk locations are available to display."
    )

else:
    map_data = (
        map_data
        .sort_values(
            "Risk_Score",
            ascending=False,
        )
        .head(500)
    )

    map_chart = px.scatter_map(
        map_data,
        lat="Latitude",
        lon="Longitude",
        color="Risk_Score",
        size="Risk_Score",
        hover_name="Street Name",
        hover_data={
            "Borough": True,
            "Risk_Score": ":.2f",
            "Complaint_Count": True,
            "Complaints_Last_3_Months": True,
            "Latitude": False,
            "Longitude": False,
        },
        zoom=9,
        title="Predicted High-Risk Road Locations",
    )

    map_chart.update_layout(
        map_style="open-street-map",
    )

    st.plotly_chart(
        map_chart,
        width="stretch",
    )


# ---------------------------------------------------------
# Risk distribution
# ---------------------------------------------------------

st.header("Predicted Maintenance Risk Distribution")

risk_counts = (
    filtered_data["Risk_Label"]
    .value_counts()
    .rename_axis("Risk Level")
    .reset_index(name="Record Count")
)

risk_chart = px.bar(
    risk_counts,
    x="Risk Level",
    y="Record Count",
    text="Record Count",
    title="Model Predictions for the Selected Period",
)

risk_chart.update_traces(
    textposition="outside",
)

st.plotly_chart(
    risk_chart,
    width="stretch",
)


# ---------------------------------------------------------
# Complaint history
# ---------------------------------------------------------

st.header("Complaint History")

history_data = data.copy()

if selected_borough != "All":
    history_data = history_data[
        history_data["Borough"] == selected_borough
    ]

complaints_over_time = (
    history_data
    .groupby(
        ["Year", "Month"],
        as_index=False,
    )["Complaint_Count"]
    .sum()
)

complaints_over_time["Date"] = pd.to_datetime(
    complaints_over_time[
        ["Year", "Month"]
    ].assign(Day=1)
)

complaint_chart = px.line(
    complaints_over_time,
    x="Date",
    y="Complaint_Count",
    title="Road Complaints Over Time",
)

complaint_chart.update_layout(
    xaxis_title="Date",
    yaxis_title="Total Complaints",
)

st.plotly_chart(
    complaint_chart,
    width="stretch",
)


# ---------------------------------------------------------
# Model performance
# ---------------------------------------------------------

st.header("Machine Learning Model Performance")

best_result = (
    model_results
    .sort_values(
        "F1",
        ascending=False,
    )
    .iloc[0]
)

st.write(
    "Logistic Regression was selected because it achieved "
    "the highest F1 score and recall, providing the strongest "
    "balance for identifying roads that may require maintenance."
)

metric1, metric2, metric3, metric4, metric5 = st.columns(5)

metric1.metric(
    "Accuracy",
    f"{best_result['Accuracy'] * 100:.2f}%",
)

metric2.metric(
    "Precision",
    f"{best_result['Precision'] * 100:.2f}%",
)

metric3.metric(
    "Recall",
    f"{best_result['Recall'] * 100:.2f}%",
)

metric4.metric(
    "F1 Score",
    f"{best_result['F1'] * 100:.2f}%",
)

metric5.metric(
    "ROC AUC",
    f"{best_result['ROC AUC'] * 100:.2f}%",
)


performance_columns = [
    "Accuracy",
    "Precision",
    "Recall",
    "F1",
    "ROC AUC",
]

performance = model_results.melt(
    id_vars="Model",
    value_vars=performance_columns,
    var_name="Metric",
    value_name="Score",
)

performance["Score"] = performance["Score"] * 100

performance_chart = px.bar(
    performance,
    x="Metric",
    y="Score",
    color="Model",
    barmode="group",
    title="Machine Learning Model Comparison",
    text="Score",
)

performance_chart.update_traces(
    texttemplate="%{text:.1f}",
    textposition="outside",
)

performance_chart.update_layout(
    xaxis_title="Evaluation Metric",
    yaxis_title="Score (%)",
    yaxis_range=[0, 100],
)

st.plotly_chart(
    performance_chart,
    width="stretch",
)


st.info(
    "Recall is especially important because a missed high-risk "
    "road may delay inspection and increase future safety or repair costs."
)


# Processed records


with st.expander("View Processed Records"):
    display_columns = [
        "Street Name",
        "Borough",
        "Year",
        "Month",
        "Complaint_Count",
        "Previous_Month_Complaints",
        "Complaints_Last_3_Months",
        "Avg_Daily_Traffic",
        "Risk_Label",
        "Risk_Score",
    ]

    st.dataframe(
        filtered_data[display_columns]
        .sort_values(
            "Risk_Score",
            ascending=False,
        ),
        width="stretch",
        hide_index=True,
    )