class Student:
    def __init__(self):
        self.__id = None
        self.__name = None
        self.__age = None
        self.__mark = None
        self.__course = {
            'CSE': 500000,
            'ECE': 4000000,
            'EEE': 3500000,
            'EE':  3200000,
            'CHEMICAL': 300000,
            'BIOTECH':  250000,
            'BCA': 200000,
            'MCA': 230000,
        }

    # Setter methods
    def set_Id(self, id):
        self.__id = id

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_mark(self, mark):
        self.__mark = mark

    # Getter methods

    def getter_Id(self):
        return self.__id

    def getter_name(self):
        return self.__name

    def getter_age(self):
        return self.__age

    def getter_mark(self):
        return self.__mark

    # Validation

    def validate_mark(self):
        if (self.__mark >= 0 and self.__mark <= 100 and self.__mark > 64):
            return True
        return False

    def validate_age(self):
        if (self.__age > 20):
            return True
        return False

    # Checking Done here
    def check_qualification(self):
        if (self.validate_age() and self.validate_mark()):
            print("Eligiable for admission\n Courses Available")
            print(' '.join(self.__course.keys()))
            course = input("Please enter the course you opt For:-")
            if (course in self.__course.keys()):
                print("You have Choosen", course)
                if (self.getter_mark() > 85):
                    print(
                        "Course fee is:-", self.__course[course] - ((25/100)*self.__course[course]))
                else:
                    print("Course fee is:-", self.__course[course])
            else:
                print("Invalid Course name Choosen")
        else:
            print("Not Eligiable for admission")


ayush = Student()
ayush.set_Id(147)
ayush.set_name("ayush")
ayush.set_mark(88)
ayush.set_age(21)
ayush.check_qualification()

print("\n")

Abhilash = Student()
Abhilash.set_Id(149)
Abhilash.set_name("Venu")
Abhilash.set_mark(64)
Abhilash.set_age(21)
Abhilash.check_qualification()
