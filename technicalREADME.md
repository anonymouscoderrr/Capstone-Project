
# AI-Powered Road Maintenance Planning System

It is an end-to-end machine learning application that helps transportation agencies proactively identify roads that may require maintenance before roadway conditions become more severe. The system combines historical New York City 311 service requests, historical weather observations, and traffic information to estimate roadway maintenance risk and prioritize inspection activities.

Unlike traditional dashboards that only summarize historical information, It includes an AI-powered Scenario Simulator that evaluates every available street profile within a selected borough under user-defined planning conditions. The simulator ranks every roadway by inspection priority and presents the highest-priority roads together with operational planning recommendations to support maintenance decision-making.

The project demonstrates the complete machine learning lifecycle, including:

- Data collection
- Data preprocessing
- Feature engineering
- Model development
- Model evaluation
- Model deployment with FastAPI
- Interactive visualization with Streamlit
- AI-powered scenario simulation
- Operational planning
- Automated testing
- Docker containerization
- CI/CD automation
- Logging and monitoring

It is designed as a production-style machine learning system that illustrates how predictive analytics can support real-world infrastructure maintenance planning.

---

# Repository Overview

This repository contains the complete implementation of the It platform.

Major project components include:

- Data preprocessing pipeline
- Feature engineering pipeline
- Machine learning model development
- Model evaluation
- Decision Tree prediction model
- FastAPI REST API
- Streamlit dashboard
- AI Scenario Simulator
- Inspection Priority Ranking Engine
- Operational Planning Engine
- Automated testing
- Docker deployment
- GitHub Actions CI/CD workflow
- Technical documentation

Each component is modular, allowing the data pipeline, machine learning model, REST API, and dashboard to be independently maintained and extended.

# Project Objectives

The primary objective of It is to demonstrate how machine learning can support proactive roadway maintenance by transforming historical infrastructure data into actionable inspection recommendations.

Rather than relying solely on historical complaint reports, the system combines multiple data sources and predictive analytics to assist transportation agencies in prioritizing inspections and evaluating future maintenance scenarios.

The project was developed around the following technical objectives:

- Build a reproducible machine learning pipeline for roadway maintenance prediction.
- Integrate multiple public datasets into a unified modeling dataset.
- Engineer meaningful spatial, temporal, weather, and traffic-related features.
- Train and evaluate multiple supervised classification models.
- Select the most appropriate production model based on performance and interpretability.
- Deploy the trained model using a production-ready FastAPI REST API.
- Develop an interactive Streamlit dashboard for operational planning.
- Simulate future roadway conditions using configurable planning scenarios.
- Evaluate every available street profile within a selected borough.
- Rank roadway inspection priorities using machine learning predictions and operational factors.
- Generate operational planning recommendations for maintenance teams.
- Demonstrate software engineering best practices including testing, logging, Docker deployment, and CI/CD automation.

---

# Repository Structure

The repository is organized into modular components that separate data processing, model development, deployment, and visualization.

```text
Capstone-Project/

├── .github/
│   └── workflows/
│       └── ci.yml
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│   ├── decision_tree_model.pkl
│   └── feature_columns.pkl
│
├── notebooks/
│
├── outputs/
│
├── src/
│   ├── api/
│   │   ├── main.py
│   │   ├── model_loader.py
│   │   └── schemas.py
│   │
│   ├── dashboard/
│   │   └── operations_planner.py
│   │
│   └── utils/
│
├── tests/
│
├── README.md
├── API_DOCUMENTATION.md
├── DASHBOARD_GUIDE.md
├── DEPLOYMENT_GUIDE.md
├── MONITORING_GUIDE.md
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── pyproject.toml
```

---

# Technology Stack

| Category | Technology |
|-----------|------------|
| Programming Language | Python 3.13 |
| Data Processing | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| Visualization | Plotly Express |
| Dashboard | Streamlit |
| REST API | FastAPI |
| Model Serialization | Joblib |
| Data Validation | Pydantic |
| Testing | Pytest |
| Containerization | Docker |
| Version Control | Git & GitHub |
| Continuous Integration | GitHub Actions |

