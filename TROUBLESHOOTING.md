# Troubleshooting Guide

## Overview

This guide provides solutions to common issues that may occur while running the RoadWise AI application.

The troubleshooting steps cover:

- FastAPI
- Streamlit Dashboard
- Machine Learning Model
- Data Loading
- Scenario Simulator

---

# 1. API Does Not Start

## Problem

The FastAPI server does not start.

Example:

```
ModuleNotFoundError
```

## Possible Causes

- Missing Python dependencies
- Incorrect working directory
- Typographical error in the startup command

## Solution

Verify that you are inside the project root.

Run:

```bash
pip install -r requirements.txt
```

Start the API again:

```bash
uvicorn src.api.main:app --reload
```

---

# 2. Dashboard Does Not Start

## Problem

The Streamlit dashboard fails to launch.

## Solution

Verify that Streamlit is installed.

```bash
pip install streamlit
```

Launch the dashboard:

```bash
python -m streamlit run src/dashboard/operations_planner.py
```

---

# 3. Model File Not Found

## Problem

```
FileNotFoundError
```

or

```
decision_tree_model.pkl not found
```

## Solution

Verify the following files exist:

```
models/

decision_tree_model.pkl
feature_columns.pkl
```

These files must be generated before running the application.

---

# 4. Processed Dataset Missing

## Problem

The dashboard reports that the processed dataset cannot be loaded.

## Solution

Verify the following file exists.

```
data/processed/model_data.csv
```

If the file is missing, rerun the preprocessing notebook to regenerate the processed dataset.

---

# 5. Prediction Endpoint Returns Validation Error

## Problem

```
422 Unprocessable Entity
```

## Cause

The request does not match the expected Pydantic schema.

## Solution

Verify that:

- Required fields are included.
- Field names match the API documentation.
- Numeric values are valid.

Swagger UI can be used to verify the request format.

```
http://127.0.0.1:8000/docs
```

---

# 6. Dashboard Appears Slow

## Problem

The dashboard requires several seconds to generate results.

## Cause

This is expected behavior.

The current implementation evaluates **every available street profile** within the selected borough before ranking inspection priorities.

Larger boroughs naturally require more processing than smaller boroughs.

## Solution

Wait for the simulation to complete.

The number of **Priority Roads to Display** affects only how many ranked roads are shown—not how many roads are evaluated.

---

# 7. No Roads Displayed

## Problem

The priority table is empty.

## Possible Causes

- The selected borough contains no processed records.
- Data filtering removed all matching roads.

## Solution

Choose another borough and rerun the simulation.

Verify that the processed dataset contains roadway records for the selected borough.

---

# 8. FastAPI Port Already in Use

## Problem

```
Address already in use
```

## Solution

Another application is already using port:

```
8000
```

Stop the existing process or use another port.

Example:

```bash
uvicorn src.api.main:app --reload --port 8001
```

---

# 9. Streamlit Port Already in Use

## Problem

Streamlit cannot start.

## Solution

Port:

```
8501
```

is already occupied.

Start Streamlit using another port.

```bash
python -m streamlit run src/dashboard/operations_planner.py --server.port 8502
```

---

# 10. Swagger Page Does Not Load

## Problem

```
http://127.0.0.1:8000/docs
```

does not open.

## Solution

Verify that the FastAPI server is running before opening Swagger.

Restart the server if necessary.

---

# 11. Prediction Results Seem Incorrect

## Possible Causes

- Incorrect input values
- Unrealistic weather scenario
- Invalid traffic assumptions

## Recommendation

Verify:

- Borough
- Planning date
- Weather scenario
- Traffic level

before rerunning the simulation.

Remember that RoadWise AI generates decision-support recommendations using historical data and machine learning predictions. Final maintenance decisions should always be confirmed through field inspection.

---

# 12. Common Startup Commands

## FastAPI

```bash
uvicorn src.api.main:app --reload
```

---

## Streamlit

```bash
python -m streamlit run src/dashboard/operations_planner.py
```

---

## Docker

```bash
docker compose up --build
```

---

# Need More Help?

If the application still does not run correctly:

1. Verify all dependencies are installed.
2. Confirm the model files exist.
3. Confirm the processed dataset exists.
4. Review the application logs.
5. Restart the API and dashboard.

Most startup issues are caused by missing files, incorrect working directories, or missing Python packages.