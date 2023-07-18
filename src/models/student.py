from src.models.person import Person
from src.database.database import Database
from src.config import config

class Student(Person):
    def __init__(self, name, surname, email, password, sex, date_of_birth, student_id, year, max_books):
        super().__init__(name, surname, email, password, sex, date_of_birth)
        self.student_id = student_id
        self.year = year
        self.max_books = max_books
        self.db = Database(config)

    def get_details(self):
        return {
            "name": self.name,
            "surname": self.surname,
            "email": self.email,
            "student_id": self.student_id,
            "year": self.year,
            "date_of_birth": self.date_of_birth,
            "sex": self.sex,
            "max_books": self.max_books,
            "borrowed_books": self.db.get_borrowed_books(self.student_id)
        }