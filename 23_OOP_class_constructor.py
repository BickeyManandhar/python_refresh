class Employee:
  salary = 50000
  age = 30

# dunder method which is automatically called when an object is created
  def __init__(self, name, salary, age):
    self.name = name        # instance attribute
    self.salary = salary    # instance attribute
    self.age = age          # instance attribute
    print("Employee class constructor called")

# need "self" parameter to access instance attributes, even if not used
  def getInfo(self):
    print(f"This is Employee class")

  # if we are not using "self", we can define method as staticmethod
  @staticmethod
  def getStaticInfo():
    print("This is a static method")

emp1 = Employee("John", 50000, 30)
print(emp1.name)    # Output: John
print(emp1.age)     # Output: 30      
print(emp1.salary)  # Output: 50000
emp2 = Employee("Jane", 60000, 25)  
print(emp2.name)    # Output: Jane
print(emp2.age)     # Output: 25
print(emp2.salary)  # Output: 60000
