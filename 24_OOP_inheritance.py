class Employee:
  company = "ABC Corp"

  def show(self):
    print(f"Employee works at {self.company}")

class Coder:
  language = "Python"
  def code(self):
    print(f"Coder writes code in {self.language}")

# Programmer class inherits from Employee class and Coder class
class Programmer(Employee, Coder):
  def getLanguage(self):
    print("Programmer codes in Python")

prog = Programmer()
prog.show()          # Output: Employee works at ABC Corp
prog.getLanguage()   # Output: Programmer codes in Python
prog.code()          # Output: Coder writes code in Python