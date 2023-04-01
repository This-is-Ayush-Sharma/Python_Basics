class Table:
    def __init__(self, status = None):
        self.status = status
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def is_full(self):
        copy = self.head
        c = 0
        while copy is not None:
            c+=1
            copy = copy.next
        if(c >= 10):
            return True
        return False
    
    def Insert_at_end(self,status):
        table = Table(status)
        if(self.is_full()):
            print("There can be only 10 tables")
        elif(self.head == None):
            self.head = table
        else:
            copy = self.head
            while copy.next is not None:
                copy = copy.next
            copy.next = table

    def printTable(self):
        copy = self.head
        c = 1
        while copy is not None:
            print(f"{c} -> ",copy.status)
            copy = copy.next
            c+=1
        print()

class BakeHouse:
    def __init__(self, head):
        self.__occupied_table_list = head
    
    def get_occupied_table_list(self):
        print("Occupied table list:-")
        copy = self.__occupied_table_list
        c = 1
        f = 0
        while copy is not None:
            if(copy.status == "O"):
                f = 1
                print(f"{c}->", copy.status)
            copy = copy.next
            c+=1
        if(f == 0):
            print("All empty")


    def allocate_table(self):
        copy = self.__occupied_table_list
        c = 1
        while copy is not None:
            if(copy.status == "E"):
                print(f"\nTable {c} assigned")
                copy.status = "O"
                break
            copy = copy.next
            c+=1

    def deallocate_table(self, table_number):
        copy = self.__occupied_table_list
        c = 1
        while copy is not None:
            if(c == table_number):
                print(f"\nTable {c} deallocated assigned")
                copy.status = "E"
                break
            copy = copy.next
            c+=1


if __name__ == '__main__':
    x = LinkedList()
    for i in range(10):
        x.Insert_at_end("E")
    # x.printTable()

    bhouse = BakeHouse(x.head)
    while(1):
        print("\n1.Get occupied table list\n2.Allocate table\n3.Deallocate table")
        n = int(input("\nEnter your Choice:-"))
        if(n == 1):
            bhouse.get_occupied_table_list()
        elif(n == 2):
            bhouse.allocate_table()
        elif(n == 3):
            tn = int(input("Enter table number:-"))
            bhouse.deallocate_table(tn)
        else:
            print("Invalid input")