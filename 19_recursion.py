def factorial(n):
  # base condition
  if(n==1 or n==0):
    return 1
  return n * factorial(n-1)

n = int(input("Enter a number to find its factorial: "))
print(f"The factorial of {n} is {factorial(n)}")


#practice

def natural_sum(n):
  # base condition
  if n == 1:
    return 1
  return n + natural_sum(n-1)

n = int(input("Enter a number to find the sum of first n natural numbers: "))
print(f"The sum of first {n} natural numbers is {natural_sum(n)}")

def remove_word_from_list_strip_word(word_list, word):
  new_list = []
  for item in word_list:
    if not (item == word):
      new_list.append(item.strip(word))
  return new_list
l = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape', 'ate', 'late']
word_to_remove = input("Enter a word to remove from the list: ")
print(f"Updated list: {remove_word_from_list_strip_word(l, word_to_remove)}")