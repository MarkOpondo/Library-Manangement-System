from models.user import User


class Admin(User):
    def __init__(self, user_id, username, password_hash):
        super().__init__(
            user_id=user_id,
            username=username,
            password_hash=password_hash,
            role="admin"
        )