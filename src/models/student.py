from .person import Person


class Student(Person):

    def __init__(self, name, surname, email, password, jmbag):
        super().__init__(name, surname, email, password)
        self.jmbag = jmbag
        self.borrowed_books = []

    def get_details(self):
        return {
            "name": self.name,
            "surname": self.surname,
            "email": self.email,
            "jmbag": self.jmbag,
            "borrowed_books": [book.get_details() for book in self.borrowed_books]
        }
    