---

# System Architecture

The following diagram illustrates the overall architecture of It.

```text
                     Public Datasets
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
        ▼                   ▼                   ▼
 NYC 311 Complaints    Weather Data      Traffic Data
        │                   │                   │
        └───────────────────┼───────────────────┘
                            │
                            ▼
                 Data Cleaning & Integration
                            │
                            ▼
                  Feature Engineering Pipeline
                            │
                            ▼
               Decision Tree Classification Model
                            │
          ┌─────────────────┴─────────────────┐
          │                                   │
          ▼                                   ▼
     FastAPI REST API                Streamlit Dashboard
                                                 │
                                                 ▼
                                   AI Scenario Simulator
                                                 │
                                                 ▼
                                Inspection Priority Engine
                                                 │
                                                 ▼
                               Operational Planning Engine
                                                 │
                                                 ▼
                            Maintenance Recommendations
```

---

# Machine Learning Workflow

It follows a reproducible machine learning workflow from raw data collection through production deployment.

```text
Raw Data Collection
        │
        ▼
Data Cleaning
        │
        ▼
Feature Engineering
        │
        ▼
Dataset Integration
        │
        ▼
Train / Test Split
        │
        ▼
Model Training
        │
        ▼
Model Evaluation
        │
        ▼
Decision Tree Selection
        │
        ▼
Model Serialization
        │
        ▼
FastAPI Deployment
        │
        ▼
AI Scenario Simulation
        │
        ▼
Operational Planning Dashboard
```

---

# Data Collection

The performance of a machine learning model depends heavily on the quality, diversity, and relevance of the data used during training. Rather than relying on a single source, It integrates multiple public datasets that collectively describe roadway conditions, environmental factors, and traffic activity throughout New York City.

Combining these datasets allows the model to learn relationships between historical roadway complaints, weather conditions, and roadway usage that would not be captured by any individual dataset.

The complete data pipeline consists of three primary sources.

| Dataset | Purpose |
|---------|---------|
| NYC 311 Service Requests | Historical roadway complaints submitted by residents |
| Historical Weather Data | Environmental conditions affecting roadway deterioration |
| NYC Traffic Data | Estimated roadway usage and traffic volume |

Each dataset contributes unique information that improves the overall predictive capability of the machine learning model.

---

# Dataset Description

## NYC 311 Service Requests

The NYC Open Data 311 Service Requests dataset serves as the primary source of historical roadway maintenance information.

The original dataset contains millions of service requests submitted by residents covering many categories unrelated to roadway maintenance. During preprocessing, only complaint categories relevant to road conditions were retained.

Examples include:

- Street Condition
- Pothole Complaints
- Damaged Roadway
- Pavement Issues
- Street Maintenance Requests

Important attributes extracted from this dataset include:

- Street Name
- Borough
- Complaint Type
- Complaint Creation Date
- Latitude
- Longitude

These records provide historical evidence of locations where roadway conditions generated public complaints.

---

## Historical Weather Data

Roadway deterioration is strongly influenced by environmental conditions. Historical weather observations were incorporated to capture seasonal and environmental effects that may contribute to roadway damage.

Weather variables include:

- Temperature
- Precipitation
- Snowfall
- Snow Depth
- Wind Speed
- Weather Condition Code

Weather observations were aligned with complaint records using temporal information before integration into the modeling dataset.

---

## NYC Traffic Data

Traffic information provides an estimate of roadway usage.

Roads experiencing higher traffic volumes generally experience greater pavement stress and increased maintenance requirements.

Traffic data was aggregated and merged with roadway records to provide an additional predictor for the machine learning model.

Traffic features include:

- Total Traffic

---

# Data Preprocessing

Each dataset required preprocessing before integration into a unified modeling dataset.

Preprocessing tasks included:

- Removing duplicate observations
- Handling missing values
- Standardizing column names
- Converting date columns into datetime format
- Correcting inconsistent categorical values
- Removing invalid geographic coordinates
- Filtering roadway-related complaint categories
- Eliminating incomplete observations where appropriate

