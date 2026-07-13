# Deployment Guide

## Overview

This guide explains how to set up, run, and test the Predictive Road Maintenance Decision Support System on a local machine.

---

# Prerequisites

Before running the project, install the following software:

- Python 3.13 or later
- Git
- Docker Desktop (optional)
- Visual Studio Code (recommended)

---

# Clone the Repository

Clone the repository from GitHub.

```bash
git clone https://github.com/anonymouscoderrr/Capstone-Project.git
cd Capstone-Project
```

---

# Create a Virtual Environment

Windows

```bash
python -m venv .venv
```

Activate the virtual environment.

PowerShell

```bash
.venv\Scripts\Activate.ps1
```

Command Prompt

```bash
.venv\Scripts\activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run the FastAPI Application

Start the API.

```bash
uvicorn src.api.main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Interactive Swagger documentation:

```
http://127.0.0.1:8000/docs
```

---

# Run the Dashboard

Launch the Streamlit dashboard.

```bash
streamlit run src/dashboard/app.py
```

The dashboard opens automatically in your browser.

Default URL:

```
http://localhost:8501
```

---

# Run Unit Tests

Run all automated tests.

```bash
python -m pytest
```

All tests should pass successfully.

---

# Docker Deployment

Build the Docker image.

```bash
docker compose up --build
```
The API will be available at:

http://localhost:8000

---

# GitHub Actions

The repository includes automated GitHub Actions workflows.

CI Workflow

- Installs project dependencies
- Runs automated tests
- Validates the project before merging

CD Workflow

- Executes after a successful CI run
- Builds the Docker image
- Confirms the project is ready for deployment

---

# Project Structure

```
Capstone-Project/
│
├── data/
├── models/
├── notebooks/
├── outputs/
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
├── requirements.txt
├── Dockerfile
└── docker-compose.yml
```

---

# Deployment Verification

Verify that deployment completed successfully.

Checklist

- API starts successfully
- Dashboard opens correctly
- Swagger documentation loads
- Unit tests pass
- Docker image builds successfully
- GitHub Actions complete without errors

---

# Next Steps

Once deployment is verified, the application is ready for demonstration, further development, or production improvements.