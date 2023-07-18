from src.models.person import Person
from src.config import config
from src.database.database import Database

class Staff(Person):
    def __init__(self, name, surname, email, password, sex, date_of_birth, position):
        super().__init__(name, surname, email, password, sex, date_of_birth)
        self.position = position
        self.db = Database(config)

    def get_details(self):
        return {
            "name": self.name,
            "surname": self.surname,
            "email": self.email,
            "position": self.position,
            "date_of_birth": self.date_of_birth,
            "sex": self.sex
        }

    def add_student(self, student):
        self.db.add_user("students", student.name, student.surname, student.email, student.password,
                         student_id=student.student_id, year=student.year,
                         date_of_birth=student.date_of_birth, sex=student.sex, max_books=student.max_books)

    def remove_student(self, student_id):
        self.db.remove_student(student_id)

    def add_book(self, book):
        self.db.add_book(book.title, book.author, book.production_year, book.total_copies, available_copies=book.available_copies)

    def remove_book(self, book_id):
        self.db.remove_book(book_id)

class AdminStaff(Staff):
    def __init__(self, name, surname, email, password, sex, date_of_birth):
        super().__init__(name, surname, email, password, sex, date_of_birth, "Admin")

    def add_staff(self, staff):
        self.db.add_user("staff", staff.name, staff.surname, staff.email, staff.password,
                         position=staff.position, date_of_birth=staff.date_of_birth, sex=staff.sex)

    def remove_staff(self, staff_id):
        self.db.remove_staff(staff_id)