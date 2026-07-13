# Predictive Road Maintenance Decision Support System

## Project Overview

The Predictive Road Maintenance Decision Support System is a machine learning application that helps identify roads that are more likely to require maintenance before serious deterioration occurs.

The project combines historical NYC 311 road complaint data with weather and traffic information to train a machine learning model capable of predicting maintenance risk. The trained model is deployed through a FastAPI service and visualized using an interactive Streamlit dashboard.

The primary goal of the project is to help transportation agencies make proactive maintenance decisions instead of relying solely on reactive repairs.

---

# Problem Statement

Road maintenance is often performed only after citizens report problems such as potholes or damaged pavement. This reactive process can increase repair costs, delay maintenance, and create unnecessary safety risks.

This project applies machine learning to historical road complaint, weather, and traffic data to predict which roads may require maintenance in the future. These predictions can help transportation departments prioritize inspections and allocate resources more effectively.

---

# Project Objectives

The project was designed to accomplish the following objectives:

- Collect and integrate multiple public datasets
- Clean and preprocess historical road maintenance data
- Engineer meaningful predictive features
- Train and evaluate multiple machine learning models
- Deploy the selected model using FastAPI
- Build an interactive Streamlit dashboard
- Automate testing and deployment using GitHub Actions
- Document the complete machine learning workflow

---

# Key Features

- Machine learning prediction of road maintenance risk
- Interactive Streamlit dashboard
- FastAPI prediction service
- Batch prediction support
- Docker containerization
- Automated GitHub Actions CI/CD pipeline
- Logging and monitoring
- Interactive filtering by borough, year, and month
- Priority road identification
- Machine learning performance visualization

---

# Tools And Frameworks Used

The project combines machine learning, web development, data visualization, and DevOps technologies.

| Category | Technologies |
|----------|--------------|
| Programming Language | Python 3.13 |
| Data Processing | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| API Framework | FastAPI |
| Dashboard | Streamlit, Plotly Express |
| Testing | Pytest |
| Containerization | Docker, Docker Compose |
| Version Control | Git, GitHub |
| CI/CD | GitHub Actions |
| Documentation | Markdown |

---

# Project Architecture

The system is organized into several components that work together to transform raw data into maintenance risk predictions.

```
                    NYC 311 Data
                         │
                    Weather Data
                         │
                    Traffic Data
                         │
              Data Cleaning & Preprocessing
                         │
                 Feature Engineering
                         │
              Machine Learning Model
                         │
      ┌──────────────────┴──────────────────┐
      │                                     │
  FastAPI Prediction API             Streamlit Dashboard
      │                                     │
      └─────────────── End Users ───────────┘
```

---

# Project Workflow

The overall workflow follows the standard machine learning lifecycle.

1. Collect public datasets.
2. Clean and standardize the data.
3. Engineer predictive features.
4. Train multiple machine learning models.
5. Evaluate model performance.
6. Select the best-performing model.
7. Deploy the model through FastAPI.
8. Visualize results with Streamlit.
9. Automate testing and deployment using GitHub Actions.

---

# Repository Structure

```
Capstone-Project/
│
├── .github/
│   └── workflows/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
├── notebooks/
├── outputs/
│
├── src/
│   ├── api/
│   ├── dashboard/
│   └── utils/
│
├── tests/
│
├── README.md
├── API_DOCUMENTATION.md
├── DASHBOARD_GUIDE.md
├── DEPLOYMENT_GUIDE.md
├── MONITORING_GUIDE.md
├── TROUBLESHOOTING.md
├── requirements.txt
├── Dockerfile
└── docker-compose.yml
```

---

# Datasets

The machine learning model was built using multiple publicly available datasets that provide information about road conditions, weather, and traffic patterns throughout New York City.

| Dataset | Purpose |
|----------|---------|
| NYC 311 Road Service Requests | Historical road-related complaints used as the primary prediction target |
| Meteostat Weather Data | Daily weather conditions including temperature, precipitation, snowfall, and wind speed |
| NYC Traffic Volume Counts | Traffic volume measurements used to estimate roadway usage |

The datasets were cleaned, standardized, and merged into a single machine learning dataset through a preprocessing pipeline.

---

# Data Preparation

Several preprocessing steps were performed before training the model.

These steps included:

- Filtering NYC 311 records to include only road-related complaints
- Removing duplicate records
- Handling missing values
- Standardizing column names and data types
- Combining weather and traffic data using matching dates
- Creating additional predictive features
- Preparing the final dataset for machine learning

The final processed dataset contains:

| Item | Value |
|------|------:|
| Processed Records | 311,796 |
| Features | 15 |
| Target Variable | Maintenance Risk |

The processed dataset used by the dashboard is located at:

```
data/processed/model_data.csv
```

---

# Machine Learning Pipeline

The project follows a complete end-to-end machine learning workflow to transform raw public datasets into maintenance risk predictions.

## Workflow

