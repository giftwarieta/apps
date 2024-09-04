import streamlit as st
import streamlit_authenticator as stauth

# Hashed passwords (you can use stauth.Hasher to hash your passwords)
hashed_passwords = stauth.Hasher(['password123', 'password456']).generate()

# User data with hashed passwords
users = {
    'user1@example.com': {'name': 'User One', 'password': hashed_passwords[0]},
    'user2@example.com': {'name': 'User Two', 'password': hashed_passwords[1]},
}

# Initialize the authenticator
authenticator = stauth.Authenticate(
    users=users,
    cookie_name='app_home',    # Unique name for your app's cookie
    key='abcdef',              # A random key to secure the cookie
    cookie_expiry_days=1       # Set cookie expiration (e.g., 1 day)
)

# Proceed with the login process
name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status:
    st.sidebar.success(f"Welcome, {name}!")
    # Your app's main content goes here
elif authentication_status == False:
    st.error("Username or password is incorrect")
elif authentication_status == None:
    st.warning("Please enter your username and password")
