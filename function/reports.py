import os
import csv
from function.menu_navigator import MenuNavigator
from datetime import datetime
from function.menu_navigator import MenuNavigator
import time
from rich.console import Console
from rich.table import Table


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
        console = Console()
        table = Table(
            title="Monthly summary report", show_lines=True, style="bold green"
        )
        table.add_column("Metric", justify="left", style="magenta")
        table.add_column("Total", justify="right", style="cyan")

        now = datetime.now()
        try:
            month = int(
                input("Enter month (1-12) or press Enter for current month: ")
                or now.month
            )
            year = int(
                input("Enter year or press Enter for current year: ") or now.year
            )

            if month < 1 or month > 12:
                raise ValueError()

        except ValueError:
            print("Invalid month or year. Using current month and year.")
            time.sleep(2)
            month = now.month
            year = now.year

        self.clear_screen()

        for row in transactions:
            date = row["date"]
            if date.month == month and date.year == year:
                amount = row["amount"]
                if row["type"] == "income":
                    income_total += amount
                elif row["type"] == "expense":
                    expenses_total += amount

        net_total = income_total - expenses_total
        table.add_row("Total Income", f"${income_total:.2f}")
        table.add_row("Total Expenses", f"${expenses_total:.2f}")
        table.add_row("Net Total", f"${net_total:.2f}")
        console.print(table)
        max_value = max(income_total, expenses_total, abs(net_total))
        console.print(
            f"[bold yellow]Visual Representation for {month}/{year}:[/bold yellow]"
        )
        console.print(
            f"\n  Income : {'█'* int(income_total/max_value * 40 )} ${income_total:.2f}",
            style="bold green",
        )
        console.print(
            f"\nExpenses : {'█'* int(expenses_total/max_value * 40 )} ${expenses_total:.2f}",
            style="bold green",
        )
        console.print(
            f"\n     Net : {'█'* int(net_total/max_value * 40 )} ${net_total:.2f}",
            style="bold green",
        )
        return income_total, expenses_total, net_total

    def category_summary(self):
        """category report"""
        self.clear_screen()
        transactions = self.read_transactions()
        console = Console()
        category_totals = {}
        income_total = 0
        expenses_total = 0
        for row in transactions:
            amount = row["amount"]
            if row["type"] == "income":
                income_total += amount
            elif row["type"] == "expense":
                expenses_total += amount

        net_total = income_total - expenses_total
        for row in transactions:
            category = row["category"]
            amount = row["amount"]
            t_type = row["type"]
            if category not in category_totals:
                category_totals[category] = {"income": 0, "expense": 0}

            category_totals[category][t_type] += amount
        table = Table(
            title="Category Summary Report", show_lines=True, style="bold green"
        )
        table.add_column("Category", justify="left", style="magenta")
        table.add_column("Income", justify="right", style="green")
        table.add_column("Expense", justify="right", style="red")
        table.add_column("Net", justify="right", style="cyan")

        for category, data in category_totals.items():
            income = data["income"]
            expense = data["expense"]
            net = income - expense
            table.add_row(
                category.capitalize(),
                f"${income:.2f}",
                f"${expense:.2f}",
                f"${net:.2f}",
            )
        table.add_row(
            "Total",
            f"${income_total:.2f}",
            f"${expenses_total:.2f}",
            f"${net_total:.2f}",
            style="bold yellow",
        )
        console.print(table)

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
        self.clear_screen()
        transactions = self.read_transactions()
        if not transactions:
            print("No transactions found, Please add transactions first.")
            time.sleep(2)
            return

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
