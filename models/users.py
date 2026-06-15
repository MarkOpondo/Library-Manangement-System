from book import Book, Transaction


class User:
    _transaction_counter = 1  # Shared counter to auto-generate transaction IDs

    def __init__(self, user_id, user_name, password, role="user"):
        self.id = user_id
        self.user_name = user_name
        self.password = password
        self.role = role
        self.borrowed_books = []  # Tracks Book objects currently borrowed by this user

    # ------------------------------------------------------------------ #
    #  Book interaction methods                                            #
    # ------------------------------------------------------------------ #

    def viewBook(self, book: Book):
        """Display details of a given Book object."""
        if not isinstance(book, Book):
            print("Invalid book object.")
            return
        print(book)

    def borrowBook(self, book: Book):
        """
        Borrow a book if it is available.
        Delegates the copy-count update to Book.borrowBook() and
        records a Transaction.

        Returns the Transaction on success, None on failure.
        """
        if not isinstance(book, Book):
            print("Invalid book object.")
            return None

        if book.borrowBook():                       # Book handles availability check
            self.borrowed_books.append(book)
            trans = Transaction(
                trans_id=User._transaction_counter,
                book_id=book.id,
                user_id=self.id,
                action="borrow"
            )
            User._transaction_counter += 1
            print(f"[SUCCESS] {self.user_name} borrowed '{book.title}'.")
            print(trans)
            return trans
        else:
            print(f"[FAILED] '{book.title}' is currently unavailable.")
            return None

    def returnBook(self, book: Book):
        """
        Return a previously borrowed book.
        Delegates the copy-count update to Book.returnBook() and
        records a Transaction.

        Returns the Transaction on success, None on failure.
        """
        if not isinstance(book, Book):
            print("Invalid book object.")
            return None

        if book not in self.borrowed_books:
            print(f"[FAILED] You have not borrowed '{book.title}'.")
            return None

        book.returnBook()                           # Book increments available copies
        self.borrowed_books.remove(book)
        trans = Transaction(
            trans_id=User._transaction_counter,
            book_id=book.id,
            user_id=self.id,
            action="return"
        )
        User._transaction_counter += 1
        print(f"[SUCCESS] {self.user_name} returned '{book.title}'.")
        print(trans)
        return trans

    def __str__(self):
        return (
            f"User(ID={self.id}, "
            f"Username='{self.user_name}', "
            f"Role='{self.role}', "
            f"Books Borrowed={len(self.borrowed_books)})"
        )


# ------------------------------------------------------------------ #
#  Admin — inherits from User                                         #
# ------------------------------------------------------------------ #

class Admin(User):

    def __init__(self, user_id, user_name, password):
        super().__init__(user_id, user_name, password, role="admin")

    # ------------------------------------------------------------------ #
    #  Library catalogue management                                        #
    # ------------------------------------------------------------------ #

    def addBook(self, catalogue: list, book: Book):
        """
        Add a Book to the library catalogue (a list of Book objects).
        Rejects duplicates by book ID.
        """
        if not isinstance(book, Book):
            print("Invalid book object.")
            return False

        if any(b.id == book.id for b in catalogue):
            print(f"[FAILED] A book with ID '{book.id}' already exists in the catalogue.")
            return False

        catalogue.append(book)
        print(f"[SUCCESS] Admin '{self.user_name}' added '{book.title}' to the catalogue.")
        return True

    def removeBook(self, catalogue: list, book_id):
        """
        Remove a Book from the catalogue by its ID.
        """
        for book in catalogue:
            if book.id == book_id:
                catalogue.remove(book)
                print(f"[SUCCESS] Admin '{self.user_name}' removed book ID '{book_id}' from the catalogue.")
                return True

        print(f"[FAILED] Book with ID '{book_id}' not found in the catalogue.")
        return False

    def updateBook(self, book: Book, title=None, author=None, category=None, available_copies=None):
        """
        Update one or more fields on an existing Book object.
        Delegates to Book.updateBook() so all validation lives there.
        """
        if not isinstance(book, Book):
            print("Invalid book object.")
            return False

        book.updateBook(
            title=title,
            author=author,
            category=category,
            available_copies=available_copies
        )
        print(f"[SUCCESS] Admin '{self.user_name}' updated book ID '{book.id}'.")
        print(book)
        return True

    def __str__(self):
        return (
            f"Admin(ID={self.id}, "
            f"Username='{self.user_name}', "
            f"Role='{self.role}')"
        )


# ------------------------------------------------------------------ #
#  Quick smoke-test (runs only when this file is executed directly)   #
# ------------------------------------------------------------------ #

if __name__ == "__main__":
    # --- Set up catalogue ---
    catalogue = [
        Book("B001", "Clean Code", "Robert C. Martin", "Programming", 3),
        Book("B002", "The Pragmatic Programmer", "Andrew Hunt", "Programming", 1),
    ]

    # --- Create users ---
    alice = User("U001", "alice", "pass123")
    admin = Admin("A001", "admin_jerry", "adminpass")

    print("=== VIEW BOOK ===")
    alice.viewBook(catalogue[0])

    print("\n=== BORROW BOOK ===")
    alice.borrowBook(catalogue[1])   # 1 copy → should succeed
    alice.borrowBook(catalogue[1])   # 0 copies → should fail

    print("\n=== RETURN BOOK ===")
    alice.returnBook(catalogue[1])   # should succeed
    alice.returnBook(catalogue[1])   # not borrowed → should fail

    print("\n=== ADMIN: ADD BOOK ===")
    new_book = Book("B003", "Design Patterns", "GoF", "Programming", 2)
    admin.addBook(catalogue, new_book)

    print("\n=== ADMIN: UPDATE BOOK ===")
    admin.updateBook(catalogue[0], available_copies=5)

    print("\n=== ADMIN: REMOVE BOOK ===")
    admin.removeBook(catalogue, "B002")

    print("\n=== CATALOGUE AFTER CHANGES ===")
    for b in catalogue:
        print(b)