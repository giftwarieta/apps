import streamlit as st
import pandas as pd
import pyotp
import plotly.express as px
import streamlit_authenticator as stauth
import geocoder
from datetime import datetime

# Function to send OTP via email (use your preferred email service API)
def send_otp(email, otp):
    # Send the OTP to the user's email
    pass

# Set up user authentication
users = {'user@example.com': {'name': 'User Name', 'password': 'hashed_password'}}
authenticator = stauth.Authenticate(users, 'app', 'auth', cookie_expiry_days=1)

name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status:
    st.sidebar.title(f"Welcome {name}")

    # Upload income and expense file
    uploaded_file = st.sidebar.file_uploader("Upload your income and expense file", type="xlsx")

    if uploaded_file:
        df = pd.read_excel(uploaded_file)
        st.write("### Data Preview")
        st.dataframe(df.head())

        # Analyze the data
        st.write("### Analysis")
        # Example analysis: total income and expense
        total_income = df[df['Type'] == 'Income']['Amount'].sum()
        total_expense = df[df['Type'] == 'Expense']['Amount'].sum()

        st.write(f"Total Income: ${total_income}")
        st.write(f"Total Expense: ${total_expense}")

        # Example visualization: income vs. expense
        fig = px.pie(df, values='Amount', names='Type', title='Income vs Expense')
        st.plotly_chart(fig)

        # Forecasting (simplified example)
        st.write("### Forecasting")
        forecast_expense = total_expense * 1.05  # Assuming a 5% increase next month
        st.write(f"Expected Expense Next Month: ${forecast_expense}")

    # Track user data
    st.write("### User Data")
    location = geocoder.ip('me')
    st.write(f"Location: {location.city}, {location.country}")
    st.write(f"Date & Time: {datetime.now()}")

    # Logout option
    if st.sidebar.button('Logout'):
        authenticator.logout('Logout', 'sidebar')

elif authentication_status == False:
    st.error('Username or password is incorrect')

elif authentication_status == None:
    st.warning('Please enter your username and password')

# Handle OTP generation and verification
if 'otp_verified' not in st.session_state:
    st.session_state['otp_verified'] = False

if not st.session_state['otp_verified']:
    user_email = st.text_input('Enter your email to receive OTP')
    if user_email:
        totp = pyotp.TOTP('base32secret3232')
        otp = totp.now()
        send_otp(user_email, otp)
        st.write('OTP sent to your email')

        user_otp = st.text_input('Enter the OTP')
        if user_otp == otp:
            st.session_state['otp_verified'] = True
            st.success('OTP Verified')
        else:
            st.error('Invalid OTP')
