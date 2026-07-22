class bank:
    def __init__(self , acoutnum , balc):
        bank.balance = balc
        bank.accountnumber = acoutnum
        print(bank.accountnumber , "your balnace is now :" , bank.balance)
    
    def credit(self , amount):
        bank.balance += amount
        self.printbalance()

    def debit(self , amount):
        bank.balance -= amount
        self.printbalance()

    def printbalance (self):
        print(bank.accountnumber , "your balnace is now :" , bank.balance)

b1 = bank(9509102373 , 1000)
b1.credit(500)
b1.debit(200)