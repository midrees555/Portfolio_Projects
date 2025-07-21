# Entry point for the CLI app

# ####### Import Essential Libraries & Packages ######
from constants import MENU


def show_menu():
    """Display options with numbers to choose action in the form of a single number at a time"""
    
    print("\n_____________________________")
    print(MENU)


def input_to_select_option():
    """Input number to select an option to perform specific action"""
    
    user_input = input("\nSelect an option: ")
    
    while user_input not in ['1', '2', '3', '4']:
        user_input = input("Choose an option (1-4): ")
    
    return user_input


def control_main_program_flow():
    """To control main program flow, Whether user want to continue or exit"""
    
    print("___________________________________")  # for clearity
    user_control_choice = input("Press Y for Continue Or N for Exit: ").strip().lower()
    
    while user_control_choice not in ['y', 'n']:
        user_control_choice = input("Press Y or N only: ").strip().lower()
    
    if user_control_choice == 'y':
        return True
    else:
        return False


# ################### Main Program ###################
# ####################################################

def main():
    """Main Program Flow is here"""
    
    while True:
        show_menu()
        user_action_choice = input_to_select_option()
        
        if user_action_choice == '1':
            print("Product Added Successfully!\n")
        
        elif user_action_choice == '2':
            print("Product Removed Successfully!\n")
            
        elif user_action_choice == '3':
            print("Product List Shown Successfully!\n")
            
        else:   # option 4 - Exit
            print("Program Terminated Successfully!\n")
        
        if control_main_program_flow():
            continue
            
        break
    
    print("\n\n|===============================|")
    print("|___ S E E   Y O U   S O O N ___|")
    print("|__________ 👋 👋 👋 ___________|")
        
            
if __name__ == '__main__':
    main()