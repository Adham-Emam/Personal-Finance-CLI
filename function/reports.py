import os
import csv
from function.menu_navigator import MenuNavigator
from datetime import datetime, date, timedelta
from collections import Counter, defaultdict
import statistics
import math

class Reports:
    def __init__(self,username):
        """
        Reports class for a given user.
        """
        self.username = username
        self.file_path = f"database/{username}/transactions.csv"

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
        transactions = self.read_transactions()
        income_total=0
        expenses_total=0
        now=datetime.now()
        last_month=now.month-1 if now.month>1 else 12
        last_month_year=now.year if now.month>1 else now.year-1
        for row in transactions:
            date=row["date"]
            if date.month==last_month and date.year==last_month_year:
                amount=row["amount"]
                if row["type"]=="income":
                    income_total+=amount
                elif row["type"]=="expense":
                    expenses_total+=amount
            net_total=income_total-expenses_total
        print(f"Monthly Summary for {last_month}/{last_month_year}:")
        print(f"Total income: ${income_total:.2f}")
        print(f"Total expenses: ${expenses_total:.2f}")
        print(f"Net total: ${net_total:.2f}")
        return income_total, expenses_total, net_total
    def category_summary(self):
        """category report"""
        transactions=self.read_transactions()
        category=input("Enter your desired category: ").strip().lower()
        total=0
        for row in transactions:
            if row["category"]== category:
                amount=row["amount"]
                total+=amount
        if total ==0:
            print(f"no transactions were found for {category} category")
        else:
            print(f"Total for category: {category} is : ${total:.2f}")
                    
        # for tx in transactions:
        #     if tx["date"].year == year and tx["date"].month == month:
        #         if tx["type"] =="income":
        #             income_total += tx["amount"]
        #         elif tx["type"] =="expense":
        #             expenses_total += tx["amount"]
        # return {"income_total": income_total, "expenses_total": expenses_total, "net_total": income_total - expenses_total}
    
    