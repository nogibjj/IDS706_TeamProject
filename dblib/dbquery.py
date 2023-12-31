"""Database query lib"""
import json
# import MySQLdb
import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class DB:
    """DB utility class to connect and query ICU data"""
    def __init__(self):
        self.connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),        # Use environment variable
            user=os.getenv("DB_USER"),        # Use environment variable
            passwd=os.getenv("DB_PASSWORD"),  # Use environment variable
            db=os.getenv("DB_NAME"),          # Use environment variable
            port=3306,    # Use environment variable (if needed)
        )
        self.cursor = self.connection.cursor()

    # def get_icu_info(self, MMSA):
    #     """Return ICU-related info for a specified MMSA"""
    #     print(MMSA)
    #     query = f'SELECT * FROM icu_beds WHERE MMSA = "{MMSA}"'
    #     self.cursor.execute(query)
    #     data = self.cursor.fetchall()

    #     result = [dict(zip(['MMSA', 'total_percent_at_risk', 'high_risk_per_icu_bed', 'high_risk_per_hospital', 'icu_beds', 'hospitals', 'total_at_risk'], row)) for row in data]
    #     return json.dumps(result)

    def get_icu_info(self, MMSA):
        """Return ICU-related info for a specified MMSA"""
        query = f'SELECT MMSA, icu_beds, hospitals FROM icu_beds WHERE MMSA = "{MMSA}"'
        self.cursor.execute(query)
        data = self.cursor.fetchall()

        result = [{'MMSA': row[0], 'count_icu_beds':row[1] ,'count_hospitals': row[2],} for row in data]
        return json.dumps(result)


    def get_hospitals_info(self):
        """Return summary info about hospitals"""
        query = 'SELECT hospitals, COUNT(*) FROM icu_beds GROUP BY hospitals'
        self.cursor.execute(query)
        data = self.cursor.fetchall()

        result = [{'hospitals': row[0], 'count': row[1]} for row in data]
        return json.dumps(result)

