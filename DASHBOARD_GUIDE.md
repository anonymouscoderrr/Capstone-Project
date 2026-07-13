# Predictive Road Maintenance Dashboard Guide

## Overview

The Predictive Road Maintenance Dashboard is an interactive Streamlit application developed to help analyze road maintenance patterns across New York City.

The dashboard combines:

- NYC 311 Road Complaint data
- Weather data
- Traffic volume data
- Machine Learning predictions

to identify roads that are more likely to require maintenance.


# Dashboard Sections

## 1. Dashboard Filters

Users can filter the dashboard by:

- Borough
- Year
- Month

Every chart and table automatically updates based on the selected filters.


## 2. Project Overview

Displays summary statistics including:

- Total Road Records
- Number of Features
- Number of Boroughs
- Years Covered


## 3. Final Processed Dataset

Shows a preview of the cleaned machine learning dataset used for training and prediction.


## 4. Road Complaint Records by Borough

Visualizes the number of road complaint records across NYC boroughs.

Purpose:

Identify which boroughs generate the highest number of road-related complaints.


## 5. Road Complaints Over Time

Displays monthly complaint trends over multiple years.

Purpose:

Identify seasonal patterns and years with unusually high complaint activity.


## 6. Maintenance Risk Distribution

Displays the machine learning prediction results.

Roads are classified as:

- Low Risk
- High Risk

Purpose:

Understand the overall distribution of predicted maintenance risk.


## 7. Priority Roads for Inspection

Ranks the highest-risk roads based on complaint history.

Purpose:

Help transportation departments prioritize inspections and maintenance.


## 8. Priority Road Details

Displays detailed information for the highest-risk roads, including:

- Street Name
- Borough
- Complaint Count
- Average Traffic
- High-Risk Records

Purpose:

Provide additional context for maintenance planning.


## 9. Machine Learning Model Performance

Displays evaluation metrics for the selected Decision Tree model.

Metrics include:

- Accuracy
- Precision
- Recall
- F1 Score

The dashboard also explains why Recall is especially important for identifying high-risk roads before they deteriorate further.


# Technologies Used

- Python
- Streamlit
- Pandas
- Plotly Express
- Scikit-learn


# Dataset

Final processed dataset:

data/processed/model_data.csv


Total records:

311,796

Features:

15


# Purpose

The dashboard provides city planners and transportation officials with an easy way to explore road conditions, monitor complaint trends, and prioritize road maintenance using machine learning predictions.