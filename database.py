from deta import Deta
import os
import yaml
from dotenv import load_dotenv
import streamlit_authenticator as stauth

# Load the environment variables
load_dotenv(".env")
db_key = os.getenv("db_key")

# Initialize the Deta Base
deta = Deta(db_key)

db = deta.Base("stock_base")

def create_user(username, password, name):
    #if user does not exist, create the user
    #if user exists, return an error
    return db.put({"key": username, "password": password, "name": name})

def insert_cookie(expiry_days,key,name):
    return db.put({"expiry_days": expiry_days, "key": key, "name": name})
def insert_user(username, password, name):
    return db.put({"key": username, "password": password, "name": name})
def fetch_all_users():
    res = db.fetch()
    return res.items

def fetch_user(username):
    #if user exists, return the user
    return db.get(username)

def delete_user(username):
    return db.delete(username)

def update_user(username):
    return db.update(username)

