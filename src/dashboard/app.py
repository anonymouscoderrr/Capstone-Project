import pandas as pd
import plotly.express as px
import streamlit as st


# Set up the page before adding dashboard content
st.set_page_config(
    page_title="Predictive Road Maintenance Dashboard",
    layout="wide",
)


# Main title and short description
st.title("Predictive Road Maintenance Dashboard")

st.write(
    "This interactive dashboard analyzes NYC road complaints, weather conditions, "
    "traffic patterns, and machine learning predictions to help identify roads "
    "that may require maintenance."
)


# Load the processed dataset
@st.cache_data
def load_data():
    return pd.read_csv("data/processed/model_data.csv")


data = load_data()


# Add filters so the user can explore the data
st.sidebar.header("Dashboard Filters")

borough_options = ["All"] + sorted(
    data["Borough"].dropna().unique().tolist()
)

selected_borough = st.sidebar.selectbox(
    "Select Borough",
    borough_options,
)

year_options = ["All"] + sorted(
    data["Year"].dropna().unique().tolist()
)

selected_year = st.sidebar.selectbox(
    "Select Year",
    year_options,
)

month_options = ["All"] + sorted(
    data["Month"].dropna().unique().tolist()
)

selected_month = st.sidebar.selectbox(
    "Select Month",
    month_options,
)


# Start with the full dataset
filtered_data = data.copy()


# Apply the selected borough filter
if selected_borough != "All":
    filtered_data = filtered_data[
        filtered_data["Borough"] == selected_borough
    ]


# Apply the selected year filter
if selected_year != "All":
    filtered_data = filtered_data[
        filtered_data["Year"] == selected_year
    ]


# Apply the selected month filter
if selected_month != "All":
    filtered_data = filtered_data[
        filtered_data["Month"] == selected_month
    ]


# Show basic project totals
st.subheader("Project Overview")

column1, column2, column3, column4 = st.columns(4)

column1.metric(
    "Records in View",
    f"{len(filtered_data):,}",
)

column2.metric(
    "Features",
    filtered_data.shape[1],
)

column3.metric(
    "Boroughs",
    filtered_data["Borough"].nunique(),
)

column4.metric(
    "Years Covered",
    filtered_data["Year"].nunique(),
)


# Show the final processed dataset
st.subheader("Final Processed Dataset")

st.caption(
    f"Displaying an interactive view of "
    f"**{len(filtered_data):,} processed records**."
)

st.dataframe(
    filtered_data,
    use_container_width=True,
)


# Complaint records by borough
st.subheader("Road Complaint Records by Borough")

borough_counts = (
    filtered_data["Borough"]
    .value_counts()
    .reset_index()
)

borough_counts.columns = [
    "Borough",
    "Complaint Records",
]

borough_chart = px.bar(
    borough_counts,
    x="Borough",
    y="Complaint Records",
    title="Road Complaint Records by Borough",
)

borough_chart.update_yaxes(
    title="Number of Complaint Records",
    automargin=True,
)

borough_chart.update_layout(
    xaxis_title="Borough",
    margin=dict(
        l=80,
        r=20,
        t=60,
        b=60,
    ),
)

st.plotly_chart(
    borough_chart,
    use_container_width=True,
)


# Show how road complaints change over time
st.subheader("Road Complaints Over Time")

complaints_over_time = (
    filtered_data
    .groupby(
        ["Year", "Month"],
        as_index=False,
    )["Complaint Count"]
    .sum()
)


# Create a date using the year and month
complaints_over_time["Date"] = pd.to_datetime(
    complaints_over_time[
        ["Year", "Month"]
    ].assign(Day=1)
)

complaint_trend_chart = px.line(
    complaints_over_time,
    x="Date",
    y="Complaint Count",
    markers=True,
    title="Road Complaint Trends Over Time",
)

complaint_trend_chart.update_yaxes(
    title="Total Complaint Count",
    rangemode="tozero",
    automargin=True,
)

complaint_trend_chart.update_layout(
    xaxis_title="Date",
    margin=dict(
        l=80,
        r=20,
        t=60,
        b=70,
    ),
)

st.plotly_chart(
    complaint_trend_chart,
    use_container_width=True,
)


# Show the distribution of predicted maintenance risk
st.header("Maintenance Risk Distribution")

