#Properties of Dictionary in Python
"""
unordered
mutable
indexed
cannot contain duplicate keys
"""
d = {} # empty dictionary
marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 90
}

print(type(marks))  # Output: <class 'dict'>

print(marks["Charlie"])  # Output: 78

##
# methods of dictionary
print("----Methods of Dictionary----")
print(marks.keys())    # Output: dict_keys(['Alice', 'Bob', 'Charlie', 'Diana'])
print(marks.values())  # Output: dict_values([85, 92, 78, 90])
marks.update({"Eve": 88})
print(marks)  # Output: {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'Diana': 90, 'Eve': 88}
marks.update({"Alice": 95})  # Updating existing key
print(marks)  # Output: {'Alice': 95, 'Bob': 92, 'Charlie': 78, 'Diana': 90, 'Eve': 88}
print(marks.get("Eve"))  # Output: 88 # Output: {'Alice': 95, 'Bob': 92, 'Charlie': 78, 'Diana': 90, 'Eve': 88}
print(marks.get("Eve2")) # Output: None