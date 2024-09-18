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

host = 'gewideas.com.ng'

st.write(host)

data_df = pd.DataFrame(
    {
        "apps": [
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/5435b8cb-6c6c-490b-9608-799b543655d3/Home_Page.png",
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/ef9a7627-13f2-47e5-8f65-3f69bb38a5c2/Home_Page.png",
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/31b99099-8eae-4ff8-aa89-042895ed3843/Home_Page.png",
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/6a399b09-241e-4ae7-a31f-7640dc1d181e/Home_Page.png",
        ],
    }
)

st.data_editor(
    data_df,
    column_config={
        "apps": st.column_config.ImageColumn(
            "Preview Image", help="Streamlit app preview screenshots"
        )
    },
    hide_index=True,
)

title = st.text_input("Movie title", "Life of Brian")
st.write("The current movie title is", title)

if title = 'Yes':
    st.markdown(
    """
    <svg height="100" width="100">
      <circle cx="50" cy="50" r="40" stroke="black" stroke-width="3" fill="red" />
    </svg>"""
    , unsafe_allow_html=True)
    
