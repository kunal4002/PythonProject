from BankAccount import BankAccount


class SavingsAccount(BankAccount):
    __AccNumber = None

    def __init__(self, AccNumber, initialAmt):
        super().__init__(AccNumber, initialAmt)
        print("Congratulations... Your Savings Account has been created :" + str(AccNumber))

    def SavDeposit(self, amount):
        Interest = amount * 3 / 100
        amount += Interest
        print(str(Interest) + " is the amount of interest  added to your account ")
        self.Deposit(amount)
