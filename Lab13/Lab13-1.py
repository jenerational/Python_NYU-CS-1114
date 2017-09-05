#Lab 13 Part II
#Jennie Walker 
# ONLY TWO UNDERSCORES 
class BankAccount(object):
    def __init__(self,account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def getBalance(self):
        return self.balance

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance-=amount
        else:
            print("You have tried to withdraw too much money.") 

    def deposit(self, amount):
        self.balance+=amount

def main():
    my_account = BankAccount("BOA123", 1000)
    print("Current balance is: ", my_account.getBalance()) #prints 1000
    my_account.deposit(100)
    print("Current balance is: ", my_account.getBalance()) #prints 1100
    my_account.withdraw(500)
    print("Current balance is: ", my_account.getBalance()) #prints 600
    my_account.withdraw(1000) #prints an error message

main()