These preprocessing steps improved data quality while ensuring consistency across all datasets.

---

# Exploratory Data Analysis (EDA)

Exploratory Data Analysis was performed before model development to understand the characteristics of the collected data.

The objectives of EDA included:

- Examining complaint distributions
- Identifying missing values
- Detecting duplicate observations
- Understanding borough-level complaint activity
- Investigating seasonal complaint trends
- Exploring weather distributions
- Examining traffic distributions
- Identifying relationships between predictor variables

Several visualizations were created during this phase, including:

- Complaint counts by borough
- Monthly complaint trends
- Weather variable distributions
- Traffic distributions
- Missing value summaries
- Correlation analysis

Insights obtained during EDA guided later feature engineering decisions and model selection.

---

# Feature Engineering

Raw datasets were transformed into machine learning features suitable for supervised classification.

The objective of feature engineering was to convert historical roadway information into structured numerical and categorical variables that improve predictive performance.

The engineered feature set consists of four categories.

---

## Spatial Features

Spatial features preserve geographic context for each roadway.

Features include:

- Borough
- Street Name
- Latitude
- Longitude

These variables allow the model to learn geographic patterns associated with roadway maintenance.

---

## Temporal Features

The original complaint timestamp was decomposed into multiple features.

Generated variables include:

- Year
- Month

Separating the timestamp allows the model to learn seasonal roadway maintenance patterns while reducing dependence on raw datetime values.

---

## Weather Features

Historical weather observations were merged into each roadway record.

Weather features include:

- Temperature
- Precipitation
- Snowfall
- Snow Depth
- Wind Speed
- Weather Code

These variables capture environmental conditions that influence roadway deterioration throughout the year.

---

## Traffic Features

Traffic volume provides an estimate of roadway usage.

Feature included:

- Total Traffic

Roadways with greater traffic volumes generally experience increased pavement stress and may require more frequent maintenance.

---

# Dataset Integration

Following preprocessing and feature engineering, all datasets were merged into a single modeling dataset.

The integration process aligned:

- Geographic information
- Historical complaint records
- Historical weather observations
- Traffic estimates

The resulting processed dataset contains one observation per historical roadway record together with all engineered predictor variables required for model development.

The processed dataset serves as the single source of truth for:

- Machine learning model training
- Model evaluation
- FastAPI inference
- Streamlit dashboard visualization
- AI Scenario Simulator

Maintaining a shared processed dataset ensures that every application component operates on identical data.

---

# Machine Learning Pipeline

The complete machine learning pipeline is illustrated below.

```text
Raw Public Data
        │
        ▼
Data Cleaning
        │
        ▼
Exploratory Data Analysis
        │
        ▼
Feature Engineering
        │
        ▼
Dataset Integration
        │
        ▼
Train / Test Split
        │
        ▼
Model Training
        │
        ▼
Model Evaluation
        │
        ▼
Best Model Selection
        │
        ▼
Model Serialization
```

---

# Train-Test Split

After preprocessing, the integrated dataset was divided into independent training and testing datasets.

The training dataset was used to learn model parameters.

The testing dataset remained completely unseen throughout training and was reserved exclusively for evaluating generalization performance.

Separating the data in this manner reduces overfitting and provides a more reliable estimate of model performance on previously unseen roadway observations.

---

# Model Development

Following feature engineering and dataset integration, multiple supervised machine learning algorithms were evaluated to identify the most appropriate model for roadway maintenance prediction.

The objective was not only to maximize predictive performance but also to select a model that could be efficiently deployed within a production environment while remaining interpretable for decision-support applications.

Each candidate model was trained using the same feature set and identical train-test split to ensure fair comparison.

Candidate models included:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier

Using multiple baseline models provided a better understanding of how different algorithms performed on the roadway maintenance prediction task.

---

# Model Evaluation

Each candidate model was evaluated using several classification metrics.

| Metric | Purpose |
|----------|--------------------------------|
| Accuracy | Overall prediction correctness |
| Precision | Percentage of predicted high-risk roads that were actually high risk |
| Recall | Ability to identify roads requiring maintenance |
| F1 Score | Balance between precision and recall |

