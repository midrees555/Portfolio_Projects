import os

FILES_TO_DELETE = [
    "data/expenses.csv",
    "data/income.csv",
    "data/balance.txt"
]


def clear_all_data():
    print("\n⚠️  WARNING: This will Delete all Transaction & Balance Data!")
    confirm = input("Do you want to erase all data? (Y/N): ").lower().strip()
    
    if confirm != 'y':
        print("✔  Data Reset Cancelled!")
        return
    
    for file_path in FILES_TO_DELETE:
        if os.path.exists(file_path):
            os.remove(file_path)
            
    
    print("☑️  All Data has been cleared successfully!")
    print("------------------------------------------\n")
    
    
    
def reset_categories_file(file_path, DEFAULT_CATEGORIES):
    with open(file_path, 'w') as file:
        for cat in sorted(DEFAULT_CATEGORIES):
            file.write(cat + '\n')
    
    print(f"☑️  Reset {file_path} to default successfully!")