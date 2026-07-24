# RoadWise AI Deployment Guide

## Overview

This guide explains how to run the complete RoadWise AI application locally.

The deployed application consists of two primary components:

- FastAPI REST API
- Streamlit Maintenance Scenario Simulator

Both components use the same trained Decision Tree model and processed dataset.

---

# System Requirements

Install the following before running the project:

- Python 3.12 or newer
- Git
- Docker Desktop (optional)
- pip

---

# Clone the Repository

```bash
git clone <repository-url>
cd Capstone-Project
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install -e .
```

---

# Verify Project Files

Before starting the application, verify the following files exist.

```
models/
│
├── best_model.pkl
├── best_model.json
├── feature_columns.pkl
└── model_results.csv

data/
│
└── processed/
    └── model_data.csv
```

These files are required by both the API and the dashboard.

---

# Running the FastAPI Server

Start the REST API.

```bash
uvicorn src.api.main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

ReDoc:

```
http://127.0.0.1:8000/redoc
```

---

# Running the Dashboard

Open a second terminal.

Run:

```bash
python -m streamlit run src/dashboard/operations_planner.py
```

The dashboard will launch at:

```
http://localhost:8501
```

---

# Dashboard Workflow

After launching the dashboard:

1. Select a borough.
2. Choose a planning date.
3. Select a weather scenario.
4. Select a traffic level.
5. Choose how many priority roads to display.
6. Click **Generate Maintenance Forecast**.

The dashboard will:

- Build one profile for every available street in the selected borough.
- Evaluate every street using the Decision Tree model.
- Calculate inspection priorities.
- Rank all roads.
- Display the highest-priority results.
- Generate operational planning recommendations.

---

# Running Both Applications

Typical development uses two terminals.

### Terminal 1

```bash
uvicorn src.api.main:app --reload
```

### Terminal 2

```bash
python -m streamlit run src/dashboard/operations_planner.py
```

---

# Docker Deployment

Build the application.

```bash
docker compose up --build
```

Docker will create containers containing:

- FastAPI
- Streamlit
- Decision Tree model
- Processed dataset
- Python dependencies

---

# Verifying Deployment

Verify the following components.

## FastAPI

Visit:

```
http://127.0.0.1:8000/docs
```

Confirm:

- Health endpoint
- Predict endpoint
- Batch prediction endpoint

---

## Dashboard

Confirm the dashboard loads successfully.

Run a sample simulation by selecting:

- Borough
- Planning Date
- Weather Scenario
- Traffic Level
- Priority Roads to Display

Verify that the following sections appear:

- Maintenance Outlook
- Automated Maintenance Brief
- Scenario Comparison
- Operational Planning Estimate
- Recommended Road Inspection Priorities
- Why These Roads Were Prioritized
- Recommended Next Steps

---

# Common Deployment Issues

## Model Not Found

Verify:

```
models/
```

contains:

```
decision_tree_model.pkl
feature_columns.pkl
```

---

## Dataset Not Found

Verify:

```
data/processed/model_data.csv
```

exists.

---

## Port Already In Use

FastAPI:

```
8000
```

Streamlit:

```
8501
```

Close any existing application using these ports before restarting.

---

# Deployment Summary

After deployment, RoadWise AI provides:

- Production-ready FastAPI REST API
- Interactive Streamlit dashboard
- AI-powered Maintenance Scenario Simulator
- Full-borough roadway evaluation
- Inspection Priority Ranking
- Operational Planning recommendations

The application is now ready for local demonstrations, development, and future cloud deployment.