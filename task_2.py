import logging
from abc import ABC, abstractmethod

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


# Class representing a book
class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


# Abstract interface for a library
class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book):
        pass

    @abstractmethod
    def remove_book(self, title: str):
        pass

    @abstractmethod
    def show_books(self):
        pass


# Concrete implementation of a library
class Library(LibraryInterface):
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        logging.info(f"Adding book: {book}")
        self.books.append(book)

    def remove_book(self, title: str):
        logging.info(f"Removing book with title: {title}")
        self.books = [book for book in self.books if book.title != title]

    def show_books(self):
        logging.info("Showing all books in the library")
        for book in self.books:
            print(book)


# Manager class to handle library operations
class LibraryManager:
    def __init__(self, library: LibraryInterface):
        self.library = library

    def add_book(self, title: str, author: str, year: int):
        book = Book(title, author, year)
        logging.info(f"Manager adding book: {book}")
        self.library.add_book(book)

    def remove_book(self, title: str):
        logging.info(f"Manager removing book with title: {title}")
        self.library.remove_book(title)

    def show_books(self):
        logging.info("Manager showing books")
        self.library.show_books()


# Main function to interact with the library
def main():
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = int(input("Enter book year: ").strip())
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                logging.warning("Invalid command. Please try again.")
                print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
