import streamlit as st
import pandas as pd
import pyotp
import hashlib
import openpyxl
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
from datetime import datetime, date


#######################################################


# configuring time
from datetime import datetime
from datetime import date
from datetime import timedelta

today = date.today()
thisday = today.strftime('%A, %B %d %Y')

print('This script ran today, ' + thisday)




################################################




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
        
        # Ensure correct columns exist
        required_columns = {'Date', 'Category', 'Payment Method', 'Amount', 'Type'}
        if not required_columns.issubset(df.columns):
            st.error("Uploaded file must contain the columns: Date, Category, Payment Method, Amount, Type")
        else:
            st.write("### Data Preview")
            st.dataframe(df.head())
            
            # Convert Date column to datetime
            df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
            
            # Check for any NaT values in Date column
            if df['Date'].isna().any():
                st.error("Date column contains invalid dates.")
            else:
                # Filters
                st.sidebar.header("Filters")

                categories = df['Category'].unique().tolist()
                selected_categories = st.sidebar.multiselect('Select Categories', categories, default=categories)

                payment_methods = df['Payment Method'].unique().tolist()
                selected_payment_methods = st.sidebar.multiselect('Select Payment Methods', payment_methods, default=payment_methods)

                min_date = df['Date'].min().date()
                max_date = df['Date'].max().date()
                selected_date_range = st.sidebar.date_input('Select Date Range', [min_date, max_date])

                # Convert selected_date_range to datetime.date objects
                start_date, end_date = selected_date_range

                # Apply filters
                filtered_df = df[
                    (df['Category'].isin(selected_categories)) &
                    (df['Payment Method'].isin(selected_payment_methods)) &
                    (df['Date'] >= pd.Timestamp(start_date)) &
                    (df['Date'] <= pd.Timestamp(end_date))
                ]
                
                # Summary Cards
                st.write("### Summary")
                total_income = filtered_df[filtered_df['Type'] == 'Income']['Amount'].sum()
                total_expense = filtered_df[filtered_df['Type'] == 'Expense']['Amount'].sum()
                net_balance = total_income - total_expense
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Total Income", f"${total_income:,.2f}")
                with col2:
                    st.metric("Total Expense", f"${total_expense:,.2f}")
                with col3:
                    st.metric("Net Balance", f"${net_balance:,.2f}")
                
                # Donut Chart: Income vs Expense
                st.write("### Donut Chart: Income vs Expense")
                fig, ax = plt.subplots()
                sizes = [total_income, total_expense]
                labels = ['Income', 'Expense']
                ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, wedgeprops=dict(width=0.4))
                st.pyplot(fig)
                
                # Bar Chart: Total Amount by Category
                st.write("### Bar Chart: Total Amount by Category")
                category_totals = filtered_df.groupby('Category')['Amount'].sum().reset_index()
                fig, ax = plt.subplots()
                sns.barplot(data=category_totals, x='Category', y='Amount', ax=ax)
                ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
                st.pyplot(fig)
                
                # Line Chart: Income vs Expense Trend
                st.write("### Line Chart: Income vs Expense Trend")
                trend_data = filtered_df.groupby(['Date', 'Type'])['Amount'].sum().reset_index()
                fig, ax = plt.subplots()
                sns.lineplot(data=trend_data, x='Date', y='Amount', hue='Type', ax=ax)
                st.pyplot(fig)
                
                # Donut Chart: Payment Method Distribution
                st.write("### Donut Chart: Payment Method Distribution")
                payment_method_totals = filtered_df.groupby('Payment Method')['Amount'].sum().reset_index()
                fig, ax = plt.subplots()
                sizes = payment_method_totals['Amount']
                labels = payment_method_totals['Payment Method']
                ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, wedgeprops=dict(width=0.4))
                st.pyplot(fig)

# Logout option
if st.sidebar.button('Logout'):
    st.session_state['logged_in'] = False
    st.session_state['otp_verified'] = False
    st.session_state['username'] = None
    st.session_state['otp'] = None  # Clear OTP
    st.success("Logged out successfully!")
