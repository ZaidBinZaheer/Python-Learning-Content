class LibraryCatalog:
    def __init__(self):
        self.books = {}

    def add_book(self, title, author):
        if title not in self.books:
            self.books[title] = {"author": author, "available": True}
            print(f"Book '{title}' by {author} has been added to the catalog.")
        else:
            print(f"Book '{title}' already exists in the catalog.")

    def borrow_book(self, title):
        if title in self.books and self.books[title]["available"]:
            self.books[title]["available"] = False
            print(f"Book '{title}' has been borrowed.")
        elif title in self.books and not self.books[title]["available"]:
            print(f"Book '{title}' is not available. It has been borrowed already.")
        else:
            print(f"Book '{title}' is not in the catalog.")

    def return_book(self, title):
        if title in self.books and not self.books[title]["available"]:
            self.books[title]["available"] = True
            print(f"Book '{title}' has been returned.")
        elif title in self.books and self.books[title]["available"]:
            print(f"Book '{title}' is already available in the catalog.")
        else:
            print(f"Book '{title}' is not in the catalog.")

    def display_catalog(self):
        print("Library Catalog:")
        for title, info in self.books.items():
            availability = "Available" if info["available"] else "Borrowed"
            print(f"Title: {title}, Author: {info['author']}, Status: {availability}")

# Creating a LibraryCatalog instance
library = LibraryCatalog()

while True:
    print("1. Add Book")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Display Catalog")
    print("5. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        library.add_book(title, author)
    elif choice == '2':
        title = input("Enter book title: ")
        library.borrow_book(title)
    elif choice == '3':
        title = input("Enter book title: ")
        library.return_book(title)
    elif choice == '4':
        library.display_catalog()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
