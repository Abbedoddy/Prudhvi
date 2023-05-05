#s="\\Hi welcome to monty python language \\ @The code should be UTF-8 and python is a interpreted language the name python discovered from the_show of monty cartoons---> Guido van Rossum is the author of python language and invented in the year @ 1991."
#print(s)
#import re
#e=re.findall(r'\w[A-Z a-z 0-9]+',s)
#print(e)
#l=""
#for i in range (0,len(e)):
#    l+=e[i]
#print(l)
#JSON is JavaScript Object Notation. It means that a script (executable) file which is made of text in a programming language, is used to store and transfer the data. Python supports JSON through a built-in package called JSON. To use this feature, we import the JSON package in Python script. The text in JSON is done through quoted-string which contains the value in key-value mapping within { }. It is similar to the dictionary in Python. JSON shows an API similar to users of Standard Library marshal and pickle modules and Python natively supports JSON features. For
#use of json package
import json
x={"name":"John",
   "age":31,
    "Salary":25000}
## conversion to JSON done by dumps() function
y=json.dumps(x)
print(y)
# Python program showing that
# json support different primitive
# types
 
import json
 
# list conversion to Array
print(json.dumps(['Welcome', "to", "Json"]))
 
# tuple conversion to Array
print(json.dumps(("Welcome", "to", "Json")))
 
# string conversion to String
print(json.dumps("Hi"))
 
# int conversion to Number
print(json.dumps(123))
 
# float conversion to Number
print(json.dumps(23.572))
 
# Boolean conversion to their respective values
print(json.dumps(True))
print(json.dumps(False))
 
# None value to null
print(json.dumps(None))
#Serializing JSON: 
#The process of encoding JSON is usually called serialization. This term refers to the transformation of data into a series of bytes (hence serial) to be stored or transmitted across a network. To handle the data flow in a file, the JSON library in Python uses dump() function to convert the Python objects into their respective JSON object, so it makes it easy to write data to files. See the following table given below.
with open("sample.json","w") as w:
    print(json.dump(x,w))#Here, the dump() takes two arguments first, the data object to be serialized, and second the object to which it will be written(Byte format). 
    print(w)
    for i in x:
        print(i)
with open("sample.json","r") as r:
    print(r)
    data=json.load(r)
    print(data)
    for i,j in data.items():
        print(str(i)+str(":")+str(j))
f=open("prudhvi.txt",'w')
e=f.write("This is nothing")
print(e)
f=open("prudhvi.txt",'r')
e=f.read()
print(e)
f=open("prudhvi.txt",'a')
e=f.write("Monty Python")
print(e)
f=open("prudhvi.txt",'r')
e=f.read()
print(e)
f=open("prudhvi.txt",'r')
e=f.readlines()
print(e)
r=""
for i in e:
   r+=i 
print(r)
print(r[::-1])