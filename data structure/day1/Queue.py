class Queue:

    def __init__(self, max_size):
        self.__max_size = max_size
        self.__elements = [None] * self.__max_size
        self.__front = 0
        self.__rear = -1

    def is_full(self):
        if(self.__rear == (self.__max_size - 1)):
            return True
        return False
    
    def is_empty(self):
        if(self.__front > self.__rear):
            return True
        return False
    
    def enqueue(self, data):
        if(self.is_full()):
            print("~ the queue is full ~")
        else:
            self.__rear += 1
            self.__elements[self.__rear] = data

    def dqueue(self):
        if(self.is_empty()):
            print("The queue is empty.")
        else:
            data = self.__elements[self.__front]
            self.__front += 1
            return data
    
    def display(self):
        if(self.is_empty()):
            print("~ The queue is empty ~")
        else:
            for i in range(self.__front, self.__rear+1):
                print(self.__elements[i],end=' ')
            print()

queue = Queue(4)


queue.is_full()
# enqueue
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)

queue.display()

print("delete",queue.dqueue())
queue.display()