import streamlit as st


st.set_page_config(page_title='Stockly', page_icon=':chart_with_upwards_trend:')

st.sidebar.header('Navigation')
page = st.sidebar.radio("Go to",
                        ('Home',
                         'Predictions',
                         'Company Chart'))
if page == 'Home':
    st.title('Stockly')
    st.write('''
        This is a simple app that shows the stock data of the companies.
        You can select a company and see the data for that company.
        ''')


elif page == 'Predictions':
    from prediction_page import run
    run()

else:
    from stock_tables import run
    run()
