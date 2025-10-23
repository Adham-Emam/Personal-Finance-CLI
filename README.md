# Personal Finance CLI

A lightweight cross-platform command-line personal finance manager to track income, expenses, budgets and generate simple reports.

- Language: Python 3.8+
- Entry point: `main.py`
- Data storage: local CSV / JSON files under `database/`
- Dependencies: See [requirements.txt](requirements.txt)

## Features

- Register / login with password hashing (`bcrypt`) — see [`function/auth.py`](function/auth.py)
- Add income and expenses (`function/add_income.py`, `function/add_expense.py`)
- View balance summary (`function/view_balance.py`)
- Transaction history with filtering, sorting and search (`function/transactions/view_transactions.py`)
- Edit and delete transactions (`function/transactions/edit_transaction.py`, `function/transactions/delete_transaction.py`)
- Import/export CSV and simple reports (`function/transactions/transaction_history.py`, `function/reports.py`)
- Basic settings and profile management (`function/settings.py`)
- Supported currencies list in [`utils/currencies.py`](utils/currencies.py)

## Quick start (Linux)

1. Clone the repo:

   ```
   git clone https://github.com/youruser/Personal-Finance-CLI.git
   cd Personal-Finance-CLI
   ```

2. Create a virtual environment and install deps:

   ```
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. Run the app:
   ```
   python3 main.py
   ```
   The app shows a simple menu-driven UI. Use the numbers to navigate (e.g. 1 = Add Income).

## Usage notes

- The app stores users in `database/users.json` and per-user transactions in `database/<username>/transactions.csv`. The repository `.gitignore` already excludes `database/`.
- CSV transaction header format:

  ```
  amount,category,description,date,type
  ```

  - `amount`: integer (positive)
  - `category`: letters only (3–20 chars)
  - `date`: YYYY-MM-DD
  - `type`: `income` or `expense`

- To import transactions, go to Transaction History -> Import Data from CSV and provide a CSV file containing the required headers.

## File map (important files)

- main entry: [`main.py`](main.py)
- Menu system: [`function/menu_navigator.py`](function/menu_navigator.py)
- Main application menu: [`function/main_menu.py`](function/main_menu.py)
- Authentication: [`function/auth.py`](function/auth.py) — registration, login, profile flow
- Add transaction: [`function/add_income.py`](function/add_income.py), [`function/add_expense.py`](function/add_expense.py)
- Transactions: [`function/transactions/view_transactions.py`](function/transactions/view_transactions.py)
- Edit/Delete transaction: [`function/transactions/edit_transaction.py`](function/transactions/edit_transaction.py), [`function/transactions/delete_transaction.py`](function/transactions/delete_transaction.py)
- Reports: [`function/reports.py`](function/reports.py)
- Settings & currencies: [`function/settings.py`](function/settings.py), [`utils/currencies.py`](utils/currencies.py)

## Development notes

- Passwords are hashed with `bcrypt` (see [`function/auth.py`](function/auth.py)).
- Users JSON is written atomically using a temporary file to avoid corruption.
- Tests are not included. Add unit tests for critical flows (auth, CSV read/write, reports).
- To debug, run functions directly (e.g. open `function/reports.py`) or add print/log statements.

## Common commands

- Create venv and install: see Quick start.
- Run: `python3 main.py`
- Reset a user's transactions: Settings -> Reset All Data (this overwrites the CSV header).

## Contributing

1. Fork the repo
2. Create a topic branch
3. Add tests for behavior you change
4. Open a pull request with a clear description
