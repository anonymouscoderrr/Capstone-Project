# Predictive Road Maintenance Using Machine Learning
## 2-Week Sprint Plan 

**Status:** Project planning complete | Ready for implementation  
**Scope:** Data engineering, machine learning, deployment, and MLOps  
**Last Updated:** June 26, 2026

---

## 1. Problem Definition

Roads are often repaired only after people report damage, which can increase repair costs, delay action, and create safety risks. This project will build a machine learning system that predicts which roads are more likely to need maintenance before problems become severe.

The model will use NYC 311 road service requests, Meteostat weather data, OpenStreetMap road information, and NYC traffic volume data to identify patterns related to road maintenance needs.
  
## 2. Sprint Overview

### Week 1: Data and Model Preparation (June 27 – July 3)
- Collect, validate, clean, and standardize all datasets.
- Engineer features and merge sources into one training dataset.
- Train and compare multiple models.
- Select the best-performing model.
- Build and test the machine learning pipeline.

### Week 2: API, Deployment, and MLOps (July 4 – July 10)
- Build FastAPI endpoints: `/health`, `/predict`, `/batch_predict`.
- Containerize the application with Docker.
- Add CI/CD, logging, and monitoring.
- Create the dashboard.
- Complete documentation and final release.

## 3. Detailed Sprint Plan

### Week 1: Model Foundation

#### Phase 1A: Dataset Collection and Validation
**Goal:** Identify, collect, and verify all public datasets needed for the project.

**Datasets:**
- NYC 311 Road Service Requests(2010–2019)
- NYC 311 Road Service Requests (2020–Present)
- Meteostat Weather Data
- OpenStreetMap Road Network
- NYC Traffic Volume Counts (Automated)
- NYC Traffic Volume Counts (Historical)



The project uses six public datasets that provide different information about road conditions and maintenance. Each dataset was selected because it contributes unique features that can improve the machine learning model.

**NYC 311 Road Service Requests:**

- Selected the NYC 311 Service Requests dataset (2020–Present).
- Verified that the dataset contains road-related complaints such as potholes and damaged streets.
- Reviewed all available columns and identified the fields needed for the project.
- Confirmed that complaint dates, street names, boroughs, and location information are available.
- Verified that the dataset can be filtered to include only road maintenance requests.

**Meteostat Weather Data:**

- Selected Meteostat as the weather data source.
- Confirmed that historical weather data is available for the same time period as the 311 dataset.
- Verified that the dataset contains daily weather measurements such as temperature, precipitation, snowfall, wind speed, and atmospheric pressure.
- Confirmed that weather data can be matched to complaint dates.

**OpenStreetMap Road Network:**

- Selected OpenStreetMap to provide road characteristics.
- Verified that road names and road classifications are available.
- Confirmed that useful attributes such as road type, number of lanes, speed limits, road length, and geometry can be extracted.
- Verified that road information can be matched using street names and geographic location.

**NYC Automated Traffic Volume Counts:**

- Selected the NYC Automated Traffic Volume Counts dataset.
- Verified that the dataset contains recent traffic information that aligns with the 2020–Present 311 dataset.
- Reviewed the available columns, including roadway name, traffic volume, direction, date, and location.
- Confirmed that traffic data can be linked to road segments used in the project.


**Key checks:**
- Confirm time range overlap.
- Review column names and date formats.
- Identify fields for merging.
- Document compatibility issues.

**Deliverables:**
- Validated datasets.
- Dataset review and compatibility report.

#### Phase 1B: Dataset Standardization

**Goal:** Create clean, project-specific datasets ready for feature engineering.

**Activities:**
- Filter NYC 311 records to road-related complaints.
- Select needed weather, road, and traffic fields.
- Remove duplicates and missing or invalid records.
- Standardize dates, names, and data types.
- Save cleaned files: `road_complaints.csv`, `weather.csv`, `roads.csv`, `traffic.csv`.

**Deliverables:**
- Clean standardized datasets.
- Data cleaning and quality reports.

#### Phase 1C: Dataset Integration and Feature Engineering
**Goal:** Merge all sources into one machine learning dataset.

**Activities:**
- Create time-based, seasonal, weather, traffic, and road features.
- Encode categorical variables.
- Merge datasets using dates, road names, boroughs, and geographic data.
- Validate missing values, feature types, and class distribution.

