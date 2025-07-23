# Will now depend on file_handler to read/write JSON
# Core logic: add, remove, display products

# ############ Import modules & packages #############
from utils import is_valid_product_name, is_valid_product_price, process_control_user_choice


def add_product(products, p_name, p_price):
    """Add products to the inventory list in the form of dict"""
    
    p_name = (is_valid_product_name(p_name)).strip().lower()
    p_price = float(is_valid_product_price(p_price))
    
    if not any(p["name"].lower() == p_name.lower() for p in products):
        products.append({"name": p_name.strip().lower(), "price": p_price})
        print(f"\nProduct '{p_name}' added successfully!".title())
    else:
        print(f"⚠️  Product {p_name} already exists! Use a differet name.\n")


def upsert_product(products):
    """If product not exists during remove_product_process or inventory empty, then add?"""
    
    product_add_user_choice = input(f"Add new product? (Y/N): ".title())
    if process_control_user_choice(product_add_user_choice):
        p_name = input("Enter product name: ")
        p_price = input("Enter product price: ")
        add_product(products, p_name, p_price)


def rem_product(products, p_name):
    """Remove products from inventory"""
    
    p_name = (is_valid_product_name(p_name)).strip().lower()
    
    if len(products) == 0:
        print("❌  Error! Prodcut inventory is empty!\n")
        upsert_product(products)    # if user want to add new product
        return
    
    # Changing a global variable like below will cause an error due scope. So, we've used 'global' keyword
    
    try:
        if any(p["name"].lower() == p_name for p in products):
            products[:] = [p for p in products if p["name"].lower() != p_name.lower()]
            print(f"\nProduct '{p_name}' removed successfully!".title())
            return
    except (ValueError, FileNotFoundError) as e:
        print(f"❌  Error: {e}\n")
    
    print(f"⚠️  Error! Product '{p_name}' doesn't exists.")
    upsert_product(products)    # if user want to add new product
    return


def list_products(products):
    """Show all inventory products to user"""
    
    if len(products) == 0:
        print("❌  Error! Product inventory is empty!\n")
        upsert_product(products)    # if user want to add new product
        return
    
    for idx, product in enumerate(products, 1):
        print(f"{idx:>2}. {product['name']:<20} ${product['price']:>10,.2f}")   # little bit formatted