class Queue:

    def __init__(self, FQsize, SQsize):
        self.__max_size = FQsize + SQsize
        
        self.__Fmax = FQsize
        self.__Smax = SQsize

        self.__element1 = [None] * FQsize
        self.__front1 = 0
        self.__rear1 = -1

        self.__element2 = [None] * SQsize
        self.__front2 = 0
        self.__rear2 = -1

        self.__element3 = [None] * (FQsize + SQsize)
        self.__front3 = 0
        self.__rear3 = -1

    
    def is_full_element1(self):
        if(self.__rear1 == self.__Fmax - 1):
            return True
        return False
    
    def is_full_element2(self):
        if(self.__rear2 == self.__Smax - 1):
            return True
        return False
    

    def is_empty_element1(self):
        if(self.__front1 > self.__rear1):
            return True
        return False

    def is_empty_element2(self):
        if(self.__front2 > self.__rear2):
            return True
        return False

    def element1_enqueue(self,data):
        if(self.is_full_element1()):
            print("Queue full")
        else:
            self.__rear1 += 1
            self.__element1[self.__rear1] = data
    
    def element2_enqueue(self,data):
        if(self.is_full_element2()):
            print("Queue full")
        else:
            self.__rear2 += 1
            self.__element2[self.__rear2] = data

    def element1_dqueue(self):
        if(self.is_empty_element1()):
            # print("Empty queue 1")
            return -999
        else:
            data = self.__element1[self.__front1]
            self.__front1 += 1
            return data
    
    def element2_dqueue(self):
        if(self.is_empty_element2()):
            # print("Empty queue 2")
            return -999
        else:
            data = self.__element2[self.__front2]
            self.__front2 += 1
            return data


    def element3_enqueue(self,data):
        self.__rear3 += 1
        self.__element3[self.__rear3] = data
    
    def logic(self):
        
        c = 0
        while(c < self.__max_size):
            c+=1
            d1 = self.element1_dqueue()
            d2 = self.element2_dqueue()
            if(d1 != -999):
                self.element3_enqueue(d1)
            if(d2 != -999):
                self.element3_enqueue(d2)
        

    
    def display1(self):
        # print(self.__element1)
        print("First queue")
        for i in range(self.__front1, self.__rear1+1):
            print(self.__element1[i],end =  ' ')
        print()

    def display2(self):
        # print(self.__element2)
        print("Second Queue")
        for i in range(self.__front2,self.__rear2+1):
            print(self.__element2[i],end = ' ')
        print()
    
    def display3(self):
        # print(self.__element3)
        print("Final queue")
        for i in range(self.__front3, self.__rear3+1):
            print(self.__element3[i],end = ' ')
        print()

queue = Queue(2,3)

queue.element1_enqueue(1)
queue.element1_enqueue(2)

queue.display1()

queue.element2_enqueue(11)
queue.element2_enqueue(22)
queue.element2_enqueue(33)

queue.display2()

queue.logic()
queue.display3()