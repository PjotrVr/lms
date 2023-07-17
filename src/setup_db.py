import sqlite3
import hashlib
import bcrypt
from .config import config


def generate_hash(password, pepper):
    salt = bcrypt.gensalt().decode('utf-8')
    combined_password = salt + password + pepper
    hashed_password = hashlib.sha512(combined_password.encode()).hexdigest()

    return salt, hashed_password


with sqlite3.connect(config['DB_PATH']) as conn:
    cur = conn.cursor()

    # create students table
    cur.execute('''
        CREATE TABLE students (
            jmbag TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            surname TEXT NOT NULL,
            year INTEGER NOT NULL,
            date_of_birth DATE NOT NULL,
            sex CHAR(1) NOT NULL CHECK (sex IN ('M', 'F', 'O')),
            email TEXT NOT NULL UNIQUE,
            hashed_password TEXT NOT NULL,
            salt TEXT NOT NULL,
            max_books INTEGER NOT NULL
        );
    ''')

    # create books table
    cur.execute('''
        CREATE TABLE books (
            book_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            production_year INTEGER NOT NULL,
            total_copies INTEGER NOT NULL,
            available_copies INTEGER NOT NULL
        );
    ''')

    # create borrowed books table
    cur.execute('''
        CREATE TABLE borrowed_books (
            borrow_id INTEGER PRIMARY KEY AUTOINCREMENT,
            jmbag TEXT,
            book_id INTEGER,
            borrow_date DATE NOT NULL,
            return_date DATE NOT NULL,
            is_overdue BOOLEAN DEFAULT 0,
            overdue_fee FLOAT DEFAULT 0,
            FOREIGN KEY(jmbag) REFERENCES students(jmbag),
            FOREIGN KEY(book_id) REFERENCES books(book_id)
        );
    ''')

    # create staff table
    cur.execute('''
        CREATE TABLE staff (
            staff_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            surname TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            hashed_password TEXT NOT NULL,
            salt TEXT NOT NULL,
            position TEXT NOT NULL
        );
    ''')

    # adding admin
    name = 'Admin'
    surname = 'Admin'
    email = config['EMAIL']
    password = config['EMAIL_PASSWORD']
    salt, hashed_password = generate_hash(password, config['PEPPER'])
    position = 'Admin'

    cur.execute('''
                INSERT INTO staff (name, surname, email, hashed_password, salt, position)
                VALUES(?, ?, ?, ?, ?, ?)
                ''', (name, surname, email, hashed_password, salt, position))