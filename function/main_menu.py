import os
import webbrowser
import time
from function.menu_navigator import MenuNavigator
from function.add_income import AddIncome
from function.add_expense import AddExpense
from function.view_balance import ViewBalance
from function.transactions.transaction_history import TransactionHistory
from function.transactions.edit_transaction import EditTransaction
from function.transactions.delete_transaction import DeleteTransaction
from function.settings import Settings


class MainMenu:
    def __init__(self, username):
        """
        Initializes the MainMenu class.

        Parameters:
        name (str): The user's name

        Returns:
        None
        """
        self.username = username
        self.menu = {
            "1": "➕ Add Income",
            "2": "➖ Add Expense",
            "3": "💰 View Balance",
            "4": "📜 Transaction History",
            "5": "✏️ Edit Transaction",
            "6": "🗑️ Delete Transaction",
            "7": "📊 Reports",
            "8": "⚙️ Settings",
            "9": "❓ Help",
            "0": "🚪 Exit",
        }

    def run(self):
        """
        Runs the main menu for the personal finance CLI.

        Prints the menu items and accepts user input.
        Based on the user's input, it will execute the corresponding action.
        """
        menu = MenuNavigator(self.menu)
        while True:
            menu.print_menu()
            choice = menu.choice()
            self.handle_choice(choice)

    def handle_choice(self, choice):
        """
        Handles the user's choice and executes the corresponding action.

        Parameters:
        choice (str): The user's choice

        Returns:
        None
        """
        match choice:
            case "1":
                self.add_income()
            case "2":
                self.add_expense()
            case "3":
                self.view_balance()
            case "4":
                self.transaction_history()
            case "5":
                self.edit_transaction()
            case "6":
                self.delete_transaction()
            case "7":
                print("Reports")
            case "8":
                self.settings()
            case "9":
                self.help_menu()

    # ---------- Menu Actions ----------

    def add_income(self):
        """
        Opens the Add Income submenu.
        """
        add_income = AddIncome(self.username)
        add_income.run()

    def add_expense(self):
        """
        Opens the Add Income submenu.
        """
        add_expense = AddExpense(self.username)
        add_expense.run()

    def view_balance(self):
        """
        Opens the View Balance submenu.

        This menu item will display the user's current balance by calculating the total income and total expense from the transactions CSV file.

        Returns:
        None
        """
        view_balance = ViewBalance(self.username)
        view_balance.run()

    def transaction_history(self):
        """
        Opens the Transaction History submenu.

        This menu item will display all transactions for the given user.

        Returns:
        None
        """
        transaction_menu = TransactionHistory(self.username)
        transaction_menu.run()

    def edit_transaction(self):
        """
        Opens the Edit Transaction submenu.

        This menu item will allow the user to edit a specific transaction by ID.

        Returns:
        None
        """
        edit_transaction = EditTransaction(self.username)
        edit_transaction.run()

    def delete_transaction(self):
        """
        Opens the Delete Transaction submenu.

        This menu item will allow the user to delete a specific transaction by ID.

        Returns:
        None
        """
        delete_transaction = DeleteTransaction(self.username)
        delete_transaction.run()

    def reports(self):
        print("Reports - coming soon...")

    def settings(self):
        """
        Opens the Settings submenu.

        This menu item will allow the user to edit their profile information, change their password, reset all data, or return to the main menu.

        Returns:
        None
        """
        settings = Settings(self.username)
        settings.run()

    def help_menu(self):
        """
        Opens the GitHub Documentation page for the Personal Finance CLI project.

        Clears the console, opens the README page in the default web browser,
        waits for a second, and then prompts the user to press Enter to continue.
        """
        os.system("cls" if os.name == "nt" else "clear")
        webbrowser.open(
            "https://github.com/Adham-Emam/Personal-Finance-CLI/blob/main/README.md"
        )
        time.sleep(1)
        input("Press Enter to continue...")
