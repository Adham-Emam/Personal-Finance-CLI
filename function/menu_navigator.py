import os
import sys
import time


class MenuNavigator:
    def __init__(self, menu):
        """
        Initializes a MenuNavigator object.

        Parameters:
        menu (dict): A dictionary with menu items as keys and descriptions as values.

        Returns:
        None
        """
        self.menu = menu

    def print_menu(self):
        """
        Prints the menu items to the console.

        Clears the console and then prints out the menu items.
        """
        os.system("cls" if os.name == "nt" else "clear")

        for key, value in self.menu.items():
            print(f"{key}. {value}")

    def choice(self):
        """
        Prompts the user to enter a choice and validates the input.

        If the user enters "0", it will exit the program.
        Otherwise, it will continue to prompt the user until a valid choice is entered.

        Returns:
            str: The user's choice
        """
        choice = input("Enter your choice: ")
        if choice == "0":
            self.exit()
            return

        while not self.validate_choice(choice):
            choice = input("Please enter a valid choice: ")
        return choice

    def validate_choice(self, choice):
        """
        Validates the user's choice against the menu items.

        Parameters:
        choice (str): The user's choice

        Returns:
        bool: True if the choice is valid, False otherwise
        """
        if choice in self.menu.keys():
            return True
        else:
            return False

    def exit(self):
        """
        Exits the program.

        Prompts the user to confirm they want to exit, and if so, clears the console and exits the program.
        If the user chooses not to exit, it returns to the main menu after a short delay.
        """
        os.system("cls" if os.name == "nt" else "clear")

        choice = input("Are you sure you want to exit? (y/n): ")
        if choice.lower() == "y":
            os.system("cls" if os.name == "nt" else "clear")
            sys.exit()
        else:
            print("Returning back...")
            time.sleep(2)
