from models.admin import Admin
from models.member import Member

from services.storage_service import StorageService

from utils.password_utils import (
    hash_password,
    verify_password
)

class AuthService:

    USERS_FILE = "data/users.json"

    current_user = None

    @classmethod
    def get_all_users(cls):
        return StorageService.load_data(
            cls.USERS_FILE
        )

    @classmethod
    def save_all_users(cls, users):
        StorageService.save_data(
            cls.USERS_FILE,
            users
        )

    @classmethod
    def register(
        cls,
        username,
        password,
        role="member"
    ):

        users = cls.get_all_users()

        for user in users:
            if user["username"] == username:
                raise ValueError(
                    "Username already exists."
                )

        user_id = f"U{len(users)+1:03}"

        password_hash = hash_password(
            password
        )

        new_user = {
            "user_id": user_id,
            "username": username,
            "password_hash": password_hash,
            "role": role
        }

        users.append(new_user)

        cls.save_all_users(users)

        return new_user

    @classmethod
    def login(
        cls,
        username,
        password
    ):

        users = cls.get_all_users()

        for user in users:

            if user["username"] == username:

                if verify_password(
                    password,
                    user["password_hash"]
                ):

                    if user["role"] == "admin":

                        cls.current_user = Admin(
                            user["user_id"],
                            user["username"],
                            user["password_hash"]
                        )

                    else:

                        cls.current_user = Member(
                            user["user_id"],
                            user["username"],
                            user["password_hash"]
                        )

                    return cls.current_user

                raise ValueError(
                    "Incorrect password."
                )

        raise ValueError(
            "User not found."
        )

    @classmethod
    def logout(cls):
        cls.current_user = None

    @classmethod
    def get_current_user(cls):
        return cls.current_user