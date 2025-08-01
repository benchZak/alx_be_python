class Book:
    """A class representing a book in a library management system"""
    
    def __init__(self, title, author):
        """Initialize a book with title, author, and set it as available"""
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability
    
    def check_out(self):
        """Mark the book as checked out"""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    
    def return_book(self):
        """Mark the book as returned (available)"""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False
    
    def is_available(self):
        """Check if the book is available"""
        return not self._is_checked_out
    
    def __str__(self):
        """String representation of the book"""
        return f"{self.title} by {self.author}"


class Library:
    """A class representing a library that manages a collection of books"""
    
    def __init__(self):
        """Initialize an empty library"""
        self._books = []  # Private list to store books
    
    def add_book(self, book):
        """Add a new book to the library"""
        if isinstance(book, Book):
            self._books.append(book)
    
    def check_out_book(self, title):
        """Check out a book by title if available"""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        return False
    
    def return_book(self, title):
        """Return a book by title if it was checked out"""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return True
        return False
    
    def list_available_books(self):
        """List all currently available books"""
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books currently available")
        else:
            for book in available_books:
                print(book)
