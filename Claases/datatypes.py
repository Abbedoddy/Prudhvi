
x = 10
y = x
k = "Python"
print(k) # Python
print(id(x)==id(y)) # True
print(id(x)==id(10)) # True
print(id(y)==id(20)) # False
z = id(x)==id(y)
print(z) # True
"""Strings - Represented in quotes, either single or double or triple
s1 = "Python"
s2 = 'Python is a programming language'
s3 = '''Python is a widelyy used language.
      It's syntax is easier to learn.'''
"""
s1 = "Python"
s2 = 'Python is a programming language'
s3 = 'Python is a widelyy used language. \
It\'s syntax is easier to learn.'
print(s1)
print(s2)
print(s3)
"""Datatypes - Immutable & Mutable
Immutables -Which cannot be modified- ex: Numbers, Strings, Tuples
Mutables - which can be modified - ex: Lists, Sets, Dictionaries

Indexing : Assigning a serial value to access the elements
Slicing : Dividing the given object into multiple parts based on indexing
"""

s1 = "Python Programming"
print(len(s1)) 
print(s1[8])
print(s1)
print(s1[::])
print(s1[:])
print(s1[::1])
print(s1[::2])
print(s1[::3])
print(s1[::-1])