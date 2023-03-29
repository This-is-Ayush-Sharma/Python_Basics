class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        if(self.head is None):
            return True
        return False
    
    def insert_at_end(self,data):
        node = Node(data)
        if(self.is_empty()):
            self.head = node
        else:
            copy = self.head
            while copy.next is not None:
                copy = copy.next
            copy.next = node
    
    def logic(self):
        start = self.head
        if(start == None):
            return
        while start.next is not None:
            nxt = start.next
            if(nxt.data == start.data):
                start.next = nxt.next
                continue
            start = start.next

    def printList(self):
        copy = self.head
        while copy is not None:
            print(copy.data, end=' ')
            copy = copy.next
        print()

x = LinkedList()
print("Linked list status",x.is_empty())
x.insert_at_end(10)
x.insert_at_end(10)
x.insert_at_end(20)
x.insert_at_end(20)
x.insert_at_end(30)
x.insert_at_end(30)
x.insert_at_end(30)
x.insert_at_end(40)
x.insert_at_end(50)

x.printList()
x.head = None
x.logic()
x.printList()