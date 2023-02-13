#LAB PP Q4 a

class Bank:
    def __init__(self, name, account_type, account_number, amount, interest_rate):
        self.name = name
        self.account_type = account_type
        self.account_number = account_number
        self.amount = amount
        self.interest_rate = interest_rate
    
    def deposit(self, amount):
        self.amount += amount
        return self.amount

    def withdraw(self, amount):
        if(self.amount < amount):
            return "Insufficient balance"
        self.amount -= amount
        return self.amount
    
    def FindInterest(self):
        if(self.amount >=500000):
            self.interest_rate = 0.08
        elif(self.amount >=100000):
            self.interest_rate = 0.07
        elif(self.amount >=50000):
            self.interest_rate = 0.06
        elif(self.amount >=10000):
            self.interest_rate = 0.05
        else:
            self.interest_rate = 0.04
        self.amount += self.amount * self.interest_rate
        return self.amount

b = Bank("Rudra", "Savings", 123456789, 1000, 0.05)
print(b.deposit(1000))
print(b.deposit(2000))
print(b.withdraw(500))
print(b.FindInterest())
