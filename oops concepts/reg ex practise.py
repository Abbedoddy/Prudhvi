import re
s="\\Hi welcome to monty python language \\ @The code should be UTF-8 and python is a interpreted language the name python discovered from the_show of monty cartoons--->Guido van Rossum is the author of python language and invented in the year @1991."
t=r'\\Hi welcome to monty python language \\ @The code should be UTF-8 and python is a interpreted language the name python discovered from the_show of monty cartoons--->Guido van Rossum is the author of python language and invented in the year @1991.'
#The raw string format should be (r'string') the r=raw. It reads whole strings no exception cases. 
print(f"The orginal string S:{s}\nThe length of orginal string:{len(s)}")
print()
print(f"The raw string S:{t}\nThe length of a raw string:{len(t)}")
#re.search(r'pattern',string)-To search given pattern present in a string or file.once find first occurence it will stop to search.
#matching = re.search(pattern,s)
#matching.group()
print(re.search(r'monty', s))
x=re.search(r'cartoon',t)
print(x.span())#span()it shows Print the position (start- and end-position) of the first match occurrence.
print(re.search(r'monty', s).group())
print(re.search(r'monty', t))
print(s[15:20]==t[16:21])
print(re.search(r'..............................................car...................',s).group())
print(re.search(r'........................91',s).group())
print(re.search(r'.......................interpreted..................',s))
print(re.search(r'.......................interpreted..................',s).group())
print(re.search(r'19..',s).group())
#find all - Returns a list containing all matches
print(re.findall(r'monty', s))
print(re.findall(r'cartoon',t))
print(re.findall(r'..............................................car...................',s))
print(re.findall(r'pyt...',s))
print(re.findall(r'--->................',s))
print(re.findall(r'@....',s))
print(re.findall(r'[A-Z]',s),len(re.findall(r'[A-Z]',s)))#Finding all upper case charecters in a given string or files.
print(re.findall(r'[a-z]',s),len(re.findall(r'[a-z]',s)))#Finding all lower case charecters in a given string or files.
print(re.findall(r'[0-9]',s))#Finding all digits in a given string or files.
print(re.findall(r'\w',s))#Finding all charecters and digits in a string.without special charecters.
print(re.findall(r'\w+',s))#Finding all words in a string without special charecters.
print(re.findall(r'\W',s))#Finding all only special charecters present in a given string.
print(re.findall(r'\W+',s))#Finding all special charecters with an continuous sequence present in a given string.
print(re.findall(r'\d',s))#Finding all digits in a given string or files.
print(re.findall(r'\d+',s))#Finding all digits in form of words in a given string or files.
print(re.findall(r'\d\d',s))#Finding two letter digit in given string or file
print(re.findall(r'\d\d\d\d',s))
print(re.findall(r'\w\w\w',s))#Returning 3 letter alphabit in a given string or file. without special charecters
print(re.findall(r'\W\W\W\W',s))
print(re.findall(r'\W[A-Z]',s))
print(re.findall(r'\w+[a-z]',s))
'''e=re.findall(r'\w+\s',s)
print(e)
r=""
for i in range(0,len(e)):
    r=r+e[i]   
print(r,type(r))'''
print(re.search(r'monty',s))
print(re.match(r'\\',s))
print(re.findall(r'\A\\H',s))#'\A string' -Returns a match if the specified characters are at the beginning of the string
print(re.findall(r'\bpy',s))#'\b string'-Returns a match where the specified characters are at the beginning or at the end of a word
print(re.findall(r'on\b',s))#'string \b'
print(re.findall(r'\Bart',s))
print(re.findall(r'art\B',s))
print(re.findall(r'\d',s))
print(re.findall(r'\D',s))
print(re.findall(r'\s', s),len(re.findall(r'\s',s)))
print(re.findall(r'\S',s))
print(re.findall(r'991.\Z',s))
print(re.findall(r'[car]',s))
print(re.findall(r'[A-H]',s))
print(re.findall(r'[a-zA-Z]+',s))
print(re.findall(r'[0-5][0-9]',s))
print(re.findall(r'[^a-z]',s))
print(re.findall(r'[+*.|()${}]',s))
print(re.findall(r'[^python]',s))
print(re.findall(r'[py.*n^]',s))
print(re.findall(r'[$python]',s))
print(re.findall(r'[91$]', s))
