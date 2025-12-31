class Employee:
  company = "ABC Corp"

  @classmethod
  def show(cls):
    print("cls.company:", cls.company)

emp = Employee()

emp.company = "XYZ Inc"
emp.show()  # This will still print "ABC Corp" because show is a class method
