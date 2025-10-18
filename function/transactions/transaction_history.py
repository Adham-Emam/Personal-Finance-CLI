import os
from function.menu_navigator import MenuNavigator
from function.transactions.view_transactions import ViewTransactions


class TransactionHistory:
    def __init__(self, username):
        self.username = username
        self.menu = {
            "1": "📋 View All Transactions",
            "2": "🏷️ Filter by Category",
            "3": "📅 Filter by Date Range",
            "4": "↕️ Sort (by Date or Amount)",
            "5": "🔍 Search by Keyword",
            "6": "🔙 Back to Main Menu",
            "0": "🚪 Exit",
        }
        self.view_transactions = ViewTransactions(self.username)

    def run(self):
        """
        Runs the Transaction History menu.

        This function will continually prompt the user with the Transaction History menu until the user chooses to exit or return to the main menu.

        The menu will display all transactions for the given user, and allow the user to filter by category, date range, or keyword.

        Returns:
        None
        """
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            print(f"🧾 Transaction History for {self.username}\n" + "=" * 40)

            menu = MenuNavigator(self.menu)
            menu.print_menu()
            choice = menu.choice()

            if choice in {"6", "0"}:
                print("Returning to main menu..." if choice == "6" else "Exiting...")
                break

            self.handle_choice(choice)

    def handle_choice(self, choice):
        match choice:
            case "1":
                self.view_all_transactions()
            case "2":
                self.filter_by_category()
            case "3":
                self.filter_by_date_range()
            case "4":
                self.sort_by_date_or_amount()
            case "5":
                self.search_by_keyword()
            case _:
                print("Invalid choice. Please try again.")

    def view_all_transactions(self):
        self.view_transactions.get_transactions()
        self.view_transactions.run()

    def filter_by_category(self):
        self.view_transactions.filter_category()
        self.view_transactions.run()

    def filter_by_date_range(self):
        self.view_transactions.filter_date()
        self.view_transactions.run()

    def sort_by_date_or_amount(self):
        self.view_transactions.sort_by()
        self.view_transactions.run()

    def search_by_keyword(self):
        self.view_transactions.search()
        self.view_transactions.run()
