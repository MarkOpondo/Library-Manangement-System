from functools import wraps
from services.auth_service import AuthService


def login_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        if AuthService.get_current_user() is None:
            print("\nPlease login first.\n")
            return

        return func(*args, **kwargs)

    return wrapper