from colorama import Fore, Style, init
from tabulate import tabulate
import os
import csv
import time
import datetime


init(autoreset=True)  # ensure color resets automatically


class ViewTransactions:
    def __init__(self, username):
        self.username = username
        self.file_path = f"database/{username}/transactions.csv"
        self.search_term = None
        self.transactions = self.get_transactions()

    def get_transactions(self):
        """
        Retrieves all transactions for the given user.

        This function will iterate through the transactions CSV file and add all transactions for the given user to the self.transactions list.

        Returns:
        list: A list of all transactions for the given user.
        """
        self.search_term = None
        transactions = []
        try:
            with open(self.file_path, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    transactions.append(row)
            return transactions
        except FileNotFoundError:
            print(
                f"No transactions found for user '{self.username}'."
                f" Please add transactions first."
            )
            time.sleep(2)
            return None

    def filter_category(self):
        """
        Filters all transactions for the given user by a category.

        This function will prompt the user to enter a category.
        It will then iterate through the transactions CSV file and add all transactions for the given user and category to the self.transactions list.

        Returns:
        list: A list of all transactions for the given user and category.
        """
        os.system("cls" if os.name == "nt" else "clear")

        while True:
            category = input("Enter the category to filter by: ").strip()

            if not category:
                print("Please enter a category.")
                continue
            break

        filtered = []

        for transaction in self.transactions:
            if transaction["category"] == category:
                filtered.append(transaction)

        if not filtered:
            print(f"No transactions found for category '{category}'.")

        self.transactions = filtered
        return self.transactions

    def filter_date(self):
        """
        Filters all transactions for the given user by a date range.

        This function will prompt the user to enter a start and end date.
        It will then iterate through the transactions CSV file and add all transactions for the given user and date range to the self.transactions list.

        Returns:
        list: A list of all transactions for the given user and date range.
        """
        os.system("cls" if os.name == "nt" else "clear")

        start_date, end_date = self.get_date_inputs()

        filtered = []

        for transaction in self.transactions:
            if transaction["date"] >= start_date and transaction["date"] <= end_date:
                filtered.append(transaction)

        if not filtered:
            print(
                f"No transactions found for date range '{start_date}' to '{end_date}'."
            )

        self.transactions = filtered
        return self.transactions

    def get_date_inputs(self):
        """
        Prompts user for start and end dates to filter transactions by.

        This function will continually prompt the user for a start and end date until a valid date is entered.

        The start date is required and the end date is optional. If the end date is not specified, it defaults to today's date.

        Returns a tuple containing the start date and end date as strings in the format YYYY-MM-DD.
        """
        while True:
            start_date = input(
                "Enter the start date to filter by (YYYY-MM-DD): "
            ).strip()

            if not start_date:
                print("Please enter a date.")
                continue

            try:
                datetime.datetime.strptime(start_date, "%Y-%m-%d")
                break
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")

        while True:
            end_date = (
                input(
                    "Enter the end date to filter by (YYYY-MM-DD) [default = today]: "
                ).strip()
                or datetime.date.today().isoformat()
            )

            try:
                datetime.datetime.strptime(end_date, "%Y-%m-%d")
                break
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")

        return start_date, end_date

    def sort_by(self):
        """
        Sorts the transactions by the given option.

        This function will continually prompt the user for an option until a valid option is entered.

        The options are:
        1. Sort by date in ascending order
        2. Sort by date in descending order (latest transactions first)
        3. Sort by amount in ascending order
        4. Sort by amount in descending order

        Returns a sorted list of transactions.

        """
        os.system("cls" if os.name == "nt" else "clear")
        print(
            f"Sort transaction by:\n1. Date Sorted\n2. Latest Transactions\n3. Amount ascending\n4. Amount descending"
        )

        while True:
            option = input("Enter the number of the option: ").strip()

            match option:
                case "1":
                    self.transactions.sort(key=lambda x: x["date"])
                    break

                case "2":
                    self.transactions.sort(key=lambda x: x["date"], reverse=True)
                    break

                case "3":
                    self.transactions.sort(
                        key=lambda x: int(x["amount"]),
                    )
                    break

                case "4":
                    self.transactions.sort(
                        key=lambda x: int(x["amount"]),
                        reverse=True,
                    )
                    break

                case _:
                    print("Invalid option. Please enter a number between 1 and 4.")

        return self.transactions

    def search(self):
        """
        Searches through all transactions for the given user and filters by a search query.

        This function will prompt the user to enter a search query.
        It will then iterate through the transactions CSV file and add all transactions for the given user and search query to the self.transactions list.

        Returns:
        list: A list of all transactions for the given user and search query.
        """
        os.system("cls" if os.name == "nt" else "clear")

        while True:
            search_term = input("Enter the search query: ").strip()

            if not search_term:
                print("Please enter a search query.")
                continue
            break

        self.search_term = search_term
        filtered = []

        for transaction in self.transactions:
            if any(
                search_term.lower() in str(value).lower()
                for value in transaction.values()
            ):
                filtered.append(transaction)

        if not filtered:
            print(f"No transactions found for search term '{search_term}'.")
        else:
            print(f"Found {len(filtered)} matching transactions.")

        self.transactions = filtered
        return self.transactions

    def highlight(self, text):
        """
        Highlights occurrences of the search term in the given text.
        """
        if not self.search_term:
            return text

        term = self.search_term
        lower_text = text.lower()
        lower_term = term.lower()

        start = 0
        highlighted = ""
        while True:
            index = lower_text.find(lower_term, start)
            if index == -1:
                highlighted += text[start:]
                break
            # add text before match, highlight match, continue
            highlighted += (
                text[start:index]
                + Fore.YELLOW
                + Style.BRIGHT
                + text[index : index + len(term)]
                + Style.RESET_ALL
            )
            start = index + len(term)
        return highlighted

    def run(self):
        """
        Prints all transactions for the given user.

        This function will clear the console, retrieve all transactions for the given user, and then print out each transaction in a formatted manner.

        If no transactions are found, it will print a message indicating so.

        After printing out all transactions, it will wait for the user to press Enter before continuing.
        """
        os.system("cls" if os.name == "nt" else "clear")

        if self.transactions is None:
            return

        if self.transactions:
            headers = ["Date", "Type", "Amount", "Category", "Description"]

            table_data = [
                [
                    self.highlight(t["date"]),
                    self.highlight(t["type"]),
                    self.highlight(t["amount"]),
                    self.highlight(t["category"]),
                    self.highlight(t["description"]),
                ]
                for t in self.transactions
            ]
            print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))

        else:
            print("No transactions found.")
        input("Press Enter to continue...")
