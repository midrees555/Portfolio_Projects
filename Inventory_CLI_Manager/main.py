# Entry point for the CLI app
# Load products at startup
# Save to file after each add/remove

# ####### Import Essential Libraries & Packages ######
from constants import MENU
from inventory import add_product, rem_product, list_products
from utils import process_control_user_choice
from file_handler import load_products_from_file, save_products_to_file


def show_menu():
    """Display options with numbers to choose action in the form of a single number at a time"""
    
    # print("\n_____________________________", end="")
    print(MENU)


def input_to_select_option():
    """Input number to select an option to perform specific action"""
    
    user_input = input("\nSelect an option: ")
    
    while user_input not in ['1', '2', '3', '4']:
        user_input = input("Choose an option (1-4): ")
        print("________________________")   # for UI clearity
    
    return user_input


def control_main_program_flow():
    """To control main program flow, Whether user want to continue or exit"""
    
    print("___________________________________")  # for clearity
    user_control_choice = input("Press Y for Continue Or N for Exit: ").strip().lower()
    return process_control_user_choice(user_control_choice)



def main():
    """Main Program Flow is here"""
    
    # ♻️ Load products list from file
    products = load_products_from_file()
    
    while True:
        show_menu()
        user_action_choice = input_to_select_option()
        
        if user_action_choice == '1':
            product_name = input("Enter a product name: ")
            product_price = input("Enter a product price: ")
            
            add_product(products, product_name, product_price)
            save_products_to_file(products)     # ✔️ Save after add
        
        
        elif user_action_choice == '2':
            list_products(products)
            
            remove_product = input("\nEnter product name to remove: ")
            rem_product(products, remove_product)
            save_products_to_file(products)     # ✔️ Save after remove
            
            
        elif user_action_choice == '3':
            list_products(products)
            
        else:   # option 4 - Exit
            print("Exiting Program...")
            print("============================================")
            break
        
        if not control_main_program_flow():
            break

    
    print("\n|===============================|")
    print("|___ S E E   Y O U   S O O N ___|")
    print("|__________ 👋 👋 👋 ___________|")
        
            
if __name__ == '__main__':
    main()