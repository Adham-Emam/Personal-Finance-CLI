# Personal Finance CLI

A command-line interface application for managing personal finances, built with Python. This application allows users to track income, expenses, view reports, and manage their financial data through an intuitive menu-driven interface.

## Features

### 🔐 Authentication System

- **User Registration**: Create new accounts with unique usernames and emails
- **Secure Login**: Password-based authentication with bcrypt hashing
- **Profile Setup**: First-time login profile completion with personal details
- **Data Security**: Passwords are hashed and stored securely

### 💰 Transaction Management

- **Add Income**: Record income transactions with categories and descriptions
- **Add Expenses**: Track expense transactions with detailed categorization
- **Transaction History**: View complete transaction history with filtering options
- **Edit Transactions**: Modify existing transaction records
- **Delete Transactions**: Remove unwanted transaction entries

### 📊 Reporting & Analytics

- **Monthly Summary**: View income/expense summaries for specific months
- **Category Analysis**: Analyze spending patterns by category
- **Financial Health Score**: Get insights into your financial wellness
- **Transaction Reports**: Generate detailed transaction reports

### ⚙️ Settings & Configuration

- **Profile Management**: Update personal information
- **Data Export**: Export transaction data
- **Account Settings**: Manage account preferences

## Project Structure

```
Personal-Finance-CLI/
├── database/                    # User data storage
│   ├── users.json              # User authentication data
│   └── {username}/             # Individual user folders
│       ├── profile.json        # User profile information
│       └── transactions.csv    # Transaction history
├── function/                   # Core application modules
│   ├── auth.py                # Authentication system
│   ├── main_menu.py           # Main menu controller
│   ├── menu_navigator.py      # Menu navigation utility
│   ├── add_income.py          # Income management
│   ├── add_expense.py         # Expense management
│   ├── view_balance.py        # Balance calculation
│   ├── reports.py             # Reporting system
│   ├── settings.py            # User settings
│   └── transactions/          # Transaction management
│       ├── transaction_history.py
│       ├── edit_transaction.py
│       └── delete_transaction.py
├── utils/                     # Utility modules
│   └── currencies.py         # Currency definitions
├── main.py                   # Application entry point
└── README.md                # Project documentation
```

## Classes Overview

### 🔐 Authenticator (`auth.py`)

Handles user authentication and profile management.

**Key Methods:**

- `register()`: User registration with validation
- `login()`: User authentication
- `first_time_profile()`: Profile completion for new users
- `hash_password()`: Secure password hashing
- `verify_password()`: Password verification

**Features:**

- Bcrypt password hashing
- Email and username validation
- Atomic file operations for data safety
- User directory creation

### 🏠 MainMenu (`main_menu.py`)

Central hub for application navigation.

**Key Methods:**

- `run()`: Main application loop
- Navigation to all application features

**Features:**

- Menu-driven interface
- Integration with all application modules
- User session management

### 🧭 MenuNavigator (`menu_navigator.py`)

Utility class for consistent menu handling across the application.

**Key Methods:**

- `print_menu()`: Display menu options
- `choice()`: Handle user input and validation
- `validate_choice()`: Input validation

### 💵 AddIncome (`add_income.py`)

Manages income transaction recording.

**Key Methods:**

- `add_income()`: Income entry workflow
- `get_valid_amount()`: Amount validation
- `get_valid_category()`: Category selection
- `save_income()`: Persist income data

**Features:**

- Input validation
- Category management
- CSV data storage
- Date handling

### 💸 AddExpense (`add_expense.py`)

Handles expense transaction recording.

**Key Methods:**

- `add_expense()`: Expense entry workflow
- `get_valid_amount()`: Amount validation
- `get_valid_category()`: Category selection
- `save_expense()`: Persist expense data

### 💰 ViewBalance (`view_balance.py`)

Calculates and displays account balances.

**Key Methods:**

- `calculate_balance()`: Compute total income/expense
- `run()`: Display balance information

### 📊 Reports (`reports.py`)

Comprehensive reporting and analytics system.

**Key Methods:**

- `monthly_summary()`: Monthly financial overview
- `category_summary()`: Category-based analysis
- `financial_health_report()`: Financial wellness scoring
- `recurring_transactions()`: Identify recurring patterns

**Features:**

- Rich table formatting
- Multiple report types
- Data visualization
- Export capabilities

### 📝 TransactionHistory (`transactions/transaction_history.py`)

Display and manage transaction records.

**Key Methods:**

- `display_transactions()`: Show transaction list
- `filter_transactions()`: Apply filters
- `search_transactions()`: Search functionality

### ✏️ EditTransaction (`transactions/edit_transaction.py`)

Modify existing transaction records.

**Key Methods:**

- `edit_transaction()`: Transaction modification workflow
- `validate_changes()`: Ensure data integrity

### 🗑️ DeleteTransaction (`transactions/delete_transaction.py`)

Remove transaction records.

**Key Methods:**

- `delete_transaction()`: Safe transaction removal
- `confirm_deletion()`: User confirmation

## Installation & Setup

### Installation

1. Clone the repository
2. Install dependencies
3. Run the application:

### Prerequisites

```bash
# Create a virtual enviroment :
python3 -m venv .venv

source .venv/bin/activate #for linux

.venv\scripts\activate #for windows

#install required required packages
pip install -r requirements.txt #while being in the same directory

```

```bash

#for linux
python3 main.py

#for windows
python main.py

```

## Usage

### First Time Setup

1. Run the application
2. Choose "Register" to create a new account
3. Provide username, email, and password
4. Login with your credentials
5. Complete your profile setup

### Daily Usage

1. **Add Income**: Record salary, freelance payments, etc.
2. **Add Expenses**: Track daily expenses with categories
3. **View Reports**: Analyze spending patterns
4. **Check Balance**: Monitor your financial status

### Data Management

- All user data is stored locally in the `database/` folder
- Transactions are saved in CSV format for easy access
- User profiles and authentication data use JSON format

## Security Features

- **Password Hashing**: Uses bcrypt for secure password storage
- **Data Validation**: Input validation prevents data corruption
- **Atomic Operations**: Safe file operations prevent data loss
- **User Isolation**: Each user's data stored separately

## Data Format

### Transaction CSV Structure

```csv
date,type,amount,category,description
2024-10-25,income,5000.00,Salary,Monthly salary
2024-10-25,expense,1200.00,Rent,Monthly rent payment
```

### User Profile JSON Structure

```json
{
  "first_name": "John",
  "last_name": "Doe",
  "email": "john.doe@example.com",
  "currency": "USD"
}
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## Future Enhancements

- [ ] Budget planning and tracking
- [ ] Bill reminders and notifications
- [ ] Data visualization with charts
- [ ] Multi-currency support
- [ ] Data backup and sync
- [ ] Mobile app integration
- [ ] Investment tracking
- [ ] Financial goal setting

## Support

For issues and feature requests, please create an issue in the project repository.

---

### Invest wisely and remember it all pays off in the end

<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExaTNudTgxa2l1YW4yeW9oendnYmt3aDU2Y214aDhwaTh5dXd4dGthaiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/X8omQqfFyeq1a/giphy.gif"/>

---
