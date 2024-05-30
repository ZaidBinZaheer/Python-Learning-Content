class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = initial_balance

    def deposit(self, amount):
        """Deposit the specified amount into the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        """Withdraw the specified amount from the account."""
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def get_balance(self):
        """Return the current account balance."""
        return self.balance

# Creating a BankAccount instance
account = BankAccount(account_number="123456789", account_holder_name="John Doe", initial_balance=1000)

# Depositing money into the account
account.deposit(500)

# Withdrawing money from the account
account.withdraw(200)

# Checking account balance
balance = account.get_balance()
print(f"Current account balance: ${balance}")
