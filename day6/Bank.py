class OverdrawException(Exception):
    pass

class LimitReachedException(Exception):
    pass

class Account:
    
    def __init__(self, account_type, balance, min_balance):
        self.__account_type = account_type
        self.__balance = balance
        self.__min_balance = min_balance

    def get_account_type(self):
        return self.__account_type
    
    def get_balance(self):
        return self.__balance
    
    def get_min_balance(self):
        return self.__min_balance
    
    def set_balance(self, balance):
        self.__balance = balance


class Customer(Account):
    def __init__(self, id, name, age, account):
        self.__customer_id = id
        self.__customer_name = name
        self.__age = age
        self.__account = account

    def withdraw(self, amount):
        try:
            balance = self.get_balance()
            if(balance < self.get_min_balance()):
                raise LimitReachedException
            elif(balance < amount):
                raise OverdrawException
            else:
                balance -= amount
                self.set_balance(balance)
        except OverdrawException:
            print("Account balance is less")
        except LimitReachedException:
            print("Limit Reached!")

    def take_card(self):
        print("Take the card out of the ATM!")

    def get_customer_id(self):
        return self.__customer_id
    def get_customer_name(self):
        return self.__customer_name
    def get_age(self):
        return self.__age
    def get_account(self):
        return self.__account
    

class PrivilegedCustomer(Customer,Account):
    def __init__(self,customer_id,customer_name,age,bonus_points, account_type, account_balance, account_min_balance):
        Customer.__init__(self,customer_id,customer_name,age, account_type)
        Account.__init__(self, account_type, account_balance, account_min_balance)
        self.__bonus_points = bonus_points

    def get_bonus_points(self):
        return self.__bonus_points
    
    

    def increase_bonus(self):
        if(self.get_balance() > 1000):
            self.__bonus_points += 10
        else:
            self.__bonus_points += 2 
    
    
person = PrivilegedCustomer(100,"Gopal",43,100,"Savings",1200,500)

amt = int(input("Please enter the Amount to be withdrawn:- "))
person.withdraw(amt)   
person.increase_bonus()
print("Remaining balance",person.get_balance(),"\nBonus Points:-",person.get_bonus_points()) 
person.take_card()