class Example:

    def __init__(self,num):
        self.num = num
    
    def setter(self,num):
        self.num = num
    
    def getter(self):
        return self.num 

object = Example(10)
print(object.getter())
object.setter(15)
print(object.getter())