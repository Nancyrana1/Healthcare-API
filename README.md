# 💰 Insurance Premium Predictor

A full-stack Machine Learning project that predicts the **insurance premium category** based on user details like age, BMI, income, lifestyle, and occupation.

---

## 🚀 Project Overview

This application allows users to input personal and lifestyle details through a **Streamlit UI**, which sends data to a **FastAPI backend**.
The backend processes the data, applies feature engineering, and uses a trained ML model to predict the premium category.

---

## 🧠 Features

* Predict insurance premium category
* Real-time API interaction using FastAPI
* Interactive frontend using Streamlit
* Feature engineering (BMI, age group, lifestyle risk, city tier)
* Clean and modular code structure

---

## 🛠️ Tech Stack

* **Backend:** FastAPI
* **Frontend:** Streamlit
* **Machine Learning:** Scikit-learn
* **Language:** Python

---

## 📂 Project Structure

```
patient_fast_api/
│
├── main.py          # FastAPI backend
├── app.py           # Streamlit frontend
├── model.pkl        # Trained ML model (optional)
├── .gitignore
└── README.md
```

---

## ▶️ How to Run Locally

### 1️⃣ Clone the repository

```
git clone https://github.com/Nancyrana1/Insurance-Premium-Predictor.git
cd Insurance-Premium-Predictor
```

---

### 2️⃣ Create virtual environment

```
python -m venv myenv
```

Activate:

```
myenv\Scripts\activate
```

---

### 3️⃣ Install dependencies

```
pip install fastapi uvicorn streamlit pandas numpy scikit-learn
```

---

### 4️⃣ Run Backend (FastAPI)

```
uvicorn main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

### 5️⃣ Run Frontend (Streamlit)

```
streamlit run app.py
```

---

## 🔄 API Endpoint

**POST /predict**

### Sample Input:

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

### Response:

```json
{
  "predicted_category": "Medium"
}
```

---

## 📊 Feature Engineering

The model uses derived features such as:

* **BMI** = weight / height²
* **Age Group** (young, adult, middle_age, senior)
* **Lifestyle Risk** (based on BMI & smoking)
* **City Tier** (Tier 1, 2, 3 classification)

---

## ⚠️ Notes

* Ensure `model.pkl` is present in the root directory
* Use correct `scikit-learn` version for compatibility
* Do not upload `myenv/` to GitHub

---

## 💼 Use Cases

* Insurance premium estimation
* Health risk categorization
* ML + API + UI integration learning

---

## 👩‍💻 Author

**Nancy Rana**

---

## ⭐ Future Improvements

* Add prediction probabilities
* Deploy on cloud (AWS / Render)
* Improve UI/UX
* Add user authentication

---

## 📌 License

This project is for educational purposes.
