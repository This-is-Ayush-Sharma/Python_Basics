types = ['small','Small','medium','Medium']

class Customer:
    def __init__(self, customer, name, qunatity):
        self.__customer_name = name.title()
        self.__quantity = qunatity

    def Validate_Quantity(self):
        if(self.__quantity in range(1,6)):
            return True
        else:
            return False
    
    def get_Customer_Name(self):
        return self.__customer_name
    
    def get_Qunatity(self):
        return self.__quantity
    
class PizzaService:
    counter = 100

    def __init__(self, customer, pizza_type, additional_toppings):
        self.__customer = customer
        self.__pizza_type = pizza_type
        self.__additional_toppings = additional_toppings
        self.pizza_cost = 0
        self.__service_id = None

    def Validate_Pizza_Type(self):
        if(self.__pizza_type.lower() in types):
            return True
        return False
    
    def Calculate_Pizza_Cost(self):
        if(self.Validate_Pizza_Type() and Customer.Validate_Quantity(self.__customer)):
            self.pizza_cost = 150 * Customer.get_Qunatity(self.__customer)

