# #file I/O operations in Python
# # There are two types of file
# 1. Text File
# 2. Binary File

#reading a file
file = open("demo_file.txt", "r") # r for read, w for write, a for append, r+ for read and write
content = file.read()
print(content)
file.close()

#writing to a file
file = open("write_demo_file.txt", "w")
file.write("Hello, this is a write demo file.\n")
file.write("This file is created using Python.\n")
file.close()

#reading the written file
file = open("write_demo_file.txt", "r")
print(file.read())
file.close()

#reading a file line by line
file = open("more_demo_file.txt", "r")
content = file.readlines() # returns a list of lines
print(content, type(content))
file.close()

#reading a file line by line with readline()
file = open("more_demo_file.txt", "r")  
line = file.readline()
while(line != ""):
    print(line)
    line = file.readline()
file.close()

#appending to a file
file = open("more_demo_file.txt", "a")
file.write("\nThis is an appended line.\n")
file.close()

# using with statement to handle file3
# it automatically closes the file after the block is executed
with open("demo_file.txt", "r") as file:
    content = file.read()
    print(content)
