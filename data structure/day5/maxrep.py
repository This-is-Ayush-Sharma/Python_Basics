class Node:
    def __init__(self,data = None):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
    
    def insert_At_end(self, data):
        node = Node(data)
        if(self.head == None):
            self.head = node
        else:
            copy = self.head
            while copy.next is not None:
                copy = copy.next
            copy.next = node

    def get_max(self):
        copy = self.head
        maxv = -999
        while copy is not None:
            if(copy.data > maxv):
                maxv = copy.data
            copy = copy.next
        return maxv
    
    def replace(self, new, maxv):
        copy = self.head
        while copy is not None:
            if(copy.data == maxv):
                copy.data = new
            copy = copy.next
    
    def printList(self):
        copy = self.head
        while copy is not None:
            print(copy.data,end= ' ')
            copy = copy.next
        print()

a = LinkedList()
a.insert_At_end(12)
a.insert_At_end(95)
a.insert_At_end(140)
a.insert_At_end(110)
a.insert_At_end(40)

print("Mav value is",a.get_max())
print("Original list")
a.printList()
a.replace(100, a.get_max())
print("after replacing max value with 100")
a.printList()