risk_counts = (
    filtered_data["Maintenance Risk"]
    .value_counts()
    .sort_index()
    .reset_index()
)

risk_counts.columns = [
    "Risk Level",
    "Record Count",
]


# Change the numeric model results into readable labels
risk_counts["Risk Level"] = risk_counts["Risk Level"].replace(
    {
        0: "Low Risk",
        1: "High Risk",
    }
)

risk_chart = px.bar(
    risk_counts,
    x="Risk Level",
    y="Record Count",
    title="Predicted Maintenance Risk Across Processed Records",
    text="Record Count",
)

risk_chart.update_traces(
    textposition="outside",
)

risk_chart.update_layout(
    xaxis_title="Predicted Risk Level",
    yaxis_title="Number of Records",
    margin=dict(
        l=80,
        r=20,
        t=60,
        b=60,
    ),
)

st.plotly_chart(
    risk_chart,
    use_container_width=True,
)


# Show high-risk roads that may need inspection first
st.header("Priority Roads for Inspection")

high_risk_roads = filtered_data[
    filtered_data["Maintenance Risk"] == 1
].copy()

priority_roads = (
    high_risk_roads
    .groupby(
        ["Street Name", "Borough"],
        as_index=False,
    )
    .agg(
        Complaint_Count=("Complaint Count", "sum"),
        Average_Traffic=("Total Traffic", "mean"),
        Record_Count=("Maintenance Risk", "count"),
    )
    .sort_values(
        by=[
            "Complaint_Count",
            "Average_Traffic",
        ],
        ascending=[
            False,
            False,
        ],
    )
    .head(10)
)

priority_roads.columns = [
    "Street Name",
    "Borough",
    "Complaint Count",
    "Average Traffic",
    "High-Risk Records",
]


if priority_roads.empty:
    st.info(
        "No high-risk roads were found for the selected filters."
    )
else:
    priority_chart = px.bar(
        priority_roads.sort_values("Complaint Count"),
        x="Complaint Count",
        y="Street Name",
        orientation="h",
        title="Top High-Risk Roads by Complaint Count",
        hover_data=[
            "Borough",
            "Average Traffic",
            "High-Risk Records",
        ],
        text="Complaint Count",
    )

    priority_chart.update_traces(
        textposition="outside",
    )

    priority_chart.update_layout(
        xaxis_title="Total Complaint Count",
        yaxis_title="Street Name",
        margin=dict(
            l=120,
            r=40,
            t=60,
            b=60,
        ),
    )

    st.plotly_chart(
        priority_chart,
        use_container_width=True,
    )

    st.subheader("Priority Road Details")

    st.dataframe(
        priority_roads,
        use_container_width=True,
        hide_index=True,
    )


# Show the performance of the selected machine learning model
st.header("Machine Learning Model Performance")

st.write(
    "Among the evaluated models, the Decision Tree was selected because it "
    "provided the best balance between precision and recall while achieving "
    "the highest F1 score for identifying high-risk roads."
)

metric1, metric2, metric3, metric4 = st.columns(4)

metric1.metric(
    "Accuracy",
    "61.57%",
)

metric2.metric(
    "Precision",
    "39.73%",
)

metric3.metric(
    "Recall",
    "66.12%",
)

metric4.metric(
    "F1 Score",
    "49.63%",
)

performance = pd.DataFrame(
    {
        "Metric": [
            "Accuracy",
            "Precision",
            "Recall",
            "F1 Score",
        ],
        "Score": [
            61.57,
            39.73,
            66.12,
            49.63,
        ],
    }
)

performance_chart = px.bar(
    performance,
    x="Metric",
    y="Score",
    title="Decision Tree Performance Metrics",
    text="Score",
)

performance_chart.update_traces(
    texttemplate="%{text:.1f}%",
    textposition="outside",
)

performance_chart.update_layout(
    xaxis_title="Evaluation Metric",
    yaxis_title="Score (%)",
    yaxis_range=[0, 100],
    margin=dict(
        l=80,
        r=20,
        t=60,
        b=60,
    ),
)

st.plotly_chart(
    performance_chart,
    use_container_width=True,
)

st.write("")

st.info(
    "Recall is especially important for this project because a missed high-risk "
    "road may delay maintenance and create additional safety or repair costs."
)