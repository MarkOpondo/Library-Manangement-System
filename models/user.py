from abc import ABC


class User(ABC):
    def __init__(self, user_id, username, password_hash, role):
        self._user_id = user_id
        self._username = username
        self._password_hash = password_hash
        self._role = role

    @property
    def user_id(self):
        return self._user_id

    @property
    def username(self):
        return self._username

    @property
    def role(self):
        return self._role

    @property
    def password_hash(self):
        return self._password_hash

    def to_dict(self):
        return {
            "user_id": self._user_id,
            "username": self._username,
            "password_hash": self._password_hash,
            "role": self._role
        }

    def __str__(self):
        return f"{self._username} ({self._role})"