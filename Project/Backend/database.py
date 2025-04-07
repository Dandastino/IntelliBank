import os
import psycopg2
from psycopg2 import OperationalError
from dotenv import load_dotenv

load_dotenv()


def save_transaction():
    try:
        conn = psycopg2.connect(
            dbname=os.getenv('POSTGRES_DB'),
            user=os.getenv('POSTGRES_USER'),
            password=os.getenv('POSTGRES_PASSWORD'),
            host=os.getenv('POSTGRES_HOST')
        )

        cur = conn.cursor()
        print("Connected to database")
        print(os.getenv('POSTGRES_HOST'))


    except OperationalError as e:
        print("Database connection failed:", e)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if 'conn' in locals():
            cur.close()
            conn.close()
            print("Connection closed.")


save_transaction()
