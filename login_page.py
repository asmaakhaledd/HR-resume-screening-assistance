# import os
# import streamlit as st
# import sqlite3
# import pickle
# import redis


# redis_url = os.environ.get("REDIS_URL", "redis://localhost:6379")
# redis_client = redis.StrictRedis.from_url(redis_url)

# LOGIN_KEY = "login_data"

# def login_page(redis_client):
#     st.title("Login")

#     username = st.text_input("Username:")
#     password = st.text_input("Password:", type="password")

#     if st.button("Login"):
#         if username and password:
#             login_data = f"Username: {username}, Password: {password}"
#             redis_client.set(LOGIN_KEY, login_data)

#             st.success("Login successful! You can now access the PDF viewer.")
#             return True
#         else:
#             st.error("Invalid credentials. Please try again.")
#     return False


# if __name__ == '__main__':
#     login_page()
#     # login_status = login_page()
#     # st.write("Login Status:", login_status)