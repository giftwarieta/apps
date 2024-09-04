import streamlit as st
import pandas as pd
import pyotp
import plotly.express as px
import streamlit_authenticator as stauth
from datetime import datetime

# Function to send OTP via email (you need to implement this using an email service API)
def send_otp(email, otp):
    # Send the OTP to the user's email (implementation depends on the service you use)
    pass

# Dummy user data (replace with your own users and hashed passwords)
users = {
    'user1@example.com': {'name': 'User One', 'password': stauth.Hasher(['password123']).generate()},
    'user2@example.com': {'name': 'User Two', 'password': stauth.Hasher(['password456']).generate()}
}

# Streamlit Authenticator
authenticator = stauth.Authenticate(users, 'app', 'abcdef', cookie_expiry_days=1)

# Handle user login
name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status:
    st.sidebar.title(f"Welcome {name}")

    # OTP Verification (if required)
    if 'otp_verified' not in st.session_state:
        st.session_state['otp_verified'] = False

    if not st.session_state['otp_verified']:
        user_email = username
        totp = pyotp.TOTP('base32secret3232')  # Generate OTP (use your own secret)
        otp = totp.now()
        send_otp(user_email, otp)  # Implement email sending

        st.write('An OTP has been sent to your registered email.')

        user_otp = st.text_input('Enter the OTP', type="password")
        if user_otp == otp:
            st.session_state['otp_verified'] = True
            st.success('OTP Verified')
        else:
            st.error('Invalid OTP. Please try again.')

    # If OTP is verified, allow file upload and data analysis
    if st.session_state['otp_verified']:
        uploaded_file = st.sidebar.file_uploader("Upload your income and expense file", type="xlsx")

        if uploaded_file:
            df = pd.read_excel(uploaded_file)
            st.write("### Data Preview")
            st.dataframe(df.head())

            # Perform analysis
            st.write("### Analysis")
            total_income = df[df['Type'] == 'Income']['Amount'].sum()
            total_expense = df[df['Type'] == 'Expense']['Amount'].sum()

            st.write(f"Total Income: ${total_income}")
            st.write(f"Total Expense: ${total_expense}")

            # Visualize the data
            fig = px.pie(df, values='Amount', names='Type', title='Income vs Expense')
            st.plotly_chart(fig)

            # Simple forecasting (e.g., predicting next month's expenses)
            st.write("### Forecasting")
            forecast_expense = total_expense * 1.05  # Assume a 5% increase for next month
            st.write(f"Expected Expense Next Month: ${forecast_expense}")

    # Option to logout
    if st.sidebar.button('Logout'):
        authenticator.logout('Logout', 'sidebar')

elif authentication_status == False:
    st.error('Username or password is incorrect')

elif authentication_status == None:
    st.warning('Please enter your username and password')
