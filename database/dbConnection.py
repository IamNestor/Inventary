import pyodbc

# database/db_connection.py
import pyodbc

def get_db_connection():
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=DESKTOP-B92HF7K;" 
        "DATABASE=Inventary;" 
        "Trusted_Connection=yes;"  
    )
    return conn
