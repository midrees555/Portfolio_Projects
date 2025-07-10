from utils.file_handler import display_report
from constants import EXPENSE_CSV_FILE

def display_expense_report():
    display_report(EXPENSE_CSV_FILE, "Expense")