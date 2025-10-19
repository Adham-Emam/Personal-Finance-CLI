import os
import csv
import time
import datetime
from function.menu_navigator import MenuNavigator


class EditTransaction:
    def __init__(self, username):
        self.username = username
        self.file_path = f"database/{username}/transactions.csv"
        self.transactions = self.get_transactions()
        self.menu = {
            "1": "💰 Change amount",
            "2": "🏷️ Change category",
            "3": "📝 Edit description",
            "4": "📅 Change date",
            "5": "🔄 Change type (Income/Expense)",
            "6": "💾 Save changes",
            "7": "🔙 Back to Main Menu",
            "0": "🚪 Exit",
        }

    def get_transactions(self):
        transactions = []
        try:
            with open(self.file_path, "r") as file:
                reader = csv.reader(file)
                next(reader)  # Skip headers
                for row in reader:
                    transactions.append(row)
            return transactions
        except FileNotFoundError:
            os.system("cls" if os.name == "nt" else "clear")
            print(
                f"No transactions found for user '{self.username}'."
                f" Please add transactions first."
            )
            time.sleep(2)
            return None

    def run(self):
        os.system("cls" if os.name == "nt" else "clear")

        if self.transactions is None:
            return

        for i, transaction in enumerate(self.transactions, 1):
            print(
                f"ID: {i}\n"
                f"Type: {transaction[4]}\n"
                f"Category: {transaction[1]}\n"
                f"Amount: {transaction[0]}\n"
                f"Date: {transaction[3]}\n"
                f"Description: {transaction[2]}"
            )
            print("-" * 30)

        while True:
            transaction_id = input(
                "Enter the ID of the transaction to edit or type '0' to go back: "
            )

            if int(transaction_id) == 0:
                return

            if not transaction_id.isdigit():
                print("Invalid input. Please enter a valid transaction ID.")
                continue
            elif not 1 <= int(transaction_id) <= len(self.transactions):
                print("Invalid transaction ID. Please enter a valid transaction ID.")
                continue
            break

        os.system("cls" if os.name == "nt" else "clear")
        menu = MenuNavigator(self.menu)
        while True:
            menu.print_menu()
            choice = menu.choice()
            self.handle_choice(choice, transaction_id)
            if choice == "7":
                print("Returning to main menu...")
                time.sleep(2)
                break
            elif choice == "0":
                print("Exiting...")
                time.sleep(2)
                MenuNavigator.exit()

    def handle_choice(self, choice, transaction_id):
        match choice:
            case "1":
                self.change_amount(transaction_id)
            case "2":
                self.change_category(transaction_id)
            case "3":
                self.edit_description(transaction_id)
            case "4":
                self.change_date(transaction_id)
            case "5":
                self.change_type(transaction_id)
            case "6":
                self.save_change()

    def change_amount(self, transaction_id):
        os.system("cls" if os.name == "nt" else "clear")
        while True:
            print("Old amount:", self.transactions[int(transaction_id) - 1][0])
            new_value = input("Enter the new amount: ")

            if not new_value.isdigit():
                print("Invalid input. Please enter a valid amount.")
                continue
            break

        self.transactions[int(transaction_id) - 1][0] = int(new_value)

    def change_category(self, transaction_id):
        os.system("cls" if os.name == "nt" else "clear")
        while True:
            print("Old category:", self.transactions[int(transaction_id) - 1][1])
            new_value = input("Enter the new category: ")

            if not new_value:
                print("This field cannot be empty.")
                continue

            if not new_value.isalpha():
                print("This field can only contain letters.")
                continue

            if not 3 <= len(new_value) <= 20:
                print("This field must be between 3 and 20 characters.")
                continue

            break

        self.transactions[int(transaction_id) - 1][1] = new_value

    def edit_description(self, transaction_id):
        os.system("cls" if os.name == "nt" else "clear")
        print("Old description:", self.transactions[int(transaction_id) - 1][2])
        new_value = input("Enter the new description: ")

        self.transactions[int(transaction_id) - 1][2] = new_value

    def change_date(self, transaction_id):
        os.system("cls" if os.name == "nt" else "clear")
        while True:
            print("Old date:", self.transactions[int(transaction_id) - 1][3])
            new_value = input("Enter the new date: ")

            if not new_value:
                print("This field cannot be empty.")
                continue

            try:
                datetime.datetime.strptime(new_value, "%Y-%m-%d")
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
                continue

            break

        self.transactions[int(transaction_id) - 1][3] = new_value

    def change_type(self, transaction_id):
        os.system("cls" if os.name == "nt" else "clear")
        while True:
            old_type = self.transactions[int(transaction_id) - 1][4]
            print("Old type:", self.transactions[int(transaction_id) - 1][4])
            new_value = input(
                f"Are you sure you want to change the type to {'expense' if old_type == 'income' else 'Income'}? (y/n): "
            )

            if new_value.lower() not in {"y", "n"}:
                print("Invalid input. Please enter 'y' or 'n'.")
                continue

            if new_value.lower() == "y":
                new_type = "expense" if old_type == "income" else "income"
                self.transactions[int(transaction_id) - 1][4] = new_type
            break

    def save_change(self):
        fieldnames = ["amount", "category", "description", "date", "type"]
        with open(self.file_path, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            if os.path.getsize(self.file_path) == 0:
                writer.writeheader()
            for transaction in self.transactions:
                writer.writerow(
                    {
                        "amount": transaction[0],
                        "category": transaction[1],
                        "description": transaction[2],
                        "date": transaction[3],
                        "type": transaction[4],
                    }
                )
        os.system("cls" if os.name == "nt" else "clear")
        print("✅ Changes saved successfully!")
        time.sleep(2)
