from datetime import datetime

class Transaction:
    def __init__(self, trans_id, book_id, user_id, action):
        self._trans_id = trans_id
        self._book_id = book_id
        self._user_id = user_id
        self._action = action
        self._date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @property
    def transaction_id(self):
        return self._transaction_id

    @property
    def user_id(self):
        return self._user_id

    @property
    def book_id(self):
        return self._book_id

    @property
    def action(self):
        return self._action

    @property
    def date(self):
        return self._date

    def to_dict(self):
        return {
            "transaction_id": self._transaction_id,
            "user_id": self._user_id,
            "book_id": self._book_id,
            "action": self._action,
            "date": self._date
        }

    def __str__(self):
        return (
            f"{self._action.upper()} | "
            f"User:{self._user_id} | "
            f"Book:{self._book_id} | "
            f"{self._date}"
        )