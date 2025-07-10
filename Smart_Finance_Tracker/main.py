# ------------------- Importing Essential Libraries & Packages -------------------|

from constants import *
from balance_handler import enter_opening_balance, initilize_balance_file, load_balance, save_balance
from utils.file_handler import initialize_categories_file
from utils.clear_data import clear_all_data
from utils.clear_data import reset_categories_file
from expenses.add import new_expense
from expenses.view import display_expense_report
from expenses.report import generate_expense_report
from income.add import new_income
from income.view import display_income_report
from income.report import generate_income_report



# ---------------------------- Initilize Application -----------------------------|

def setup_application():
    initilize_balance_file()        # initilizing balance_file once
    initialize_categories_file(EXPENSE_CATEGORIES_FILE, EXPENSE_CATEGORIES)
    initialize_categories_file(INCOME_CATEGORIES_FILE, INCOME_CATEGORIES)
    
    return load_balance()



# ------------------------------ Utility Functions -------------------------------|

def continue_to_main_menu():
    user_choice = input("\nContinue to Main Menu? (Y/N): ").lower().strip()
    
    while user_choice not in ['y', 'n']:
        user_choice = input("Enter Y or N only: ").lower().strip()
        
    return user_choice == 'n'


def continue_to_process(process):
    user_choice = input(f"\nContinue to {process} process? (Y/N): ").lower().strip()
    while user_choice not in ['y', 'n']:
        user_choice = input("Enter Y or N only: ").lower().strip()
        
    return user_choice == 'n'



# -------------------------------- Main Program ----------------------------------|

def main():
    print("\n|-------------------------------------|")
    print("|----- WELCOME TO EXPENSE MANAGER ------|")
    print("|-------------------------------------|\n")
    
    current_balance = setup_application()
    
    if current_balance == 0:
        current_balance = enter_opening_balance()
    else:
        print(f"Your Current Balance 💲{current_balance:,.2f}")
        
    while True:
        while True:
            print("----------------------------")
            print("\nWhat would you like to do?")
            print("--------------------------")
            print("1. Add Expenses")
            print("2. Add Income")
            print("3. View / Generate Report")
            print("4. View Balance & Exit")
            print("5. Reset Categories to Default")
            print("6. Clear All Data & Reset App")
            
            main_menu_choice = input("\nEnter a choice (1-4): ").strip()
            print("---------------")
            
            if main_menu_choice not in ['1', '2', '3', '4', '5', '6']:
                print("⛔ Invalid choice! Please enter a number from (1-4)")
                continue
            
            if main_menu_choice == '1':
                while True:
                    expense_amount = new_expense()
                    current_balance -= expense_amount
                    save_balance(current_balance)
                    
                    if continue_to_process("Expense"):
                        print("\n🔄 Returning to Main Menu")
                        print("---------------------------")
                        break
                    
            elif main_menu_choice == '2':
                while True:
                    income_amount = new_income()
                    current_balance += income_amount
                    save_balance(current_balance)
                    
                    if continue_to_process("Income"):
                        print("\n🔄 Returning to Main Menu")
                        print("---------------------------")
                        break
                    
            elif main_menu_choice == '3':
                print("\n📊 Report Options:\n")
                print("1. View Expense Report")
                print("2. View Income Report")
                print("3. Generate Expense Report")
                print("4. Generate Income Report")
                
                report_choice = input("\nEnter report choice (1-4): ").strip()
                print("---------------")
                
                while report_choice not in ['1', '2', '3', '4']:
                    report_choice = input("⛔ Invalid chocie! Please enter (1-4): ")
                    
                if report_choice == '1':
                    display_expense_report()
                    
                elif report_choice == '2':
                    display_income_report()
                    
                elif report_choice == '3':
                    generate_expense_report()
                    
                elif report_choice == '4':
                    generate_income_report()
                    
            elif main_menu_choice == '4':
                print(f"📊 Current Balance: 💲{current_balance:,.2f}")
                break
            
            elif main_menu_choice == '5':
                reset_cat_confirm = input("Do you want to reset categories? (Y/N): ").strip()
                if reset_cat_confirm.lower() == 'y':
                    while reset_cat_confirm not in ['n', 'y']:
                        reset_cat_confirm = input("Please Enter Y or N only: ").strip().lower()
                    reset_categories_file(EXPENSE_CATEGORIES_FILE, EXPENSE_CATEGORIES)
                    reset_categories_file(INCOME_CATEGORIES_FILE, INCOME_CATEGORIES)
                    print("------------------------------------------\n")
                else:
                    print("✔ Categories Reset Cancelled!")
            
            elif main_menu_choice == '6':
                clear_all_data()
                current_balance = enter_opening_balance()   # Ask again after reseting app
                
            
        if continue_to_main_menu():
            print("\n|-------- T H A N K   Y O U ---------|")
            print("|----- S E E   Y O U   S O O N ------|")
            print("|------------------------------------|\n")
            break
            
        print("|--- Restarting - Finance Tracker ---|")
            
if __name__ == "__main__":
    main()