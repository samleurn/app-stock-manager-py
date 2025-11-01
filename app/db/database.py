import os
from dotenv import load_dotenv
import psycopg2

load_dotenv('config/.env')


class Query:
    def __init__(self, query):
        self._query = query
        self.connect()

    def connect(self):
        try:

            db_name = os.getenv('DB_NAME')
            db_user = os.getenv('DB_USER')
            db_pass = os.getenv('DB_PASS')
            db_host = os.getenv('DB_HOST')
            db_port = os.getenv('DB_PORT')

            conn = psycopg2.connect(
                dbname=db_name, user=db_user, password=db_pass, host=db_host, port=db_port or "5432")
            
            self._conn = conn
            self._cur = conn.cursor()

            print("Database connected successfully")

        except Exception as e:
            print(f"Error connecting to database: {e}")
            raise

    def query(self):
        try:
            query = self._query
            self._cur.execute(query)
            data = self._cur.fetchall()
            return data
        except Exception as e:
            print(f"Error executing query: {e}")
        finally:
            self.close()

    def close(self):
        self._cur.close()
        self._conn.close()
        print("Closing database connection")
