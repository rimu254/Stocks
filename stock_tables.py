from urllib.error import URLError

import streamlit as st
import yfinance as yf
import pandas as pd
import altair as alt

def run():
    st.header('Company Stock Charts :chart_with_upwards_trend:')
    st.write("""  
           ##  Stock Charts
             The charts are interactive and you can zoom in and out of the charts and view the exact price in relation to the date.
              You can view the charts of the opening, volume and closing price of the companies.
                """)

    tesla = 'TSLA'
    apple = 'AAPL'
    netflix = 'NFLX'
    amazon = 'AMZN'
    google = 'GOOGL'
    meta = "META"
    twitter = "TWTR"
    microsoft = "MSFT"

    company_names= [tesla, apple, netflix, amazon, google, meta, twitter, microsoft]

    tesla_data = yf.Ticker(tesla)
    apple_data = yf.Ticker(apple)
    netflix_data = yf.Ticker(netflix)
    amazon_data = yf.Ticker(amazon)
    google_data = yf.Ticker(google)
    meta_data = yf.Ticker(meta)
    twitter_data = yf.Ticker(twitter)
    microsoft_data = yf.Ticker(microsoft)



    companies_data = yf.download(tickers=[tesla, apple, netflix, amazon, google, meta,twitter,microsoft], period='1d', interval='1d')

    st.subheader('Date range')
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input('Start date', value=pd.to_datetime('2013-1-1'))
    with col2:
        end_date = st.date_input('End date', value=pd.to_datetime('2023-1-31'))

    if(start_date != None or end_date != None):
        if start_date > end_date:
            tickerData_dates = companies_data[start_date:end_date]
    elif start_date > end_date:
        st.warning('Invalid date range. Please try again.')
        st.stop()
    else:
        st.warning('Invalid date range. Please try again.')

    tesla_df = tesla_data.history(period='1d', start=start_date, end=end_date)
    apple_df = apple_data.history(period='1d', start=start_date, end=end_date)
    netflix_df = netflix_data.history(period='1d', start=start_date, end=end_date)
    amazon_df = amazon_data.history(period='1d', start=start_date, end=end_date)
    google_df = google_data.history(period='1d', start=start_date, end=end_date)
    meta_df = meta_data.history(period='1d', start=start_date, end=end_date)
    twitter_df = twitter_data.history(period='1d', start=start_date, end=end_date)
    microsoft_df = microsoft_data.history(period='1d', start=start_date, end=end_date)

    tesla_df['Company'] = 'Tesla Inc'
    apple_df['Company'] = 'Apple Inc.'
    netflix_df['Company'] = 'Netflix Inc'
    amazon_df['Company'] = 'Amazon.com Inc.'
    google_df['Company'] = 'Alphabet Inc. Class A'
    meta_df['Company'] = 'Meta Platforms Inc.'
    twitter_df['Company'] = 'Twitter Inc.'
    microsoft_df['Company'] = 'Microsoft Corporation'

    companies = pd.concat([tesla_df, apple_df, netflix_df, amazon_df, google_df, meta_df, twitter_df, microsoft_df])

    companies.rename(columns={0: 'Date'}, inplace=True)

    st.subheader('Table of The Stock Information The Companies ')
    companies['Date'] = companies.index
    companies['Date'] = companies['Date'].apply(lambda x: x.date())


    companies

    try:
        st.sidebar.header("Stock Charts")
        company_info = st.sidebar.multiselect("Select a company", companies['Company'].unique(), default=['Tesla Inc'])

        if len(company_info) == 0:
            st.error('Please select a company.')
        else:
            data = companies[companies['Company'].isin(company_info)]
            st.write("# Company Charts")

            closing_chart = alt.Chart(data).mark_area(opacity=0.6).encode(
                x='Date:T',
                y=alt.Y('Close:Q', stack=None),
                color="Company:N",
                tooltip=['Company', 'Close', 'Date']
            ).interactive()

            opening_chart = alt.Chart(data).mark_area(opacity=0.6).encode(
                x='Date:T',
                y=alt.Y('Open:Q', stack=None),
                color="Company:N",
                tooltip=['Company', 'Open', 'Date']
            ).interactive()

            volume_chart = alt.Chart(data).mark_area(opacity=0.6).encode(
                x='Date:T',
                y=alt.Y('Volume:Q', stack=None),
                color="Company:N",
                tooltip=['Company', 'Volume', 'Date']
            ).interactive()

            try:
                tab1, tab2, tab3 = st.tabs(["Open Price Chart","Close Price Chart", "Volume Price Chart"])
                with tab1:
                    st.altair_chart(opening_chart, use_container_width=True)
                with tab2:
                    st.altair_chart(closing_chart, use_container_width=True)
                with tab3:
                    st.altair_chart(volume_chart, use_container_width=True)
            except Exception as e:
                st.error("An error occurred while rendering the chart: %s" % str(e))

    except URLError as e:
        st.error(
            """
            **Please make sure you are connected th.**
    
            Connection error: %s
            """ % e.reason
        )
