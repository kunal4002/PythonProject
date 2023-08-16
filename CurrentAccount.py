from BankAccount import BankAccount


class CurrentAccount(BankAccount):

    def __init__(self, AccNumber, initialAmt):
        super().__init__(AccNumber, initialAmt)
        print("Congratulations .... your current account has been created: " + str(self._AccNumber))

    def withdrawal(self, amount):
        amount -= 100
        print("Charge 200 is applicable for every withdraw: ")
        self.withdraw(amount)






