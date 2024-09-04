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

