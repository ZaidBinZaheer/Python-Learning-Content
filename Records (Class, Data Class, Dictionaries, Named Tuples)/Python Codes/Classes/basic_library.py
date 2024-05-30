# Define a Book class to represent individual books
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def check_out(self):
        if self.available:
            self.available = False
            return f"{self.title} by {self.author} has been checked out."
        else:
            return f"{self.title} by {self.author} is already checked out."

    def check_in(self):
        if not self.available:
            self.available = True
            return f"Thank you for returning {self.title} by {self.author}."
        else:
            return f"{self.title} by {self.author} is already available."

# Define a Library class to manage books
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            status = "Available" if book.available else "Checked Out"
            print(f"{book.title} by {book.author} - {status}")

# Create instances of the Book class
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("1984", "George Orwell")

# Create an instance of the Library class
library = Library()

# Add books to the library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# List books in the library
print("Books in the library:")
library.list_books()

# Check out a book
print("\nChecking out a book:")
print(book1.check_out())

# List books in the library after check-out
print("\nUpdated list of books:")
library.list_books()

# Check in a book
print("\nChecking in a book:")
print(book1.check_in())

# List books in the library after check-in
print("\nUpdated list of books:")
library.list_books()
