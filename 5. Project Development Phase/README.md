# 🏦 Smart Lender – AI-Powered Loan Approval Prediction System

## 📌 Project Overview

Smart Lender is a Machine Learning-based web application that predicts whether a loan application is likely to be approved or rejected. The system analyzes applicant information such as income, education, credit history, employment status, and property area to help users determine loan eligibility.

The project is developed using **Python**, **Flask**, **Scikit-learn**, **HTML**, and **CSS**. It provides a simple and user-friendly interface where users can enter loan applicant details and receive an instant prediction.

---

## 🚀 Features

* Predicts whether a loan will be Approved or Rejected.
* User-friendly web interface.
* Machine Learning-based prediction using Random Forest Classifier.
* Displays prediction confidence score.
* Handles missing values through data preprocessing.
* Fast and accurate prediction system.
* Responsive web design.

---

## 🛠️ Technologies Used

* Python
* Flask
* Pandas
* NumPy
* Scikit-learn
* Joblib
* HTML5
* CSS3

---

## 📂 Project Structure

```text
Smart Lender/
│
├── app.py
├── train_model.py
├── model.pkl
├── requirements.txt
├── README.md
│
├── dataset/
│   └── loan_data.csv
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   └── style.css
```

---

## 📊 Dataset

The project uses a Loan Prediction dataset containing applicant details such as:

* Gender
* Marital Status
* Dependents
* Education
* Self Employed
* Applicant Income
* Coapplicant Income
* Loan Amount
* Loan Amount Term
* Credit History
* Property Area
* Loan Status

---

## ⚙️ Installation

1. Clone the repository.
2. Create a virtual environment.
3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

Start the Flask application:

```bash
py app.py
```

Then open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## 📈 Machine Learning Model

* **Algorithm:** Random Forest Classifier
* **Model Accuracy:** **83.74%**

---

## 🔮 Future Enhancements

* User authentication and login
* Loan application history
* Email notification system
* Cloud deployment
* Integration with banking APIs
* Interactive analytics dashboard

---

## 👩‍💻 Developer

**Deepthi Bethamsetty**

SmartBridge Internship Project

Year: 2026