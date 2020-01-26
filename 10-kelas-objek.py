class Employee:
    'Common baes class for all employee'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary : ", self.salary)


emp1 = Employee("Habibi", 2000)
emp2 = Employee("Fath", 3000)
emp1.displayEmployee()
emp2.displayEmployee()
emp2.displayCount()
