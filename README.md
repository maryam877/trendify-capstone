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


## 🔄 Pipeline Steps

1. **Load Data**  
   All CSVs are loaded using modular functions in `load.py`.

2. **Transform & Clean**  
   `transform.py` merges and cleans datasets, and creates:
   - `delivery_delay`
   - `wait_time`
   - `is_late` (flag)
   - `review_score_bucket`

3. **Export Output**  
   Cleaned dataset is saved to `outputs/final_orders_clean.csv`.

## 🛠️ Technologies Used

- Python 3.12
- Pandas
- Modular Python structure
- Git for version control

## ✅ Output

This ETL pipeline prepares a ready-to-analyze dataset that helps Trendify:
- Identify late deliveries
- Correlate delivery time with reviews
- Flag sellers with poor performance

---

## 📌 Author

Maryam – Capstone Project for Data Consulting

# trendify-capstone
07311b17a6d48223c48b0bfa2f447bd5cb9fe1a6
