import streamlit as st
import streamlit_authenticator as sa
import os
import yaml
from yaml.loader import SafeLoader
import hashlib
import database as db


# Setting the page title and icon
icon = "https://thumbs.dreamstime.com/b/growing-up-trend-stem-chart-trading-vector-design-illustration-template-160606828.jpg"
st.set_page_config(page_title='Stockly', page_icon=icon)

#Hiding the hamburger menu and streamlit footer
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

#user authentication
user = db.fetch_all_users()

authenticator = sa.Authenticate(user)
name, authenticator, username = authenticator.login("Login", "sidebar")

if authenticator == None:
    st.warning("Please login to continue")

elif authenticator == False:
    st.error("Invalid username or password")

else:
    st.success(f"Logged in as {name}")


    #st.sidebar.title(f"Welcome {name}!")
    st.sidebar.header('Navigation')
    # authenticator.logout("Logout", "sidebar")


    page = st.sidebar.radio("Go to:",
                            ('Home',
                            'Predictions',
                            'Company Charts'))

    if page == 'Home':
        from home import run
        run()

    elif page == 'Predictions':
        from predictions import run
        run()

    else:
        from company_charts import run
        run()
