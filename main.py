from services.auth_service import AuthService
from services.library_service import LibraryService


def get_input(prompt):
    value = input(prompt).strip()
    if not value:
        print("Input cannot be empty.")
        return None
    return value

def auth_menu():
    while True:

        print("\n===== LIBRARY SYSTEM =====")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose option: ").strip()

        if choice == "1":

            username = get_input("Username: ")
            password = get_input("Password: ")

            if username and password:
                try:
                    user = AuthService.register(username, password)
                    print(f"\nUser {user['username']} registered successfully.\n")
                except Exception as e:
                    print(e)

        elif choice == "2":

            username = get_input("Username: ")
            password = get_input("Password: ")

            if username and password:
                try:
                    user = AuthService.login(username, password)
                    print(f"\nWelcome {user.username}!\n")
                    main_menu()
                except Exception as e:
                    print(e)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


def user_menu():

    while True:

        print("\n===== USER MENU =====")
        print("1. View Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Logout")

        choice = input("Choose option: ").strip()

        if choice == "1":
            LibraryService.view_books()

        elif choice == "2":
            book_id = get_input("Enter Book ID: ")
            if book_id:
                LibraryService.borrow_book(book_id)

        elif choice == "3":
            book_id = get_input("Enter Book ID: ")
            if book_id:
                LibraryService.return_book(book_id)

        elif choice == "4":
            AuthService.logout()
            print("\nLogged out.\n")
            break

        else:
            print("Invalid option.")


def admin_menu():

    while True:

        print("\n===== ADMIN MENU =====")
        print("1. View Books")
        print("2. Add Book")
        print("3. Remove Book")
        print("4. Logout")

        choice = input("Choose option: ").strip()

        if choice == "1":
            LibraryService.view_books()

        elif choice == "2":

            title = get_input("Title: ")
            author = get_input("Author: ")
            category = get_input("Category: ")
            copies = get_input("Total Copies: ")

            if title and author and category and copies:

                if not copies.isdigit():
                    print("Copies must be a number.")
                    continue

                LibraryService.add_book(
                    title,
                    author,
                    category,
                    int(copies)
                )

        elif choice == "3":
            book_id = get_input("Book ID: ")
            if book_id:
                LibraryService.remove_book(book_id)

        elif choice == "4":
            AuthService.logout()
            print("\nLogged out.\n")
            break

        else:
            print("Invalid option.")

def main_menu():

    user = AuthService.get_current_user()

    if user.role == "admin":
        admin_menu()
    else:
        user_menu()

if __name__ == "__main__":
    auth_menu()

    