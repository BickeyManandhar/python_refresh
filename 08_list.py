listofrandom = ["apple", "banana",False, True, 4, 4.25, None]
print(listofrandom)
listofrandom[0] = "orange" #mutable
print(listofrandom)
print(listofrandom[1:3])

#functions
print(len(listofrandom))
listofrandom.append("new item")
print(listofrandom)
listofrandom.remove(False)
print(listofrandom)
listofrandom.insert(2, "inserted item")
print(listofrandom)
listofrandom.pop()
print(listofrandom)
# listofrandom.sort() #will give error because of mixed data types
# print(listofrandom)
listofrandom.reverse()
print(listofrandom)