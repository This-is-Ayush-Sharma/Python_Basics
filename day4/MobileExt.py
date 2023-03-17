class Mobile:

    def __init__(self,brand,price):
        self.price = price
        self.brand = brand

    def returnedAmt(self):
        print(self.price - self.total_price)
    def purchase(self):
        if(self.brand == "Apple"):
            discount = 10
        else:
            discount = 5
        self.total_price = self.price - self.price * (discount/100)
        print("Brand is",self.brand,"Total price is",self.total_price)
        self.returnedAmt()

mob1 = Mobile("Apple", 20000)
mob2 = Mobile("Samsung", 10000)
mob1.purchase()
mob2.purchase()