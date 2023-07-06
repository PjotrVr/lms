# Database Schema for Library System

## Tables:

### 1. Students

This table stores information about each student.

Fields:
- **JMBAG (Primary Key, TEXT):** A unique identifier for each student.
- **Name (TEXT):** The student's first name.
- **Surname (TEXT):** The student's last name.
- **Year (INTEGER):** The year the student is currently in.
- **DateOfBirth (DATE):** The student's date of birth.
- **Sex (TEXT):** The student's sex.

### 2. Books

This table stores information about each book.

Fields:
- **Book_ID (Primary Key, INTEGER):** A unique identifier for each book. This is autoincremented for each new book.
- **Title (TEXT):** The title of the book.
- **Author (TEXT):** The author of the book.
- **Production_Year (INTEGER):** The year the book was published.
- **Total_Copies (INTEGER):** The total number of copies of the book in the library.
- **Available_Copies (INTEGER):** The number of copies currently available for borrowing.

### 3. BorrowedBooks

This table stores information about the books that have been borrowed.

Fields:
- **Borrow_ID (Primary Key, INTEGER):** A unique identifier for each borrowing instance. This is autoincremented for each new instance.
- **JMBAG (TEXT):** The ID of the student who has borrowed the book. This is a foreign key referencing the JMBAG field in the Students table.
- **Book_ID (INTEGER):** The ID of the book that has been borrowed. This is a foreign key referencing the Book_ID field in the Books table.
- **Borrow_Date (DATE):** The date when the book was borrowed.
- **Return_Date (DATE):** The date when the book is due to be returned.

---

This schema describes the minimum viable product (MVP) for the library system. Additional tables and fields may be added in the future to support new features, such as a waiting list.
