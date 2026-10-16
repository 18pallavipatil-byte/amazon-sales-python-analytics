import urllib.parse
import pandas as pd
from sqlalchemy import create_engine

# 1. Define your database connection credentials
db_user = 'postgres'
db_password = 'Dats@123'
db_host = 'localhost'
db_port = '5432'
db_name = 'amazon_sales_db'

# 2. Build the connection string safely (handles special characters like '@')
encoded_password = urllib.parse.quote_plus(db_password)
connection_string = f"postgresql+psycopg2://{db_user}:{encoded_password}@{db_host}:{db_port}/{db_name}"

# 3. Create the SQLAlchemy engine
engine = create_engine(connection_string)

# 4. Pull your cleaned SQL view directly into a Pandas DataFrame
query = 'SELECT * FROM v_amazon_sales_cleaned;'
df = pd.read_sql(query, con=engine)

# 5. Verify the data loaded successfully
print('Successfully loaded Amazon data into Pandas!')
print(f'Total Rows and Columns: {df.shape}')
print('\nFirst 5 rows of your DataFrame:')
print(df.head())