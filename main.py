# banking system 
import random
user_data={}
transaction_history={}
MIN_BALANCE=500

def saving_account(username: str, user_password: int = 0, user_deposit: int = 0):
    """This function creates the Saving Account."""
    if user_password == 0:
        user_password = random.randint(1000, 9999)
    user_ac_no=random.randint(10_00_00_000, 99_99_99_999)
    if username in user_data:
        print("\n❌ Account already exists. Try a different username.")
        return
    user_data[username]={
        "Userpassword":user_password,
        "Userdeposit":user_deposit ,
        "UserAccountNumber":user_ac_no,
        "AccountType":"Savings A/C"
    }
    transaction_history[username ]=[]
    print(f"✅ Ok {username}, your Saving A/C is opened now.")
    print(f"🔑 Your password is {user_password}, and you deposited ₹{user_deposit}.")
    
    
 

    
def current_account(username: str, user_password: int = 0, user_deposit: int = 0):
    """This function creates the Current Account."""
    if user_password == 0:
        user_password = random.randint(1000, 9999)
    user_ac_no=random.randint(10_00_00_000, 99_99_99_999)
    if username in user_data:
        print("\n❌ Account already exists. Try a different username.")
        return
    user_data[username]={
        "Userpassword":user_password,
        "Userdeposit":user_deposit ,
        "UserAccountNumber":user_ac_no,
        "AccountType":"Current A/C"
    }
    transaction_history[username ]=[]
    print(f"✅ Ok {username}, your Current A/C is opened now.")
    print(f"🔑 Your password is {user_password}, and you deposited ₹{user_deposit}.")
    
    
def fixed_deposit_account(username: str, user_password: int = 0, user_deposit: int = 0):
    """This function creates the Fixed deposit Account."""
    if user_password == 0:
        user_password = random.randint(1000, 9999)
    user_ac_no=random.randint(10_00_00_000, 99_99_99_999)
    if username in user_data:
        print("\n❌ Account already exists. Try a different username.")
        return
    user_data[username]={
        "Userpassword":user_password,
        "Userdeposit":user_deposit ,
        "UserAccountNumber":user_ac_no,
        "AccountType":"Fixed Deposit A/C"
    }

    print(f"✅ Ok {username}, your Fixed deposit A/C is opened now.")
    print(f"🔑 Your password is {user_password}, and you deposited ₹{user_deposit}.")
    

def create_account(user_account_type):
    '''
    This function opens  the bank account
    1. Saving A/C
    2. Current A/C
    3. Fixed Deposit A/C
    
    '''
    try:
        if user_account_type not in [1, 2, 3]:
            print("\n❌ Invalid choice! Please enter a number between 1 and 3.")
            return
        
        username=input("Enter your Name : ").lower()
        user_password=int(input("Enter your password : "))
        user_deposit=int(input("Enter your initial Deposit : "))
        
        if user_account_type == 1:
            saving_account(username,user_password,user_deposit)
        elif user_account_type == 2:
            current_account(username,user_password,user_deposit)
        elif user_account_type == 3:
            fixed_deposit_account(username,user_password,user_deposit)
            
    except ValueError:
        print("\n❌ Invalid input! Please enter a number (1, 2, or 3).")
        
def check_balance(username):
    '''This is going to check the balance of the user'''
    if username not in user_data:
        print("\n❌ User not found! Please check the username.")
        return
    print("Your details is : ")
    for i, (key, value) in enumerate(user_data[username].items(), start=1):
        print(f"\t{i}. {key}: {value}")
       
       
def deposit_money(username):
    '''This function deposit the money in  the user account '''   
    if username not in user_data:
        print("\n❌ User not found! Please check the username.")
        return 
    try:
        if  user_data[username]["AccountType"] != "Fixed Deposit A/C":
            amount=int(input("Enter the money that you want to deposit: "))
            if amount <= 0:
                print("\n\u274C Invalid amount! Enter a positive value.")
                return
            user_data[username]["Userdeposit"] += amount
            transaction_history[username].append(f"Deposited ₹{amount}. New Balance: ₹{user_data[username]['Userdeposit']}")
            print(f"\n✅ Successfully deposited ₹{amount}. Your new balance is ₹{user_data[username]['Userdeposit']}.")
        else:
            print("You have a fixed deposit account . you cannot deposit the money")
    except ValueError:
        print("\n❌ Invalid amount! Please enter a valid number.")
    
def withdraw_money(username):
    '''This function withdraw the money in  the user account '''
    if username not in user_data:
        print("\n❌ User not found! Please check the username.")
        return
    try:
        if user_data[username]["AccountType"] == "Fixed Deposit A/C":
            print("\n🚫 Withdrawals are not allowed for Fixed Deposit accounts!")
            return
        
        amount=int(input("Enter the money that you want to Withdraw: "))
        if amount <= 0:
            print("\n\u274C Invalid amount! Enter a positive value.")
            return
        if user_data[username]["Userdeposit"] - amount < MIN_BALANCE:
            print("\n❌ You must maintain a minimum balance of ₹500.")
            return
        if user_data[username]["Userdeposit"] >= amount:
            user_data[username]["Userdeposit"]-=amount
            transaction_history[username].append(f"withdrawed ₹{amount}. New Balance: ₹{user_data[username]['Userdeposit']}")
            print(f"\n✅ Successfully withdrawed ₹{amount}. Your new balance is ₹{user_data[username]['Userdeposit']}.")
        else:
            print("\n❌ Insufficient balance! Please deposit money first. ")
    except ValueError:
        print("\n❌ Invalid amount! Please enter a valid number.") 
        
