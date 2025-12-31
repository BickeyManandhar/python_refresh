class Employee:
  company = "ABC Corp"
  def __init__(self):
    print("Employee class constructor called")


class Programmer(Employee):
  
  def __init__(self):
    super().__init__()  # call the constructor of the parent class
    print("Programmer class constructor called")

prog = Programmer()
