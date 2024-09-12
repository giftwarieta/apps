# import required python libraries/modules


import streamlit as st
import pandas as pd
import mysql.connector
import os
from pathlib import Path
from dotenv import load_dotenv

# configuring time
from datetime import datetime
from datetime import date
from datetime import timedelta

today = date.today()
thisday = today.strftime('%A, %B %d %Y')

print('This script ran today, ' + thisday)


env_path = Path.cwd() / '.evn'

current_dir = Path(_file_).resolve().parent if "_file_" in locals() else Path.cwd()
envars = current_dir / ".env"
load_dotenv(envars)
load_dotenv(dotenv_path = env_path)


db = mysql.connector.connect(
        host = os.environ['host'],
        user = os.environ['user'],
        password = os.environ['password'],
        database = os.environ['database']
)

cursor = db.cursor()


#cursor.execute("show databases")


#for x in cursor:
#	print(x)

data = cursor.execute("Select * from users")

#print(cursor.fetchall())

print(cursor.fetchone())


st.title('I am doing great')

#df = pd.DataFrame(data, columns=cursor.column_names)

#st.write(df)
