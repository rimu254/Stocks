import streamlit as st
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


def signup():
    st.sidebar.subheader('Sign up')
    username = st.sidebar.text_input('Username')
    password = st.sidebar.text_input('Password', type='password')
    name = st.sidebar.text_input('Name')
    if st.sidebar.button('Create User'):
        db.insert_user(username, password, name)
        st.success('User created successfully')


def login():
    st.subheader('Confirm Credentials')
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    if st.button('Login'):
        user = db.fetch_user(username)
        if user:
            if user['password'] == password:
                st.success(f'Welcome to Stockly ' + user['name'])
                return user
            else:
                st.error('Incorrect password')
        else:
            st.error('User not found, signup first')


st.sidebar.header('STOCKLY APP')
opts = ['Login', 'Sign Up']
option = st.sidebar.selectbox("Login to continue:", opts)
if option == 'Login':
        user=login()
        st.sidebar.header('Navigation')

        page = st.sidebar.radio("Go to:", (
                'Home',
                'Predictions',
                'Company Charts'
            ))

        if page == 'Home':
            from home import run
            run()

        elif page == 'Predictions':
            from predictions import run
            run()

        else:
            from company_charts import run
            run()


else:
    st.sidebar.warning("Please log in after sign up to view the content.")
    signup()




