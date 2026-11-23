# Insurance Premium Predictor API

A machine-learning application that predicts an **insurance premium category** from user-provided demographic, income, lifestyle, and location details. The project combines a **FastAPI backend** for request validation and model inference with a **Streamlit frontend** for interactive input.

> **Educational project:** Predictions are produced by a trained machine-learning model and should not be treated as insurance quotes, medical advice, or financial advice.

## Overview

The application accepts details such as age, weight, height, annual income, smoking status, city, and occupation. The API validates the input with Pydantic, derives additional features, constructs a pandas DataFrame, and passes it to a serialized scikit-learn-compatible model for category prediction.

## Features

- Interactive Streamlit interface for entering user details
- FastAPI `POST /predict` endpoint
- Pydantic input validation with constrained fields and allowed occupation values
- Computed features:
  - **BMI:** weight divided by height squared
  - **Age group:** young, adult, middle-aged, or senior
  - **Lifestyle risk:** derived from smoking status and BMI
  - **City tier:** mapped from the configured Tier 1 and Tier 2 city lists; other cities are assigned Tier 3
- Model inference using a locally loaded `model.pkl` artifact
- Interactive API documentation provided by FastAPI

## Architecture

```text
User
 |
 v
Streamlit UI (frontend.py)
 |
 | POST /predict (JSON)
 v
FastAPI application (main.py)
 |
 v
Pydantic validation + feature engineering
 |
 v
Pandas input DataFrame
 |
 v
Trained model (model.pkl)
 |
 v
Predicted premium category
```

## Tech Stack

| Layer | Technologies |
|---|---|
| Language | Python |
| API backend | FastAPI, Uvicorn |
| Frontend | Streamlit |
| Data processing | Pandas |
| Input validation | Pydantic |
| Machine learning | Serialized model loaded with Pickle |
| HTTP requests | Requests |

## Repository Structure

```text
Healthcare-API/
├── main.py        # FastAPI backend, validation, feature engineering, prediction
├── frontend.py    # Streamlit user interface and API request
├── model.pkl      # Required trained model artifact (not present in the current repository tree)
├── .gitignore
└── README.md
```

**Important:** The current repository listing does not include `model.pkl`. The API loads this file when `main.py` starts, so you must provide the compatible trained model artifact before running the backend. Do not commit large or sensitive model/data artifacts unless appropriate for the project.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Nancyrana1/Healthcare-API.git
cd Healthcare-API
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\\Scripts\\Activate.ps1
```

macOS/Linux:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install fastapi uvicorn streamlit pandas pydantic scikit-learn requests
```

Use a scikit-learn version compatible with the version used to serialize `model.pkl`. Pickle model files are not generally guaranteed to be portable across library versions.

### 4. Add the trained model

Place the compatible `model.pkl` file in the project root, alongside `main.py`.

### 5. Start the API

```bash
uvicorn main:app --reload
```

The API will be available at:

- Base URL: `http://127.0.0.1:8000`
- Interactive documentation: `http://127.0.0.1:8000/docs`

### 6. Start the Streamlit frontend

Open a second terminal with the virtual environment activated:

```bash
streamlit run frontend.py
```

The frontend is configured to send requests to `http://127.0.0.1:8000/predict`. Run the API locally before submitting a prediction.

## API Reference

### Predict premium category

`POST /predict`

Example request:

```json
{
  "age": 30,
  "weight": 65,
  "height": 1.7,
  "income_lpa": 10,
  "smoker": false,
  "city": "Mumbai",
  "occupation": "private_job"
}
```

Allowed occupation values:

```text
retired
freelancer
student
government_job
business_owner
unemployed
private_job
```

Example response shape:

```json
{
  "predicted_category": "Medium"
}
```

The actual category depends on the trained model and supplied input.

## Implementation Notes

- The model is deserialized at API startup from `model.pkl`.
- The request schema validates age, weight, height, income, smoking status, city, and occupation.
- Feature names passed to the model are `bmi`, `age_group`, `lifestyle_risk`, `city_tier`, `income_lpa`, and `occupation`.
- City-tier mapping is based on the lists defined in `main.py`; an unlisted city is currently treated as Tier 3.
- The Streamlit frontend uses a local API URL. Update `API_URL` in `frontend.py` when connecting to a separately hosted backend.

## Future Improvements

- Add automated tests for request validation and prediction behaviour
- Add a dependency file with tested, pinned package versions
- Add configurable API URL and improved request timeout/error handling in the frontend
- Document model training data, evaluation metrics, and model provenance
- Add input range checks and edge-case tests for BMI and city mapping
- Deploy the API and frontend with environment-based configuration

## Author

**Nancy Rana**

- GitHub: [@Nancyrana1](https://github.com/Nancyrana1)
- Portfolio: [Personal Portfolio](https://portfolio-nancyrana1s-projects.vercel.app/)
- LinkedIn: [Nancy Rana](https://www.linkedin.com/in/nancy-rana-2441942a4/)

---

*Built as a practical project to explore machine-learning inference through a REST API and an interactive Python frontend.*
