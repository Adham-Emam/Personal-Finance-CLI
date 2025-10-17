import os
import csv


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
        self.file_path = "database/transactions.csv"

    def calculate_balance(self):
        """
        Calculates the user's total income and expense from the transactions CSV file.

        This function will iterate through the transactions CSV file and sum up the total income and expense for the given username.

        Returns a tuple containing the total income and total expense as integers.
        """
        total_income = 0
        total_expense = 0
        with open(self.file_path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["username"] == self.username:
                    if row["type"] == "income":
                        total_income += int(row["amount"])
                    elif row["type"] == "expense":
                        total_expense += int(row["amount"])
        return total_income, total_expense

    def run(self):
        """
        Clears the console, calculates the user's total income and expense, and then prints out a balance summary.

        This includes the total income, total expense, and the current balance.

        After printing out the balance summary, it waits for the user to press Enter before continuing.
        """
        os.system("cls" if os.name == "nt" else "clear")
        total_income, total_expense = self.calculate_balance()
        print("💰 Balance Summary")
        print(f"Total Income: {total_income}$")
        print(f"Total Expense: {total_expense}$")
        print(f"Current Balance: {total_income - total_expense}$")
        input("Press Enter to continue...")
