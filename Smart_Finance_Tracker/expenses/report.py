from utils.file_handler import generate_report
from constants import EXPENSE_CSV_FILE

def generate_expense_report():
    while True:
        expense_report_name = input("Enter Expense Report Name To Generate: ").strip()
        
        try:
            str(expense_report_name)
            break
        except:
            print("⚠️ Invalid name! Please enter a valid name.\n")
        
    if expense_report_name:
        generate_report(EXPENSE_CSV_FILE, expense_report_name, 'Expense')
            