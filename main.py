# main.py
from library.book import Book
from library.user import User
from library.library_manager import LibraryManager

def main():
    # Initialize LibraryManager
    library = LibraryManager()

    # Create users
    user1 = User(name="John Doe", email="john.doe@example.com")
    user2 = User(name="Jane Smith", email="jane.smith@example.com")

    # Add users to the library
    library.add_user(user1)
    library.add_user(user2)

    # Create books
    book1 = Book(title="Python 101", author="John Author", isbn="1234567890")
    book2 = Book(title="Data Science Essentials", author="Jane Author", isbn="0987654321")

    # Add books to the library
    library.add_book(book1)
    library.add_book(book2)

    # Let user1 borrow a book
    library.borrow_book(user1, book1)

    # Let user2 try to borrow a book that is already borrowed
    library.borrow_book(user2, book1)

    # Let user1 return a book
    library.return_book(user1, book1)

    # Display current library status
    library.display_status()

if __name__ == "__main__":
    main()
