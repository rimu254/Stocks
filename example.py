import yfinance as yf
import pandas as pd
import streamlit as st
import streamlit_authenticator as stauth
from pathlib import Path
import pickle
import yaml
from streamlit_authenticator import Authenticate

#https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title='Stockly', page_icon= ':chart_with_upwards_trend:', layout="wide")

# USER AUTHENTICATION
#hash_passwords = stauth.Hasher(['ja4u', 'g0at', 'daredev1l']).generate()
names = ['John Smith', 'Rebecca Briggs']
usernames = ['jsmith', 'rbriggs']
passwords = ['123', '456']

hashed_passwords = stauth.Hasher(passwords).generate()

authenticator = Authenticate(usernames, passwords, names)

name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status == False:
    st.error("Username or password is incorrect")

if authentication_status == None:
    st.warning("Please enter your Username and password")

if authentication_status == True:

    #Main Page
    st.title('Tesla')
    st.write("""
       ## Shown are the stock closing price and volume of Tesla!
       There is a bar graph, line graph and a table of the data. You can download the data as a csv file.
            """)

    tickerSymbol = 'TSLA'

    tickerData = yf.Ticker(tickerSymbol)

    tickerDf = tickerData.history(period='1d', start='2012-5-31', end='2022-5-31')

    tickerDf

    st.write(""" Tesla closing price """)
    st.line_chart(tickerDf.Close)
    st.write(""" Tesla Volume price """)
    st.line_chart(tickerDf.Volume)
    st.write(""" Tesla closing price """)
    st.bar_chart(tickerDf.Volume)

    #Sidebar
    authenticator.logout('Logout', 'sidebar')
    st.sidebar.title(f'Welcome {name}!')
