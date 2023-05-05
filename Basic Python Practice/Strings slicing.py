#s = "MontyPython'sFlyingCircus"

'''
print("1.", s)
print("2.", len(s))
print("3.", s[:])
print("4.", s[::])
print("5.", s[0:len(s):1])
print("6.", s[1:])
print("7.", s[-1:])
print("8.", s[1:-1])
print("9.", s[1:-1])

'''
'''
print("10.", s[-1])
print("11.", s[::-1])
print("12.", s[::-2])
print("13.", s[::1])
print("14.", s[::2])
print("15.", s[::3])
print("16.", s[:-3])
print("17.", s[-3::-1])
print("18.", s[-3::1])

print("19.", s[13::-1])
print("20.", s[13::1])
print("21.", s[1:1:1])
print("22.", s[1::1])
print("23.", s[-1::-1])
print("24.", s[3:-27])
print("25.", s[4:-17])
print("26.", s[-21:-11])
print("27.", s[-21:11])

print("28.", s[21:11])
print("29.", s[21:-11])
print("30.", s[13::-1])
print("31.", s[13::1])
print("32.", s[:15:-1])
print("33.", s[:15:1])
print("34.", s[21:-11:-1])
print("35.", s[13:-13:-1])
print("36.", s[5:-8:1])
print("37.", s[5:-8:-1])
print("38.", s[5:8:1])
print("39.", s[5:8:-1])
print("40.", s[-5:-8:1])
print("41.", s[-5:-8:-1])
print("42.", s[-5:8:1])
print("43.", s[-5:8:-1])
print("44.", s[8:-5:2])
print("45.", s[8:-5:-2])
print("46.", s[-8:-5:2])
print("47.", s[-8:-5:-2])
print("48.", s[-8:5:2])
print("49.", s[-8:5:-2])
print("50.", s[8:-5:2])
print("51.", s[8:-5:-2])
print("52.", s[30:])
print("53.", s[30:])'''
p="hi\thello\tPrudhvi\tyour\tid\tis\t1201"
q="Phython\'s\t123\tInstitute"
print(q)
print(len(p))#lenth of a string
print(p.capitalize())#The first charecter in the string Uppercase remaing all are lower case
print(p.casefold())#The all charecters in string returns lowercase
s=p.center(50,'-')#The center() method will center align the string, using a specified character (space is default) as the fill character.
print(s)
print(p.count("h"))#Mentioned charecter or word it counts how many times occurs in a whole string
print(p.count('h',0,10))#string.count(value, start, end)
print(p.encode())#we use encode fuction the starting of the string with ' encoute and ending of the string with encoute
print(q.encode())#if any string contains 'encoutes it stated with " and ends with "
print(p.endswith('1201'))#The endswith() method returns True if a string ends with the specified suffix. If not, it returns False.
s=q.expandtabs(2)#The expandtabs() returns a string where all '\t' characters are replaced with whitespace characters until the next multiple of tabsize parameter.
print(s)#The default tab is 8 we can use fuction expand tabs and we can also pass tabsize also 
print(p.expandtabs(5))#given tab size 5
s=q.find("123")#The find() method finds the first occurrence of the specified value.
print(s)
print(q.index("123")==s)#The index() method returns the position at the first occurrence of the specified value.
t=p.find("1211")#The find() method returns -1 if the value is not found.
print(t)
u=p.find('hello',0,16)#string.find(value, start, end) start	Optional. Where to start the search. Default is 0,Optional. Where to end the search. Default is to the end of the string
print(u)
#print(p.format()) The placeholder is defined using curly brackets: {}. Read more about the placeholders in the Placeholder section below.The format() method returns the formatted string.
a='your id is {id:}'#With Single Prefix 
print(a.format(id=1201))
b='User Name is {Myname:} and id is {id:}'.format(Myname="Prudhvi Reddy",id=1201)#With One or More Prefix Used string.format{value1=input1,value=input2}
print(b)
c={'x':'Prudhvi','y':'1201'}
print("My name {x} and id is {y}".format_map(c))
profession={'Name':['Prudhvi','Raghav'],'Profession':['Pyton Developer','Admin'],'Age':['29','31']}
print('{Name[0]} is an {Profession[0]} and he is {Age[0]} years old'.format_map(profession))#we can accees by using index value 
print('{Name[1]} is an {Profession[1]} and he is {Age[1]} years old'.format_map(profession))
g="I am super hero of my self"
d = g.split(" ")#By split we can split string ['word', 'word1', 'word3']
print(d)
e="prudhvi123"
print(e.isalnum())#The isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).
f="prudhvi 123"
print(f.isalnum())#Example of characters that are not alphanumeric: (space)!#%&? etc. It's show False 
g="Hello"
print(g.isalpha())#The isalpha() method returns True if all the characters are alphabet letters (a-z).
print(f.isalpha())#False:Example of characters that are not alphabet letters: (space)!#%&? etc.
print(g.isascii())#It contains the numbers from 0-9, the upper and lower case English letters from A to Z, and some special characters.
h="\u0030"
i="\u0047"
print(h.isdecimal())#The isdecimal() method returns True if all the characters are decimals (0-9).This method is used on unicode objects.
print(i.isdecimal())
print(e.isdigit())#The isdigit() method returns True if all the characters are digits, otherwise False.
print(h.isdigit())
print(e.isidentifier())#The isidentifier() method returns True if the string is a valid identifier, otherwise False.A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). A valid identifier cannot start with a number, or contain any spaces.
print(f.isidentifier())
print(e.islower())#The islower() method returns True if all the characters are in lower case, otherwise False.Numbers, symbols and spaces are not checked, only alphabet characters.
print(g.islower())
print(h.isnumeric())#The isnumeric() method returns True if all the characters are numeric (0-9), otherwise False.Exponents, like ² and ¾ are also considered to be numeric values."-1" and "1.5" are NOT considered numeric values, because all the characters in the string must be numeric, and the - and the . are not.
print(i.isnumeric())
print(e.isprintable())#The given string printable its return True otherwise its false
x="%1 \n of @"
print(x.isprintable())
y="  "
print(y.isspace())#The isspace() method returns True if all the characters in a string are whitespaces, otherwise False.
t="Hi How Are You"
#t.istitle()
print(t.istitle())#The istitle() method returns True if all words in a text start with a upper case letter, AND the rest of the word are lower case letters, otherwise False.Symbols and numbers are ignored.
k=",,,PRUDHVI DHAR REDDY  "
print(k.isupper())#The isupper() method returns True if all the characters are in upper case, otherwise False.Numbers, symbols and spaces are not checked, only alphabet characters.
tuple1=("Peter","John","Victor")
i=",".join(tuple1)#The join() method takes all items in an iterable and joins them into one string.A string must be specified as the separator.
print(i)#string.join(iterable)
y=k.ljust(18)
print(y,"Is a Phython Developer")
print(len(k))
print(len(y))
print(k.lower())#The lower() method returns a string where all characters are lower case.
print(k.lstrip())#The lstrip() method removes any leading characters (space is the default leading character to remove)
n=k.lstrip(",PRUDHVI")#string.lstrip(characters)
print(n)







