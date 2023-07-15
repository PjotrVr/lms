import sqlite3


with sqlite3.connect('src/database/library.db') as conn:
    cur = conn.cursor()

    # Create students table
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

    # Create books table
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

    # Create borrowed books table
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