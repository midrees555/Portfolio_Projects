# Helper functions (input validation, formatting, etc.)

def is_valid_product_price(p_price):
    """Validate product price to avoid errors"""
    try:
        return float(p_price)
    except ValueError:
        print("Error! Invalide Price")
            
        p_price = input("Enter price again: ")
        return is_valid_product_price(p_price)
    
    
def is_valid_product_name(p_name):
    """Validate product name to avoid errors"""
    p_name = p_name.strip()
    if not p_name:      # Check if empty after strip
        print(" ❌ Error! Product name can't be blank.")
        p_name = input("Enter product name again: ")
        return is_valid_product_name(p_name)
    return p_name
        
        
def process_control_user_choice(user_choice):
    """This function will use to control the process termination where user needs to either continue or exit"""
    
    user_choice = user_choice.strip().lower()
    while user_choice not in ['y', 'n']:
        user_choice = input("Enter Y or N only: ").strip().lower()
        
    if user_choice == 'y':
        return True
    else:
        return False


# Optional: We can add a clear_console() for clean UI
