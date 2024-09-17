"""
Created on Wed Sep 11 14:22:27 2024

@author: giftwarieta
"""

import streamlit as st
import pandas as pd
import mysql.connector
import os
from pathlib import Path

# configuring time
from datetime import datetime
from datetime import date
from datetime import timedelta

today = date.today()
thisday = today.strftime('%A, %B %d %Y')

st.write('This script ran today, ' + thisday)

host = secrets.HOST

st.write(host)
