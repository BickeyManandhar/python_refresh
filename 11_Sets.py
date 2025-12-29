s = {1,5,32,32,32,32}
e = set() # empty set

#properties of sets
"""
unique elements
unordered
mutable
"""

#methods
s.add(10)
print(s)
s.remove(5) # raises error if not found
print(s)
s.discard(100) # does not raise error if not found
print(s)
s.pop() # removes and returns an random element
print(s)
print(len(s))

s2 = {1,5,32,32,32,32}
print(s.union(s2)) # union
print(s.intersection(s2)) # intersection


