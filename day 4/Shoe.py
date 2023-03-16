class Shoe:
    def __init__(self, price, material):
        self.price = price
        self.material = material

s1 = Shoe(1000, "Canvas")
print("Unique id of object",id(s1))
print(s1.price, s1.material)

s2 = Shoe(1000, "Canvas")
print("Unique id of object",id(s2))
print(s2.price, s2.material)