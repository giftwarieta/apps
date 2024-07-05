pip install -r requirements.txt


import plotly.express as px
import streamlit as st
import pandas as pd
import numpy as np
import time
import streamlit.components.v1 as stc

#st.logo('https://raw.githubusercontent.com/giftwarieta/Python/main/assets/GiftWarieta_Logo.png', link="https://raw.githubusercontent.com/giftwarieta/Python/main/assets/GiftWarieta_Logo.png", icon_image=LOGO_URL_SMALL)

st.set_page_config(
    page_title="Uber pickups in NYC :: Developed by Warieta Gift Ejovwoke",
    page_icon="🚘",
)

st.title('Uber pickups in NYC 🚘')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

st.sidebar.success("Welcome!")
st.sidebar.warning("Testing app")
#st.sidebar.information("This is a practice app")
st.sidebar.error("Error not found!")

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Done!")

with st.expander("Data View"):
    st.dataframe(data)
    
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Number of pickups by hour')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

# Some number in the range 0-23
# adding filter slider
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.map(filtered_data)

#Population Map Configuration


def load_data():
   return pd.read_csv("data/worldcities.csv")

world = load_data()

unique_country = sorted(world['country'].unique())
st.write(unique_country)
selected_country = st.selectbox('Select a Country', unique_country)
#selected_country = st.selectbox('Select a Country', ['Nigeria','Ghana'])
selected_data = world[world['country'] == selected_country].sort_values("country")

st.subheader('Data for ' + selected_country)

st.dataframe(selected_data)
#st.map(selected_country)

## Practice Scripts

RESULT_TEMP = """
<div style="width:90%;height:100%;margin:1px;padding:5px;position:relative;border-radius:5px;border-bottom-right-radius: 60px;
box-shadow:0 0 15px 5px #ccc; background-color: #a8f0c6;
  border-left: 5px solid #6c6c6c;">
<h4>{}</h4>
<p style="color:blue;"><span style="color:black;">📈Score::</span>{}</p>
<p style="color:blue;"><span style="color:black;">🔗</span><a href="{}",target="_blank">Link</a></p>
<p style="color:blue;"><span style="color:black;">💲Price:</span>{}</p>
<p style="color:blue;"><span style="color:black;">🧑‍🎓👨🏽‍🎓 Students:</span>{}</p>

</div>
"""
stc.html(RESULT_TEMP,height=350)

st.metric(label="Temperature", value="70 °F", delta="1.2 °F")



pricing_data, other_data, news = st.tabs(["Pricing Data", "Other Data", "Top 10 News"])

with pricing_data:
    st.header("My data")
    st.write(data)
with other_data:
    a = 5
    b = 8
    c = a-b
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Temperature", "70 °F", "1.2 °F")
    col2.metric("Wind", "9 mph", "-8%")
    col3.metric("Humidity", "86%", "4%")
    col4.metric("Revenue", "N35.2b", f"{c}%")
with news:
    st.markdown("This website is developed and maintained by Warieta Gift Ejovwoke")
    
