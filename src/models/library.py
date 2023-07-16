class Library:
    
    def __init__(self):
        self.students = {}
        self.books = {}  

    def add_student(self, student):
        self.students[student.jmbag] = student

    def remove_student(self, jmbag):
        del self.students[jmbag]

    def add_book(self, book):
        self.books[book.book_id] = book

    def remove_book(self, book_id):
        del self.books[book_id]

    def borrow_book(self, jmbag, book_id):
        student = self.students[jmbag]
        book = self.books[book_id]
        student.borrow_book(book)

    def return_book(self, jmbag, book_id):
        student = self.students[jmbag]
        book = self.books[book_id]
        student.return_book(book)