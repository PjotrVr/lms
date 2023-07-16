class Book:

    def __init__(self, book_id, title, author, production_year, total_copies, available_copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.production_year = production_year
        self.total_copies = total_copies
        self.available_copies = available_copies

    def borrow_book(self):    
        if self.available_copies > 0:
            self.available_copies -= 1
            return True
        
        return False

    def return_book(self):
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            return True
        
        return False
    
    def add_copies(self, num_of_copies):
        self.total_copies += num_of_copies
        self.available_copies += num_of_copies

    def remove_copies(self, num_of_copies):
        to_delete = min(self.available_copies, self.total_copies, num_of_copies)
        self.total_copies -= to_delete
        self.available_copies -= to_delete
        
        return True if self.available_copies >= num_of_copies else False

    