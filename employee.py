class Commission:
    def __init__(self, commissionType):
        self.commissionType = commissionType
        self.fixedCommission = 0
        self.commissionRate = 0
        self.contractLanded = 0 

    def setFixedCommission(self, bonus):
        self.fixedCommission = bonus

    def setCommissionRate(self, rate):
        self.commissionRate = rate

    def setContractLanded(self, contracts):
        self.contractLanded = contracts
    
    def getBonusCommission(self):
        return self.commissionRate * self.contractLanded
    
    def calcCommission(self):
        if self.commissionType == "Bonus Commission":
            return self.getBonusCommission()
        elif self.commissionType == "Fixed Commission":
            return self.fixedCommission
        else:
            return 0
        
    def commission(self):
        if self.commissionType == "Bonus Commission":
            return f" and receives a commission for {self.contractLanded} contract(s) at {self.commissionRate}/contract."
        elif self.commissionType == "Fixed Commission":
            return f" and receives a bonus commission of {self.fixedCommission}."
        else:
            return '.' 


class MonthlySalary(Commission):
    def __init__(self, commissionType, salary):
        super().__init__(commissionType)
        self.salary = salary

    def salary_pay(self): 
        return self.salary + Commission.calcCommission(self)
    

class HourlySalary(Commission):
    def __init__(self, commissionType, hoursWorked, hourRate):
        super().__init__(commissionType)
        self.hoursWorked = hoursWorked
        self.hourRate = hourRate 

    def hourly_pay(self):
        return (self.hoursWorked * self.hourRate) + Commission.calcCommission(self)

class Employee:
    def __init__(self, name, contractType):
        self.name = name
        self.contractType = contractType
        self.commissionType = ''
        self.salary = 0
        self.hoursWorked = 0
        self.hourRate = 0
        self.commission_obj = Commission(self.commissionType)

    def set_commission_type(self, commissionType):
        self.commissionType = commissionType
        self.commission_obj.commissionType = commissionType

    def set_salary(self, salary):
        self.salary = salary

    def setHoursWorked(self, hoursWorked):
        self.hoursWorked = hoursWorked

    def setWage(self, hourRate):
        self.hourRate = hourRate 
    
    def set_fixed_commission(self, commission):
        self.commission_obj.setFixedCommission(commission)

    def set_commission_rate(self, commissionRate):
        self.commission_obj.setCommissionRate(commissionRate)

    def set_contract_landed(self, contractLanded):
        self.commission_obj.setContractLanded(contractLanded)

    def get_pay(self):
        commission_amount = self.commission_obj.calcCommission()
        if self.contractType == "Monthly Contract":
            return self.salary + commission_amount
        elif self.contractType == "Hourly Contract":
            return (self.hoursWorked * self.hourRate) + commission_amount
        else:
            return 0
        
    def __str__(self):
        if self.contractType == "Monthly Contract":
            contract_info = f"{self.name} works on a monthly salary of {self.salary}{self.commission_obj.commission()} Their total pay is {self.get_pay()}."
        else:
            if self.hoursWorked == 1:
                hours = "hour"
            else:
                hours = "hours"
            contract_info = f"{self.name} works on a contract of {self.hoursWorked} {hours} at {self.hourRate}/hour{self.commission_obj.commission()} Their total pay is {self.get_pay()}."

        return contract_info
        

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee("Billie", "Monthly Contract")
billie.set_commission_type("No Commission")
billie.set_salary(4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee("Charlie", "Hourly Contract")
charlie.set_commission_type("No Commission")
charlie.setHoursWorked(100)
charlie.setWage(25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee("Renee",  "Monthly Contract")
renee.set_commission_type("Bonus Commission")
renee.set_salary(3000)
renee.set_commission_rate(200)
renee.set_contract_landed(4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee("Jan", "Hourly Contract")
jan.set_commission_type("Bonus Commission")
jan.setHoursWorked(150)
jan.setWage(25)
jan.set_commission_rate(220)
jan.set_contract_landed(3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee("Robbie", "Monthly Contract")
robbie.set_commission_type("Fixed Commission")
robbie.set_salary(2000)
robbie.set_fixed_commission(1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee("Ariel", "Hourly Contract")
ariel.set_commission_type("Fixed Commission")
ariel.setHoursWorked(120)
ariel.setWage(30)
ariel.set_fixed_commission(600)
