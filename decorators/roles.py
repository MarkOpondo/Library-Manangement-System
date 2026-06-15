from functools import wraps
from services.auth_service import AuthService


def admin_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        user = AuthService.get_current_user()

        if user is None:
            print("\nPlease login first.\n")
            return

        if user.role != "admin":
            print("\nAdmin access required.\n")
            return

        return func(*args, **kwargs)

    return wrapper