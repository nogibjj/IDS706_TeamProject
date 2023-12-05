import pandas as pd
import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        port=3306,
    )


def save_data(connection, row):
    cursor = connection.cursor()
    MMSA, total_percent, *rest = row
    # original code
    # total_percent = float(total_percent.strip('%'))
    # / 100 if '%' in total_percent else None
    total_percent = total_percent.strip("%") if "%" in total_percent else None
    total_percent = float(total_percent) / 100 if total_percent is not None else None

    values = [MMSA, total_percent] + [None if r == "NA" else r for r in rest]
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
