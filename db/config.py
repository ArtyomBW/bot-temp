
from psycopg2 import connect

class DBConfig:
    DB_NAME = 'films_db'
    DB_USER = 'films_db'
    DB_HOST = 'localhost'
    DB_PORT = 5432
    DB_PASSWORD = 1
    connect = connect(
            dbname= DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT )
    cur = connect.cursor()



