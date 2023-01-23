import yfinance as yf
import pandas as pd
import streamlit as st

st.title('Stock Price App')
st.write("""
        
       ## Shown are the stock closing price and volume of Tesla!
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