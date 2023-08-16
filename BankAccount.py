
class BankAccount:
    _CurrentBalance = None
    _AccNumber = None

    def __init__(self, AccNumber, CurrentBalance):
        self._CurrentBalance = CurrentBalance
        self._AccNumber = AccNumber

    def ShowBalance(self):
        print("Your current balance for the account : "+ str(self._AccNumber) + " is " + str(self._CurrentBalance))

    def CheckBalance(self, amount):
        if self._CurrentBalance < amount:
            return False
        else:
            return True


    def withdraw(self, amount):
        if self.CheckBalance(amount):
            self._CurrentBalance -= amount
            print(str(amount) + " is withdrawn from your account: " + str(self._AccNumber))
        else:
            print("Insufficient amount in account number: " + str(self._AccNumber))

    def Deposit(self, amount):
        self.CheckBalance(amount)
        self._CurrentBalance += amount
        print(str(amount) + " is deposited in your account : " + str(self._AccNumber))


    def Transfer(self,amount, BankAccount):
        self.withdraw(amount)
        BankAccount.Deposit(amount)














