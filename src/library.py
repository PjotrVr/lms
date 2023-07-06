import sqlite3
from enum import Enum


class BorrowResult(Enum):
    BOOK_NOT_FOUND = 1
    BOOK_AVAILABLE = 2
    BOOK_UNAVAILABLE = 3


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
