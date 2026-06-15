import sys
from utils.auth import register_user, login_user
from utils.persistence import load_data, save_data
from models.book import Book
from models.admin import Admin
from models.transaction import Transaction

BOOKS_FILE = "data/books.json"
TRANSACTIONS_FILE = "data/transactions.json"

def main():
    print("📚 Welcome to the Library Management System 📚")
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            role = input("Enter role (user/admin): ")
            print(register_user(username, password, role))

        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            user = login_user(username, password)
            if user:
                print(f"Login successful! Welcome {user['username']} ({user['role']})")
                if user["role"] == "admin":
                    admin_menu(user)
                else:
                    user_menu(user)
            else:
                print("Invalid credentials.")

        elif choice == "3":
            print("Goodbye!")
            sys.exit()

def admin_menu(user):
    while True:
        print("\nAdmin Menu:\n1. Add Book\n2. Remove Book\n3. View Books\n4. Logout")
        choice = input("Choose: ")
        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            category = input("Category: ")
            copies = int(input("Available copies: "))
            books = load_data(BOOKS_FILE)
            book_id = len(books) + 1
            new_book = {"id": book_id, "title": title, "author": author, "category": category, "availableCopies": copies}
            books.append(new_book)
            save_data(BOOKS_FILE, books)
            print(f"Book '{title}' added.")
        elif choice == "2":
            book_id = int(input("Book ID to remove: "))
            books = load_data(BOOKS_FILE)
