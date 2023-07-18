import sqlite3
import bcrypt
import hashlib
from ..models.staff import Staff, AdminStaff
from ..models.student import Student
from ..models.book import Book


class Database:

    def __init__(self, config):
        self.config = config

    def connect(self):
        return sqlite3.connect(self.config["DB_PATH"])
    
    def generate_hash(self, password):
        pepper = self.config["PEPPER"]
        salt = bcrypt.gensalt().decode("utf-8")
        combined_password = salt + password + pepper
        hashed_password = hashlib.sha512(combined_password.encode()).hexdigest()

        return salt, hashed_password

    def verify_password(self, password, salt, saved_password):
        pepper = self.config["PEPPER"]
        combined_password = salt + password + pepper
        computed_password = hashlib.sha512(combined_password.encode()).hexdigest()

        return computed_password == saved_password

    
    def get_user_by_email(self, email):
        with self.connect() as conn:
            cur = conn.cursor()

            # checking if student exists with such email
            cur.execute("SELECT * FROM students WHERE email = ?", (email,))
            student_data = cur.fetchone()

            if student_data is not None:
                return Student(*student_data)
            
            # checking if staff member exists with such email
            cur.execute("SELECT * FROM staff WHERE email = ?", (email,))
            staff_data = cur.fetchone()

            if staff_data is not None:
                return AdminStaff(*staff_data) if staff_data[-1] == "Admin" else Staff(*staff_data)

            return None
        
    def get_user_by_id(self, id):
        with self.connect() as conn:
            cur = conn.cursor()

            # checking if student exists with such id
            cur.execute("SELECT * FROM students WHERE student_id=?", (id,))
            user_data = cur.fetchone()
            if user_data is not None:
                return Student(*user_data)

            # checking if staff member exists with such id
            cur.execute("SELECT * FROM staff WHERE staff_id=?", (id,))
            user_data = cur.fetchone()
            if user_data is not None:
                return AdminStaff(*user_data) if user_data[-1] == "Admin" else Staff(*user_data)

            return None
        
    def get_book_by_id(self, book_id):
        with self.connect() as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM books WHERE book_id=?", (book_id,))
            book_data = cur.fetchone()
            if book_data is not None:
                return Book(*book_data)

            return None

    def get_book_by_title(self, title):
        with self.connect() as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM books WHERE title=?", (title,))
            return [Book(*book_data) for book_data in cur.fetchall()]

    def get_books_by_author(self, author):
        with self.connect() as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM books WHERE author=?", (author,))
            return [Book(*book_data) for book_data in cur.fetchall()]

    def get_students_by_year(self, year):
        with self.connect() as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM students WHERE year=?", (year,))
            return [Student(*student_data) for student_data in cur.fetchall()]

    def get_all_books(self):
        with self.connect() as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM books")
            return [Book(*book_data) for book_data in cur.fetchall()]

    def get_all_users(self):
        with self.connect() as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM students")
            students = [Student(*student_data) for student_data in cur.fetchall()]

            cur.execute("SELECT * FROM staff")
            staff = [AdminStaff(*staff_data) if staff_data[-1] == "Admin" else Staff(*staff_data) for staff_data in cur.fetchall()]

            return students + staff

    def add_user(self, user_type, name, surname, email, password, **kwargs):
        user = None
        user_type = user_type.lower()
        
        if user_type == "students":
            user = Student(name, surname, email, password, **kwargs)
        elif user_type == "staff":
            user = Staff(name, surname, email, password, **kwargs)

        if user:
            with self.connect() as conn:
                cur = conn.cursor()
                salt, hashed_password = self.generate_hash(password)
                
                columns = ', '.join(kwargs.keys())
                placeholders = ', '.join('?' * len(kwargs))
                
                query = f"INSERT INTO {user_type} (name, surname, email, hashed_password, salt, {columns}) VALUES (?, ?, ?, ?, ?, {placeholders})"
                
                cur.execute(query, (name, surname, email, hashed_password, salt, *kwargs.values()))
                
                return user
        else:
            raise ValueError("Invalid user_type")
        
    def add_book(self, book_id, title, author, production_year, total_copies):
        with self.connect() as conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO books VALUES (?, ?, ?, ?, ?, ?)", (book_id, title, author, production_year, total_copies, total_copies))

        return Book(book_id, title, author, production_year, total_copies, total_copies)
    
    def remove_user_by_id(self, user_id):
        with self.connect() as conn:
            cur = conn.cursor()
            for table in ["students", "staff"]:
                try:
                    cur.execute(f"DELETE FROM {table} WHERE id = ?", (user_id,))
                except sqlite3.Error as e:
                    print(f"An error occurred: {e.args[0]}")
                    return False
                else:
                    if cur.rowcount > 0:
                        conn.commit()
                        return True
            
            return False

    def remove_user_by_email(self, email):
        with self.connect() as conn:
            cur = conn.cursor()
            for table in ["students", "staff"]:
                try:
                    cur.execute(f"DELETE FROM {table} WHERE email = ?", (email,))
                except sqlite3.Error as e:
                    print(f"An error occurred: {e.args[0]}")
                    return False
                else:
                    if cur.rowcount > 0:
                        conn.commit()
                        return True
            
            return False

    def update_user(self, user_id, name=None, surname=None, email=None, password=None):
        with self.connect() as conn:
            cur = conn.cursor()

            cur.execute("SELECT * FROM students WHERE student_id = ?", (user_id,))
            if cur.fetchone() is not None:
                if name is not None:
                    cur.execute("UPDATE students SET name = ? WHERE student_id = ?", (name, user_id))

                if surname is not None:
                    cur.execute("UPDATE students SET surname = ? WHERE student_id = ?", (surname, user_id))

                if email is not None:
                    cur.execute("UPDATE students SET email = ? WHERE student_id = ?", (email, user_id))

                if password is not None:
                    hashed_password, salt = self.generate_hash(password)
                    cur.execute("UPDATE students SET hashed_password = ?, salt = ? WHERE student_id = ?", (hashed_password, salt, user_id))
                    
                return True

            cur.execute("SELECT * FROM staff WHERE staff_id = ?", (user_id,))
            if cur.fetchone() is not None:
                if name is not None:
                    cur.execute("UPDATE staff SET name = ? WHERE staff_id = ?", (name, user_id))

                if surname is not None:
                    cur.execute("UPDATE staff SET surname = ? WHERE staff_id = ?", (surname, user_id))

                if email is not None:
                    cur.execute("UPDATE staff SET email = ? WHERE staff_id = ?", (email, user_id))

                if password is not None:
                    hashed_password, salt = self.generate_hash(password)
                    cur.execute("UPDATE staff SET hashed_password = ?, salt = ? WHERE staff_id = ?", (hashed_password, salt, user_id))
                    
                return True
            
        return False
