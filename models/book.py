class Book:
    def __init__(
        self,
        book_id,
        title,
        author,
        category,
        total_copies
    ):
        self._book_id = book_id
        self._title = title
        self._author = author
        self._category = category
        self._total_copies = total_copies
        self._available_copies = total_copies

    @property
    def book_id(self):
        return self._book_id

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def available_copies(self):
        return self._available_copies

    def borrow_copy(self):
        if self._available_copies <= 0:
            raise ValueError("No copies available.")

        self._available_copies -= 1

    def return_copy(self):
        if self._available_copies < self._total_copies:
            self._available_copies += 1

            

    def to_dict(self):
        return {
            "book_id": self._book_id,
            "title": self._title,
            "author": self._author,
            "category": self._category,
            "total_copies": self._total_copies,
            "available_copies": self._available_copies
        }

    def __str__(self):
        return (
            f"{self._title} by {self._author} "
            f"({self._available_copies}/{self._total_copies} available)"
        )