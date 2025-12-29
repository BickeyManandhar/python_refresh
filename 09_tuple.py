# tuple is immutable data type in python

t = (1, 2, 3, 4, 5,3,2,3,3,3)
print(type(t))
print(t)

t1 = (1,) # single element tuple
print(type(t1))
print(t1)
# t1[1] = 2 # this will raise error because tuple is immutable


#################
# functions of tuple

no = t.count(3) # count of element in tuple
print(f"number of 3 in tuple is {no}")

index = t.index(4) # index of element in tuple
print(f"index of 4 in tuple is {index}")