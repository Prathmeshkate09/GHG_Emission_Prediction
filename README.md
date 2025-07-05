# GHG_Emission_Prediction
Streamlit app for predicting supply chain GHG emissions
# 🌿 Supply Chain GHG Emission Predictor

This Streamlit web application predicts **Supply Chain Greenhouse Gas (GHG) Emission Factors with Margins** using DQ (Data Quality) metrics and other input parameters.

🔗 **Live App**: [https://ghgemissionprediction-eks3vkopzoov9evmepha3w.streamlit.app](https://ghgemissionprediction-eks3vkopzoov9evmepha3w.streamlit.app)

---

## 📌 Features

- Predicts emission factors with margins for:
  - Carbon dioxide
  - Methane
  - Nitrous oxide
  - Other GHGs
- Based on:
  - DQ scores (Reliability, Temporal, Geographical, Technological, Data Collection)
  - Supply Chain emission data without margins
  - Margins
  - Unit & Source

- Trained using Linear Regression model
- Input features scaled using StandardScaler
- Frontend built using Streamlit

---

## 🧠 How It Works

1. User enters emission factors and DQ metrics
2. Input is preprocessed and scaled
3. Model predicts final emission factor with margins

---

## 🛠️ Tech Stack

| Layer        | Tools/Libraries                |
|--------------|--------------------------------|
| UI / App     | Streamlit                      |
| ML Model     | scikit-learn (Linear Regression) |
| Data Handling| pandas, numpy                  |
| Model Saving | joblib                         |
| Deployment   | Streamlit Cloud                |

---

## 📁 Folder Structure

GHG_Emission_Prediction/
├── app.py # Main Streamlit app
├── requirements.txt # Python dependencies
├── models/
│ ├── LR_model.pkl # Trained model
│ └── scaler.pkl # Scaler used during training
└── utils/
└── preprocessor.py # Input preprocessing logic


---

## 🚀 Run Locally

1. Clone the repository

```bash
git clone https://github.com/Prathmeshkate09/GHG_Emission_Prediction.git
cd GHG_Emission_Prediction
Install dependencies

```
2. Install dependencies
```
pip install -r requirements.txt

```
3. Run The App
```
streamlit run app.py
```
🧪 Requirements
```
Python 3.11+

Streamlit

scikit-learn

pandas

numpy

joblib
