# Predictive Road Maintenance Decision Support System

## Project Overview

The Predictive Road Maintenance Decision Support System is a machine learning application that helps identify roads that are more likely to require maintenance before serious deterioration occurs.

The project combines historical NYC 311 road complaint data with weather and traffic information to train a machine learning model capable of predicting maintenance risk. The trained model is deployed through a FastAPI service and visualized using an interactive Streamlit dashboard.

The primary goal of the project is to help transportation agencies make proactive maintenance decisions instead of relying solely on reactive repairs.

## Complete Project Timeline

This project was developed in two major phases: machine learning development and production deployment.

### Phase 1 — Data Science & Machine Learning

1. Data Collection  
2. Data Cleaning & Standardization  
3. Exploratory Data Analysis (EDA)  
4. Feature Engineering  
5. Dataset Integration  
6. Model Training  
7. Model Evaluation  
8. Machine Learning Pipeline  

### Phase 2 — Production Deployment

9. FastAPI Development  
10. Streamlit Dashboard  
11. Docker Deployment  
12. Monitoring & Logging  
13. GitHub Actions CI/CD  
14. Documentation  

## Problem Statement

Road maintenance is often performed only after citizens report problems such as potholes or damaged pavement. This reactive process can increase repair costs, delay maintenance, and create unnecessary safety risks.

This project applies machine learning to historical road complaint, weather, and traffic data to predict which roads may require maintenance in the future. These predictions can help transportation departments prioritize inspections and allocate resources more effectively.

## Project Objectives

- Collect and integrate multiple public datasets  
- Clean and preprocess historical road maintenance data  
- Engineer meaningful predictive features  
- Train and evaluate multiple machine learning models  
- Deploy the selected model using FastAPI  
- Build an interactive Streamlit dashboard  
- Automate testing and deployment using GitHub Actions  
- Document the complete machine learning workflow  

## Key Features

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

The project combines machine learning, web development, data visualization, and DevOps Tools/Frameworks.
## Tools And Frameworks Used

| Category | Tools/Frameworks |
| Category | Tools/Frameworks |
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

## Project Architecture

The system is organized into several connected components that transform raw public data into road maintenance risk predictions.

```text
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
              Machine Learning Pipeline
                         │
      ┌──────────────────┴──────────────────┐
      │                                     │
 FastAPI Prediction API           Streamlit Dashboard
      │                                     │
      └─────────────── End Users ───────────┘
```

## Project Workflow

1. Collect public datasets  
2. Clean and standardize the data  
3. Perform exploratory data analysis  
4. Engineer predictive features  
5. Train multiple machine learning models  
6. Evaluate model performance  
7. Select the best-performing model  
8. Build a reusable machine learning pipeline  
9. Deploy the model through FastAPI  
10. Visualize results with Streamlit  
11. Containerize the application with Docker  
12. Automate testing and deployment using GitHub Actions  

## Repository Structure

