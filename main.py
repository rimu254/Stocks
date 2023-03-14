import streamlit as st
import database as db
from streamlit.server.server import Server
from streamlit.scriptrunner import get_script_run_ctx as get_report_ctx


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

class SessionState:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.server = Server.get_current()
        self.session_id = get_report_ctx().session_id
        self._lock = None

    def __getitem__(self, key):
        return self.__dict__.get(key, None)

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __repr__(self):
        return str(self.__dict__)

    def acquire(self):
        if self._lock is None:
            self._lock = self.server._session_info_by_id[self.session_id].ws._lock
        return self._lock.acquire()

    def release(self):
        self._lock.release()

    @staticmethod
    def get(**kwargs):
        for key, val in kwargs.items():
            if not hasattr(SessionState, key):
                setattr(SessionState, key, val)
        return SessionState(**kwargs)

def signup():
    st.header('Sign up')
    st.write("""
        ## Sign up to view the app
        """)
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    name = st.text_input('Name')
    if st.button('Create User'):
        db.insert_user(username, password, name)
        st.success('User created successfully')

def login():
    st.header('Login')
    st.write("""
        ## Login to the app
        """)
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    if st.button('Login'):
        user = db.fetch_user(username)
        if user:
            if user['password'] == password:
                st.success('Login successful')
                return user
            else:
                st.error('Incorrect password')
        else:
            st.error('User not found, signup first')


# Initialize the session state
session_state = SessionState.get(logged_in=False)

# Create login page
st.sidebar.header('STOCKLY LOGIN')

opts = ['Login', 'Sign Up']
option = st.sidebar.selectbox("Select an option:", opts)
#while not session_state.logged_in:
if option == 'Login':
        user = login()
        st.sidebar.header('Navigation')

        page_options = ['Home', 'Predictions', 'Company Charts']
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
    st.warning("Please log in after sign up to view the content.")
    signup()





