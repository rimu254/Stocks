import streamlit as st
from datetime import date
import yfinance as yf
from prophet import Prophet
import altair as alt

def run():
    st.header("Stock Price Prediction")

    years = st.number_input('Enter the number of years you want to predict the stock price for', min_value=1,
                            max_value=10, value=1)
    st.write('You selected:', years, 'years')
    duration = years * 365

    tesla = 'TSLA'
    apple = 'AAPL'
    netflix = 'NFLX'
    amazon = 'AMZN'
    google = 'GOOGL'
    meta = "META"
    twitter = "TWTR"
    microsoft = "MSFT"

    company_names = [tesla, apple, netflix, amazon, google, meta, twitter, microsoft]

    selected_company = st.selectbox('Select the company you want to predict the stock price for', company_names)

    starts = "2017-01-01"
    ends = date.today().strftime("%Y-%m-%d")

    def load_data(ticker):
        companies = yf.download(ticker, start=starts, end=ends)
        companies.reset_index(inplace=True)
        return companies

    companies = load_data(selected_company)

    def plot_raw_data():
        open_close_chart = alt.Chart(companies).mark_line().encode(
            x='Date',
            y='Open',
            color=alt.value('red')
        ).properties(
            title='Stock Open and Close Prices'
        ) + alt.Chart(companies).mark_line().encode(
            x='Date',
            y='Close',
            color=alt.value('blue')
        ).interactive()
        st.altair_chart(open_close_chart, use_container_width=True)

    plot_raw_data()

    df_train = companies[['Date', 'Close']]
    df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

    m = Prophet()
    m.fit(df_train)
    future = m.make_future_dataframe(periods=duration)
    forecast = m.predict(future)

    def plot_forecast_data():
        forecast_chart = alt.Chart(forecast).mark_line().encode(
            x='ds',
            y='yhat',
        ).properties(
            title='Stock Price Forecast'
        ).interactive()

        st.altair_chart(forecast_chart, use_container_width=True)

    plot_forecast_data()





