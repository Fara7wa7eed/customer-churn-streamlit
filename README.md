# 📊 Customer Churn Prediction using Machine Learning

A Machine Learning web application that predicts whether a telecom customer is likely to churn based on demographic, service, and billing information.

The application is built with **Python**, **Scikit-learn**, and **Streamlit**, and is deployed online using **Streamlit Community Cloud**.

---

# 🚀 Live Demo

🔗 **Try the application here:**

https://customer-churn-app-76mbhvghhnrqkdo3yqjnrk.streamlit.app/

---

# 📖 Project Overview

Customer churn prediction is an important business problem that helps companies identify customers who are likely to stop using their services. By predicting churn in advance, businesses can improve customer retention through targeted marketing campaigns and better customer support. :contentReference[oaicite:0]{index=0}

This application allows users to enter customer information and instantly receive:

- ✅ Churn Prediction
- 📈 Churn Probability
- 📉 Stay Probability

---

# 📂 Dataset

This project uses the **Telco Customer Churn Dataset**.

The dataset includes customer information such as:

- Gender
- Senior Citizen
- Partner
- Dependents
- Phone Service
- Multiple Lines
- Internet Service
- Online Security
- Online Backup
- Device Protection
- Tech Support
- Streaming TV
- Streaming Movies
- Contract Type
- Paperless Billing
- Payment Method
- Tenure Months
- Monthly Charges
- Total Charges
- Customer Lifetime Value (CLTV)

---

# 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib

---

# 🤖 Machine Learning Model

**Model Used:**

- Random Forest Classifier

**Preprocessing:**

- ColumnTransformer
- One-Hot Encoding
- Feature Transformation

The trained model and preprocessing pipeline are saved using Joblib:

- `model.pkl`
- `preprocessor.pkl`

---

# ✨ Features

- 📋 Interactive customer information form
- 🤖 Real-time customer churn prediction
- 📊 Churn probability visualization
- 📉 Stay probability visualization
- ⚡ Fast prediction using a trained Random Forest model
- 🌐 Web application deployed with Streamlit

---

# 📁 Project Structure

```text
customer-churn-streamlit/
│
├── app.py
├── model.pkl
├── preprocessor.pkl
├── requirements.txt
├── Telco_customer_churn.csv
├── ML_Customer_Churn_.ipynb
├── ml_customer_churn_.py
└── README.md
```

---

# ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/Fara7wa7eed/customer-churn-streamlit.git
```

### Navigate to the project folder

```bash
cd customer-churn-streamlit
```

### Install the required packages

```bash
pip install -r requirements.txt
```

### Run the application

```bash
streamlit run app.py
```

---

# 📸 Application Preview

> Add a screenshot of your Streamlit application here.

Example:

```md
![Application Screenshot](screenshot.png)
```

---

# 📈 Prediction Output

The application predicts whether a customer is likely to churn.

Example outputs:

- ✅ Customer is likely to stay
- ⚠️ Customer is likely to churn

The application also displays:

- Stay Probability
- Churn Probability
- Prediction Confidence

---

# 🔮 Future Improvements

- SHAP Explainability
- Feature Importance Visualization
- Interactive Dashboard
- Data Visualization
- Model Comparison
- Authentication System
- Database Integration

---







# 📄 License

This project was developed for educational purposes and as part of a Machine Learning portfolio.
