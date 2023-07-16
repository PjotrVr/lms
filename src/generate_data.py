import sqlite3
from faker import Faker
import random
from datetime import datetime
import hashlib
from .config import config
import os
import binascii


fake = Faker()
NUM_STUDENTS = 100
NUM_BOOKS = 50
NUM_STAFF = 20

# Function to generate password, salt and hashed_password
def get_password_components(password):
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    hashed_password = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
    hashed_password = binascii.hexlify(hashed_password)
    return salt.decode('ascii'), hashed_password.decode('ascii')

with sqlite3.connect(config['DB_PATH']) as conn:
    cur = conn.cursor()

    # generate students data
    for _ in range(NUM_STUDENTS):
        jmbag = '00365' + ''.join([str(random.randint(0, 9)) for _ in range(5)])
        name = fake.first_name()
        surname = fake.last_name()
        year = random.randint(1, 5)
        date_of_birth = fake.date_of_birth(minimum_age=18, maximum_age=30).isoformat()
        sex = random.choice(['M', 'F', 'O'])
        email = fake.email()
        password = fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)
        max_books = config['MAX_BORROWED_BOOKS']
        salt, hashed_password = get_password_components(password)

        cur.execute('''
            INSERT INTO students (jmbag, name, surname, year, date_of_birth, sex, email, hashed_password, salt, max_books) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        ''', (jmbag, name, surname, year, date_of_birth, sex, email, hashed_password, salt, max_books))

    # generate books data
    for _ in range(NUM_BOOKS):
        title = fake.catch_phrase()
        author = fake.name()
        production_year = random.randint(1980, datetime.now().year)
        total_copies = random.randint(5, 50)
        available_copies = random.randint(0, total_copies)

        cur.execute('''
            INSERT INTO books (title, author, production_year, total_copies, available_copies) 
            VALUES (?, ?, ?, ?, ?);
        ''', (title, author, production_year, total_copies, available_copies))

    # generate staff data
    for _ in range(NUM_STAFF):
        name = fake.first_name()
        surname = fake.last_name()
        email = fake.company_email()
        position = fake.job()
        password = fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)
        salt, hashed_password = get_password_components(password)

        cur.execute('''
            INSERT INTO staff (name, surname, email, hashed_password, salt, position) 
            VALUES (?, ?, ?, ?, ?, ?);
        ''', (name, surname, email, hashed_password, salt, position))

    #conn.commit()
