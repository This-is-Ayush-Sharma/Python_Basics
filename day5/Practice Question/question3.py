class Customer:
    def __init__(self,quantity):
        self.quantity = quantity
    def validate_quantity(self):
        if(self.quantity >= 1 and  self.quantity <= 5):
            return True
        return False
    
class PizzaService(Customer):
    counter = 100

    def __init__(self, quantity, type, toppings):
        Customer.__init__(self, quantity)
        self.type = type
        self.topping = toppings
        self.cost = None

    def validate_pizza_type(self):
        if((self.type == "small" or self.type == "medium") and self.validate_quantity()):
            return True
        return False
    
    def Calculate_pizza_cost(self):
        PizzaService.counter+=1
        print(f"S{PizzaService.counter}")
        print("------Testing------")
        if(self.type == "small" and self.topping == True):
            self.cost = 150+35
        elif(self.type == "small" and self.topping == False):
            self.cost = 150
        if(self.type == "medium" and self.topping == True):
            self.cost = 200+50
        elif(self.type == "medium" and self.topping == False):
            self.cost = 200
        else:
            self.cost = -1


class Doordelivery(PizzaService):

    def __init__(self,distance):
        self.distance_in_kms = distance
    
    def validate_distance_in_kms(self):
        if(self.distance_in_kms >=1 and self.distance_in_kms <= 10):
            return True
        else:
            return False
        

Pizza_Service = PizzaService(4,"small",True)
Pizza_Service.Calculate_pizza_cost()
print(Pizza_Service.cost)
# Door_Step_Delevary = Doordelivery()
    
    
