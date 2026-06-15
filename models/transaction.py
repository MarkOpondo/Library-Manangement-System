from datetime import datetime

class Transaction:
    def __init__(self, trans_id, book_id, user_id, action):
        self.trans_id = trans_id
        self.book_id = book_id
        self.user_id = user_id
        self.action = action
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f"Transaction(ID={self.trans_id}, BookID={self.book_id}, UserID={self.user_id}, Action={self.action}, Date={self.date})"
