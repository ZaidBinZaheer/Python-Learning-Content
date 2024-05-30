from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    quantity: int

class InventoryManager:
    def __init__(self):
        self.inventory = {}

    def add_product(self, name, price, quantity):
        if name in self.inventory:
            print(f"Product '{name}' already exists. Use update_product to modify.")
        else:
            self.inventory[name] = Product(name, price, quantity)
            print(f"Product '{name}' added to inventory.")

    def remove_product(self, name):
        if name in self.inventory:
            del self.inventory[name]
            print(f"Product '{name}' removed from inventory.")
        else:
            print(f"Product '{name}' not found in inventory.")

    def update_product(self, name, new_price=None, new_quantity=None):
        if name in self.inventory:
            product = self.inventory[name]
            if new_price is not None:
                product.price = new_price
            if new_quantity is not None:
                product.quantity = new_quantity
            print(f"Product '{name}' updated in inventory.")
        else:
            print(f"Product '{name}' not found in inventory.")

    def display_inventory(self):
        print("Current Inventory:")
        for name, product in self.inventory.items():
            print(f"Product: {name}, Price: {product.price}, Quantity: {product.quantity}")

# Creating an InventoryManager instance
inventory_manager = InventoryManager()

while True:
    print("1. Add Product")
    print("2. Remove Product")
    print("3. Update Product")
    print("4. Display Inventory")
    print("5. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))
        inventory_manager.add_product(name, price, quantity)
    elif choice == '2':
        name = input("Enter product name to remove: ")
        inventory_manager.remove_product(name)
    elif choice == '3':
        name = input("Enter product name to update: ")
        new_price = float(input("Enter new product price (or press Enter to skip): ") or None)
        new_quantity = int(input("Enter new product quantity (or press Enter to skip): ") or None)
        inventory_manager.update_product(name, new_price, new_quantity)
    elif choice == '4':
        inventory_manager.display_inventory()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
