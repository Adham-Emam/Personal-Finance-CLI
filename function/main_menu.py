import sys
from menu_navigator import MenuNavigator


class MainMenu:
    def __init__(self, username, balance):
        """
        Initializes the MainMenu class.

        Parameters:
        name (str): The user's name
        balance (int): The user's balance

        Returns:
        None
        """
        self.username = username
        self.balance = balance
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
                print("Add Income")
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
