from datetime import datetime

# input_value validation
def is_valid_amount(amount):
    try:
        float(amount)
        return True
    except ValueError:
        print("⛔ Invalid input! Enter numeric value.")
        print('----------')
        return False
    
# Date validation
def is_valid_date(string):
    try:
        # datetime.strftime() is used to format a 'datetime object' to 'string'
        user_date = datetime.strftime(string, "%Y-%m-%d").date()
        return user_date <= datetime.today().date()
    
    except:
        print("⛔ Invalid date! Use format as [YYYY-MM-DD].")
        print('----------')
        return False
    
    
    
# ----------------START PARSE-DATE-OR-NONE SECTION------------------|

def parse_date_or_none(string):
    """Function to return exact date object for reporting (View/Generate)"""
    try:
        # datetime.strptime() is used to convert 'string date' to a 'date object'
        user_date = datetime.strptime(string, '%Y-%m-%d').date()
    
        if user_date <= datetime.today().date():
            return user_date
        print("⚠️ Dates can't be in the future.")
    except ValueError:
        print("⛔ Invalid date format! Use [YYYY-MM-DD].")
    
    return None
# ----------------END PARSE-DATE-OR-NONE SECTION--------------------|
# ------------------------------------------------------------------|