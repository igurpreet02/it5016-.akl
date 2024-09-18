class Account:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.__balance=balance
    def deposite(self,amount):
        if amount>0:
            self.__balance += amount
            print(f"${amount} deposited.")
        else:
            print("deposited amount must be postivily")
        
    def withdraw(self,amount):
        if 0<amount<=self.__balance:
            self.__balance-=amount
            print(f"${amount} withdraw")
        else:
            print("insufficient balance or invalid amount:")
    def get_balance(self):
        return self.__balance
acc=Account("james",100)
print(acc.owner)
acc.deposite(50)
print(acc.get_balance())
acc.withdraw(75)
print(acc.get_balance())