from utils.file_handler import generate_report
from constants import INCOME_CSV_FILE

def generate_income_report():
    while True:
        income_report_name = input("Enter Income Report Name To Generate: ").strip()
        
        try:
            str(income_report_name)
            break
        except:
            print("⚠️ Invalid name! Please enter a valid name.\n")
            
    if income_report_name:
        generate_report(INCOME_CSV_FILE, income_report_name, 'Income')