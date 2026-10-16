import urllib.parse
import pandas as pd
from sqlalchemy import create_engine

# 1. Connect to the database and load data
db_user = 'postgres'
db_password = 'Dats@123'
db_host = 'localhost'
db_port = '5432'
db_name = 'amazon_sales_db'

encoded_password = urllib.parse.quote_plus(db_password)
connection_string = f"postgresql+psycopg2://{db_user}:{encoded_password}@{db_host}:{db_port}/{db_name}"

engine = create_engine(connection_string)
query = "SELECT * FROM v_amazon_sales_cleaned;"
df = pd.read_sql(query, con=engine)

print("=" * 50)
print(" 🚀 AMAZON SALES DATASET - EXPLORATORY DATA ANALYSIS")
print("=" * 50)

# 2. Inspect basic structure and missing values
print("\n[1] DATASET STRUCTURE & NULL CHECK:")
print(f"Total Rows: {df.shape[0]}, Total Columns: {df.shape[1]}")
print("\nMissing values per column:")
print(df.isnull().sum())

# 3. View data types
print("\n[2] COLUMN DATA TYPES:")
print(df.dtypes)

# 4. Summary statistics for numerical columns
print("\n[3] NUMERICAL SUMMARY STATISTICS:")
print(df.describe())

# 5. Quick Business Aggregations (Top 5 Products by Review Count or Rating if applicable)
if 'product_name' in df.columns and 'rating' in df.columns:
  print("\n[4] TOP 5 HIGHEST RATED PRODUCTS (Sample):")
  top_products = (
      df[['product_name', 'rating', 'rating_count']]
      .drop_duplicates()
      .head(5)
  )
  print(top_products.to_string(index=False))

print("\n" + "=" * 50)
print(" ✅ EDA Script Completed Successfully!")
print("=" * 50)