class People:
    def __init__(self, name, age, gender):
        self.name = name 
        self.age = age 
        self.gender = gender

class Queue:
    def __init__(self, total_size):
        self.maxSize = total_size
        
        self.queue = [None]*self.maxSize
        self.front = 0
        self.rear = -1

    def is_full(self):
        if(self.rear == (self.maxSize - 1)):
            return True
        return False
    
    def is_empty(self):
        if(self.rear < self.front):
            return True
        return False
    
    def Insert_At_End(self, data):
        if(self.is_full()):
            print("Queue is full")
        else:
            self.rear += 1
            self.queue[self.rear] = data


    def logic(self,gender):
        if(self.is_empty()):
            print("The list is empty")
        else:
            for i in range(self.front, self.rear+1):
                if(self.queue[i].gender == gender):
                    print(self.queue[i].name, self.queue[i].age, self.queue[i].gender)
            

people1 = People("ayush",12,"Male")
people2 = People("shami",13,"Male")
people3 = People("rohan",14,"Male")
people4 = People("aastha",15,"Female")
people5 = People("shreya",16,"Female")

x = Queue(5)
x.Insert_At_End(people1)
x.Insert_At_End(people2)
x.Insert_At_End(people3)
x.Insert_At_End(people4)
x.Insert_At_End(people5)

x.logic('Male')