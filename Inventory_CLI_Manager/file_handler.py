# Will handle:

# - load_products_from_file()
# - save_products_to_file()
# - PRODUCT_FILE_PATH = 'data/products.json

# ####### Import Essential Libraries & Packages ######
import os
import json

# File path for storing products
PRODUCTS_FILE_PATH = 'data/products.json'


def load_products_from_file():
    """To safely load products from a JSON file (data/products.json). 
    If file doesn't exist or is corrupted, return an empty list[] safely."""
    
    if not os.path.exists(PRODUCTS_FILE_PATH):
        # File doesn't exist, return empty products list
        print("=================================================================")  # for clearity
        print("⚠️  No existing product file found! Starting with empty inventory.")
        return []
    
    try:
        with open(PRODUCTS_FILE_PATH, 'r') as file:
            products = json.load(file)
            if isinstance(products, list):      # Make sure it's a list
                return products
            else:
                print("⚠️  File format incorrect! Expected a list.")
                return []
            
    except (json.JSONDecodeError, IOError) as e:
        print(f"❌  Failed to load products!\nError was {e}")
        return []
    
    
def save_products_to_file(products_list):
    """
    Save the current list of products to a JSON file.
    This will overwrite the previous contents with updated inventory.
    """
    
    # Ensure 'data' directory exists
    os.makedirs(os.path.dirname(PRODUCTS_FILE_PATH), exist_ok=True)
    
    try:
        with open(PRODUCTS_FILE_PATH, 'w') as file:
            json.dump(products_list, file, indent=4)
            print("✔️  Products list updated successfully!")
    except IOError as e:
        print(f"❌  Failed to save products!\nError was {e}")