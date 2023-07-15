import sqlite3
from enum import Enum
from datetime import date, datetime


class BorrowResult(Enum):
    BOOK_NOT_FOUND = 1
    BOOK_AVAILABLE = 2
    BOOK_UNAVAILABLE = 3


class ReturnResult(Enum):
    NOT_BORROWED = 1
    RETURN_SUCCESSFUL = 2
    RETURN_OVERDUE = 3
    

def borrow_book(cursor, jmbag, book_id, borrow_date, return_date):
    # check if the book exists
    cursor.execute("SELECT available_copies FROM books WHERE book_id = ?", (book_id,))
    result = cursor.fetchone()

    if result is None:
        return BorrowResult.BOOK_NOT_FOUND
    
    available_copies = result[0]
    if available_copies <= 0:
        return BorrowResult.BOOK_UNAVAILABLE
    
    # updating one less available book
    cursor.execute("UPDATE books SET available_copies = ? WHERE book_id = ?", (available_copies - 1, book_id))

    # insert new entry inside borrowed_books table
    cursor.execute("INSERT INTO borrowed_books (jmbag, book_id, borrow_date, return_date) VALUES(?, ?, ?, ?)", (jmbag, book_id, borrow_date, return_date))

    return BorrowResult.BOOK_AVAILABLE


def return_book(cursor, jmbag, book_id, current_date):
    # check if the book is currently borrowed by the student
    cursor.execute("SELECT return_date FROM borrowed_books WHERE jmbag = ? AND book_id = ?", (jmbag, book_id))
    result = cursor.fetchone()

    if result is None:
        return ReturnResult.NOT_BORROWED

    return_date = datetime.strptime(result[0], '%Y-%m-%d').date()

    # increase the available copies of the book
    cursor.execute("UPDATE books SET available_copies = available_copies + 1 WHERE book_id = ?", (book_id,))

    # remove the entry from the borrowed_books table
    cursor.execute("DELETE FROM borrowed_books WHERE jmbag = ? AND book_id = ?", (jmbag, book_id))

    if return_date > current_date:
        return ReturnResult.RETURN_OVERDUE
    
    else:
        return ReturnResult.RETURN_SUCCESSFUL
    

def search_book():
    pass