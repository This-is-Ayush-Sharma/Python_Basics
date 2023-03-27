class Queue:

    def __init__(self,max_size):
        self.__max_size = max_size
        
        self.__elements = [None] * self.__max_size
        self.__evenly_divisible = [None] * self.__max_size
        
        self.__elementsFront = 0
        self.__elementsRear = -1

        self.__evenlyFront = 0
        self.__evenlyRear = -1
    
    def is_full(self):
        if(self.__elementsRear == self.__max_size - 1):
            return True
        else:
            return False
    
    def is_empty(self):
        if(self.__elementsFront > self.__elementsRear):
            return True
        else:
            return False
    
    def elementEnqueue(self, data):
        if(self.is_full()):
            print("~ the queue is full!")
        else:
            self.__elementsRear += 1
            self.__elements[self.__elementsRear] = data


    def evenlyEnqueue(self, data):
        self.__evenlyRear += 1
        self.__evenly_divisible[self.__evenlyRear] = data


    def logic(self):
        for i in range(self.__elementsFront, self.__elementsRear+1):
            c = 0
            for j in range(1,11):
                if(self.__elements[i] % j == 0):
                    c+=1
            if(c == 10):
                self.evenlyEnqueue(self.__elements[i])
                        

    def Elementsdisplay(self):
        for i in range(self.__elementsFront, self.__elementsRear+1):
            print(self.__elements[i], end= ' ')
        print()

    def display(self):
        for i in range(self.__evenlyFront, self.__evenlyRear+1):
            print(self.__evenly_divisible[i], end= ' ')
        print()

queue = Queue(5)
queue.elementEnqueue(13983)
queue.elementEnqueue(10080)
queue.elementEnqueue(7113)
queue.elementEnqueue(2520)
queue.elementEnqueue(2500)

queue.logic()

print("Original queue:-",end = ' ')
queue.Elementsdisplay()

print("After action:-", end = ' ')
queue.display()
