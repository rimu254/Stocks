
import streamlit as st


icon = "https://thumbs.dreamstime.com/b/growing-up-trend-stem-chart-trading-vector-design-illustration-template-160606828.jpg"
st.set_page_config(page_title='Stockly', page_icon=icon)

st.sidebar.header('Navigation')
page = st.sidebar.radio("Go to:",
                        ('Home',
                         'Predictions',
                         'Company Charts'))
if page == 'Home':
    from home import run
    run()


elif page == 'Predictions':
    from volume import run
    run()

else:
    from stock_tables import run
    run()
