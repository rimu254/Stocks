import yfinance as yf
import pandas as pd
import streamlit as st

st.set_page_config(page_title='Stockly', page_icon= ':chart_with_upwards_trend:', layout="wide")

st.title('Tesla Stock Price App')
st.write("""  
       ## Shown are the stock closing price and volume of Tesla!
       There is a bar graph, line graph and a table of the data. You can download the data as a csv file.
            """)

tickerSymbol = 'TSLA'

tickerData = yf.Ticker(tickerSymbol)
tickerData_dates = tickerData
st.subheader('Date range')
col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input('Start date', value=pd.to_datetime('2012-5-31'))
with col2:
    end_date = st.date_input('End date', value=pd.to_datetime('2022-5-31'))

if(start_date != None or end_date != None):
    if start_date > end_date:
        tickerData_dates = tickerData[start_date:end_date]
elif start_date > end_date:
    st.warning('Invalid date range. Please try again.')
    st.stop()
else:
    st.warning('Invalid date range. Please try again.')
st.subheader('Tesla stock in table')
tickerDf = tickerData.history(period='1d', start= start_date, end= end_date)

tickerDf

st.write(""" Tesla closing price """)
st.line_chart(tickerDf.Close)
st.write(""" Tesla Volume price """)
st.line_chart(tickerDf.Volume)
st.write(""" Tesla closing price """)
st.bar_chart(tickerDf.Volume)