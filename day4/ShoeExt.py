class Shoe:
    def __init__(self, price, material):
        self.price = price
        self.material = material
    
    def __str__(self):
        return f"{self.price} {self.material}"
    
s1 = Shoe(1000, "Canvas")
print(s1)