Although accuracy provides a useful overall measure, roadway maintenance prediction places greater importance on Recall and F1 Score because failing to identify a high-risk roadway may delay inspections and increase maintenance costs.

---

# Final Model Selection

Following model comparison, the Decision Tree Classifier was selected as the production model.

The Decision Tree demonstrated the best balance between predictive performance, inference speed, model interpretability, and deployment simplicity.

Reasons for selecting the Decision Tree include:

- Strong predictive performance
- Competitive F1 Score
- Good recall for identifying higher-risk roads
- Fast inference time
- Easy model interpretation
- Lightweight deployment
- Minimal computational requirements
- Seamless integration with FastAPI and Streamlit

Although more complex ensemble models were evaluated, the Decision Tree provided the most practical balance for an operational planning application.

---

# Model Serialization

After training, the production model was serialized using Joblib.

The following artifacts are stored within the repository.

| Artifact | Purpose |
|-----------|------------------------------|
| decision_tree_model.pkl | Trained Decision Tree classifier |
| feature_columns.pkl | Preserves feature ordering during inference |

Persisting these artifacts guarantees that production predictions use the exact preprocessing assumptions established during training.

---

# Production Deployment

After selecting the production model, It was organized into modular software components responsible for prediction, visualization, and operational planning.

The production system consists of:

- Machine Learning Prediction Pipeline
- FastAPI REST API
- Streamlit Dashboard
- AI Scenario Simulator
- Inspection Priority Ranking Engine
- Operational Planning Engine

Separating these responsibilities simplifies maintenance, testing, and future system expansion.

---

# Prediction Pipeline

During inference, every prediction request follows an identical processing pipeline.

```text
User Input
      │
      ▼
Pydantic Validation
      │
      ▼
Feature Formatting
      │
      ▼
Load Serialized Model
      │
      ▼
Decision Tree Prediction
      │
      ▼
Prediction Probability
      │
      ▼
Risk Classification
      │
      ▼
JSON Response
```

This standardized workflow guarantees consistent predictions regardless of whether requests originate from the REST API or the dashboard.

---

# Model Loading

When the FastAPI application starts, the trained model is loaded into memory.

Artifacts loaded during startup include:

- decision_tree_model.pkl
- feature_columns.pkl

Loading the model once during application startup significantly reduces prediction latency by eliminating repeated disk access for every request.

---

# FastAPI Architecture

FastAPI provides the production inference layer for It.

Rather than interacting directly with the machine learning model, client applications communicate through REST endpoints that perform request validation, feature preparation, prediction, and response formatting.

The API performs the following operations:

1. Validate incoming requests using Pydantic.
2. Convert user input into model-ready features.
3. Execute the Decision Tree classifier.
4. Calculate prediction probability.
5. Generate a human-readable maintenance risk label.
6. Return a structured JSON response.

---

# API Request Flow

```text
HTTP Request
      │
      ▼
FastAPI Endpoint
      │
      ▼
Pydantic Validation
      │
      ▼
Prediction Pipeline
      │
      ▼
Decision Tree Model
      │
      ▼
Probability Calculation
      │
      ▼
JSON Response
```

---

# REST API Endpoints

It exposes three primary REST endpoints.

| Endpoint | Method | Purpose |
|-----------|---------|--------------------------------------|
| /health | GET | Verify API availability |
| /predict | POST | Predict maintenance risk for a single roadway |
| /batch_predict | POST | Predict maintenance risk for multiple roadways |

These endpoints allow external applications to consume It predictions without requiring direct access to the underlying machine learning model.

---

# Prediction Response

Each prediction returns both the binary classification and the associated probability generated by the Decision Tree classifier.

Example response:

```json
{
    "prediction": 1,
    "risk_label": "High Risk",
    "risk_score": 82.46
}
```

Response fields include:

| Field | Description |
|---------|--------------------------------|
| prediction | Binary model prediction |
| risk_label | Human-readable maintenance category |
| risk_score | Predicted maintenance probability expressed as a percentage |

---

# Request Validation

