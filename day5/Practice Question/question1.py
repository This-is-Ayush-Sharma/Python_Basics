class WeCare:
    def __init__(self):
        self.__id = None
        self.__type = None
        self.__cost = None
        self.__premium_amount = None

    def getter_Id(self):
        print("ID",self.__id)
        return self.__id
    
    def getter_Type(self):
        print("Type",self.__type)
        return self.__type

    def getter_Cost(self):
        print("Cost",self.__cost)
        return self.__cost

    def getter_Premium_Amount(self):
        print("Premium Amount",self.__premium_amount)
        return self.__premium_amount
    
    def setter_Id(self, id):
        self.__id = id
    def setter_Type(self, type):
        self.__type = type
    def setter_Cost(self, cost):
        self.__cost = cost

    def Calculate_premium_amount(self):
        if(self.__type == "Two Wheeler"):
            self.__premium_amount = (2/100) * self.__cost
        elif(self.__type == "Four Wheeler"):
            self.__premium_amount = (6/100) * self.__cost
        else:
            self.__premium_amount = "Invalid Vehicle Type"

obj = WeCare()
obj.setter_Id(123)
obj.setter_Type("Four Wheeler")
obj.setter_Cost(123343)
obj.Calculate_premium_amount()
obj.getter_Id()
obj.getter_Type()
obj.getter_Cost()
obj.getter_Premium_Amount()

# Update Id 
print("\nUpdating the id of the Objec/Instance using setter_Id method\n")
obj.setter_Id(125)
obj.getter_Id()
obj.getter_Type()
obj.getter_Cost()
obj.getter_Premium_Amount()
