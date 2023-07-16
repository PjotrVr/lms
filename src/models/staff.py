from .person import Person
#from .library import Library

class Staff(Person):

    def __init__(self, name, surname, email, password, staff_id, position, library):
        super().__init__(name, surname, email, password)
        self.staff_id = staff_id
        self.position = position
        self.library = library

    def get_details(self):
        return {
            "name": self.name,
            "surname": self.surname,
            "email": self.email,
            "staff_id": self.staff_id,
            "position": self.position
        }

    def add_student(self, student):
        self.library.add_student(student)
        
    def remove_student(self, student_id):
        self.library.remove_student(student_id)

    def add_book(self, book):
        self.library.add_book(book)

    def remove_book(self, book_id):
        self.library.remove_book(book_id)
        

class AdminStaff(Staff):

    def __init__(self, name, surname, email, password, staff_id, library):
        super().__init__(name, surname, email, password, staff_id, "Admin", library)
        self.staff = {}

    def add_staff(self, staff):
        self.staff[staff.staff_id] = staff

    def remove_staff(self, staff_id):
        del self.staff[staff_id]