FastAPI uses Pydantic models to validate every incoming prediction request before inference.

Validation ensures:

- Required fields are present.
- Numeric values are correctly formatted.
- Data types match the expected schema.
- Invalid requests are rejected before reaching the machine learning model.

This validation layer improves application robustness while preventing malformed requests from producing unreliable predictions.

---

# Logging

Centralized application logging records important events throughout execution.

Examples include:

- API startup
- Health endpoint requests
- Single prediction requests
- Batch prediction requests
- Prediction completion
- Unexpected application errors

Application logs improve debugging, simplify monitoring, and provide an execution history during deployment.

---

# Software Design

It follows a modular architecture in which each subsystem performs a well-defined responsibility.

```text
Prediction Layer
│
├── FastAPI
│
├── Decision Tree Model
│
├── Pydantic Validation
│
└── Logging

Visualization Layer
│
├── Streamlit Dashboard
│
├── Scenario Simulator
│
├── Inspection Priority Ranking
│
└── Operational Planning

Data Layer
│
├── Processed Dataset
│
├── Serialized Model
│
└── Feature Definitions
```

This modular organization improves maintainability, encourages code reuse, and simplifies future enhancements without requiring significant architectural changes.

---

# Streamlit Dashboard

It includes an interactive Streamlit dashboard that transforms machine learning predictions into an operational decision-support interface.

While the FastAPI REST API provides prediction services for external applications, the dashboard enables planners to explore roadway conditions, simulate future scenarios, compare maintenance outlooks, and prioritize inspection activities.

Unlike a traditional reporting dashboard, the application evaluates machine learning predictions together with operational planning metrics to assist maintenance scheduling.

---

# Dashboard Components

The dashboard consists of several integrated modules.

## Maintenance Outlook

Provides an executive summary of the selected planning scenario.

Displayed information includes:

- Total Roads Evaluated
- Priority Roads
- Operational Workload
- Highest Priority Road

These metrics provide planners with a high-level overview before examining individual roadway recommendations.

---

## Automated Maintenance Brief

The dashboard automatically generates a plain-language summary describing the simulated maintenance outlook.

The maintenance brief summarizes:

- Selected planning date
- Borough being analyzed
- Weather scenario
- Traffic scenario
- Number of roads evaluated
- Number of priority roads
- Highest priority roadway
- Recommended inspection strategy

This allows decision-makers to understand the overall scenario without manually reviewing every roadway.

---

## Scenario Comparison

It compares the selected planning scenario against a baseline "Normal Conditions" scenario.

Comparison metrics include:

- Total roads evaluated
- Priority roads
- Operational workload
- Average inspection priority
- Highest inspection priority
- Highest-priority roadway

This comparison helps planners understand how changing environmental conditions influence maintenance priorities.

---

# AI Scenario Simulator

The AI Scenario Simulator extends the machine learning model by allowing users to evaluate hypothetical future maintenance conditions.

Rather than predicting only historical observations, the simulator modifies environmental assumptions before executing the prediction pipeline.

Users may configure:

- Borough
- Planning Date
- Weather Scenario
- Traffic Level
- Number of Priority Roads Displayed

Supported weather scenarios include:

- Normal
- Heavy Rain
- Snow
- Extreme Heat

Traffic scenarios include:

- Low
- Normal
- High

Each scenario updates the model inputs before generating new roadway predictions.

---

# Full Borough Evaluation

Unlike earlier prototype versions that evaluated only a sample of roadways, the production implementation evaluates **every available street profile** within the selected borough.

The simulation workflow consists of the following steps.

1. Filter the processed dataset by borough.
2. Aggregate historical observations into one profile per street.
3. Apply the selected planning scenario.
4. Generate predictions for every roadway profile.
5. Calculate inspection priority scores.
6. Rank every roadway.
7. Display only the highest-priority roads selected by the user.

Evaluating the complete borough ensures that every available roadway is considered before inspection priorities are generated.

---

# Scenario Simulation Workflow

