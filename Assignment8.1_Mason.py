#********************************************************
# CIS245 Week 8 Assignment 8.1
# Banking Application 
# Robin Mason    October 20, 2019
# *******************************************************
class BankAccount:
    def __init__(self, accountNumber, balance):
        self.accountNumber = accountNumber
        self.balance = float(balance)

    def withdrawal(self, amount):
        self.amount = amount
        self.balance = self.balance - self.amount
        return self.balance

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        return self.balance
            
    def getBalance(self):
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, accountNumber, balance, interestRate, minBalance):
        BankAccount.__init__(self, accountNumber, balance)
        self.interestRate = float(interestRate)
        self.minBalance = float(minBalance)

    def addInterest(self, interestRate):
        self.interest = self.balance * self.interestRate
        self.balance = self.balance + self.interest
        return 'Interest of ' + str('${0:1.2f}'.format(self.interest)) + ' will be added bringing the balance to ' + str('${0:1.2f}'.format(self.balance))

    def checkMinimumBalance(self, minBalance):
        if self.balance < self.minBalance:
            return 'The balance of ' + str('${0:1.2f}'.format(self.balance)) + ' is below the minimum balance requirement of ' + str('${0:1.2f}'.format(self.minBalance))
        else:
            return 'The balance of ' + str('${0:1.2f}'.format(self.balance)) + ' meets the minimum balance requirement of ' + str('${0:1.2f}'.format(self.minBalance))

class CheckingAccount(BankAccount):
    def __init__(self, accountNumber, balance, fee, minBalance):
        BankAccount.__init__(self, accountNumber, balance,)
        self.fee = float(fee)
        self.minBalance = float(minBalance)	
    def deductFees(self, fee):
        self.balance = self.balance - self.fee
        return self.balance

    def checkMinimumBalance(self, minBalance):
        if self.balance < self.minBalance:
            return 'The balance of ' + str('${0:1.2f}'.format(self.balance)) + ' is below the minimum balance requirement of ' + str('${0:1.2f}'.format(self.minBalance)) + '.\nA fee of ' + str('${0:1.2f}'.format(self.fee)) + ' will be deducted bringing the balance to ' + str('${0:1.2f}'.format(self.deductFees(self.fee)))
        else:
            return 'The balance of ' + str('${0:1.2f}'.format(self.balance)) + ' meets the minimum balance requirement of ' + str('${0:1.2f}'.format(self.minBalance))

def main():
    runNum = 1
    bal = float(0)
    bal1 = float(100)
    bal2 = float(25)
    fees = float(5)
    minBal = float(50)
    rate = float(0.02)
    amount = float(0)
    newBalance = float(0)
    star = '*'
    choice = 'y'
    account = 'z'
    option = '1' 
    
    while runNum < 3:
        if runNum == 1:
            bal = bal1
        else:
            bal = bal2
        print()
        print('Banking Options (run number ' + str(runNum) + ') starting balance is: ' + str('${0:1.2f}'.format(bal)))
        print(60*star)
        account = input('Select an account: "c" for checking, "s" for savings, or "x" to exit: ')
        account = account.lower()
        if account == 'c':
            checking = CheckingAccount('C11223', bal, fees, minBal)
            print()
            while choice == 'y':
                print()
                print('Checking Options for account number: ' + checking.accountNumber)
                print(42*star)
                print('Check Balance: option=1')
                print('Withdrawal: option=2')
                print('Deposit: option=3')
                print('Exit: option=4')
                print()
                option = input('Enter the desired option: ')
                print()
                if option == '1':
                    newBalance = checking.getBalance()
                    print(checking.checkMinimumBalance(minBal))
                elif option == '2':
                    try:
                        amount = float(input('Enter the amount: '))
                    except:
                        print('That is not a valid amount, try again.')
                        continue 
                    newBalance = checking.withdrawal(amount)
                    print(checking.checkMinimumBalance(minBal))
                elif option == '3':
                    try:
                        amount = float(input('Enter the amount: '))
                    except:
                        print('That is not a valid amount, try again.')
                        continue 
                    newBalance = checking.deposit(amount)
                    print(checking.checkMinimumBalance(minBal))
                elif option == '4':
                    account = 'x'
                    runNum = 2
                    break
                else:
                    print('That is not a valid option, try again.')
                    continue
                    

        elif account == 's':
            savings = SavingsAccount('S11223', bal, rate, minBal)
            print()
            while choice == 'y':
                print()
                print('Savings Options for account number: ' + savings.accountNumber)
                print(42*star)
                print()
                print('Check Balance: option=1')
                print('Withdrawal: option=2')
                print('Deposit: option=3')
                print('Exit: option=4')
                print()
                option = input('Enter the desired option: ')
                if option == '1':
                    newBalance = savings.getBalance()
                    print(savings.checkMinimumBalance(minBal))
                elif option == '2':
                    try:
                        amount = float(input('Enter the amount: '))
                    except:
                        print('That is not a valid amount, try again.')
                        continue                   
                    newBalance = savings.withdrawal(amount)
                    print(savings.checkMinimumBalance(minBal))
                elif option == '3':
                    try:
                        amount = float(input('Enter the amount: '))
                    except:
                        print('That is not a valid amount, try again.')
                        continue
                    newBalance = savings.deposit(amount)
                    print(savings.addInterest(rate))
                elif option == '4':
                    account = 'x'
                    runNum = 2
                    break
                else:
                    print('That is not a valid option, try again.')
                    continue

        elif account != 'c' and account != 's' and account != 'x':
            print('That is not a valid option, try again')
            account = 'z'
        elif account == 'x':
            break

main()