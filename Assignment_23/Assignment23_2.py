class BankAccount:

    ROI = 10.5

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print("Account Holder Name:", self.Name)
        print("Current Balance:", self.Amount)

    def Deposit(self, amt):
        self.Amount = self.Amount + amt
        print(amt, "deposited successfully.")

    def Withdraw(self, amt):
        if self.Amount >= amt:
            self.Amount = self.Amount - amt
            print(amt, "Withdrawn successfully.")
        else:
            print("Insufficient balance!")

    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100
        return Interest


obj1 = BankAccount("Rahul", 5000)
obj1.Display()
obj1.Deposit(2000)
obj1.Display()
obj1.Withdraw(3000)
obj1.Display()

Ret = obj1.CalculateInterest()
print("Interest on current balance:", Ret)

print("-" * 50)

obj2 = BankAccount("Amit", 10000)
obj2.Display()
obj2.Deposit(5000)
obj2.Withdraw(2000)
obj2.Display()

Ret = obj2.CalculateInterest()
print("Interest on current balance:", Ret)
