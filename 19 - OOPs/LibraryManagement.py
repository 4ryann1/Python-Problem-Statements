# Problem 29:
# Create Book and Library classes. Book stores title, author, and availability.
# Library stores Book objects
# and provides add_book(), show_books(), borrow_book(title), and return_book(title).
#
# Goal: Learn how multiple basic classes and objects work together.
# Do not use inheritance or other advanced OOP.

class Book:
    def __init__(self,book_title, book_author, book_availability):
        self.book_title = book_title
        self.book_author = book_author
        self.book_availability = book_availability

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"{book.book_title} is added to the library.")

    def show_books(self,book):
        if not self.books:
            print("Book not available in the library.")
            return

        print(f"\n------ Library Books ------")
        for book in self.books:
            status = "Available" if book.book_availability else "Not available"
            print(f"Title : {book.book_title}")
            print(f"Author : {book.book_author}")
            print(f"Status : {status}")
            print(f"-"*30)

    def borrow_book(self,title):
        if title in self.books:
            self.books.remove(title)
            print(f"{title} is available in the library.")
            print(f"You have successfully borrowed {title}.")
        else:
            print(f"{title} is not available in the library.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.available:
                    book.available = True
                    print(f"'{book.title}' has been returned.")
                else:
                    print(f"'{book.title}' was not borrowed.")
                return
        print(f"Book '{title}' not found.")

# Create Book objects
book1 = Book("Python Programming", "Mark Lutz")
book2 = Book("Clean Code", "Robert C. Martin")
book3 = Book("The Pragmatic Programmer", "Andrew Hunt")

# Create Library object
library = Library()

# Add books
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Show books
library.show_books()

# Borrow a book
library.borrow_book("Clean Code")

# Show books again
library.show_books()

# Return the book
library.return_book("Clean Code")

# Show books again
library.show_books()