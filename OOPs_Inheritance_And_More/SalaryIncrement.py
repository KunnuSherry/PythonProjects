# Create a class ‘Employee’ and add salary and increment properties to it.Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter which changes the value of increment based on the salary.


class Employee:
    salary = 240
    increment = 20

    @property
    def SalaryAfterIncrement(self):
        return (self.salary + self.increment)
    @SalaryAfterIncrement.setter
    def SalaryAfterIncrement(self, Increment):
        self.increment = Increment

e = Employee()
print(e.SalaryAfterIncrement)
e.SalaryAfterIncrement = 40
print(e.SalaryAfterIncrement)