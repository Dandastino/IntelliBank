import psycopg2
from psycopg2 import OperationalError


def save_transaction(user_id, description, quantities):
    try:
        # Attempt to establish connection
        conn = psycopg2.connect(dbname="intellibank",user="postgres",password="password",host="localhost")

        cur = conn.cursor()
        #print("Successfully connected to database")

    except OperationalError as e:
        print("Failed to connect to database:", e)
    finally:
        if 'conn' in locals():
            cur.close()
            conn.close()
