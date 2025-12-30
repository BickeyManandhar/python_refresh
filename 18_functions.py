# function defination
def avg():
  a= int(input("Enter first number: "))
  b= int(input("Enter second number: "))
  c= int(input("Enter third number: "))
  average = (a+b+c)/3
  print("Average is:", average)

def print_message(message):
  print(type(message))
  print(message)

def multiply(x, y):
  return x * y

def greet(msg, name="User"):
  print(f"Hello {name}!, {msg}")

# function call
avg()
print_message("Hello, welcome to the function demonstration!")
print_message(42)

mul=multiply(6, 7)
print("Multiplication result is:", mul)

greet("Welcome to Python functions!", "Alice")
greet("Welcome to Python functions!")