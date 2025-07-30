from dataset_manager.file_validator import FileValidator

validator = FileValidator()
file_path = 'data/sample.xlsx'   # we'll try to chnage this path to test

try:
    validator.validate(file_path)
    print("✅ File validation passed successfully!")
except Exception as e:
    print(f"❌ Validation failed: {e}")