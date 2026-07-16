# RoadWise AI Dashboard Guide

## Overview

The RoadWise AI dashboard is an interactive Streamlit application designed to support road inspection planning across New York City.

Unlike a traditional analytics dashboard that only summarizes historical complaints, the current version includes a Maintenance Scenario Simulator. The simulator evaluates every available street profile in the selected borough, applies the chosen planning conditions, ranks all roads by inspection priority, and displays the highest-priority results.

The dashboard combines:

- NYC 311 road complaint history
- Historical weather information
- Traffic data
- Decision Tree predictions
- Inspection priority scoring
- Operational planning estimates

The goal is to help users move from historical analysis to actionable inspection planning.

---

# Launching the Dashboard

From the project root, run:

```bash
python -m streamlit run src/dashboard/operations_planner.py
```

The dashboard will open automatically in a browser.

Default URL:

```text
http://localhost:8501
```

---

# Dashboard Workflow

The dashboard follows this process:

```text
Select Planning Scenario
        │
        ▼
Filter Selected Borough
        │
        ▼
Build One Profile Per Street
        │
        ▼
Evaluate Every Available Street
        │
        ▼
Generate Decision Tree Predictions
        │
        ▼
Calculate Inspection Priorities
        │
        ▼
Rank All Roads
        │
        ▼
Display Highest-Priority Results
        │
        ▼
Generate Operational Recommendations
```

---

# Scenario Controls

The left sidebar contains the controls used to create a planning scenario.

## Planning Date

The planning date determines the future year and month passed to the machine learning model.

The selected date does not claim to provide an exact real-world weather forecast. It provides the temporal context used during scenario simulation.

---

## Borough

The Borough selector determines which part of New York City is evaluated.

For the selected borough, the dashboard:

1. Filters the processed dataset.
2. Groups repeated historical records into one profile per street.
3. Evaluates every available street profile.
4. Ranks the resulting inspection priorities.

Available borough values depend on the records contained in the processed dataset.

---

## Weather Scenario

The Weather Scenario selector applies predefined environmental assumptions.

Available scenarios include:

- Normal
- Heavy Rain
- Snow
- Extreme Heat

Each option updates the weather-related model inputs, including temperature, precipitation, snowfall, snow depth, weather code, and wind speed.

The simulator then compares the selected conditions against a normal-weather baseline.

---

## Traffic Level

The Traffic Level selector adjusts the historical traffic estimate used during simulation.

Available levels include:

- Low
- Normal
- High

Traffic conditions are applied through predefined multipliers before model prediction and inspection priority calculation.

---

## Priority Roads to Display

This slider controls how many of the highest-ranked roads are shown in the dashboard table.

Available values range from 10 to 100.

The slider does not control how many streets are evaluated.

The simulator evaluates every available street profile within the selected borough. The slider only limits how many ranked results are displayed so the output remains readable.

For example:

```text
Total Roads Evaluated: 1,950
Priority Roads Displayed: 100
```

This means all 1,950 street profiles were evaluated, but only the top 100 were displayed.

---

# Generate Maintenance Forecast

After selecting the planning conditions, click:

```text
Generate Maintenance Forecast
```

The dashboard then:

1. Creates one aggregated historical profile per street.
2. Runs the Decision Tree model for every street profile.
3. Calculates a composite Inspection Priority score.
4. Ranks all evaluated roads.
5. Generates workload and staffing estimates.
6. Displays the highest-priority roads.
7. Produces a plain-language maintenance brief.

---

# Dashboard Sections

## 1. Maintenance Outlook

The Maintenance Outlook provides a high-level summary of the completed simulation.

Displayed metrics include:

### Total Roads Evaluated

The total number of unique street profiles evaluated within the selected borough.

This number may be much larger than the number displayed in the priority table.

### Priority Roads

The number of roads classified as either:

- Immediate Attention
- Inspection Recommended

Roads categorized as Routine Monitoring are not included in this count.

### Expected Workload

A high-level workload classification based on the number of roads requiring action.

Possible values include:

- Light
- Moderate
- Heavy

### Highest Priority Road

The roadway with the highest calculated Inspection Priority score under the selected conditions.

---

## 2. Automated Maintenance Brief

The Automated Maintenance Brief generates a plain-language summary of the scenario.

The brief explains:

- Planning date
- Selected borough
- Weather conditions
- Traffic conditions
- Total roads evaluated
- Number of roads requiring action
- Change from normal conditions
- Highest-priority roadway
- Recommended inspection order

This section allows users to understand the scenario without reading the full ranked table.

---

## 3. Scenario Comparison

The scenario comparison evaluates the selected conditions against a baseline scenario using:

- Normal weather
- Normal traffic

The comparison includes:

- Total roads evaluated
- Roads requiring action
- Expected workload
- Average inspection priority
- Highest inspection priority
- Highest-priority road

This helps users understand whether the chosen scenario changes the number of roads requiring action or only increases their urgency.

