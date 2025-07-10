# Defining default expense categories
DEFAULT_EXPENSE_CATEGORIES = {
    "Health",
    "Education",
    "Transport",
    "Shopping",
    "Entertainment",
    "Food",
}

EXPENSE_CATEGORIES = set(DEFAULT_EXPENSE_CATEGORIES)

# Default expense categories file path
EXPENSE_CATEGORIES_FILE = 'data/expense_categories.txt'


# Defining default income categories
DEFAULT_INCOME_CATEGORIES = {
    "Salary",
    "Freelance",
    "Gift",
    "Return"
}

INCOME_CATEGORIES = set(DEFAULT_INCOME_CATEGORIES)

# Default income categories file path
INCOME_CATEGORIES_FILE = 'data/income_categories.txt'


# Report path
EXPENSE_CSV_FILE = 'data/expenses.csv'
INCOME_CSV_FILE = 'data/income.csv'