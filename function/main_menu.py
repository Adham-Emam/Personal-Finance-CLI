import sys
from menu_navigator import MenuNavigator
from add_income import AddIncome


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
            "1": "Add Income",
            "2": "Add Expense",
            "3": "View Balance",
            "4": "Transaction History",
            "5": "Edit Transaction",
            "6": "Delete Transaction",
            "7": "Reports",
            "8": "Settings",
            "9": "Help",
            "0": "Exit",
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
                print("Add Expense")
            case "3":
                print("View Balance")
            case "4":
                print("Transaction History")
            case "5":
                print("Edit Transaction")
            case "6":
                print("Delete Transaction")
            case "7":
                print("Reports")
            case "8":
                print("Settings")
            case "9":
                print("Help")

    # ---------- Menu Actions ----------

    def add_income(self):
        """
        Opens the Add Income submenu.
        """
        add_income = AddIncome(self.username)
        add_income.run()

    def add_expense(self):
        """
        Placeholder for Add Expense submenu.
        """
        print("Add Expense - coming soon...")

    def view_balance(self):
        print("View Balance - coming soon...")

    def transaction_history(self):
        print("Transaction History - coming soon...")

    def edit_transaction(self):
        print("Edit Transaction - coming soon...")

    def delete_transaction(self):
        print("Delete Transaction - coming soon...")

    def reports(self):
        print("Reports - coming soon...")

    def settings(self):
        print("Settings - coming soon...")

    def help_menu(self):
        print("Help - coming soon...")
