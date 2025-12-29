import os

# specifying directory
directory = "/"

# using os module to list contents of directory
contents = os.listdir(directory)

# print each file and dir name 
for item in contents:
    print(item)