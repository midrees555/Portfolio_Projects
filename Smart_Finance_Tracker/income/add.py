# importing essential modules and packages
from utils.file_handler import input_and_validate_amount, select_date, select_category, save_transaction_to_csv
from constants import INCOME_CATEGORIES_FILE, INCOME_CSV_FILE

# Definig new_income function
def new_income():
    # To get income amount
    income_amount = input_and_validate_amount("Enter Income Amount: ")
    print('----------------')
    
    # To get income category
    income_category = select_category(INCOME_CATEGORIES_FILE, "Income Category")
    print('----------------')
    
    # To get income date
    income_date = select_date("Enter Income Date (YYYY-MM-DD) or Press enter for Today: ")
    print('----------------')
    
    
    # New Income Transaction Data
    income_data = {
        'Amount': income_amount,
        'Category': income_category,
        'Date': income_date
    }
    
    # Saving New Income Transaction Data
    save_transaction_to_csv(INCOME_CSV_FILE, income_data)
    
    return income_amount