class Bank:

    def __init__(self, id, name, age, balance):
        self.cust_id = id
        self.name = name 
        self.age = age 
        self.__wallet_balance = balance

    def showBalance(self):
        print("Your balance is",self.__wallet_balance)

    def update_balance(self,amount):
        if(amount < 1000 and amount > 0):
            self.__wallet_balance+=amount

c1 = Bank(1,"Venu", 22, 700000)
c1.showBalance()
c1.update_balance(500)
c1.showBalance()