class DataStructure:
    def __init__(self,totalSize):
        self.maxSize = totalSize

        self.stack = [None] * self.maxSize
        self.top = -1

        self.queue = [None] * self.maxSize
        self.front = 0
        self.rear = -1

    def is_Q_full(self):
        if(self.rear == self.maxSize-1):
            return True
        return False
    
    def is_stack_full(self):
        if(self.top == self.maxSize - 1):
            return True
        return False

    def Insert_Q_end(self,data):
        if(self.is_Q_full()):
            print("Queue is full")
        else:
            self.rear += 1
            self.queue[self.rear] = data

    def insert_into_stack(self, data):
        if(self.is_stack_full()):
            print("The stack is full")
        else:
            self.top += 1
            self.stack[self.top] = data

    def printQueue(self):
        print("The data in the queue is:-",end=' ')
        for i in range(self.front, self.rear+1):
            print(self.queue[i],end = ' ')
        print()

    def printStack(self):
        for i in range(self.top, -1,-1):
            print(self.stack[i], end=' ')
        print()

    def logic(self):
        for i in range(self.front, self.rear+1):
            if(i % 2 == 1):
                # self.insert_into_stack(self.queue[i])
                for j in range(1,self.queue[i]+1):
                    n = (j * (j+1))//2
                    if(n == self.queue[i]):
                        self.insert_into_stack(self.queue[i])
                        break
                    if(n > self.queue[i]):
                        break


ds = DataStructure(10)
ds.Insert_Q_end(7)
ds.Insert_Q_end(28)
ds.Insert_Q_end(8)
ds.Insert_Q_end(35)
ds.Insert_Q_end(3)
ds.Insert_Q_end(6)
ds.Insert_Q_end(5)
ds.Insert_Q_end(15)
ds.Insert_Q_end(2)
ds.Insert_Q_end(5)

ds.printQueue()
ds.logic()
ds.printStack()