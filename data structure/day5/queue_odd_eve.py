class Queue:
    def __init__(self, total_size):
        self.maxSize = total_size
        
        self.queue1 = [None]*self.maxSize
        self.front1 = 0
        self.rear1 = -1

        self.queue2 = [None]*self.maxSize
        self.front2 = 0
        self.rear2 = -1

        self.queue3 = [None]*self.maxSize
        self.front3 = 0
        self.rear3 = -1

    def is_full(self):
        if(self.rear1 == (self.maxSize - 1)):
            return True
        return False
    
    def is_empty(self):
        if(self.rear1 < self.front1):
            return True
        return False
    
    def Insert_At_End(self, data):
        if(self.is_full()):
            print("Queue is full")
        else:
            self.rear1 += 1
            self.queue1[self.rear1] = data

    def printQ1(self, lst, start, end):
        for i in range(start,end+1):
            print(lst[i],end=' ')
        print()

    def logic(self):
        if(self.is_empty()):
            print("The list is empty")
        else:
            for i in range(self.front1, self.rear1+1):
                if(self.queue1[i] % 2 == 0):
                    self.rear2 += 1
                    self.queue2[self.rear2] = self.queue1[i]
                else:
                    self.rear3 += 1
                    self.queue3[self.rear3] = self.queue1[i]
x = Queue(5)
x.Insert_At_End(1)
x.Insert_At_End(2)
x.Insert_At_End(3)
x.Insert_At_End(4)
x.Insert_At_End(5)

x.logic()
print("The original queue")
x.printQ1(x.queue1,x.front1,x.rear1)

print("The even values")
x.printQ1(x.queue2,x.front2,x.rear2)

print("The odd values")
x.printQ1(x.queue3,x.front3,x.rear3)


