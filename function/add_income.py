import os
import csv
import datetime


class AddIncome:
    def __init__(self, username):
        """
        Handles adding income transactions for a given user.
        """
        self.username = username
        self.file_path = "database/transactions.csv"

    def add_income(self):
        """
        Handles user input for adding a new income transaction.
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
            self.save_income(amount, category, description, date)
            print("\n✅ Transaction added successfully.")
        else:
            print("\n❌ Transaction not added.")

    # ---------- Helper Methods ----------

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

    def save_income(self, amount, category, description, date):
        """
        Appends the income transaction to a CSV file.
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
                writer.writerow(
                    ["username", "amount", "category", "description", "date", "type"]
                )
            writer.writerow(
                [self.username, amount, category, description, date, "income"]
            )

    def run(self):
        """
        Entry point for running this menu.
        """
        os.system("cls" if os.name == "nt" else "clear")
        self.add_income()
