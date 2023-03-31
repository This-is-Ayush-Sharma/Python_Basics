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
    
    def logic(self, posn, slist_head):
        c = 0
        copy = self.head
        while copy is not None:
            c+=1
            if(c == posn):
                d = copy.next
                while slist_head is not None:
                    node = Node(slist_head.data)
                    copy.next = node
                    copy = copy.next
                    slist_head = slist_head.next
                copy.next = d
                break
            copy = copy.next

    def printList(self):
        copy = self.head
        while copy is not None:
            print(copy.data,end=' ')
            copy = copy.next
        print()

a = LinkedList()
a.insert_At_end(1)
a.insert_At_end(2)
a.insert_At_end(4)
a.insert_At_end(3)
a.insert_At_end(5)
print("First linked List")
a.printList()

b = LinkedList()
b.insert_At_end(9)
b.insert_At_end(8)
b.insert_At_end(11)
print("Second Linked List")
b.printList()

a.logic(2, b.head)
a.printList()