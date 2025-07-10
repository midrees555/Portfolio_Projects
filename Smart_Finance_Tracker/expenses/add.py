# importing essential moduls & packages
from utils.file_handler import input_and_validate_amount, select_date, select_category, save_transaction_to_csv
from constants import EXPENSE_CATEGORIES_FILE, EXPENSE_CSV_FILE

# Defining new_expense function
def new_expense():
    # To get expense amount
    expense_amount = input_and_validate_amount("Enter Expense Amount: ")
    print('----------------')
    
    # To get expense category
    expense_category = select_category(EXPENSE_CATEGORIES_FILE, "Expense Category")
    print('----------------')
    
    # To get expense date
    expense_date = select_date("Enter Expense Date (YYYY-MM-DD) or Press enter for Today: ")
    print('----------------')
    
    # New Expense Transaction Data
    expense_data = {
        'Amount': expense_amount,
        'Category': expense_category,
        'Date': expense_date
    }
    
    # Saving New Expense Transaction Data
    save_transaction_to_csv(EXPENSE_CSV_FILE, expense_data)
    
    
    return expense_amount
    