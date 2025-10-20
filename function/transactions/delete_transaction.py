import os
import time
import csv
from tabulate import tabulate


class DeleteTransaction:
    def __init__(self, username):
        self.username = username
        self.file_path = f"database/{username}/transactions.csv"
        self.transactions = self.get_transactions()

    def get_transactions(self):
        transactions = []
        try:
            with open(self.file_path, "r") as file:
                reader = csv.reader(file)
                next(reader)  # Skip headers
                for row in reader:
                    transactions.append(row)
            return transactions
        except FileNotFoundError:
            os.system("cls" if os.name == "nt" else "clear")
            print(
                f"No transactions found for user '{self.username}'."
                f" Please add transactions first."
            )
            time.sleep(2)
            return None

    def run(self):
        os.system("cls" if os.name == "nt" else "clear")

        if self.transactions is None:
            return

        headers = ["ID", "Type", "Category", "Amount", "Date", "Description"]

        table_data = [
            [
                i,
                transaction[4],
                transaction[1],
                transaction[0],
                transaction[3],
                transaction[2],
            ]
            for i, transaction in enumerate(self.transactions, 1)
        ]

        print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))

        while True:
            transaction_id = input(
                "Enter the ID of the transaction to Delete or type '0' to go back: "
            )

            if int(transaction_id) == 0:
                return

            if not transaction_id.isdigit():
                print("Invalid input. Please enter a valid transaction ID.")
                continue
            elif not 1 <= int(transaction_id) <= len(self.transactions):
                print("Invalid transaction ID. Please enter a valid transaction ID.")
                continue
            break

        os.system("cls" if os.name == "nt" else "clear")
        while True:
            confirm = input("Are you sure you want to delete this transaction? (y/n): ")
            if confirm.lower() not in ["y", "n"]:
                print("Invalid input. Please enter 'y' or 'n'.")
                continue
            if confirm.lower() == "y":
                self.delete_transaction(int(transaction_id))
                break
            else:
                break

    def delete_transaction(self, transaction_id):
        fieldnames = ["amount", "category", "description", "date", "type"]
        self.transactions.pop(transaction_id - 1)
        with open(self.file_path, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            if os.path.getsize(self.file_path) == 0:
                writer.writeheader()
            for transaction in self.transactions:
                writer.writerow(
                    {
                        "amount": transaction[0],
                        "category": transaction[1],
                        "description": transaction[2],
                        "date": transaction[3],
                        "type": transaction[4],
                    }
                )
        os.system("cls" if os.name == "nt" else "clear")
        print("✅ Transaction deleted successfully!")
        time.sleep(2)
