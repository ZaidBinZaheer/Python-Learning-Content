from collections import namedtuple

# Define the named tuple 'Product' with fields: name, price, quantity
Product = namedtuple("Product", ["name", "price", "quantity"])

# Initialize an empty list to store products in the inventory
inventory = []

def add_product(name, price, quantity):
    """Add a new product to the inventory."""
    product = Product(name, price, quantity)
    inventory.append(product)
    print(f"{name} has been added to the inventory.")

def update_price(name, new_price):
    """Update the price of a product in the inventory."""
    for i, product in enumerate(inventory):
        if product.name == name:
            updated_product = product._replace(price=new_price)
            inventory[i] = updated_product
            print(f"The price of {name} has been updated to {new_price}.")

def check_stock(name):
    """Check the stock level of a product in the inventory."""
    for product in inventory:
        if product.name == name:
            print(f"Stock level of {name}: {product.quantity}")
            return
    print(f"{name} not found in the inventory.")

# Add some initial products to the inventory
add_product("Apple", 0.5, 100)
add_product("Banana", 0.3, 150)
add_product("Orange", 0.4, 120)

# Update the price of a product
update_price("Banana", 0.35)

# Check stock levels
check_stock("Apple")
check_stock("Banana")
check_stock("Mango")  # Product not in the inventory

# Print the current inventory
print("\nCurrent Inventory:")
for product in inventory:
    print(product)