```text
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

## Datasets

The machine learning model was built using multiple publicly available datasets that provide information about road conditions, weather, and traffic patterns across New York City.

| Dataset | Purpose |
|----------|---------|
| NYC 311 Road Service Requests | Historical road-related complaints used as the primary prediction target |
| Meteostat Weather Data | Daily weather conditions including temperature, precipitation, snowfall, and wind speed |
| NYC Traffic Volume Counts | Traffic volume measurements used to estimate roadway usage |

## Phase 1 — Data Collection & Preparation

This phase focused on building a clean, reliable dataset before any machine learning models were trained.

### Notebooks

| Notebook | Purpose |
|----------|--------|
| `01_data_loading.ipynb` | Load and inspect all public datasets |
| `02_preprocessing.ipynb` | Clean and standardize the datasets |
| `03_eda.ipynb` | Explore data distributions and identify trends |
| `04_feature_engineering.ipynb` | Create new predictive features |
| `05_model_training.ipynb` | Train and compare machine learning models |
| `06_ml_pipeline.ipynb` | Build a reusable prediction pipeline |

## Data Cleaning & Standardization

The original public datasets contained different formats, naming conventions, and levels of detail. Before the datasets could be combined, several preprocessing steps were performed:

- Removed duplicate records  
- Standardized column names  
- Converted data types  
- Verified latitude and longitude values  
- Standardized borough names  
- Reviewed missing values  
- Validated date formats  
- Removed unnecessary columns  
- Created project-specific datasets  

The result was four standardized datasets ready for feature engineering and integration.

## Exploratory Data Analysis

Exploratory Data Analysis (EDA) was performed before model training to better understand the structure of the data and identify potential issues.

The analysis included:

- Distribution of road complaints across boroughs  
- Complaint trends over time  
- Weather variable distributions  
- Traffic volume analysis  
- Summary statistics  
- Missing value inspection  
- Correlation analysis  
- Outlier detection  

The insights gained from EDA guided the feature engineering process and helped identify the most useful variables for model training.

## Feature Engineering

The following features were created or selected to help the model learn how historical road issues, environmental conditions, traffic load, and time patterns relate to maintenance risk.

| Feature | Purpose |
|--------|--------|
| Complaint Count | Historical maintenance activity |
| Temperature | Pavement expansion and contraction |
| Precipitation | Water-related road damage |
| Snowfall | Freeze-thaw effects |
| Snow Depth | Winter road conditions |
| Weather Code | General weather conditions |
| Wind Speed | Additional environmental factor |
| Traffic Volume | Road wear caused by vehicle usage |
| Borough | Geographic variation |
| Month | Seasonal patterns |
| Year | Long-term trends |

## Dataset Integration

After preprocessing and feature engineering, the individual datasets were merged into a single machine learning dataset.

The integration process included:

- Matching complaint records with historical weather observations  
- Merging traffic volume measurements  
- Matching records by borough, road name, and date  
- Resolving naming differences  
- Removing duplicate records  
- Validating merged records  
- Confirming feature completeness  

The final integrated dataset contained 311,796 processed records and 15 predictive features, ready for model training.

## Machine Learning Model Comparison

Several supervised machine learning models were trained and evaluated using the same training and testing datasets to ensure a fair comparison.

The evaluation process included:

- Train/test split  
- Common preprocessing pipeline  
- Accuracy comparison  
- Precision comparison  
- Recall comparison  
- F1-score comparison  
- Confusion matrix analysis  
- Feature importance analysis  

The best-performing model was selected based on overall performance and suitability for deployment.

## Machine Learning Pipeline

Instead of saving only the trained model, a complete machine learning pipeline was created.

The pipeline automatically performs:

- Input validation  
- Feature preparation  
- Feature ordering  
- Data preprocessing  
- Prediction generation  
- Prediction output formatting  

Using a complete pipeline ensures that the same preprocessing steps are applied during both training and prediction, improving consistency and reducing deployment errors.

## Processed Dataset Summary

The final processed dataset used by the dashboard and prediction system is stored at:

```text
data/processed/model_data.csv
```

| Item | Value |
|------|------:|
| Processed Records | 311,796 |
| Features | 15 |
| Target Variable | Maintenance Risk |

## Model Evaluation

The trained model was evaluated using a separate testing dataset.

Performance metrics included:

- Accuracy  
- Precision  
- Recall  
- F1 Score  

These metrics help measure how well the model identifies roads that are likely to require maintenance.

> **Note:** The dashboard displays model evaluation metrics to provide transparency into prediction performance.

## Prediction Output

The model predicts one of two maintenance risk levels:

| Prediction | Meaning |
|------------|---------|
| Low Risk | Road is unlikely to require immediate maintenance |
| High Risk | Road is more likely to require maintenance and should be prioritized for inspection |

## Phase 2 — Production Deployment

Phase 2 focused on transforming the trained machine learning pipeline into a usable software product that could be tested, demonstrated, and deployed consistently. This phase extended the project beyond notebook-based model development by introducing an API layer, an interactive dashboard, containerization, workflow automation, deployment verification, and technical documentation.

## FastAPI Development

FastAPI was used to deploy the trained machine learning pipeline as a REST API so predictions could be requested programmatically by other components of the system. FastAPI supports request validation, structured routing, and interactive documentation, which makes it a strong framework for production-style Python APIs.

The API provides three core endpoints for application health and prediction services:

| Endpoint | Purpose |
|----------|---------|
| `GET /health` | Confirms that the API is running successfully |
| `POST /predict` | Returns a maintenance risk prediction for a single road record |
| `POST /batch_predict` | Returns predictions for multiple road records in one request |

Key FastAPI responsibilities in this project include:

- Loading the saved machine learning pipeline  
- Validating incoming request data  
- Supporting single-record inference  
- Supporting batch inference  
- Returning structured JSON responses  
- Exposing interactive Swagger documentation  

The API can be started locally using:

```bash
uvicorn src.api.main:app --reload
```

After startup, the API is available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation is available at:

```text
http://127.0.0.1:8000/docs
```

## Streamlit Dashboard

A Streamlit dashboard was developed to provide an interactive interface for exploring the processed road maintenance dataset and reviewing prediction results. Streamlit is designed for fast creation of data apps and interactive dashboards, making it a practical frontend layer for machine learning demonstrations and visual analysis.

The dashboard serves as the presentation and analysis layer of the project. It allows users to move beyond raw model output and interact with the data visually through filters, summary metrics, and charts.

Dashboard capabilities include:

- Interactive filtering by borough, year, and month  
- High-level project summary metrics  
- Preview of the processed dataset  
- Complaint distribution analysis  
- Complaint trends over time  
- Predicted maintenance risk visualization  
- Priority road identification for inspection  
- Machine learning model performance summary  

The dashboard is launched locally using:

```bash
streamlit run src/dashboard/app.py
```

By default, it is available at:

```text
http://localhost:8501
```

## Docker Deployment

Docker was used to containerize the application so it could run in a consistent and reproducible environment. Docker-based workflows are commonly used to package Python applications and support repeatable build and deployment steps across machines and environments.

Containerization provides several advantages:

- Consistent runtime behavior across machines  
- Simplified deployment setup  
- Easier dependency management  
- Better portability for testing and demonstration  

The project includes both a `Dockerfile` and a `docker-compose.yml` file to support local container-based deployment.

To build and start the application with Docker:

```bash
docker compose up --build
```

After the container starts successfully, the API is available at:

```text
http://localhost:8000
```

## Monitoring & Logging

Basic monitoring and logging practices were included to improve deployment reliability and troubleshooting. Operational visibility and service verification are important parts of application deployment because they help confirm that the backend is healthy before it is used by other components.

These capabilities support the project by:

- Confirming the API is running through the health endpoint  
- Helping identify startup or pipeline loading issues  
- Supporting debugging during local deployment  
- Improving visibility into backend behavior during testing and demonstration  

The `GET /health` endpoint acts as a lightweight service check and provides a simple way to verify that the backend is operational before sending prediction requests.

## GitHub Actions CI/CD

GitHub Actions was used to automate project validation and deployment preparation. GitHub defines workflows as automated processes written in YAML and triggered by repository events such as pushes, pull requests, or manual dispatches.

### CI Workflow

The Continuous Integration workflow automatically validates the backend whenever code changes are pushed or submitted for review. The workflow is triggered on pushes to `main`, `draft`, and `feature/api-development`, and on pull requests into `main`.

The CI workflow performs the following steps:

1. Checks out the repository code  
2. Sets up Python 3.13  
3. Installs project dependencies from `requirements.txt`  
4. Runs API unit tests using `python -m pytest tests/test_api.py`  
5. Verifies that the FastAPI app and saved pipeline load successfully  

This workflow helps catch issues early and ensures that code changes do not break the API or deployment setup.

### CD Workflow

A separate Continuous Deployment workflow was created to automate deployment preparation for the API. The workflow is triggered on pushes to `feature/api-development` and can also be started manually using `workflow_dispatch`.

The CD workflow performs the following steps:

1. Checks out the repository  
2. Builds the Docker image for the application  
3. Confirms that the deployment workflow completed successfully  

This workflow verifies that the application can be packaged successfully for deployment and demonstrates that the project is ready for a repeatable container-based release process.

## REST API

A FastAPI application provides prediction services for the trained machine learning pipeline.

### Available Endpoints

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

```text
http://127.0.0.1:8000/docs
```

## Dashboard

The project includes an interactive Streamlit dashboard that allows users to explore the processed road maintenance dataset and machine learning predictions.

### Dashboard Features

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

```text
http://localhost:8501
```

## Installation

### Clone the Repository

```bash
git clone https://github.com/anonymouscoderrr/Capstone-Project.git
cd Capstone-Project
```

### Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the environment.

### PowerShell

```bash
.venv\Scripts\Activate.ps1
```

### Command Prompt

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Running the Project

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

### Run with Docker

```bash
docker compose up --build
```

## Final Project Deliverables

### Phase 1 Deliverables

- Data collection pipeline  
- Data cleaning pipeline  
- Exploratory Data Analysis  
- Feature engineering  
- Integrated dataset  
- Machine learning model comparison  
- Selected production model  
- Reusable machine learning pipeline  

### Phase 2 Deliverables

- FastAPI prediction service  
- Streamlit dashboard  
- Docker deployment  
- GitHub Actions CI/CD  
- Automated testing  
- Monitoring  
- Documentation  

## Available Documentation

The repository includes additional documentation for each major project component.

| Document | Description |
|----------|-------------|
| `README.md` | Project overview and setup instructions |
| `API_DOCUMENTATION.md` | API endpoints, requests, and responses |
| `DASHBOARD_GUIDE.md` | Dashboard features and usage |
| `DEPLOYMENT_GUIDE.md` | Local deployment instructions |
| `MONITORING_GUIDE.md` | Logging and monitoring information |
| `TROUBLESHOOTING.md` | Common issues and solutions |

## Testing

The project includes automated tests to verify the API and deployment readiness.

Run all tests using:

```bash
python -m pytest
```

The CI workflow specifically runs:

```bash
python -m pytest tests/test_api.py
```

GitHub Actions automatically runs these checks whenever supported branches are updated or pull requests are opened.

## CI/CD

GitHub Actions is used to automate validation and deployment preparation.

The CI workflow automatically:

- Installs project dependencies  
- Executes automated tests  
- Verifies the FastAPI application  
- Confirms that the saved machine learning pipeline loads successfully  

The CD workflow automatically:

- Checks out the repository  
- Builds the Docker image  
- Confirms the project is ready for deployment  

## Deployment Verification

Deployment was verified using the following checklist:

- API starts successfully  
- Dashboard opens correctly  
- Swagger documentation loads  
- Unit tests pass  
- Docker image builds successfully  
- GitHub Actions workflows complete without errors  

## Future Improvements

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

## Conclusion

The Predictive Road Maintenance Decision Support System demonstrates how machine learning can support proactive infrastructure maintenance.

By combining historical road complaints with weather and traffic information, the system identifies roads that may require maintenance before problems become more severe. The project includes a complete machine learning workflow, REST API, interactive dashboard, automated testing, CI/CD pipeline, and supporting documentation, providing a practical example of an end-to-end machine learning application.

---

By combining historical road complaints with weather and traffic information, the system identifies roads that may require maintenance before problems become more severe. The project includes a complete machine learning workflow, reusable pipeline, REST API, interactive dashboard, Docker deployment, automated testing, CI/CD automation, monitoring support, and technical documentation.