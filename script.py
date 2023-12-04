import pandas as pd
import MySQLdb
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_connection():
    return MySQLdb.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        passwd=os.getenv("DB_PASSWORD"),
        db=os.getenv("DB_NAME"),
        port=int(os.getenv("DB_PORT"))
    )

def save_data(connection, row):
    cursor = connection.cursor()
    MMSA, total_percent, *rest = row
    total_percent = float(total_percent.strip('%')) / 100 if '%' in total_percent else None
    values = [MMSA, total_percent] + [None if r == 'NA' else r for r in rest]
    query = "INSERT INTO icu_beds VALUES (%s, %s, %s, %s, %s, %s, %s);"
    cursor.execute(query, values)
    connection.commit()

def save_all_data():
    df = pd.read_csv("./mmsa-icu-beds.csv", encoding="utf-8")
    connection = get_connection()
    for index, row in df.iterrows():
        try:
            save_data(connection, row)
        except Exception as e:
            print(e)
            continue
    connection.close()

if __name__ == "__main__":
    save_all_data()
