import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier

# Load dataset
data = pd.read_csv("dataset/loan_data.csv")

# Fill missing values
data["Gender"] = data["Gender"].fillna(data["Gender"].mode()[0])
data["Married"] = data["Married"].fillna(data["Married"].mode()[0])
data["Dependents"] = data["Dependents"].fillna(data["Dependents"].mode()[0])
data["Self_Employed"] = data["Self_Employed"].fillna(data["Self_Employed"].mode()[0])
data["LoanAmount"] = data["LoanAmount"].fillna(data["LoanAmount"].median())
data["Loan_Amount_Term"] = data["Loan_Amount_Term"].fillna(data["Loan_Amount_Term"].mode()[0])
data["Credit_History"] = data["Credit_History"].fillna(data["Credit_History"].mode()[0])

# Convert categorical values
data["Dependents"] = data["Dependents"].replace("3+", 3)
data["Dependents"] = pd.to_numeric(data["Dependents"])

data["Gender"] = data["Gender"].map({"Male":1,"Female":0})
data["Married"] = data["Married"].map({"Yes":1,"No":0})
data["Education"] = data["Education"].map({"Graduate":1,"Not Graduate":0})
data["Self_Employed"] = data["Self_Employed"].map({"Yes":1,"No":0})
data["Property_Area"] = data["Property_Area"].map({
    "Rural":0,
    "Semiurban":1,
    "Urban":2
})
data["Loan_Status"] = data["Loan_Status"].map({"N":0,"Y":1})

# Drop Loan_ID
data.drop("Loan_ID", axis=1, inplace=True)

# Features and Target
X = data.drop("Loan_Status", axis=1)
y = data["Loan_Status"]

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# Train Random Forest
model = RandomForestClassifier(
    n_estimators=300,
    max_depth=12,
    min_samples_split=4,
    random_state=42
)

model.fit(X_train, y_train)

# Accuracy
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print(f"Model Accuracy: {accuracy*100:.2f}%")

# Save Model
joblib.dump(model, "model.pkl")

print("model.pkl saved successfully.")