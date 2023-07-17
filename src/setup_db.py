import sqlite3
from src.config import config
from src.database.database import Database

with sqlite3.connect(config["DB_PATH"]) as conn:
    db = Database(config)
    cur = conn.cursor()

    # create students table
    cur.execute('''
        CREATE TABLE students (
            student_id TEXT PRIMARY KEY,
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
            student_id TEXT,
            book_id INTEGER,
            borrow_date DATE NOT NULL,
            return_date DATE NOT NULL,
            is_overdue BOOLEAN DEFAULT 0,
            overdue_fee FLOAT DEFAULT 0,
            FOREIGN KEY(student_id) REFERENCES students(student_id),
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
            date_of_birth DATE NOT NULL,
            sex CHAR(1) NOT NULL CHECK (sex IN ('M', 'F', 'O')),
            hashed_password TEXT NOT NULL,
            salt TEXT NOT NULL,
            position TEXT NOT NULL
        );
    ''')

    # adding admin
    name = "Admin"
    surname = "Admin"
    email = config["EMAIL"]
    password = config["EMAIL_PASSWORD"]
    salt, hashed_password = db.generate_hash(password)
    position = "Admin"

    cur.execute('''
                INSERT INTO staff (name, surname, email, hashed_password, salt, position, sex, date_of_birth)
                VALUES(?, ?, ?, ?, ?, ?, ?, ?)
                ''', (name, surname, email, hashed_password, salt, position, "O", ""))

    