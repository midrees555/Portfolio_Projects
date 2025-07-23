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
    