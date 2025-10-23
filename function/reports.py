import os
import csv
from function.menu_navigator import MenuNavigator
from datetime import datetime
from function.menu_navigator import MenuNavigator
import time


class Reports:
    def __init__(self, username):
        """
        Reports class for a given user.
        """
        self.username = username
        self.file_path = f"database/{username}/transactions.csv"

        self.menu = {
            "1": "Monthly Summary",
            "2": "Category Summary",
            "3": "Financial Health Report",
            "4": "Recurring Transactions",
            "5": "Back to Main Menu",
        }
        self.navigator = MenuNavigator(self.menu)

    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def read_transactions(self):
        """
        Reads transactions from the user's CSV file.
        Returns a list of transaction dictionaries.
        """
        transactions = []
        if not os.path.exists(self.file_path):
            return transactions

        with open(self.file_path, "r", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                row["amount"] = float(row["amount"])
                row["date"] = datetime.strptime(row["date"], "%Y-%m-%d").date()
                row["category"] = row["category"].strip().lower()
                transactions.append(row)
        return transactions

    def monthly_summary(self):
        """monthly report"""
        self.clear_screen()
        transactions = self.read_transactions()
        income_total = 0
        expenses_total = 0
        now = datetime.now()
        try:
            month = int(
                input("Enter month (1-12) or press Enter for current month: ")
                or now.month
            )
            year = int(
                input("Enter year or press Enter for current year: ") or now.year
            )

        except ValueError:
            print("Invalid input. Using current month and year.")
            time.sleep(2)
            self.clear_screen()
            month = now.month
            year = now.year

        if not (1 <= month <= 12) or year <= now.year:
            print("Invalid month or year. Using current month and year.")
            time.sleep(2) 
            self.clear_screen()
            month = now.month
            year = now.year

        for row in transactions:
            date = row["date"]
            if date.month == month and date.year == year:
                amount = row["amount"]
                if row["type"] == "income":
                    income_total += amount
                elif row["type"] == "expense":
                    expenses_total += amount

        net_total = income_total - expenses_total
        print(f"Monthly Summary for {month}/{year}:")
        print(f"Total income: ${income_total:.2f}")
        print(f"Total expenses: ${expenses_total:.2f}")
        print(f"Net total: ${net_total:.2f}")
        return income_total, expenses_total, net_total

    def category_summary(self):
        """category report"""
        self.clear_screen()
        transactions = self.read_transactions()
        category = input("Enter your desired category: ").strip().lower()
        total = 0
        for row in transactions:
            if row["category"] == category:
                amount = row["amount"]
                total += amount
        if total == 0:
            print(f"no transactions were found for {category} category")
        else:
            print(f"Total for category: {category} is : ${total:.2f}")

    def financial_health_report(self):
        """financial health report"""
        self.clear_screen()
        transactions = self.read_transactions()
        total_income = 0
        total_expenses = 0
        health_status = ""
        for row in transactions:
            amount = row["amount"]
            if row["type"] == "income":
                total_income += amount
            elif row["type"] == "expense":
                total_expenses += amount
        if total_income == 0:
            print("no income recorded, cannot calculate financial health.")
            return
        savings_rate = ((total_income - total_expenses) / total_income) * 100
        if savings_rate < 0:
            health_status = "broke"
        elif 0 <= savings_rate < 10:
            health_status = "struggling"
        elif 10 <= savings_rate < 20:
            health_status = "getting by"
        elif 20 <= savings_rate < 30:
            health_status = "promising"
        elif savings_rate >= 30:
            health_status = "healthy"
        elif savings_rate >= 50:
            health_status = "financial genius"
        print(f"Financial Health Report:")
        print(f"Total Income: ${total_income:.2f}")
        print(f"Total Expenses: ${total_expenses:.2f}")
        print(f"Savings Rate: {savings_rate:.2f}%")
        print(f"Financial Health Status: {health_status}")

    def recurring_transactions(self):
        """recurring transactions report"""
        self.clear_screen()
        transactions = self.read_transactions()
        transaction_count = {}
        for row in transactions:
            key = (row["type"], row["category"], row["amount"])
            if key in transaction_count:
                transaction_count[key] += 1
            else:
                transaction_count[key] = 1
        print("Recurring Transactions:")
        for key, count in transaction_count.items():
            if count > 1:
                t_type, category, amount = key
                print(
                    f"{t_type} of ${amount:.2f} in category '{category}' occurred {count} times."
                )

    def handle_choice(self, choice):
        """handle reports menu choice"""
        match choice:
            case "1":
                self.monthly_summary()
            case "2":
                self.category_summary()
            case "3":
                self.financial_health_report()
            case "4":
                self.recurring_transactions()
            case "5":
                return False
            case _:
                print("Invalid choice. Please try again.")
        input("Press Enter to continue...")
        return True

    def run(self):
        while True:
            print("\n--- Reports Menu ---")
            print("")
            print("")
            print("")
            print("")
            self.navigator.print_menu()
            choice = self.navigator.choice()
            if choice and not self.handle_choice(choice):
                break
