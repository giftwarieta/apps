import streamlit as st
import pandas as pd
import pyotp
import hashlib

# Function to hash the password
def hash_password(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

# Function to verify the OTP
def verify_otp(secret, user_otp):
    totp = pyotp.TOTP(secret)
    return totp.verify(user_otp)

# Dummy user data (replace with your own user credentials)
users = {
    'user1@example.com': {'name': 'User One', 'password': hash_password('password123')},
    'user2@example.com': {'name': 'User Two', 'password': hash_password('password456')}
}

# Function to send OTP via email (implement using your email service)
def send_otp(email, otp):
    st.info(f"OTP {otp} has been sent to {email} (Simulated)")

# Set session states for login and OTP
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'otp_verified' not in st.session_state:
    st.session_state['otp_verified'] = False

# Login form
if not st.session_state['logged_in']:
    st.title('Login')

    username = st.text_input('Email')
    password = st.text_input('Password', type='password')

    if st.button('Login'):
        if username in users and users[username]['password'] == hash_password(password):
            st.session_state['logged_in'] = True
            st.success(f"Welcome {users[username]['name']}!")
        else:
            st.error("Invalid username or password")

# OTP Verification
if st.session_state['logged_in'] and not st.session_state['otp_verified']:
    st.title("
