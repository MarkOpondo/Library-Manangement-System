import hashlib
from utils.persistence import load_data, save_data

USERS_FILE = "data/users.json"

def register_user(username, password, role="user"):
    users = load_data(USERS_FILE)
    hashed_pw = hashlib.sha256(password.encode()).hexdigest()
    user_id = len(users) + 1
    users.append({"id": user_id, "username": username, "password": hashed_pw, "role": role})
    save_data(USERS_FILE, users)
    return f"User '{username}' registered successfully."

def login_user(username, password):
    users = load_data(USERS_FILE)
    hashed_pw = hashlib.sha256(password.encode()).hexdigest()
    for user in users:
        if user["username"] == username and user["password"] == hashed_pw:
            return user
    return None
