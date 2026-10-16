# 🛒 E-Commerce Sales & Pricing Analysis (End-to-End Data Pipeline)

An end-to-end data engineering and analytics project analyzing Amazon product listings, discount structures, and customer ratings to extract actionable business insights regarding product pricing and customer engagement.

---

## 📌 Business Problem
In competitive e-commerce marketplaces like Amazon, understanding how pricing strategies, discount percentages, and product categories impact customer ratings and review volumes is critical for inventory and promotional planning. This project establishes an automated pipeline to clean raw transactional data, normalize pricing metrics, and perform exploratory data analysis (EDA) to identify top-performing product segments and high-engagement pricing tiers.

---

## 🛠️ Tech Stack & Architecture
* **Database & Data Cleansing:** PostgreSQL (SQL Views, String Sanitization, Data Type Casts)
* **Pipeline & Analysis:** Python (`pandas`, `SQLAlchemy`, `psycopg2`)
* **Environment Management:** PyCharm IDE, Python Virtual Environments (`venv`)
* **Version Control:** Git & GitHub

---

## 🔄 Data Pipeline Workflow
1. **Ingestion & Storage:** Raw e-commerce CSV data is ingested into a PostgreSQL relational database.
2. **Cleansing & Normalization:** Built a dedicated SQL view (`v_amazon_sales_cleaned`) to handle currency symbol stripping, percentage string parsing, numeric type casting, and handling nulls.
3. **Extraction & EDA:** A Python script connects securely to the PostgreSQL database using SQLAlchemy, queries the clean SQL view into a Pandas DataFrame, and executes exploratory data analysis (EDA) including summary statistics and business aggregations.

---

## 📂 Project Structure
```text
📦 amazon-sales-python-analytics
│
├── 📜 analyze_amazon.py           # Database connection & data extraction script
├── 📜 eda_analysis.py             # Exploratory Data Analysis (Pandas aggregations & stats)
├── 📜 README.md                   # Project documentation
└── 📜 .gitignore                  # Excludes local virtual environments and caches