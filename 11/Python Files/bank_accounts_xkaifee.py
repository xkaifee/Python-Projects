"""
Author: Xaen, xkaifee@purdue.edu
Assignment: 11.4 - Bank Accounts
Date: 11/13/2023

Description:
    This program creates a class that represents a bank account and a class.

Contributors:
    Name, login@purdue.edu [repeat for each]

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

"""Import additional modules below this line (starting with unit 6)."""


"""Write new functions below this line (starting with unit 4)."""
class Account: # This class provides the data of the account
    def __init__(self, balance): # This method initializes the account
        self.balance = balance
        print(f"New account balance: ${self.balance:.2f}")

    def deposit(self, amount): # This method deposits money into the account
        print(f"Deposit: ${amount:.2f}")
        self.balance += amount

    def withdraw(self, amount): # This method withdraws money from the account
        if self.balance >= amount:
            print(f"Withdraw: ${amount:.2f}")
            self.balance -= amount
        else:
            print(f"Withdraw: ${amount:.2f}")
            print("Insufficient funds. Withdrawal canceled.")

    def get_balance(self): # This method gets the balance of the account
        print(f"Balance: ${self.balance:.2f}")


class Savings(Account): # This class provides the functionality of the Account class
    def __init__(self, balance, interest_rate): # This method initializes the Savings account
        super().__init__(balance)
        self.interest_rate = interest_rate / 100

    def accrue_interest(self): # This method accrues interest on the Savings account
        interest_payment = self.balance * self.interest_rate
        print(f"Interest payment: ${interest_payment:.2f}")
        self.balance += interest_payment


def main():
  
    savings_account = Savings(balance=200, interest_rate=10)
    
    savings_account.get_balance()
    savings_account.deposit(12.34)
    savings_account.get_balance()
    savings_account.withdraw(40.00)
    savings_account.get_balance()
    savings_account.withdraw(200.00)
    savings_account.get_balance()
    savings_account.accrue_interest()
    savings_account.accrue_interest()
    savings_account.accrue_interest()
    savings_account.withdraw(200.00)
    savings_account.get_balance()

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
