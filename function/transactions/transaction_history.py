import os
import time
import csv
import datetime
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
            "6": "📥 Import Data from CSV",
            "7": "📤 Export Data to CSV",
            "8": "🔙 Back to Main Menu",
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
        if self.view_transactions.transactions is None:
            return

        while True:
            os.system("cls" if os.name == "nt" else "clear")
            print(f"🧾 Transaction History for {self.username}\n" + "=" * 40)

            menu = MenuNavigator(self.menu)
            menu.print_menu()
            choice = menu.choice()

            if choice == "8":
                print("Returning to main menu...")
                time.sleep(2)
                break
            elif choice == "0":
                print("Exiting...")
                time.sleep(2)
                MenuNavigator.exit()
            self.handle_choice(choice)

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
            case "6":
                self.import_data()
            case "7":
                self.export_data()
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

    def import_data(self):
        os.system("cls" if os.name == "nt" else "clear")

        while True:
            file_path = input(
                "Enter the path to the CSV file or type '0' to cancel: "
            ).strip()

            if file_path == "0":
                print("Returning back to main menu...")
                time.sleep(2)
                return

            if not os.path.isfile(file_path):
                print("File not found. Please enter a valid file path.")
                continue

            if not file_path.lower().endswith(".csv"):
                print("Invalid file format. Please enter a CSV file.")
                continue

            break

        dest_file = f"database/{self.username}/transactions.csv"

        imported_rows = 0
        skipped_rows = 0

        try:
            with open(file_path, "r") as source_file:
                fieldnames = {"amount", "category", "description", "date", "type"}
                reader = csv.DictReader(source_file)

                if not fieldnames.issubset(reader.fieldnames):
                    print("Invalid CSV file format. Missing required headers.")
                    time.sleep(2)
                    return

                with open(dest_file, "a", newline="") as dest_csv:
                    writer = csv.writer(dest_csv)

                    for i, row in enumerate(reader, start=2):
                        amount = row.get("amount", "").strip()
                        category = row.get("category", "").strip()
                        description = row.get("description", "").strip()
                        date_str = row.get("date", "").strip()
                        transaction_type = row.get("type", "").strip()

                        if not amount.isdigit() or int(amount) <= 0:
                            print(f"⚠️  Line {i}: Invalid amount '{amount}'. Skipped.")
                            skipped_rows += 1
                            continue

                        if not category.isalpha() or not (3 <= len(category) <= 20):
                            print(
                                f"⚠️  Line {i}: Invalid category '{category}'. Skipped."
                            )
                            skipped_rows += 1
                            continue

                        try:
                            datetime.datetime.strptime(date_str, "%Y-%m-%d")
                        except ValueError:
                            print(f"⚠️  Line {i}: Invalid date '{date_str}'. Skipped.")
                            skipped_rows += 1
                            continue

                        if not transaction_type.lower() in ["expense", "income"]:
                            print(
                                f"⚠️  Line {i}: Invalid transaction type '{transaction_type}'. Skipped."
                            )
                            skipped_rows += 1
                            continue

                        writer.writerow(
                            [
                                amount,
                                category,
                                description,
                                date_str,
                                transaction_type.lower(),
                            ]
                        )
                        imported_rows += 1
            print(
                f"\n✅ Successfully imported {imported_rows} transactions.\n⚠️ Skipped {skipped_rows} invalid rows."
            )
            time.sleep(2)
        except Exception as e:
            print(f"An error occurred during import: {e}")
            time.sleep(2)

    def export_data(self):
        os.system("cls" if os.name == "nt" else "clear")
        while True:
            file_path = input(
                "Enter the directory path to save the CSV file or type '0' to cancel: "
            ).strip()

            if file_path == "0":
                print("Returning back to main menu...")
                time.sleep(2)
                return

            if os.path.isdir(file_path):
                break
            else:
                print("Invalid directory path. Please try again.")

        with open(
            f"{file_path}/{self.username}_transactions_backup.csv", "w", newline=""
        ) as file:
            writer = csv.writer(file)
            writer.writerow(["amount", "category", "description", "date", "type"])
            for transaction in self.view_transactions.transactions:
                writer.writerow(
                    [
                        transaction["amount"],
                        transaction["category"],
                        transaction["description"],
                        transaction["date"],
                        transaction["type"],
                    ]
                )
        print("✅ Data exported successfully!")
        time.sleep(2)
