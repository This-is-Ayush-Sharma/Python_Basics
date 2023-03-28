
class Node:
    def __init__(self, data = None):
        self.dataval = data
        self.nextval = None

class SlinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

lst = SlinkedList()
lst.headval = Node(2)
e2 = Node(3)
e3 = Node(4)

#link part
lst.headval.nextval = e2
lst.headval.nextval.nextval = e3 

lst.listprint()