```text
Select Planning Scenario
          │
          ▼
Filter Selected Borough
          │
          ▼
Create Street Profiles
          │
          ▼
Evaluate Every Street
          │
          ▼
Decision Tree Prediction
          │
          ▼
Inspection Priority Ranking
          │
          ▼
Rank All Streets
          │
          ▼
Display Top Priority Roads
          │
          ▼
Operational Planning Recommendations
```

---

# Inspection Priority Ranking Engine

The Decision Tree model predicts maintenance risk for each roadway.

It then combines this prediction with additional operational factors to generate an Inspection Priority score.

The priority score incorporates:

- Predicted maintenance probability
- Historical complaint activity
- Traffic volume
- Selected weather scenario

These factors are combined into a composite planning score ranging from 0 to 100.

Higher scores indicate that a roadway should receive earlier inspection attention under the selected planning conditions.

After every roadway profile has been evaluated, roads are sorted by Inspection Priority and ranked from highest to lowest.

The dashboard displays only the highest-ranked roads requested by the user while preserving the complete evaluation internally.

---

# Operational Planning Engine

Prediction alone does not tell maintenance personnel what actions should be taken.

The Operational Planning Engine converts machine learning predictions into practical planning recommendations.

The engine generates:

- Total roads evaluated
- Priority roads requiring action
- Operational workload
- Highest-priority roadway
- Suggested inspection teams
- Estimated workdays
- Ranked inspection list
- Recommended operational actions

These outputs assist maintenance planners in allocating field resources more effectively.

---

# Explainability

To improve transparency, It explains why each roadway was prioritized.

Each priority roadway includes:

- Inspection Priority Score
- Maintenance Status
- Historical Complaint Count
- Traffic Level
- Why the roadway was prioritized
- Recommended inspection response

Providing these explanations allows users to understand the reasoning behind each recommendation rather than relying solely on model predictions.

---

# Dashboard Architecture

The Streamlit dashboard follows the workflow below.

```text
User Planning Inputs
          │
          ▼
Scenario Configuration
          │
          ▼
Create Street Profiles
          │
          ▼
Evaluate Every Street
          │
          ▼
Decision Tree Prediction
          │
          ▼
Inspection Priority Ranking
          │
          ▼
Operational Planning Engine
          │
          ▼
Interactive Dashboard
```

---

# Dashboard Outputs

The dashboard produces multiple operational outputs for each planning scenario.

Primary outputs include:

- Maintenance Outlook
- Automated Maintenance Brief
- Scenario Comparison
- Operational Planning Estimate
- Ranked Inspection Priorities
- Road-Level Explanations
- Recommended Next Steps

These outputs transform raw machine learning predictions into actionable planning information that can support inspection scheduling and maintenance prioritization.

# Testing

Comprehensive testing was performed throughout development to verify the correctness of the machine learning model, REST API, dashboard, and scenario simulation engine.

Testing focused on ensuring reliable predictions, validating user inputs, and confirming that all deployed components function correctly together.

---

# Machine Learning Testing

The Decision Tree classifier was evaluated using an independent testing dataset that remained unseen during training.

Model evaluation included:

- Accuracy
- Precision
- Recall
- F1 Score

These metrics were used to compare candidate models before selecting the final production model.

The final Decision Tree model demonstrated the best balance between predictive performance, interpretability, and deployment efficiency for this application.

---

# API Testing

The FastAPI application was tested using the automatically generated Swagger UI.

The following endpoints were validated.

| Endpoint | Purpose | Status |
|----------|---------|--------|
| GET /health | Verify API availability | ✅ Passed |
| POST /predict | Single roadway prediction | ✅ Passed |
| POST /batch_predict | Multiple roadway predictions | ✅ Passed |

Testing verified:

- Request validation
- Prediction accuracy
- JSON response formatting
- Error handling
- Batch prediction support

---

# Dashboard Testing

The Streamlit dashboard was tested using multiple planning scenarios.

Testing included:

- Borough selection
- Planning date selection
- Weather scenario changes
- Traffic level changes
- Full-borough roadway evaluation
- Inspection priority ranking
- Scenario comparison
- Operational planning estimates
- Explainability summaries
- Recommended next steps