1. Collect road complaint, weather, and traffic datasets.
2. Clean and standardize the data.
3. Engineer predictive features.
4. Split the dataset into training and testing sets.
5. Train the machine learning model.
6. Evaluate model performance.
7. Save the trained model.
8. Deploy the model through FastAPI.
9. Display predictions using the Streamlit dashboard.

---

# Feature Engineering

The following features were created or selected for model training.

| Feature Category | Examples |
|------------------|----------|
| Road Complaints | Complaint Count |
| Weather | Temperature, Precipitation, Snowfall, Wind Speed |
| Traffic | Total Traffic Volume |
| Time | Year, Month |
| Location | Borough |

These features help the model learn how environmental conditions and complaint history relate to future maintenance needs.

---

# Machine Learning Model

A Decision Tree Classifier was selected as the production model for this project.

Reasons for selecting the model include:

- Easy to interpret
- Fast prediction speed
- Works well with mixed feature types
- Suitable for tabular datasets
- Produces understandable decision rules

---

# Model Evaluation

The trained model was evaluated using a separate testing dataset.

Performance metrics included:

- Accuracy
- Precision
- Recall
- F1 Score

These metrics help measure how well the model identifies roads that are likely to require maintenance.

> **Note:** The dashboard displays the model's evaluation metrics to provide transparency into prediction performance.

---

# Prediction Output

The model predicts one of two maintenance risk levels:

| Prediction | Meaning |
|------------|---------|
| Low Risk | Road is unlikely to require immediate maintenance |
| High Risk | Road is more likely to require maintenance and should be prioritized for inspection |

---

# Dashboard

The project includes an interactive Streamlit dashboard that allows users to explore the processed road maintenance dataset and machine learning predictions.

## Dashboard Features

- Interactive filtering by Borough, Year, and Month
- Project overview metrics
- Preview of the processed dataset
- Road complaint counts by borough
- Road complaint trends over time
- Predicted maintenance risk distribution
- Priority roads for inspection
- Machine learning performance summary

The dashboard can be launched using:

```bash
streamlit run src/dashboard/app.py
```

By default, it is available at:

```
http://localhost:8501
```

---

# REST API

A FastAPI application provides prediction services for the trained machine learning model.

## Available Endpoints

| Endpoint | Description |
|----------|-------------|
| `GET /health` | Verifies that the API is running |
| `POST /predict` | Predicts maintenance risk for a single road record |
| `POST /batch_predict` | Predicts maintenance risk for multiple road records |

Start the API using:

```bash
uvicorn src.api.main:app --reload
```

Interactive API documentation is automatically generated and available at:

```
http://127.0.0.1:8000/docs
```

---

# Installation

## Clone the Repository

```bash
git clone <repository-url>
cd Capstone-Project
```

## Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the environment.

PowerShell

```bash
.venv\Scripts\Activate.ps1
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Project

### Start the API

```bash
uvicorn src.api.main:app --reload
```

### Start the Dashboard

```bash
streamlit run src/dashboard/app.py
```

### Run Unit Tests

```bash
python -m pytest
```

---

# Project Results

The completed system provides an end-to-end machine learning solution for predicting road maintenance risk using historical public datasets.

Project deliverables include:

- Data collection and preprocessing pipeline
- Feature engineering workflow
- Trained Decision Tree machine learning model
- FastAPI prediction service
- Interactive Streamlit dashboard
- Docker deployment
- GitHub Actions CI/CD pipeline
- Automated unit testing
- Monitoring and logging
- Complete technical documentation

---

# Available Documentation

The repository includes additional documentation for each major project component.

| Document | Description |
|----------|-------------|
| `README.md` | Project overview and setup instructions |
| `API_DOCUMENTATION.md` | API endpoints, requests, and responses |
| `DASHBOARD_GUIDE.md` | Dashboard features and usage |
| `DEPLOYMENT_GUIDE.md` | Local deployment instructions |
| `MONITORING_GUIDE.md` | Logging and monitoring information |
| `TROUBLESHOOTING.md` | Common issues and solutions |

---

# Testing

The project includes automated tests to verify the API.

Run all tests using:

```bash
python -m pytest
```

GitHub Actions automatically runs these tests whenever code is pushed to the repository.

---

# CI/CD

GitHub Actions is used to automate project validation.

The workflow automatically:

- Installs project dependencies
- Executes automated tests
- Verifies the FastAPI application
- Builds the Docker image
- Confirms the project is ready for deployment

---

# Future Improvements

Several enhancements could be added in future versions of the project.

Possible improvements include:

- Support additional NYC datasets
- Predict a maintenance risk score from 0–100
- Integrate real-time weather and traffic data
- Display interactive road maps
- Compare multiple machine learning models
- Deploy the application to a cloud platform
- Schedule automatic model retraining
- Add user authentication and role-based access

---

# Conclusion

The Predictive Road Maintenance Decision Support System demonstrates how machine learning can support proactive infrastructure maintenance.

By combining historical road complaints with weather and traffic information, the system identifies roads that may require maintenance before problems become more severe. The project includes a complete machine learning workflow, REST API, interactive dashboard, automated testing, CI/CD pipeline, and supporting documentation, providing a practical example of an end-to-end machine learning application.

---