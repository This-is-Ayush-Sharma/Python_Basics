class Employee:

    def __init__(self):
        print("Print constructor")
        self.emp_id = None
    def Check(self):
        if(self.emp_id >= 9000 and self.emp_id <= 1000):
            print("Eligible for benifits")
        else:
            print("not Eligible for benifits")

emp1 = Employee()
emp1.emp_id = 22
emp1.Check()

emp2 = Employee()
emp2.emp_id = 9001
emp2.Check()
