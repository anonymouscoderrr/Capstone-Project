# Troubleshooting Guide

## Overview

This guide documents common issues that may occur while setting up, running, or testing the Predictive Road Maintenance Decision Support System.

---

# API Does Not Start

## Problem

The FastAPI server fails to start.

### Possible Causes

- Virtual environment is not activated.
- Project dependencies are not installed.
- Incorrect command was used.

### Solution

Activate the virtual environment.

```bash
.venv\Scripts\Activate.ps1
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Run the API.

```bash
uvicorn src.api.main:app --reload
```

---

# Dashboard Does Not Open

## Problem

The Streamlit dashboard does not launch.

### Solution

Run:

```bash
streamlit run src/dashboard/app.py
```

Verify that the processed dataset exists:

```
data/processed/model_data.csv
```

---

# ModuleNotFoundError: No module named 'src'

## Problem

Pytest cannot locate the project modules.

### Solution

Run tests using:

```bash
python -m pytest
```

instead of

```bash
pytest
```

Running the tests as a Python module ensures the project root is included in the module search path.

---

# GitHub Actions Fails

## Problem

The CI workflow reports failed tests.

### Possible Causes

- Health endpoint response does not match the expected test result.
- Missing project dependencies.
- Test files were modified without updating expected outputs.

### Solution

Run the tests locally before pushing.

```bash
python -m pytest
```

Verify that all tests pass before committing changes.

---

# Git Push Rejected

## Problem

Git reports:

```
non-fast-forward
```

### Solution

Pull the latest changes before pushing.

```bash
git pull --rebase origin feature/api-development
```

Resolve any merge conflicts and continue the rebase.

---

# Merge Conflict During Rebase

## Problem

Git reports merge conflicts while rebasing.

### Solution

Resolve the conflicting files manually.

After resolving:

```bash
git add .
git rebase --continue
```

Repeat until the rebase completes successfully.

---

# Docker Build Fails

## Problem

The Docker image cannot be created.

### Possible Causes

- Docker Desktop is not running.
- Missing project dependencies.
- Invalid Dockerfile configuration.

### Solution

Verify Docker Desktop is running.

Rebuild the image.

```bash
docker build -t road-maintenance-api .
```

---

# Large File Push Rejected

## Problem

GitHub rejects large dataset files.

### Solution

Only include the processed dataset required for the dashboard.

Keep large raw datasets outside of the repository 

---

# Dashboard Displays Incorrect Data

## Problem

Charts or metrics appear incorrect.

### Possible Causes

- Filters are applied.
- The processed dataset has not been regenerated.
- The dashboard is loading an outdated CSV.

### Solution

Verify the active filters.

Regenerate the processed dataset if necessary.

Restart the Streamlit application.

---

# Unit Tests Fail

## Problem

One or more automated tests fail.

### Solution

Run:

```bash
python -m pytest
```

Review the error message.

Verify that the API responses still match the expected test values.

---

# Additional Help

If problems continue:

- Verify all required Python packages are installed.
- Confirm the virtual environment is activated.
- Review the deployment and API documentation.
- Check GitHub Actions logs for detailed error messages.