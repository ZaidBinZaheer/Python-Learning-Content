class ContactBook:
    def __init__(self):
        self.contacts = {}  # Dictionary to store contacts

    def add_contact(self, name, phone_number, email):
        if name not in self.contacts:
            self.contacts[name] = {"phone": phone_number, "email": email}
            print(f"Contact '{name}' added to the contact book.")
        else:
            print(f"Contact '{name}' already exists.")

    def update_contact(self, name, phone_number=None, email=None):
        if name in self.contacts:
            if phone_number:
                self.contacts[name]["phone"] = phone_number
            if email:
                self.contacts[name]["email"] = email
            print(f"Contact '{name}' updated.")
        else:
            print(f"Contact '{name}' does not exist.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted.")
        else:
            print(f"Contact '{name}' does not exist.")

    def display_contacts(self):
        print("Contacts:")
        for name, details in self.contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")

# Creating a ContactBook instance
contact_book = ContactBook()

while True:
    print("1. Add Contact")
    print("2. Update Contact")
    print("3. Delete Contact")
    print("4. Display Contacts")
    print("5. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        name = input("Enter name: ")
        phone_number = input("Enter phone number: ")
        email = input("Enter email: ")
        contact_book.add_contact(name, phone_number, email)
    elif choice == '2':
        name = input("Enter name: ")
        phone_number = input("Enter new phone number (leave blank to skip): ")
        email = input("Enter new email (leave blank to skip): ")
        contact_book.update_contact(name, phone_number, email)
    elif choice == '3':
        name = input("Enter name: ")
        contact_book.delete_contact(name)
    elif choice == '4':
        contact_book.display_contacts()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
