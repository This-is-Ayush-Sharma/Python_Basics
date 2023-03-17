class Mobile:
    def __init__(self):
        print(id(self))
    def display(self):
        print("Display details")
    
    def purchase(self):
        self.display()
        print("Calculating the price")

Mobile().purchase()
Mobile().purchase()
Mobile().purchase()