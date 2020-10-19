
# Encapsulation Assignment

# class Employee
class Employee:
    # initialize the object's values before object is created
    def __init__(self, name, email, salary, pin):
        # protected variable
        self.name = 'Unknown'
        self.email = 'Unknown'
        self._salary = 900 # protected attribute
        self.__pin = 9999 # private attribute

    # Private method
    def __getPin(self):
        print("Your private pin number: {}", self.__pin)

# Instantiate a class object
emp1 = Employee("Bob Smith", "bobsmith@gmail.com", 22000, 1612)
print(emp1.name)
print(emp1.email")
print(emp1._salary)
emp1.__getPin()
        
     
        
