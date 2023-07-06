import sqlite3
from faker import Faker
import random
from datetime import datetime


fake = Faker()

# constants
NUM_STUDENTS = 100
NUM_BOOKS = 50

with sqlite3.connect('src/database/library.db') as conn:
    cur = conn.cursor()

    # generate students data
    for _ in range(NUM_STUDENTS):
        jmbag = '00365' + ''.join([str(random.randint(0, 9)) for _ in range(5)])
        name = fake.first_name()
        surname = fake.last_name()
        year = random.randint(1, 5)
        date_of_birth = fake.date_of_birth(minimum_age=18, maximum_age=30).isoformat()
        sex = random.choice(['M', 'F', 'O'])
        
        cur.execute('''
            INSERT INTO students (jmbag, name, surname, year, date_of_birth, sex) 
            VALUES (?, ?, ?, ?, ?, ?);
        ''', (jmbag, name, surname, year, date_of_birth, sex))

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

