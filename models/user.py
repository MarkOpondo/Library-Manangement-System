import hashlib
from models.book import Book

class User:
    def __init__(self, user_id, username, password, role="user"):
        self.__id = user_id
        self.__username = username
        self.__password = self.hash_password(password)
        self.__role = role

    @property
    def id(self): return self.__id
    @property
    def username(self): return self.__username
    @property
    def role(self): return self.__role

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def verify_password(self, password):
        return self.__password == hashlib.sha256(password.encode()).hexdigest()

    def viewBook(self, book: Book):
        return str(book)

    def borrowBook(self, book: Book):
        return book.borrowBook()

    def returnBook(self, book: Book):
        return book.returnBook()
