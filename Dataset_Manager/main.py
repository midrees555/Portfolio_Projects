# Entry point for CLI usage (interacts with user)

from dataset_manager.file_validator import FileValidator
from dataset_manager.dataset_interface import DataSetInterface  # to access get_data(), which is inside DataSetInterface

def main():
    file_path = input("📂 Enter dataset file path (.csv or .xlsx): ").strip()
    validator = FileValidator()
    try:
        if validator.validate(file_path):
            interface = DataSetInterface()
            data = interface.get_data(file_path)
            if data is not None:
                print("✅ Data loaded successfully!")
                print(data.head())      # or passed data to next logic
            else:
                print("❌ Data loading failed...")
    except Exception as e:
        print(f"❌ Error: {e}")
        

if __name__ == '__main__':
    main()