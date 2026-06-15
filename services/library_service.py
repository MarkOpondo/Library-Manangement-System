from services.storage_service import StorageService
from services.auth_service import AuthService

from models.book import Book
from models.transaction import Transaction

from decorators.roles import admin_required
from decorators.auth import login_required
from decorators.logger import log_action


class LibraryService:

    BOOKS_FILE = "data/books.json"
    TRANSACTIONS_FILE = "data/transactions.json"

    # -------------------------
    # Helpers
    # -------------------------

    @staticmethod
    def load_books():
        return StorageService.load_data(LibraryService.BOOKS_FILE)

    @staticmethod
    def save_books(books):
        StorageService.save_data(LibraryService.BOOKS_FILE, books)

    @staticmethod
    def load_transactions():
        return StorageService.load_data(LibraryService.TRANSACTIONS_FILE)

    @staticmethod
    def save_transactions(transactions):
        StorageService.save_data(LibraryService.TRANSACTIONS_FILE, transactions)

    # -------------------------
    # BOOK MANAGEMENT (ADMIN)
    # -------------------------

    @staticmethod
    @admin_required
    @log_action
    def add_book(title, author, category, total_copies):

        books = LibraryService.load_books()

        book_id = f"B{len(books)+1:03}"

        new_book = Book(
            book_id,
            title,
            author,
            category,
            total_copies
        )

        books.append(new_book.to_dict())
        LibraryService.save_books(books)

        print(f"\nBook '{title}' added successfully.\n")

    # -------------------------

    @staticmethod
    @admin_required
    @log_action
    def remove_book(book_id):

        books = LibraryService.load_books()

        updated_books = [
            b for b in books if b["book_id"] != book_id
        ]

        if len(updated_books) == len(books):
            print("\nBook not found.\n")
            return

        LibraryService.save_books(updated_books)

        print("\nBook removed successfully.\n")

    # -------------------------
    # VIEW BOOKS
    # -------------------------

    @staticmethod
    @login_required
    def view_books():

        books = LibraryService.load_books()

        if not books:
            print("\nNo books available.\n")
            return

        print("\n--- Library Books ---\n")

        for b in books:
            print(
                f"{b['book_id']} | "
                f"{b['title']} | "
                f"{b['author']} | "
                f"{b['available_copies']} copies"
            )

    # -------------------------
    # BORROW BOOK
    # -------------------------

    @staticmethod
    @login_required
    @log_action
    def borrow_book(book_id):

        user = AuthService.get_current_user()

        books = LibraryService.load_books()

        for b in books:
            if b["book_id"] == book_id:

                if b["available_copies"] <= 0:
                    print("\nNo copies available.\n")
                    return

                b["available_copies"] -= 1

                LibraryService.save_books(books)

                transaction = Transaction(
                    transaction_id=f"T{len(LibraryService.load_transactions())+1:03}",
                    user_id=user.user_id,
                    book_id=book_id,
                    action="BORROW"
                )

                transactions = LibraryService.load_transactions()
                transactions.append(transaction.to_dict())

                LibraryService.save_transactions(transactions)

                print("\nBook borrowed successfully.\n")
                return

        print("\nBook not found.\n")

    # -------------------------
    # RETURN BOOK
    # -------------------------

    @staticmethod
    @login_required
    @log_action
    def return_book(book_id):

        user = AuthService.get_current_user()

        books = LibraryService.load_books()

        for b in books:
            if b["book_id"] == book_id:

                if b["available_copies"] < b["total_copies"]:
                    b["available_copies"] += 1
                else:
                    print("\nInvalid return.\n")
                    return

                LibraryService.save_books(books)

                transaction = Transaction(
                    transaction_id=f"T{len(LibraryService.load_transactions())+1:03}",
                    user_id=user.user_id,
                    book_id=book_id,
                    action="RETURN"
                )

                transactions = LibraryService.load_transactions()
                transactions.append(transaction.to_dict())

                LibraryService.save_transactions(transactions)

                print("\nBook returned successfully.\n")
                return

        print("\nBook not found.\n")