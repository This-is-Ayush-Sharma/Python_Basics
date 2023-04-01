class Employee:
    
    def __init__(self, basic, qualification, ):
        self.basic = basic
        self.qualification = qualification
    
    def validate_basic_salary(self):
        if(self.basic > 3000):
            return True
        return False
    
    def validate_qualification(self):
        if(self.qualification not in ["Bachelors", "Masters"]):
            return False
        return True
    
class Graduate(Employee):

    def __init__(self, band):
        self.band = band
        self.gross = None
    
    def validate_job_band(self):
        if(self.band not in ["A", "B", "C"]):
            return False
        return True
    
    
