from datetime import datetime
class Book:
    def __init__(self,book_id,title,author,category,available_copies):
        self.__id = book_id
        self.__title = title
        self.__author = author
        self.__category = category
        self.__available_copies = available_copies
    
    @property
    def id(self):
        return self.__id
    
    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, value):
        self.__title = value    
    
    @property
    def author(self):
        return self.__author
    
    @author.setter
    def author(self, value):
        self.__author = value
    
    @property
    def category(self):
        return self.__category
    
    @category.setter
    def category(self, value):
        self.__category = value
    
    @property
    def available_copies(self):
        return self.__available_copies

    @available_copies.setter
    def available_copies(self, value):
        if value < 0:
            raise ValueError("Available copies cannot be negative.")
        self.__available_copies = value 

    def isAvailable(self):
        return self.__available_copies > 0

    def borrowBook(self):
        if self.isAvailable():
            self.__available_copies -= 1
            return True    
        raise ValueError ("Book is not available for borrowing.")
    
    def returnBook(self):
        self.__available_copies += 1
        return f"Book '{self.__title}' successfully returned. Available copies: {self.__available_copies}"
    
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
            f"Book(ID={self.__id}, "
            f"Title='{self.__title}', "
            f"Author='{self.__author}', "
            f"Category='{self.__category}', "
            f"Available Copies={self.__available_copies})"
        )
                        
class Transaction(Book):
    def __init__(self, trans_id, book_id, user_id, action):
        super().__init__(book_id)
        self.trans_id = trans_id
        self.user_id = user_id
        self.action = action
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M")

    def __str__(self):
        return f"Transaction ID: {self.trans_id}, User: {self.user_id}, performed: {self.action}, Book: {self.book_id}, Time: {self.date}"