For example, heavy rain may leave the number of priority roads unchanged while increasing the average inspection priority.

---

## 4. Operational Planning Estimate

The Operational Planning Estimate converts priority results into staffing guidance.

Displayed values include:

### Immediate Reviews

Roads with an Inspection Priority high enough to require immediate attention.

### Scheduled Reviews

Roads recommended for inspection but not classified as immediate.

### Suggested Field Teams

An estimated number of teams needed to address the current action list.

The current planning assumption is:

```text
One field team can review approximately four priority roads per workday.
```

### Estimated Workdays

An estimate of how long the current action list may take using the suggested number of teams.

These are planning estimates only. They do not assign routes or guarantee completion time.

---

## 5. Recommended Road Inspection Priorities

This table displays the highest-ranked roads selected by the user.

Columns include:

| Column | Description |
|---|---|
| Priority Rank | Position after sorting all evaluated roads |
| Street Name | Roadway being evaluated |
| Maintenance Status | Recommended operational category |
| Inspection Priority | Composite planning score from 0 to 100 |
| Complaint Count | Historical complaint activity |
| Traffic Level | Relative traffic category or unavailable status |
| Why It Was Flagged | Plain-language explanation |
| Recommended Response | Suggested inspection action |

The dashboard may show only the first 10 rows on screen, but the table remains scrollable when more roads are selected.

---

## 6. Why These Roads Were Prioritized

The dashboard provides expandable explanations for the top five ranked roads.

Each explanation includes:

- Maintenance status
- Inspection priority
- Historical complaint count
- Traffic level
- Reason for prioritization
- Recommended response

This section improves transparency by showing why the system ranked one road above another.

---

## 7. Recommended Next Steps

The final section converts the ranked results into a concise operational recommendation.

It identifies:

- Expected workload
- Roads to inspect first
- Highest-priority roadway
- Suggested number of teams
- Estimated completion time

The recommendation uses only roads classified as Immediate Attention or Inspection Recommended.

---

# Inspection Priority Score

The Inspection Priority score is a composite planning measure.

It combines:

- Predicted maintenance probability
- Historical complaint activity
- Traffic exposure
- Selected weather scenario

The score ranges from 0 to 100.

Higher scores indicate a greater need for earlier inspection under the selected scenario.

The score is used for ranking and planning. It is not a guaranteed measurement of physical road damage.

Final maintenance decisions should be confirmed through field inspection and professional judgment.

---

# Maintenance Status Categories

Roads are placed into one of three categories.

| Status | Meaning |
|---|---|
| Immediate Attention | Inspect as soon as possible or within 24–48 hours |
| Inspection Recommended | Schedule an inspection within the current planning period |
| Routine Monitoring | Continue monitoring unless conditions change |

The maintenance status is derived from the Inspection Priority score.

---

# Full-Borough Evaluation

The current dashboard evaluates every available street profile in the selected borough.

Historical rows are first aggregated by street because the processed dataset contains repeated observations for the same roadway across different dates and conditions.

The result is one profile per street containing information such as:

- Average geographic location
- Historical complaint count
- Average traffic estimate
- Selected future year and month
- Selected weather assumptions
- Selected traffic adjustment

The model evaluates all profiles in one batch, ranks the outputs, and displays only the highest-priority results.

---

# Data Source

The dashboard uses:

```text
data/processed/model_data.csv
```

The processed dataset contains approximately:

```text
311,796 historical records
15 columns
```

These are historical observations rather than 311,796 unique roads.

The number of unique evaluated street profiles depends on the selected borough.

---

# Model Artifacts

The dashboard loads the following files:

```text
models/decision_tree_model.pkl
models/feature_columns.pkl
```

The first file contains the trained Decision Tree model.

The second preserves the expected model feature order during inference.

---

# Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Joblib

---

# Important Interpretation Notes

The dashboard is a decision-support prototype.

It does not:

- Confirm actual road damage
- Replace engineering inspections
- Use live weather forecasts
- Use live traffic feeds
- Assign exact inspection routes
- Guarantee staffing or completion estimates

It is designed to organize inspection priorities using historical data, machine learning predictions, and user-defined planning scenarios.

---

# Recommended Demo Scenario

A useful demonstration is:

```text
Borough: Bronx
Weather Scenario: Normal
Traffic Level: Low
Priority Roads to Display: 100
```

Then compare it against:

```text
Borough: Bronx
Weather Scenario: Heavy Rain
Traffic Level: High
Priority Roads to Display: 100
```

During the comparison, focus on:

- Changes in average inspection priority
- Changes in highest inspection priority
- Changes in priority-road count
- Changes in recommended workload
- Changes in staffing estimates

---

# Purpose

The RoadWise AI dashboard transforms historical road complaints, weather information, traffic data, and machine learning predictions into a ranked inspection plan.

Its main purpose is to demonstrate how a machine learning model can be extended beyond prediction into scenario simulation, explainability, and operational planning.