def transfer_money(sender):
    '''This function transfer the money from the user account '''
    if sender not in user_data:
        print("\n❌ User not found! Please check the username.")
        return
    if user_data[sender]["AccountType"] == "Fixed Deposit A/C":
        print("\n🚫 Transfers are not allowed for Fixed Deposit accounts!")
        return

    recipient = input("Enter the recipient's username: ").lower()
    if recipient not in user_data:
        print("\n❌ Recipient not found! Please check the username.")
        return
    try:
        amount=int(input("Enter the money that you want to Transfer: "))
        if amount <= 0:
            print("\n❌ Invalid amount! Enter a positive value.")
            return
        if user_data[sender]["Userdeposit"] - amount < MIN_BALANCE:
            print("\n❌ You must maintain a minimum balance of ₹500.")
            return
        if user_data[sender]["Userdeposit"] >= amount:
            user_data[sender]["Userdeposit"] -= amount
            user_data[recipient]["Userdeposit"] += amount
            
            transaction_history[sender].append(f"Transferred ₹{amount} to {recipient}. New Balance: ₹{user_data[sender]['Userdeposit']}")
            transaction_history[recipient].append(f"Received ₹{amount} from {sender}. New Balance: ₹{user_data[recipient]['Userdeposit']}")

            print(f"\n✅ Successfully transferred ₹{amount} to {recipient}. Your new balance is ₹{user_data[sender]['Userdeposit']}.")
        else:
            print("\n❌ Insufficient balance! Please deposit money first.")
    except ValueError:
        print("\n❌ Invalid amount! Please enter a valid number.")

    
def transactionhistory(username):
    '''Displays the user's transaction history.'''
    if username not in user_data:
        print("\n❌ User not found! Please check the username.")
        return
    if user_data[username]["AccountType"] == "Fixed Deposit A/C":
            print("\n🚫 There are no Transactions as you have a  Fixed Deposit accounts!")
            return
    if not transaction_history[username]:
        print("\n📜 No transactions found!")
        return
 
    print("\n📜 Transaction History:")
    for i , transaction in enumerate(transaction_history[username],start=1):
        print(f"\t{i}. {transaction}")
         
def login():
    """Logs in the user before transactions."""
    try:
        username = input("Enter your username: ").lower()
        if username in user_data:
            print("\tYou have an account.")
            for i in range(3,0,-1):  
                try:   
                    password = int(input("Enter your password: "))
                    if user_data[username]["Userpassword"] == password:
                        print(f"\n\u2705 Login successful! Welcome {username}.")
                        return username
                    
                    print(f"\n\u274C Incorrect Password.remaining chances {i-1} ") if (i-1) > 0 else None
                        
                except ValueError:
                     print("\n❌ Invalid input! Please enter a valid number.")
            print("\n🚫 Too many failed attempts. Please try again later.")
            return None         
        else:
            print("\n\u274C Your don't have any account yet.Please make an account first .")
            return None    
    except ValueError:
        print("\n\u274C Invalid data! . please enter again ")   

def main():
    '''
    This is the main function of the banking program 
    That shows the choices to the customer
    '''
    
    print("\n💳 Welcome to the Banking System!")
    print("\nEnter your choice: ")
    print("\t1. Create an account")
    print("\t2. Login to your account")
    print("\t3. Exit")
    while True:
        try:
            user_input=int(input("Enter Your Choice or Tell the number (1/3):"))
            if user_input == 1:            
                print("\tSo you want to open a bank account sir ")
                print("\tWhich bank account you want to open with us>>  ")
                account_type=["Saving a/c ","Current a/c","Fixed Deposit a/c" ]
                for i ,account in enumerate(account_type,start=1):
                    print(f"\t{i}. {account}")           
                try:
                    user_account_type = int(input("\nEnter the Type of Account (1-3): "))
                    create_account(user_account_type)
                except ValueError:
                    print("\n❌ Invalid input! Please enter a number between 1 and 3.")
            elif user_input == 2:
                username=login()
                if username:
                    print("\n\U0001F4BC Banking Menu: ")
                    print("\t1. Check Balance")
                    print("\t2. Deposit Money")
                    print("\t3. Withdraw Money")
                    print("\t4. Transfer Money")
                    print("\t5. View Transaction History")
                    print("\t6. Logout")
                    while True:
                        choice = int(input("\nEnter your choice (1-6): "))
                        if choice == 1:
                            check_balance(username)
                        elif choice == 2:
                            deposit_money(username)
                        elif choice == 3:
                            withdraw_money(username)
                        elif choice == 4:
                            transfer_money(username)
                        elif choice == 5:
                            transactionhistory(username)
                        elif choice == 6:
                            print("\n👋 Logged out successfully.")
                            break
                        else:
                            print("\n\u274C Invalid choice!")
                        
            elif user_input == 3:
                print("\n👋 Thank you for using my banking system. Have a great day!") 
                break
            else:
                print("\n🚧 Feature under development. Please choose another option.")   
    
        except ValueError:
            print("\n❌ Invalid input! Please enter a number between 1 and 3.")
            
      
  
if __name__ == "__main__":
    main()
    