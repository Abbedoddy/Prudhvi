#Regular Expressions - Sequence of characters that define a search pattern in a given string/file.
#Applications:
#• Search for particular patterns in string
#• File Processing
#• Extract data from log files by matching certain patterns
#In order to work with regular expressions, we need to import module RE.
'''This RE module provides a set of in-built functions, that enables programmer to
search for matching patterns/string.'''
#matching = re.search(pattern,s)
#matching.group()

import re
s = "His@_name is \\Prudhvi\\ and he is a python developer. Employee code is:IN0011591"
t = r"His@_name is \\Prudhvi\\ and he is a python developer. Employee code is:IN0011591"
print(s)
print(t)
print("The matching word using search in string s:",re.search(r'Prudhvi',s))
print("The matching word using search in string t:",re.search(r'Prudhvi', t))
print(s[14:21])
print(t[15:22])
'''print(re.search(r'Prudhvi',s).group())
matching = re.search(r'Prudhvi',s)
name_variable = matching.group()
print(name_variable)
print(re.search(r'P',s).group())
print(re.search(r'P......',s).group())
print(re.search(r'P..', s).group())
print(re.search(r'IN....',s).group())
print(re.search(r'......591',s))
print(re.search(r'......591',s).group())
print(re.findall(r'....1',s))
print(re.findall(r'....i',s))
print(re.findall(r'...i',s))
print(re.findall(r'p',s))
print(len(re.findall(r'p',s)))
print(re.search(r'...d...',s).group())
print(s,'\n'+str(len(s)))
print(re.search(r'\w',s).group())#w-1st occurence of a charecter in a given string.Using search keyword
print(re.search(r'\w+',s).group())#w+=1st occurence of a word in a given string.Using search keyword
print(re.search(r'\W',s).group())#W-Nonword 1st occurence accurence in a given string.Using search keyword 
print(re.findall(r'\w',s))#w-Total charecters in a given string.Using findall keyword
print(len(re.findall(r'\w',s)))
print(re.findall(r'\W',s))#W=Total Nonword charecters in a given string.Using findall keyword
print(len(re.findall(r'\W',s)))
print(re.findall(r'\w+',s))
print(len(re.findall(r'\w+',s)))
print(re.findall(r'\d',s))
print(re.findall(r'\d+',s))
print(re.findall(r'\d\d\d',s))
print(re.findall(r'\w\w\w',s))
print(re.findall(r'\w+\d',s))
e=re.search(r'...h', s)
print(e.group())
print(re.findall(r'IN',s))'''