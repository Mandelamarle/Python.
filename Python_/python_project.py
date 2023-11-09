#A simple bank account depositing system

class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def get_balance(self):
        #Returns the current balance of the account.
        return self.balance

    def deposit(self, amount):
        #Deposits the given amount into the account.

        #Args:
            #amount: The amount to deposit.

        #Returns:
            #A string indicating whether the deposit was successful.
        
        if amount <= 0:
            return "Invalid deposit amount."

        self.balance += amount
        return f"Deposit of ${amount} successful. New balance: ${self.balance}"

    def withdraw(self, amount):
        #Withdraws the given amount from the account.

        #Args:
            #amount: The amount to withdraw.

        #Returns:
            #A string indicating whether the withdrawal was successful.
        
        if amount <= 0 or amount > self.balance:
            return "Dear customer, your account balance is to complete this transaction."

        self.balance -= amount
        return f"Withdrawal of ${amount} successful. New balance: ${self.balance}"


class SavingsAccount(BankAccount):
    #Represents a savings account.

    def __init__(self, account_holder, balance=0, interest_rate=0.02):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        #Calculates the interest earned on the account.
        #Returns:
        #A string indicating the amount of interest earned.
        
        interest_amount = self.balance * self.interest_rate
        return f"Interest calculated: ${interest_amount}"


def print_account_info(account):
    #Prints the account information to the console.
    #Args:
    #Account: The bank account object.
    
    print(f"Account Holder: {account.account_holder}")
    print(f"Balance: ${account.get_balance()}")
    print("---------------")

# Creating a basic bank account

account1 = BankAccount("Mandela Koja")
print(account1.deposit(10000))
print(account1.withdraw(300))
print_account_info(account1)

# Creating a savings account

savings_account = SavingsAccount("Mandela Koja", 20000)
print(savings_account.deposit(500))
print(savings_account.calculate_interest())
print_account_info(savings_account)