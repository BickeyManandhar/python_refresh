class Employee:
  a =1

  @property
  def name(self):
    return f"{self.fname} {self.lname}"
  
  @name.setter
  def name(self, name):
    self.fname= name.split(" ")[0]
    self.lname = name.split(" ")[1]


emp1 = Employee()
emp1.name = "John Doe"
print(emp1.fname)  # Output: John Doe
print(emp1.lname) # Output: John