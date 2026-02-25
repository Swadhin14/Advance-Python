class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.borrowed = False

    def borrow(self):
        if not self.borrowed:
            self.borrowed = True
            return "Book has been borrowed."
        else:
            return "This book is already borrowed."

    def return_book(self):
        if self.borrowed:
            self.borrowed = False
            return "Book has been returned."
        else:
            return "This book is not borrowed."


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and not book.borrowed:
                return book.borrow()
        return "This book is either not available or already borrowed."

    def return_book_to_library(self, title):
        for book in self.books:
            if book.title == title:
                return book.return_book()
        return "Book not found."


# Usage example
library = Library()

while True:
    print("1. Add a book to the library")
    print("2. Borrow a book from the library")
    print("3. Return a book to the library")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter the book's title: ")
        author = input("Enter the book's author: ")
        library.add_book(title, author)
    elif choice == "2":
        title = input("Enter the book's title you want to borrow: ")
        print(library.borrow_book(title))
    elif choice == "3":
        title = input("Enter the book's title you want to return: ")
        print(library.return_book_to_library(title))
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please choose a valid option.")