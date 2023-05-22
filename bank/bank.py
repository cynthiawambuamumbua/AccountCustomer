
# Add these attributes and behaviors to the class Account
# Add attributes deposits and withdrawals in the init method 
# which are empty lists by default and another attribute loan_balance
# which is zero by default.
class Account:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.deposits = []
        self.withdrawals = []
        self.loan_balance = 0

# Add a method check_balance which returns the account’s balance
    def check_balance(self):
        return self.balance
account = Account("cynthia")

# Update the deposit method to append each withdrawal transaction
#  to the deposits list. Each transaction should be in form of a dictionary
# like this  
# {
#    "amount": amount,
#    "narration": “deposit”
# }
def deposit(self, amount):
        self.balance += amount
        self.deposits.append({
            "amount": amount,
            "narration": "deposit"
        })
        account.deposit(1000)
   
# Update the withdrawal method to append each withdrawal transaction 
# to the withdrawals list. Each transaction should be in form of a dictionary 
# like like this 
# {
#    "amount": amount,
#    "narration": “withdrawal”
# }
def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.withdrawals.append({
                "amount": amount,
                "narration": "withdrawal"
            })
        else:
            print("Insufficient balance")
        account.withdraw(500)

# Add a new method  print_statement which combines both deposits 
# and withdrawals into one list and, using a for loop, prints each
# transaction in a new line like this
# deposit - 1000
# withdrawal - 500
def print_statement(self):
        for transaction in self.deposits + self.withdrawals:
            print(f"{transaction['narration']} - {transaction['amount']}")
        account.print_statement()

# Add a borrow_loan method which allows a customer to borrow if they
# meet these conditions:
# Account has no outstanding loan
# Loan amount requested is more than 100
# Customer has made at least 10 deposits.
# Amount requested is less than or equal to 13 of their total sum of all deposits.
# A successful loan increases the loan_balance by requested amount
def borrow_loan(self, amount):
        if self.loan_balance == 0 and amount > 100 and len(self.deposits) >= 10 and amount <= self.total_deposits() / 3:
            self.loan_balance += amount
        else:
            print("Loan not approved")
        account.borrow_loan(200)

# Add a repay_loan method with this functionality
# A customer can repay a loan to reduce the current loan_balance
# Overpayment of a loan increases the accounts current balance
def repay_loan(self, amount):
        if amount <= self.loan_balance:
            self.loan_balance -= amount
            self.balance += amount
        else:
            print("Loan amount exceeds outstanding loan ")
        account.repay_loan(100)
        

# Add a transfer method which accepts two attributes (amount and instance 
# of another account). If the amount is less than the current instance's 
# balance, the method transfers the requested amount from the current
# account to the passed account. The transfer is accomplished by reducing
# the current account balance and depositing the requested amount to
# the passed account.
def transfer(self, amount, another_account):
        if amount <= self.balance:
            self.balance -= amount
            another_account.balance += amount
        else:
            print("Insufficient balance")
        account.transfer(100, Account("jeff"))
        
def total_deposits(self):
        return sum([transaction["amount"] for transaction in self.deposits])
print(account.balance)