# library/book.py

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def __str__(self):
        return f"'{self.title}' by {self.author}, ISBN: {self.isbn}"

    def borrow(self):
        self.is_borrowed = True

    def return_book(self):
        self.is_borrowed = False