from models.user import User
from models.book import Book

class Admin(User):
    def __init__(self, user_id, username, password):
        super().__init__(user_id, username, password, role="admin")

    def addBook(self, book_list, book: Book):
        book_list.append(book)
        return f"Book '{book.title}' added successfully."

    def removeBook(self, book_list, book_id):
        for b in book_list:
            if b.id == book_id:
                book_list.remove(b)
                return f"Book '{b.title}' removed successfully."
        return "Book not found."

    def updateBook(self, book: Book, **kwargs):
        book.updateBook(**kwargs)
        return f"Book '{book.title}' updated successfully."
