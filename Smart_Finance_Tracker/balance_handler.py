import os

BALANCE_FILE = 'data/balance.txt'



# ----------------------------- Get Opening Balance ------------------------------|

def enter_opening_balance():
    while True:
        try:
            user_input = input("Enter your starting balance: ")
            opening_balance = float(user_input.replace(',', ''))
            break
        except ValueError:
            print("⛔ Invalid input! Enter a valid numeric value")
            print("---------------")
            
    print(f"\n✔️ Opening Balance 💲{opening_balance:,.2f} Deposited Successfully!")
    print(f"----------------------------------------------------")
    print(f"Current Balance: 💲{opening_balance:,.2f}")
    
    save_balance(opening_balance)
    return opening_balance



def initilize_balance_file():
    """Create the balance file if it doesn't exist"""
    
    if not os.path.exists(BALANCE_FILE):
        with open(BALANCE_FILE, 'w') as file:
            file.write('0.00')
            
        

def load_balance():
    """Load the current balance from file"""
    
    try:
        with open(BALANCE_FILE, 'r') as file:
            return float(file.read().strip())
        
    except (FileNotFoundError, ValueError):
        return 0.00


def save_balance(balance):
    with open(BALANCE_FILE, 'w') as file:
        file.write(str(balance))