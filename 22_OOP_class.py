class Employee:
  salary = 50000
  age = 30
  
  # need "self" parameter to access instance attributes, even if not used
  def getInfo(self):
    print(f"This is Employee class")

  # if we are not using "self", we can define method as staticmethod
  @staticmethod
  def getStaticInfo():
    print("This is a static method")

# Creating an instance of the Employee class
# Here name is instance/object attribute and age, salary are class attributes
emp1 = Employee()
emp1.name = "John"
print(emp1.name)    # Output: John
print(emp1.age)     # Output: 30
print(emp1.salary)  # Output: 50000
emp1.getInfo()  # Output: This is Employee class, 30 years old.
Employee.getStaticInfo()  # Output: This is a static method