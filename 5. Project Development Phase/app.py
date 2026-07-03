from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load("model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    input_data = pd.DataFrame([{
        "Gender": int(request.form["gender"]),
        "Married": int(request.form["married"]),
        "Dependents": int(request.form["dependents"]),
        "Education": int(request.form["education"]),
        "Self_Employed": int(request.form["self_employed"]),
        "ApplicantIncome": float(request.form["applicant_income"]),
        "CoapplicantIncome": float(request.form["coapplicant_income"]),
        "LoanAmount": float(request.form["loan_amount"]),
        "Loan_Amount_Term": float(request.form["loan_amount_term"]),
        "Credit_History": float(request.form["credit_history"]),
        "Property_Area": int(request.form["property_area"])
    }])

    prediction = model.predict(input_data)[0]

    confidence = model.predict_proba(input_data)[0]
    confidence_score = max(confidence) * 100

    if prediction == 1:
        result = "✅ Loan Approved"
    else:
        result = "❌ Loan Rejected"

    return render_template(
        "result.html",
        prediction=result,
        confidence=f"{confidence_score:.2f}%"
    )

if __name__ == "__main__":
    app.run(debug=True)