class Book:
    def __init__(self,book_id,title,author,category,available_copies):
        self.id = book_id
        self.title = title
        self.author = author
        self.category = category
        self.available_copies = available_copies

    def isAvailable(self):
        return self.available_copies > 0

    def borrowBook(self):
        if self.isAvailable():
            self.available_copies -= 1
            return True    
        return False
    
    def returnBook(self):
        self.available_copies += 1
        return True
    
    def updateBook(self, title=None, author=None, category=None, available_copies=None):
        if title is not None:
            self.title = title

        if author is not None:
            self.author = author

        if category is not None:
            self.category = category

        if available_copies is not None:
            self.available_copies = available_copies

    def __str__(self):
        return (
            f"Book(ID={self.id}, "
            f"Title='{self.title}', "
            f"Author='{self.author}', "
            f"Category='{self.category}', "
            f"Available Copies={self.available_copies})"
        )
                        