# handles file-level checks (like path, type, readability)

# |========== importing essential libraries & packages ==========|

import os

class FileValidator:
    def __init__(self, allowed_file_types=None):
        # Default to CSV & Excel
        self.allowed_file_types = allowed_file_types or ['.csv', '.xlsx']
        
    def validate(self, file_path):
        """
        Validate file existence, extension, and readability.
        Returns True if valid, otherwise raises appropriate error.
        """
        
        # 1. Check if path exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: '{file_path}'")
        
        # 2. Check file extension
        _, extension = os.path.splitext(file_path)              # _ (ignoring this place) & .splitext(file_path) > separate path+extension
        if extension.lower() not in self.allowed_file_types:
            raise ValueError("Unsupported file type!")
            
        # 3. Check if file is readable
        try:
            if not os.access(file_path, os.R_OK):
                raise OSError("File is not readable or accessible!")
            
        except OSError:
            raise OSError("File is not readable or accessible!")
        
        return True
    
