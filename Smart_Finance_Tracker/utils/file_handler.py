# importing essential libraries & packages
from utils.validation import is_valid_amount, is_valid_date, parse_date_or_none
import os
from datetime import datetime
import csv
from tabulate import tabulate



# --------------------- AMOUNT -------------------------|

def input_and_validate_amount(prompt="Enter amount: "):
    while True:
        user_input = input(prompt)
        if is_valid_amount(user_input):
            return float(user_input)
        
        print("⚠️ Invalid input! Please etnter a valid amount.")
        
# ------------------------------------------------------|
# ------------------------------------------------------|




# -------------------- CATEGORY ------------------------|

def save_unique_category(category, file_path):
    """
    saves categories only if not already present (and should be case-insensitive).
    Returns 'True' if added successfully, 'False' if it's duplicate.
    """
    
    category = category.strip()
    if not category:
        return False
    
    try:
        with open(file_path, 'r') as file:
            existing = {line.strip().lower() for line in file if line.strip()}
            
    except FileNotFoundError:
        existing = set()
        
    if category.lower() in existing:
        return False        # category already exist (case-insensitive)
    
    # if category not found in existing
    with open(file_path, 'a') as file:
        file.write(category.title() + '\n')
        
    return True


# Initializing categories_file once in start for both (expense & income)
def initialize_categories_file(category_file_path: str, DEFAULT_CATEGORIES):
    """Initilize category file with unique default values (if not already present)"""
    
    existing_categories = set()
    
    # Load current categories from file
    try:
        with open(category_file_path, 'r') as file:
            existing_categories = {line.strip().lower() for line in file if line.strip()}
    except FileNotFoundError:
        pass
    
    # Add only missing categories from default (case-insensitive)
    with open(category_file_path, 'a') as file:
        for category in sorted(DEFAULT_CATEGORIES):
            if category.lower() not in existing_categories:
                file.write(category.title() + '\n')



def select_category(category_file_path: str, category_type: str='category'):
    """
    User will select category from existing categories if not exist will enter new one (case-insensitive)
    """
    categories = []
    
    if os.path.exists(category_file_path):
        with open(category_file_path, 'r') as file:
            categories = [line.strip() for line in file if line.strip()]
            
    print(f"\nChoose {category_type}:")
    
    for idx, cat in enumerate(categories, 1):
        print(f"{idx}. {cat}")
    print(f"{len(categories) + 1}. Add new {category_type}")
    
    choice = input("Enter you choice: ")
    
    try:
        choice = int(choice)
        
        if 1 <= choice <= len(categories):
            return categories[choice - 1]
        
        elif choice == len(categories) + 1:
            new_category = input(f"Enter new {category_type} name: ").strip()
            if not new_category:
                raise ValueError
            
            added = save_unique_category(new_category, category_file_path)
            
            if added:
                print(f" ✔️  New {category_type} '{new_category}' added successfully!\n")
            else:
                print(f" ⚠️  {category_type.capitalize()} '{new_category}' already exists (case-insensitive)\n")
        
            return new_category.title()
    
    except:
        print(" ⛔ Invalid input OR Error occurred!")
        
    print(" ⚠️ Invalid choice! Defaulting to 'Other'")
    return 'Other'
# ------------------------------------------------------|
# ------------------------------------------------------|



# ------------------- SELECT-DATE ----------------------|

def select_date(prompt="Enter Date (YYYY-MM-DD) or Press enter for Today: "):
    default_date = datetime.today().strftime('%Y-%m-%d')
    
    while True:
        user_input = input(f"{prompt} [{default_date}]: ").strip()
        
        if user_input == '':
            return default_date
        
        elif is_valid_date(user_input):
            return user_input
        
        print("⚠️ Invalid date! Please use YYYY-MM-DD format & Ensure it's not in the future.")
# ------------------------------------------------------|
# ------------------------------------------------------|



# ------------- SAVE-TRANSACTION -----------------------|

def save_transaction_to_csv(file_path: str, data: dict):
    
    file_exists = os.path.isfile(file_path)
    
    with open(file_path, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Amount', 'Category', 'Date'])
        
        if not file_exists:
            writer.writeheader()
        
        writer.writerow(data)
        
    print("✔️  Data Saved Successfully!")
    print("-----------------------------------------------|")

# ------------------------------------------------------|
# ------------------------------------------------------|



# -------------- VIEW & GENERATE REPORT ----------------|

# <<--- Getting Date Range --->>
def get_date_range():
    pass
    while True:
        start_input = input("Enter Start Date (YYYY-MM-DD): ").strip()
        end_input = input("Enter End Date (YYYY-MM-DD): ").strip()
        
        start_date = parse_date_or_none(start_input)
        end_date = parse_date_or_none(end_input)
        
        if not start_date or not end_date:
            print("⚠️ Invalid date(s)! Please try again...\n")
            continue
        
        if start_date > end_date:
            print("⚠️ Start Date can't be after End Date!")
            continue
        
        return start_date, end_date




# <<--- TRANSACTION REPORTING --->>
def read_transaction(file_path, start_date, end_date):
    matched_records = []
    
    if not os.path.exists(file_path):
        print("⛔ Error: File not found!", file_path)
        print("-----------------------------------------------\n")
        return matched_records # ✔️ early return
    
    else:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                txn_date = parse_date_or_none(row['Date'])
                
                if not txn_date:
                    print(f"⛔ Error parsing date: {row['Date']}. Skipping Records!")
                    continue
                
                if start_date <= txn_date <= end_date:
                    matched_records.append(row)
                    
    return matched_records



# <<--- Filtering Record By Date --->
def filter_records_by_date(file_path, title='Record'):
    """ To avoid repeating get_date_range() + read_transaction() in both display and generate functions."""
    
    start_date, end_date = get_date_range()
    records = read_transaction(file_path, start_date, end_date)
    
    if not records:
        print(f"\n😕 No {title.lower()} records found from {start_date} - {end_date}")
        print("-----------------------------------------------")
        
        return None, None, None
    
    return records, start_date, end_date



# <<--- VIEW REPORT --->>
def display_report(file_path, title):
    """ Here's the logic to view or display the records only"""
    
    records, start_date, end_date = filter_records_by_date(file_path, title)
    
    if not records:
        return
    
    print(f"\n📊 {title} Report from {start_date} - {end_date}")
    print("-----------------------------------------------")
    print(tabulate(records, headers='keys', tablefmt='grid'))
            
    
    
# <<--- GENERATE REPORT --->>
def generate_report(file_path, report_name, title):
    """ Here's the logic to generate report (Expense/Income)"""
    
    records, start_date, end_date = filter_records_by_date(file_path, title)
    
    if not records:
        return
    
    report_file = f'data/{report_name}.csv'
    
    with open(report_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Amount', 'Category', 'Date'])
        writer.writeheader()
        for row in records:
            writer.writerow(row)
        
        
    total = sum(float(row['Amount']) for row in records)
    
    print(f"\n✔️ {title} Report Saved Successfully at \n'{report_file}'")
    print("-----------------------------------------------\n")
    
    print(f"{title} report".title())
    print(tabulate(records, headers='keys', tablefmt='grid'))
    print(f"\n📌 Ttotal {title}: ${total:,.2f}")
    print("-----------------------------------------------")
    
# ------------------------------------------------------|
# ------------------------------------------------------|


