import pandas as pd
import MySQLdb
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_connection():
    """Returns a connection to the database"""
    connection = MySQLdb.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        passwd=os.getenv("DB_PASSWORD"),
        db=os.getenv("DB_NAME"),
        port=int(os.getenv("DB_PORT"))  # Assuming port is an integer
    )
    return connection

def save_data(connection, MMSA, total_percent_at_risk, high_risk_per_icu_bed, high_risk_per_hospital, icu_beds, hospitals, total_at_risk):
    cursor = connection.cursor()
    query = (
        "INSERT INTO icu_beds VALUES ('"
        + MMSA
        + "',"
        + str(total_percent_at_risk)
        + ","
        + str(high_risk_per_icu_bed)
        + ","
        + str(high_risk_per_hospital)
        + ","
        + str(icu_beds)
        + ","
        + str(hospitals)
        + ","
        + str(total_at_risk)
        + ");"
    )
    cursor.execute(query)
    connection.commit()

def save_all_data():
    """Saves the csv data to the database"""
    df = pd.read_csv("./mmsa-icu-beds.csv", encoding="utf-8")
    connection = get_connection()
    for index, row in df.iterrows():
        try:
            save_data(
                connection,
                row["MMSA"],
                row["total_percent_at_risk"],
                row["high_risk_per_icu_bed"],
                row["high_risk_per_hospital"],
                row["icu_beds"],
                row["hospitals"],
                row["total_at_risk"],
            )
        except Exception as e:
            print(e)
            continue

    connection.close()

if __name__ == "__main__":
    save_all_data()
