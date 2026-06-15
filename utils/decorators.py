from functools import wraps

def require_role(role):
    def decorator(func):
        @wraps(func)
        def wrapper(user, *args, **kwargs):
            if user["role"] != role:
                raise PermissionError("Access denied. Insufficient role.")
            return func(user, *args, **kwargs)
        return wrapper
    return decorator
