from BankAccount import BankAccount
from SavingsAccount import SavingsAccount
from CurrentAccount import CurrentAccount


print("     Test Case 1     ")

B1 = BankAccount(101,500)
B2 = BankAccount(102,200)

B1.ShowBalance()
B2.ShowBalance()
B1.withdraw(200)
B2.Deposit(1000)
B2.Transfer(500,B1)
B1.ShowBalance()
B2.ShowBalance()

print("___________________________________________")

print("     Test Case 2    ")
S1 = SavingsAccount(103, 2000)
S1.ShowBalance()
S1.SavDeposit(500)
S1.ShowBalance()

print("________________________________________________")

print("     Test Case 3     ")

C1 = CurrentAccount(104,2000)
C1.Deposit(500)
C1.withdrawal(300)
C1.Transfer(500,S1)
C1.ShowBalance()
S1.ShowBalance()
print("________________________________________________")