**Deliverables:**
- Engineered feature set.
- Final merged dataset.
- Integration and validation report.

#### Phase 1D: Model Training and Evaluation
**Goal:** Train and compare models to select the best one for deployment.

**Activities:**
- Split data into training and testing sets.
- Train baseline, Random Forest, XGBoost, LightGBM, and CatBoost models.
- Evaluate accuracy, precision, recall, F1-score, and confusion matrices.
- Review feature importance and prediction errors.

**Deliverables:**
- Trained models.
- Evaluation report.
- Performance comparison table.
- Selected production model.

#### Phase 1E: Machine Learning Pipeline
**Goal:** Build a reusable pipeline that combines preprocessing and the selected model.

**Activities:**
- Package preprocessing and prediction steps into one workflow.
- Test the pipeline on sample inputs.
- Save pipeline artifacts, feature order, and mappings.
- Prepare the pipeline for API use.

**Deliverables:**
- Complete ML pipeline.
- Saved pipeline artifact.
- Pipeline validation report.
- Deployment-ready files.

### Week 2: Deployment and Delivery

#### Phase 2A: API Development
**Goal:** Build a FastAPI service for predictions.

**Activities:**
- Create the FastAPI app structure.
- Add `/health`, `/predict`, and `/batch_predict`.
- Validate inputs with Pydantic models.
- Load the saved pipeline and return JSON responses.
- Test all endpoints locally.

**Deliverables:**
- FastAPI application.
- Endpoint tests and example responses.
- Pipeline loading logic.

#### Phase 2B: Docker and Local Deployment
**Goal:** Containerize the application for consistent local execution.

**Activities:**
- Create a Dockerfile.
- Copy project files, dependencies, and pipeline artifacts.
- Build and test the Docker image.
- Add Docker Compose if needed.

**Deliverables:**
- Dockerfile.
- `docker-compose.yml`.
- Tested local container.
- Deployment documentation.

#### Phase 2C: CI/CD Pipeline
**Goal:** Automate testing and validation with GitHub Actions.

**Activities:**
- Run tests on push and pull requests.
- Check formatting, dependencies, and API behavior.
- Verify Docker builds and pipeline loading.

**Deliverables:**
- GitHub Actions workflow.
- Automated test pipeline.
- CI/CD documentation.

#### Phase 2D: Monitoring and Logging
**Goal:** Track API activity, prediction latency, and errors.

**Activities:**
- Log requests, responses, and prediction outputs.
- Monitor response time and failures.
- Document troubleshooting and retraining guidance.

**Deliverables:**
- Logging setup.
- `MONITORING_GUIDE.md`.

#### Phase 2E: Dashboard Development

**Goal:** Build an interactive AI-powered maintenance planning dashboard that transforms machine learning predictions into operational inspection recommendations.

**Activities:**

- Develop an interactive Streamlit dashboard for maintenance planning.
- Build an AI Scenario Simulator that allows users to create future roadway conditions.
- Allow users to select a borough, planning date, weather scenario, traffic level, and number of priority roads to display.
- Evaluate every available street profile within the selected borough using the trained Decision Tree model.
- Rank all evaluated roads by inspection priority.
- Compare simulated conditions against a normal planning scenario.
- Generate operational planning estimates, including expected workload, suggested field teams, and estimated workdays.
- Provide explainable recommendations describing why roads were prioritized.
- Generate automated maintenance summaries and recommended next steps.

**Deliverables:**

- Interactive Streamlit dashboard.
- AI Scenario Simulator.
- Inspection Priority Ranking Engine.
- Operational Planning Engine.
- Automated Maintenance Brief.
- Scenario Comparison dashboard.
- Dashboard User Guide.

#### Phase 2F: Documentation and Final Presentation

**Goal:** Complete the technical documentation, business presentation materials, and prepare the final project demonstration.

**Activities:**

- Complete the technical README.
- Create API, deployment, monitoring, and dashboard documentation.
- Prepare business-oriented presentation materials.
- Organize the GitHub repository.
- Prepare the final project demonstration.

**Deliverables:**

- Technical documentation.
- Business presentation materials.
- Organized GitHub repository.
- Final project demonstration.

## 4. Quick Links (will be updated regularly)

- `README.md`
- `API_DOCUMENTATION.md`
- `DEPLOYMENT_GUIDE.md`
- `MONITORING_GUIDE.md`
- `TROUBLESHOOTING.md`



