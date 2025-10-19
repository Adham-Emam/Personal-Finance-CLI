import os
import csv
import datetime


class AddExpense:
    def __init__(self, username):
        """
        Handles adding expense transactions for a given user.
        """
        self.username = username
        self.file_path = f"database/{username}/transactions.csv"

        if not os.path.exists(f"database/{username}"):
            os.mkdir(f"database/{username}")

    def add_expense(self):
        """
        Handles user input for adding a new expense transaction.
        All inputs are validated before saving.
        """
        amount = self.get_valid_amount()
        category = self.get_valid_category()
        description = input(
            "Enter the description of the transaction (optional): "
        ).strip()
        date = self.get_valid_date()

        # Confirm transaction details before saving
        os.system("cls" if os.name == "nt" else "clear")
        print("\nPlease confirm the transaction details:")
        print(f"Amount: {amount}")
        print(f"Category: {category}")
        print(f"Description: {description or 'N/A'}")
        print(f"Date: {date}")

        confirm = input("Confirm and save? (y/n): ").strip().lower()
        while confirm not in ["y", "n"]:
            confirm = input("Please enter 'y' or 'n': ").strip().lower()

        if confirm == "y":
            self.save_expense(amount, category, description, date)
            print("\n✅ Transaction added successfully.")
        else:
            print("\n❌ Transaction not added.")

    def get_valid_amount(self):
        """
        Prompt user for a valid positive number as amount.
        """
        while True:
            amount = input("Enter the amount of the transaction: ").strip()
            try:
                amount = int(amount)
                if amount <= 0:
                    print("Amount must be greater than zero.")
                else:
                    return amount
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

    def get_valid_category(self):
        """
        Prompts user for a non-empty input string.
        """
        while True:
            value = input("Enter the category of the transaction: ").strip()

            if not value:
                print("This field cannot be empty.")
                continue
            if not value.isalpha():
                print("This field can only contain letters.")
                continue
            if not 3 <= len(value) <= 20:
                print("This field must be between 3 and 20 characters.")
                continue

            return value

    def get_valid_date(self):
        """
        Validates date input or uses today's date by default.
        """
        while True:
            date_str = input("Enter the date (YYYY-MM-DD) [default = today]: ").strip()
            if not date_str:
                return datetime.date.today().isoformat()
            try:
                datetime.datetime.strptime(date_str, "%Y-%m-%d")
                return date_str
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")

    def save_expense(self, amount, category, description, date):
        """
        Appends the expense transaction to a CSV file.
        """
        # Ensure the CSV file has headers if it’s newly created
        file_exists = False
        try:
            with open(self.file_path, "r"):
                file_exists = True
        except FileNotFoundError:
            pass

        with open(self.file_path, "a", newline="") as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["amount", "category", "description", "date", "type"])
            writer.writerow(
                [
                    amount,
                    category,
                    description,
                    date,
                    "expense",
                ]
            )

    def run(self):
        """
        Entry point for running this menu.
        """
        os.system("cls" if os.name == "nt" else "clear")
        self.add_expense()
