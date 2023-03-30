class Node:
    def __init__(self,name, no_of_customers, no_of_seats):
        self.name = name
        self.no_of_seats_reaserved = no_of_customers
        self.total_seats = no_of_seats
        self.next = None
    
class Compartments:
    def __init__(self):
        self.head = None

    def show_compartment(self):
        printval = self.head

        while printval is not None:
            print(printval.name,printval.no_of_seats_reaserved,printval.total_seats)
            printval = printval.next
        
    def Insert_At_End(self,name, no_of_customers, no_of_seats):
        node = Node(name, no_of_customers, no_of_seats)
        if(self.head is None):
            self.head = node
        else:
            copy = self.head
            while copy.next is not None:
                copy = copy.next
            copy.next = node

class Train:
    def __init__(self, train_name, compartment_List):
        self.__train_name = train_name
        self.__compartment_list = compartment_List
        
    def get_train_name(self):
        return self.__train_name

    def get_compartment_list(self):
        copy = self.__compartment_list
        print("Compartment list",end= ' ')
        while copy is not None:
            print(copy.name,end = ' ')
            copy = copy.next
        print()
    def count_compartments(self):
        copy = self.__compartment_list
        c = 0
        while copy is not None:
            c+=1
            copy = copy.next
        return c
    
    def check_vacancy(self):
        copy = self.__compartment_list
        c = 0
        while copy is not None:
            if((copy.total_seats//2) > copy.no_of_seats_reaserved):
                c+=1
            copy = copy.next
        return c





x = Compartments()
x.Insert_At_End("SL",250,400)
x.Insert_At_End("2AC",125,280)
x.Insert_At_End("3AC",120,300)
x.Insert_At_End("FC",160,300)
x.Insert_At_End("1AC",100,210)

# x.show_compartment()


t = Train("rajya raani",x.head)
print("Train name",t.get_train_name())
print("Total compartments",t.count_compartments())        
t.get_compartment_list()
print("Vacancy list", t.check_vacancy())

