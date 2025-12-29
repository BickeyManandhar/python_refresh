name = "bickey"
greeting = f"Hello, {name}!"
print(greeting)

#Bickey 
# index
#012345
#-6-5-4-3-2-1

nameshort = name[0:3] # include 0 to 2 not 3
print(nameshort)

nameshort2 = name[-3:]
print(nameshort2)  # same as above

#skipping
newname = "Bickeyyyyy"
skippedname = newname[0:8:2]  # start to 7, step by 2
print(skippedname)

#string functions
lengthname = len(name)
print(lengthname)
print(name.endswith("y"))
print(name.startswith("Bick"))
print(name.capitalize())
uppername = name.upper()
print(uppername)
lowername = name.lower()
print(lowername)

findname = name.find("key")
print(findname)

findname2 = name.find("ikey") 
print(findname2) # returns index of first occurrence or -1 if not found

newstring = "Hello name, today is date."

replacedstring = newstring.replace("name", "Bickey").replace("date", "Monday")
print(replacedstring)