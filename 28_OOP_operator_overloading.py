class Number:
  def __init__(self, value):
    self.value = value

# Operator Overloading for +
  def __add__(self, other):
    return self.value + other.value

n = Number(10)
m = Number(20)

print (n + m)