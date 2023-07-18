from getpass import getpass
from src.database.database import Database
from ..config import config


db = Database()

def check_credentials(email, password):
    #student


    return False

def login():
    while True:
        email = input("Email > ")
        password = getpass("Password > ")

        if check_credentials(email, password):
            break

