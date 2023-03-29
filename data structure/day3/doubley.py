class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class DLinked:
    
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        if(self.head == None):
            return True
        return False

    def insert_at_first(self,data):
        node = Node(data)
        if(self.is_empty()):
            self.head = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node

    def insert_at_end(self,data):
        node = Node(data)
        if(self.is_empty()):
            self.head = node
        else:
            copy = self.head
            while copy.next is not None:
                copy = copy.next
            copy.next = node
            node.prev = copy

    def length(self):
        copy = self.head
        c = 0 
        while copy is not None:
            c+=1
            copy=copy.next
        return c



    def printList(self):
        copy = self.head
        while copy is not None:
            print(copy.data, end=' ')
            copy = copy.next
        print()

    def insert_at_position(self, data, pos):
        copy = self.head
        c = 0
        while copy is not None:
            c += 1
            if(c == pos-1):
                break
            copy = copy.next
        if(pos == 1):
            self.insert_at_first(data)
        elif copy is None:
            self.insert_at_end(data)
        elif copy.next is None:
            self.insert_at_end(data)
        else:
            node = Node(data)
            node.next = copy.next
            node.prev = copy
            copy.next = node
        
    def delete_from_beginning(self):
        if(self.is_empty()):
            print("List is empty")
        else:
            self.head = self.head.next
            self.head.prev = None

    def delete_from_last(self):
        copy = self.head

        while copy.next is not None:
            copy = copy.next
        
        copy = copy.prev
        copy.next = None

    def delete_from_position(self,pos):
        if(self.is_empty()):
            print("The list is empty")
        elif(pos == 1):
            self.delete_from_beginning()
        else:
            copy = self.head
            c = 1
            while copy is not None:
                if(c == pos):
                    break
                copy = copy.next
                c+=1
            if(copy is None):
                print("Suffecient element are not there")
            elif(copy.next is None):
                self.delete_from_last()
            else:
                temp = copy.prev
                temp.next = copy.next
                temp.next.prev = copy.prev  
                
            
x = DLinked()
print("Check for empty status", x.is_empty())
print("Insert at first")
x.insert_at_first(1)
x.insert_at_first(2)
x.insert_at_first(3)
x.insert_at_first(4)

x.printList()
print("Size the linked list",x.length())
print("Insert at end")
x.insert_at_end(23)
x.insert_at_end(12)
x.printList()

print("Insert At position 2 data = 5")
x.insert_at_position(5, 1)
x.printList()

print("Delete the first node")
x.delete_from_beginning()
x.printList()

print("Delete from last")
x.delete_from_last()
x.printList()

print("Delete from position")
x.delete_from_position(2)
x.printList()