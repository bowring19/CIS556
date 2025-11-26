import os
import psycopg2
import pandas as pd
from sqlalchemy import create_engine


DB_CONFIG = {
    'USER': 'postgres',
    'PASSWORD': 'GkQkXJPvPoHlzNtnZLOnAcbvbRVmHxAw',  
    'HOST': 'caboose.proxy.rlwy.net',
    'PORT': '19372',
    'DBNAME': 'railway'
}

DATABASE_URL = (
    f"postgresql://{DB_CONFIG['USER']}:{DB_CONFIG['PASSWORD']}"
    f"@{DB_CONFIG['HOST']}:{DB_CONFIG['PORT']}/{DB_CONFIG['DBNAME']}"
)


engine = create_engine(DATABASE_URL)
print("Connected PostgreSQL successfully!")


DATA_DIR = "f1_data_postgres_ready"  

for file in sorted(os.listdir(DATA_DIR)):
    if file.endswith(".csv"):
        table_name = file.replace(".csv", "").lower()

        print(f"\nLoading table: {table_name}")

        df = pd.read_csv(f"{DATA_DIR}/{file}")
        df.to_sql(table_name, engine, if_exists='replace', index=False)

        print(f"Loaded {len(df)} rows into {table_name}")

print("\nALL TABLES SUCCESSFULLY LOADED INTO POSTGRESQL DATABASE!")
