import streamlit as st
import pandas as pd
import numpy as np

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
st.sidebar.title("Web app developed by Warieta Gift Ejovwoke")

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Done! (using st.cache_data)")

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

## Practice Scripts

st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
