# Core logic: add, remove, display products

products = []

def add_product(p_name, p_price):
    """Add products to the inventory list in the form of dict"""
    
    if p_name and p_price:
        products.append({"name": p_name.lower(), "price": float(p_price)})
    else:
        print("Error! Product name & price can't be empty!")


def rem_product(p_name):
    """Remove products from inventory"""
    
    if not products:
        print("Error! No products found!")
        return
    
    if products["name"] == p_name.lower():
        products.remove(p_name)
    else:
        print("Invalid Name Error! Please re-enter product name.")

def list_products():
    """Show all inventory products to user"""
    
    if not products:
        print("Error! No Product Found!\n")
        return
    
    for idx, prodcut in enumerate(products):
        print(f"{idx}. {prodcut}")