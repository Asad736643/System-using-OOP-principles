# library/library_manager.py
from library.book import Book
from library.user import User

class LibraryManager:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book: Book):
        self.books.append(book)

    def add_user(self, user: User):
        self.users.append(user)

    def borrow_book(self, user: User, book: Book):
        if book in self.books and not book.is_borrowed:
            book.borrow()
            print(f"{user.name} has borrowed the book: {book.title}")
        else:
            print(f"Sorry, the book '{book.title}' is either unavailable or already borrowed.")

    def return_book(self, user: User, book: Book):
        if book in self.books and book.is_borrowed:
            book.return_book()
            print(f"{user.name} has returned the book: {book.title}")
        else:
            print(f"The book '{book.title}' was not borrowed or does not exist.")

    def display_status(self):
        print("Library Status:")
        for book in self.books:
            status = "Available" if not book.is_borrowed else "Borrowed"
            print(f"{book} - Status: {status}")
