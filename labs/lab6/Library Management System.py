class Student:
    def __init__(self, name_student):
        self.name = name_student
        self.borrowed_books = []

class Book:
    def __init__(self, name_book, author, year):
        self.name = name_book
        self.author = author
        self.year = year
        self.is_borrowed = False
        self.borrowed_by = None

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, student, book_name):
        for book in self.books:
            if book.name == book_name:
                if not book.is_borrowed:
                    book.is_borrowed = True
                    book.borrowed_by = student
                    student.borrowed_books.append(book)
                    print(f"{student.name} borrowed {book.name}")
                    return
                else:
                    print(f"Sorry, {book.name} is already borrowed by {book.borrowed_by.name}")
                    return
        print(f"Book {book_name} not found in library")

    def show_books(self):
        for book in self.books:
            status = "Available" if not book.is_borrowed else f"Borrowed by {book.borrowed_by.name}"
            print(f"{book.name} by {book.author} ({book.year}) - {status}")
