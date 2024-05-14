from sqlalchemy import create_engine
import os
import pandas as pd
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

db_connection_string = os.environ['DB_CONNECTION_STRING']

try:
    engine = create_engine(db_connection_string,
                           connect_args={"ssl": {
                               "ssl_ca": "/etc/ssl/cert.pem"
                           }})
except Exception as e:
    logging.error(f"Failed to create database engine: {e}")
    raise

def load_data_from_db():
    try:
        with engine.connect() as conn:
            # Load Xy_withASR data into a pandas DataFrame
            result = conn.execute("SELECT * FROM Xy_withASR")
            Xy_withASR_df = pd.DataFrame(result.fetchall(), columns=result.keys())
            return Xy_withASR_df
    except Exception as e:
        logging.error(f"Error loading data from database: {e}")
        raise
