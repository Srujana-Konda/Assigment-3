#Program 2: Create a vector and reshape it to 4/5 followed by replacing highest value in each row

import numpy as np
# Initializing random vector and reshaping it to 4,5
reshaped_vector = np.random.uniform(1, 20, 20).reshape(4, 5)
print("reshaped_vector:",reshaped_vector)
# Finding the maximum value's index
max_values = np.argmax(reshaped_vector , axis=1)
print(max_values)
# Replace max value of each row to 0
reshaped_vector[np.arange(reshaped_vector.shape[0]), max_values] = 0
print("reshaped_vector with replacement of highest values:", reshaped_vector)


#Program 1:
class EmployeeClass:
    # Create a data member to count the number of Employees
    count = 0
    
    # Create a constructor to initialize name, family, salary, department
    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        #Incrementing the count of employees 
        EmployeeClass.count += 1
    # Create a function to average salary
    def avg_salary(self):
        return self.salary / EmployeeClass.count

# Create a Fulltime Employee class and ensure it inherits the properties of Employee class
class FulltimeEmployee(EmployeeClass):
    pass
# Creating the instances of Fulltime Employee class and Employee class 
emp1 = EmployeeClass("Srujana", "Konda", 60000, "Manager")
emp2 = FulltimeEmployee("Mitra", "K", 70000, "Tester")
# Calling functions
print(emp1.avg_salary())
print(emp2.avg_salary())


