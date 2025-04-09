import os
import psycopg2
from psycopg2 import OperationalError
from dotenv import load_dotenv

#sudo systemctl stop postgresql
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

        # Query per ottenere le tabelle
        cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
        tables = cur.fetchall()

        if tables:
            print("Tables in the database:")
            for table in tables:
                print(table)
        else:
            print("No tables found in the database.")

        # Se ci sono tabelle, eseguiamo la query per ottenere tutte le righe della tabella AppUser
        if tables:
            try:
                cur.execute("SELECT * FROM AppUser;")
                rows = cur.fetchall()
                if rows:
                    print("Rows in the AppUser table:")
                    for row in rows:
                        print(row)
                else:
                    print("No rows found in the AppUser table.")
            except Exception as e:
                print(f"Error fetching data from AppUser table: {e}")
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
