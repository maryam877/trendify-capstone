# Trendify ETL Pipeline

This project is part of a data consulting capstone. It processes Brazilian e-commerce dataset to generate clean, structured data for business analysis.

## 🧩 Project Structure

```
trendify_etl/
├── data/ # Raw CSV files
├── etl/ # ETL logic
│ ├── load.py
│ └── transform.py
├── outputs/ # Cleaned data output
│ └── final_orders_clean.csv
├── main.py # Runs the ETL pipeline
├── test_load.py # Load test
└── README.md
```
---

## 🔄 Pipeline Steps

1. **Load Data**
   - CSVs loaded via modular functions in `load.py`.

2. **Transform & Clean**
   - `transform.py` merges datasets and computes:
     - `delivery_delay`
     - `wait_time`
     - `is_late` (late delivery flag)
     - `review_score_bucket` (good/neutral/bad)

3. **Export Output**
   - Final clean file saved to `outputs/final_orders_clean.csv`.

---

## 📊 EDA Summary

The following insights were uncovered via `run_eda.py`:

- **Late Deliveries:** Majority orders are on time.
- **Review Scores:** Most customers give 5-star reviews.
- **Delay vs Review:** Late deliveries often result in bad reviews.
- **Seller Performance:** Sellers with repeated delays or bad reviews are identified.
- **Top Under-performing States** also visualized.

---

## 🤖 Predicting Problematic Orders

Using `predict_problematic_orders.py`, a Random Forest classifier was trained to flag orders likely to:

- be **delivered late**
- or receive a **bad review**

The model uses:
- `wait_time`
- `price`
- `freight_value`

✅ Results: Classification report and confusion matrix are plotted after training.

---

## 🛠️ Technologies Used

- Python 3.12
- Pandas
- Matplotlib & Seaborn
- Scikit-learn
- Git & GitHub

---

## ✅ Deliverables

This pipeline enables Trendify to:

- Identify sellers/regions with recurring delays or bad feedback.
- Correlate delivery performance with reviews.
- **Predict problematic orders before they happen**.
- Support better decision-making on logistics and seller partnerships.

---

## 📌 Author

**Maryam**  
Capstone Project for Data Consulting  
GitHub: [maryam877](https://github.com/maryam877)

---
