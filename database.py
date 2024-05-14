from sqlalchemy import create_engine
import os
import pandas as pd
import logging

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                           "ssl_ca": "/etc/ssl/cert.pem"
                       }})

def load_data_from_db():
  with engine.connect() as conn:
    # Load Xy_withASR data into a pandas DataFrame
    result = conn.execute("SELECT * FROM Xy_withASR")
    Xy_withASR_df = pd.DataFrame(result.fetchall(), columns=result.keys())

  return Xy_withASR_df
