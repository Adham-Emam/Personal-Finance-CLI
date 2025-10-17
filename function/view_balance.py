import os
import csv


class ViewBalance:
    def __init__(self, username):
        self.username = username
        self.file_path = "database/transactions.csv"

    def calculate_balance(self):
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
        os.system("cls" if os.name == "nt" else "clear")
        total_income, total_expense = self.calculate_balance()
        print("💰 Balance Summary")
        print(f"Total Income: {total_income}$")
        print(f"Total Expense: {total_expense}$")
        print(f"Current Balance: {total_income - total_expense}$")
        input("Press Enter to continue...")
