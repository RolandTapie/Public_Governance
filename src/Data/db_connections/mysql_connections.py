import mysql.connector
import pandas as pd
from sqlalchemy import create_engine

def sql_connection(table):
    config = {
        "database": "Monitoring",
        "user": "root",
        "password": "mysql",
        "host": "localhost",
        "port": 3306
    }

    # Créer l'URL de connexion
    url = (f"mysql+mysqlconnector://{config['user']}:{config['password']}"
           f"@{config['host']}:{config['port']}/{table}")

    # Créer l'engine SQLAlchemy
    engine = create_engine(url)
    return engine

#conn = sql_connection("monitoring")
# df = pd.read_sql("SELECT * FROM events", con=conn)
# print(df)
#
# conn = sql_connection("treasury_catalogs")
# df = pd.read_sql("SELECT * FROM data_catalog", con=conn)
# print(df)