Each scenario was verified to ensure that changes to planning conditions produced updated roadway rankings and operational recommendations.

---

# Deployment

Supports deployment using Docker.

The Docker environment packages:

- FastAPI application
- Streamlit dashboard
- Machine learning model
- Python dependencies

Build the application:

```bash
docker compose up --build
```

After deployment:

FastAPI

```
http://localhost:8000
```

Swagger Documentation

```
http://localhost:8000/docs
```

---

# Continuous Integration

GitHub Actions was configured to automate repository validation.

The CI workflow performs:

- Repository checkout
- Python environment setup
- Dependency installation
- Automated testing
- Build verification

Continuous Integration ensures that repository updates remain stable before deployment.

---

# Logging

It uses centralized logging throughout the application.

Logged events include:

- API startup
- Health endpoint requests
- Prediction requests
- Batch prediction requests
- Prediction completion
- Application errors

Logging improves debugging while providing visibility into application behavior during execution.

---

# Monitoring

Although the application is designed for local deployment, the project follows production monitoring practices.

Recommended monitoring metrics include:

- API uptime
- Prediction latency
- Request volume
- Error frequency
- Model performance
- Data drift
- Feature drift

These metrics provide visibility into system health and long-term model reliability.

---

# Limitations

The current implementation has several limitations.

## Historical Data

Predictions are based on historical public datasets.

Unexpected roadway events or future infrastructure changes cannot be predicted directly.

---

## Weather Assumptions

Scenario simulations use predefined weather conditions.

Future versions could integrate live weather forecast APIs for real-time planning.

---

## Traffic Estimates

Traffic information represents historical estimates rather than live roadway traffic.

Future work may integrate real-time transportation data.

---

## Geographic Scope

The current implementation focuses exclusively on New York City.

The overall architecture can be adapted for other municipalities by replacing the underlying datasets.

---

# Future Improvements

Several enhancements could further extend It.

## Machine Learning

- Gradient Boosting
- XGBoost
- LightGBM
- Hyperparameter optimization
- Automated model retraining

---

## Scenario Simulation

- Live weather forecasts
- Live traffic feeds
- Multi-day planning simulations
- Budget estimation
- Road deterioration forecasting

---

## Operational Planning

- Crew assignment optimization
- Route optimization
- Maintenance scheduling
- GIS-based inspection mapping
- Work order generation

---

## Deployment

- Cloud deployment
- User authentication
- Database integration
- Scheduled retraining pipeline
- Real-time monitoring dashboards

---

# Lessons Learned

Developing It demonstrated that building a successful machine learning application extends far beyond training a predictive model.

Several important lessons emerged throughout development.

- High-quality data preprocessing is critical for reliable predictions.
- Feature engineering significantly influences model performance.
- Model interpretability is important for operational decision support.
- Deploying machine learning models requires additional software engineering beyond model training.
- Interactive dashboards improve accessibility for non-technical users.
- Scenario simulation adds practical value by supporting planning rather than simply generating predictions.
- Modular software architecture simplifies testing, maintenance, and future enhancements.

The project reinforced the importance of combining machine learning, software engineering, and user-centered design into a unified decision-support system.

---

# References

The following public resources were used throughout development.

### Datasets

- NYC Open Data
- Historical Weather Data
- NYC Traffic Data

### Documentation

- Scikit-learn
- FastAPI
- Streamlit
- Plotly
- Pandas
- NumPy
- Docker
- GitHub Actions

---

# Conclusion

It demonstrates a complete end-to-end machine learning workflow, beginning with public data collection and concluding with a production-ready decision-support application.

The project integrates data engineering, feature engineering, supervised machine learning, REST API deployment, interactive visualization, and AI-powered scenario simulation into a unified software platform.

Unlike traditional dashboards that summarize historical information, It evaluates every available street profile within a selected borough, ranks roadway inspection priorities, and generates operational planning recommendations that assist transportation agencies in making proactive maintenance decisions.

The modular architecture, reproducible machine learning pipeline, and production-ready deployment provide a strong foundation for future research and real-world infrastructure maintenance applications.

---

