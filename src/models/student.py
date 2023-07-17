from .person import Person


class Student(Person):

    def __init__(self, name, surname, email, password, student_id):
        super().__init__(name, surname, email, password)
        self.student_id = student_id
        self.borrowed_books = []

    def get_details(self):
        return {
            "name": self.name,
            "surname": self.surname,
            "email": self.email,
            "student_id": self.student_id,
            "borrowed_books": [book.get_details() for book in self.borrowed_books]
        }
    