import pandas as pd
from sqlalchemy import create_engine
import pymysql

df = pd.read_csv("The Telco Churn.csv")
con = create_engine("mysql+pymysql://root:1234@localhost:3306/telco_churn")

df.to_sql('telco', con, if_exists='append', index=False)