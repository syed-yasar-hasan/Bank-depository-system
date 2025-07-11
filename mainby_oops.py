import random

# Constants
MIN_BALANCE = 500

class BankAccount:
    def __init__(self, username, account_type, password=None, initial_deposit=0):
        """Initialize a new bank account."""
        self.username = username.lower()
        self.account_type = account_type
        self.password = password if password else random.randint(1000, 9999)
        self.account_number = random.randint(10_00_00_000, 99_99_99_999)
        self.balance = initial_deposit
        self.transaction_history = []

    def deposit(self, amount):
        """Deposit money into the account."""
        if self.account_type == "Fixed Deposit A/C":
            print("🚫 Deposits are not allowed for Fixed Deposit accounts!")
            return
        if amount <= 0:
            print("❌ Invalid amount! Enter a positive value.")
            return
        self.balance += amount
        self.transaction_history.append(f"Deposited ₹{amount}. New Balance: ₹{self.balance}")
        print(f"✅ Successfully deposited ₹{amount}. Your new balance is ₹{self.balance}.")

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if self.account_type == "Fixed Deposit A/C":
            print("🚫 Withdrawals are not allowed for Fixed Deposit accounts!")
            return
        if amount <= 0:
            print("❌ Invalid amount! Enter a positive value.")
            return
        if self.balance - amount < MIN_BALANCE:
            print("❌ You must maintain a minimum balance of ₹500.")
            return
        self.balance -= amount
        self.transaction_history.append(f"Withdrew ₹{amount}. New Balance: ₹{self.balance}")
        print(f"✅ Successfully withdrew ₹{amount}. Your new balance is ₹{self.balance}.")

    def transfer(self, recipient_account, amount):
        """Transfer money to another account."""
        if self.account_type == "Fixed Deposit A/C":
            print("🚫 Transfers are not allowed for Fixed Deposit accounts!")
            return
        if amount <= 0:
            print("❌ Invalid amount! Enter a positive value.")
            return
        if self.balance - amount < MIN_BALANCE:
            print("❌ You must maintain a minimum balance of ₹500.")
            return
        self.balance -= amount
        recipient_account.balance += amount
        self.transaction_history.append(f"Transferred ₹{amount} to {recipient_account.username}. New Balance: ₹{self.balance}")
        recipient_account.transaction_history.append(f"Received ₹{amount} from {self.username}. New Balance: ₹{recipient_account.balance}")
        print(f"✅ Successfully transferred ₹{amount} to {recipient_account.username}. Your new balance is ₹{self.balance}.")

    def show_balance(self):
        """Display account balance."""
        print(f"Your balance is ₹{self.balance}")
    def show_details(self):
        '''Display the details of the user'''
        print(f"Username: {self.username}")
        print(f"Account No : {self.account_number}")
        print(f"Password : {self.password}")
        print(f"Account Type  : {self.account_type}")
        print(f"Accounts balance  : {self.balance}")

    def show_transaction_history(self):
        """Show transaction history."""
        if not self.transaction_history:
            print("📜 No transactions found!")
            return
        print("\n📜 Transaction History:")
        for i, transaction in enumerate(self.transaction_history, start=1):
            print(f"\t{i}. {transaction}")

class BankingSystem:
    def __init__(self):
        """Initialize the banking system."""
        self.accounts = {}

    def create_account(self, account_type):
        """Create a new bank account."""
        username = input("Enter your Name: ").lower()
        if username in self.accounts:
            print("❌ Account already exists. Try a different username.")
            return
        password = int(input("Enter your password: "))
        initial_deposit = int(input("Enter your initial Deposit: "))
        self.accounts[username] = BankAccount(username, account_type, password, initial_deposit)
        
        print(f"✅ Account created successfully! \n\tUsername: {username},\tPassword: {password},\t Account Type {account_type}")

    def login(self):
        """Login to an account."""
        username = input("Enter your username: ").lower()
        if username not in self.accounts:
            print("❌ Account not found! Please create an account first.")
            return None
        for i in range(3,0,-1):
            try:
                password = int(input("Enter your password: "))
                if self.accounts[username].password == password:
                    print(f"✅ Login successful! Welcome, {username}.")
                    return self.accounts[username]
                print(f"❌ Incorrect Password.remaining chances {i-1} ") if (i-1) > 0 else None
            except ValueError:
                print("❌ Invalid input! Please enter a number.")
        print("🚫 Too many failed attempts. Try again later.")
        return None

    def run(self):
        """Run the banking system interface."""
        while True:
            print("\n💳 Welcome to the Banking System!")
            print("1. Create an account")
            print("2. Login to your account")
            print("3. Exit")
            try:
                choice = int(input("Enter Your Choice (1-3): "))
                if choice == 1:
                    print("Which bank account do you want to open?")
                    account_types = ["Savings A/C", "Current A/C", "Fixed Deposit A/C"]
                    for i, acc in enumerate(account_types, start=1):
                        print(f"{i}. {acc}")
                    acc_choice = int(input("Enter the Type of Account (1-3): "))
                    if acc_choice in [1, 2, 3]:
                        self.create_account(account_types[acc_choice - 1])
                    else:
                        print("❌ Invalid choice!")
                    
                elif choice == 2:
                    account = self.login()
                    if account:
                        print("\n1. Check Balance")
                        print("2.\t Deposit Money")
                        print("3.\t Withdraw Money")
                        print("4.\t Transfer Money")
                        print("5.\t View Transaction History")
                        print("6.\t View Account Details")
                        print("7.\t Logout")
                        while True:
                            option = int(input("Enter your choice (1-7): "))
                            if option == 1:
                                account.show_balance()
                            elif option == 2:
                                while True:
                                    try:
                                        amount = int(input("Enter deposit amount: "))
                                        if amount <= 0:
                                            print("❌ Please enter a valid amount!")
                                        elif amount == "exit":
                                            break
                                        else:
                                            account.deposit(amount)
                                            break
                                    except ValueError:
                                        print("❌ Invalid input! Enter a number.")
                            elif option == 3:
                                amount = int(input("Enter withdrawal amount: "))
                                account.withdraw(amount)
                            elif option == 4:
                                recipient_username = input("Enter recipient's username: ").lower()
                                if recipient_username in self.accounts:
                                    amount = int(input("Enter transfer amount: "))
                                    account.transfer(self.accounts[recipient_username], amount)
                                else:
                                    print("❌ Recipient not found!")
                            elif option == 5:
                                account.show_transaction_history()
                            elif option == 6:
                                account.show_details()
                            elif option == 7:
                                print("👋 Logged out successfully.")
                                break
                            else:
                                print("❌ Invalid choice!")
                elif choice == 3:
                    print("👋 Thank you for using the banking system. Have a great day!")
                    break
                else:
                    print("❌ Invalid choice! Enter 1, 2, or 3.")
            except ValueError:
                print("❌ Invalid input! Please enter a number.")

if __name__ == "__main__":
    system = BankingSystem()
    system.run()
