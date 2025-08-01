# Entry point for CLI usage (interacts with user)

# |========== Importing essential modules & libraries ==========|
from dataset_manager.file_validator import FileValidator
from dataset_manager.dataset_interface import DataSetInterface

def get_file_path():
    return input("📂 Enter Dataset File Path (.csv or .xlsx): ").strip()

def load_and_preview_data(file_path):
    try:
        # Step 1: Validate the file
        validator = FileValidator()
        if validator.validate(file_path):
            # Step 2: Load the data
            interface = DataSetInterface()
            data = interface.get_data(file_path)
            
            if data is not None:
                print("\n✅ Data Loaded Successfully!")
                print("📊 Preview (Top 5 Rows): ")
                print(data.head())
            else:
                print("Data loading failed! Please try another file.")
    except Exception as e:
        print(f"❌ Error: {e}")
        
        
def main():
    print("\n|============================================================|")
    print("|========== WELCOME  TO  DATASET_MANAGER  CLI  APP ==========|")
    print("Easily validate & preview your .csv or .xlsx datasets\n".title())
    
    while True:
        file_path = get_file_path()
        load_and_preview_data(file_path)
        
        # Ask user if they want to try another file
        choice = input("🔁 Do you want to load another file? (Y/N): ").strip().lower()
        while choice not in ['y', 'n']:
            choice = input("Enter Y or N only: ").strip().lower()
        if choice != 'y':
            print("👋 Exiting... Thank You For Using Dataset_Manager")
            break
        
        
if __name__ == '__main__':
    main()