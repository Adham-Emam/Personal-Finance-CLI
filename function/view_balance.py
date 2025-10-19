import os
import csv
import time


class ViewBalance:
    def __init__(self, username):
        """
        Initializes a ViewBalance object.

        Parameters:
        username (str): The user's name

        Returns:
        None
        """
        self.username = username
        self.file_path = f"database/{username}/transactions.csv"

    def calculate_balance(self):
        """
        Calculates the user's total income and expense from the transactions CSV file.

        This function will iterate through the transactions CSV file and sum up the total income and expense for the given username.

        Returns a tuple containing the total income and total expense as integers.
        """
        total_income = 0
        total_expense = 0
        try:
            with open(self.file_path, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row["type"] == "income":
                        total_income += int(row["amount"])
                    elif row["type"] == "expense":
                        total_expense += int(row["amount"])
            return total_income, total_expense
        except FileNotFoundError:
            print(
                f"No transactions found for user '{self.username}'."
                f" Please add transactions first."
            )
            time.sleep(2)
            return None

    def run(self):
        """
        Prints the user's current balance.

        This function will clear the console, calculate the user's total income and expense from the transactions CSV file, and then print out the balance summary.

        If no transactions are found for the given user, it will print a message indicating so and wait for the user to press Enter before continuing.

        Returns:
        None
        """
        os.system("cls" if os.name == "nt" else "clear")
        if not self.calculate_balance() is None:
            total_income, total_expense = self.calculate_balance()
            print("💰 Balance Summary")
            print(f"Total Income: {total_income}$")
            print(f"Total Expense: {total_expense}$")
            print(f"Current Balance: {total_income - total_expense}$")
            input("Press Enter to continue...")
