import os
import csv
import time
import getpass
from function.menu_navigator import MenuNavigator
from function.auth import Authenticator
from utils.currencies import currencies


class Settings:
    def __init__(self, username):
        self.username = username
        self.menu = {
            "1": "📝 Edit Profile",
            "2": "🔑 Change Password",
            "3": "🗑️ Reset All Data",
            "4": "🔙 Back to Main Menu",
            "0": "🚪 Exit",
        }
        self.users_file = "database/users.json"
        self.db_path = f"database/{username}/transactions.csv"
        self.menu_navigator = MenuNavigator(self.menu)
        self.auth = Authenticator()

    def run(self):
        os.system("cls" if os.name == "nt" else "clear")
        while True:
            self.menu_navigator.print_menu()
            choice = self.menu_navigator.choice()
            if choice == "0":
                self.menu_navigator.exit()
                return
            if choice == "4":
                return

            if self.menu_navigator.validate_choice(choice):
                self.handle_choice(choice)
                break
            else:
                print("Please enter a valid choice.")

    def handle_choice(self, choice):
        match choice:
            case "1":
                self.edit_profile()
            case "2":
                self.change_password()
            case "3":
                self.reset_all_data()

    def edit_profile(self):
        """
        Allows the user to edit their profile information.

        This function will retrieve the user's current profile information from the users JSON file.
        It will then prompt the user to enter their new first name, last name, and currency.
        If any of the fields are left blank, the current value will be used instead.
        The new profile information will then be stored in the users JSON file.
        """
        os.system("cls" if os.name == "nt" else "clear")
        users = self.auth.load_users()
        user = users.get(self.username, {})

        first_name = input(
            f"Current first name: {user.get('first_name', '')}. Enter new first name (leave blank to keep current): "
        ).strip()
        if not first_name:
            first_name = user.get("first_name", "")

        last_name = input(
            f"Current last name: {user.get('last_name', '')}. Enter new last name (leave blank to keep current): "
        ).strip()
        if not last_name:
            last_name = user.get("last_name", "")

        currency = (
            input(
                f"Current currency: {user.get('currency', 'USD')}. Enter new currency (leave blank to keep current): "
            )
            .upper()
            .strip()
        )
        if not currency or currency not in currencies:
            print("Invalid currency. Using the current currency.")
            time.sleep(2)
            currency = user.get("currency", "USD")

        user["first_name"] = first_name
        user["last_name"] = last_name
        user["currency"] = currency
        users[self.username] = user
        self.auth.save_users(users)

    def change_password(self):
        """
        Changes the user's password.

        This function will prompt the user to enter their old password, which is verified against the stored password hash.
        If the old password is correct, the user is prompted to enter a new password, which is validated against the password rules (min 8 chars).
        If the new password is valid, it is hashed and stored in the users JSON file.
        If the passwords do not match, the user is prompted to try again.
        If the old password is incorrect, the user is prompted to try again.
        """
        os.system("cls" if os.name == "nt" else "clear")
        users = self.auth.load_users()

        # Get Old Password
        while True:
            old_password = getpass.getpass("Enter your old password: ")
            hashed_password = users[self.username]["password"]

            if not self.auth.verify_password(old_password, hashed_password):
                print("Incorrect password. Try again.")
            else:
                break

        # Get New Password & Confirm
        while True:
            new_password = getpass.getpass("Enter your new password: ")

            if not self.auth.validate_password(new_password):
                print("Password too short (min 8 chars). Try again.")
                continue
            elif new_password == old_password:
                print("New password cannot be the same as old password. Try again.")
                continue

            confirm_password = getpass.getpass("Confirm your new password: ")

            if new_password != confirm_password:
                print("Passwords do not match. Try again.")
            else:
                break

        # Update Password
        users[self.username]["password"] = self.auth.hash_password(new_password)
        self.auth.save_users(users)

        os.system("cls" if os.name == "nt" else "clear")
        print("✅ Password changed successfully.")
        time.sleep(2)

    def reset_all_data(self):
        """
        Resets all transactions for the given user.

        This function will continually prompt the user until a valid choice is entered.
        If the user chooses to reset all transactions, it will overwrite the transactions CSV file and reset all transactions to an empty state.
        """
        os.system("cls" if os.name == "nt" else "clear")
        while True:
            choice = (
                input("Are you sure you want to reset all your transactions? (y/n) ")
                .strip()
                .lower()
            )
            if choice in ["y", "n"]:
                break
        if choice == "y":
            headers = ["amount", "category", "description", "date", "type"]
            try:
                with open(self.db_path, "w") as f:
                    writer = csv.writer(f)
                    writer.writerow(headers)
                print("✅ All transactions has been reset.")
                time.sleep(2)
            except FileNotFoundError:
                print("No transactions found. Nothing to reset.")
                time.sleep(2)
