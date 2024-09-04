import streamlit as st
import pandas as pd
import pyotp
import hashlib
import openpyxl
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
# Function to hash the password
def hash_password(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

# Function to send OTP via email (implement using your email service)
def send_otp(email, otp):
    st.info(f"OTP {otp} has been sent to {email} (Simulated)")  # Replace with actual email-sending code

# Dummy user data (replace with your own user credentials)
users = {
    'user1@example.com': {'name': 'User One', 'password': hash_password('password123')},
    'user2@example.com': {'name': 'User Two', 'password': hash_password('password456')}
}

# Set session states for login, OTP, and username
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'otp_verified' not in st.session_state:
    st.session_state['otp_verified'] = False
if 'username' not in st.session_state:
    st.session_state['username'] = None
if 'otp' not in st.session_state:
    st.session_state['otp'] = None

# Login form
if not st.session_state['logged_in']:
    st.title('Login')

    username = st.text_input('Email')
    password = st.text_input('Password', type='password')

    if st.button('Login'):
        if username in users and users[username]['password'] == hash_password(password):
            st.session_state['logged_in'] = True
            st.session_state['username'] = username  # Store username in session state
            st.success(f"Welcome {users[username]['name']}!")
        else:
            st.error("Invalid username or password")

# OTP Verification
if st.session_state['logged_in'] and not st.session_state['otp_verified']:
    st.title("OTP Verification")

    # Generate OTP once and store in session state if not already generated
    if st.session_state['otp'] is None:
        secret = pyotp.random_base32()  # In production, use a fixed secret for each user
        totp = pyotp.TOTP(secret)
        otp = totp.now()
        st.session_state['otp'] = otp  # Store the OTP in session state
        send_otp(st.session_state['username'], otp)  # Simulate sending OTP

    user_otp = st.text_input('Enter the OTP', type='password')

    if st.button('Verify OTP'):
        # Verify the OTP against the stored OTP
        if user_otp == st.session_state['otp']:
            st.session_state['otp_verified'] = True
            st.success('OTP Verified')
        else:
            st.error('Invalid OTP. Please try again.')

# Main app functionality
if st.session_state['logged_in'] and st.session_state['otp_verified']:
    st.sidebar.title(f"Welcome, {users[st.session_state['username']]['name']}")

    # File upload
    uploaded_file = st.sidebar.file_uploader("Upload your income and expense file", type="xlsx")

    if uploaded_file:
        df = pd.read_excel(uploaded_file)
        st.write("### Data Preview")
        st.dataframe(df.head())

        # Analyze the data
        st.write("### Analysis")
        total_income = df[df['Type'] == 'Income']['Amount'].sum()
        total_expense = df[df['Type'] == 'Expense']['Amount'].sum()

        st.write(f"Total Income: ${total_income}")
        st.write(f"Total Expense: ${total_expense}")

        # Visualization: Income vs. Expense
        st.write("### Visualization")
        st.bar_chart(df.groupby('Type')['Amount'].sum())

        # Simple forecasting
        st.write("### Forecasting")
        forecast_expense = total_expense * 1.05  # Assume 5% increase next month
        st.write(f"Expected Expense Next Month: ${forecast_expense}")

# Logout option
if st.sidebar.button('Logout'):
    st.session_state['logged_in'] = False
    st.session_state['otp_verified'] = False
    st.session_state['username'] = None
    st.session_state['otp'] = None  # Clear OTP
    st.success("Logged out successfully!")
