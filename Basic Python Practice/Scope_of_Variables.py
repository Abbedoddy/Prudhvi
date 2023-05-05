#scope of a variable=A variable is only available from inside the region it is created. This is called scope.
#1.Global scope variables=A variable created in the main body of the Python code is a global variable and belongs to the global scope.Global variables are available from within any scope, global and local.
a=50
b=100
def add(x,y):
    global a,b
    return x+y
def mul1(x,y):
    a=20 #expetional varibles or local variables in function
    b=3
    print("multiplication of local values in function",str(a)+"*"+str(b)+"="+str(a*b))
def mul(x,y):
    global a,b
    return x*y
print("global a="+str(a),"b="+str(b))
print("Accessing global values in the function addition is:",add(a, b))
mul1(a,b)
print("By accessing global values multiplicaton of",str(a)+"*"+str(b)+"="+str(a*b))
a=10#local variable(1st preference)
print("local a="+str(a))
global x,y
a=100
b=200
print("By changing global values in program before function calling a="+str(a),"b="+str(b)) 
def div(x,y):
    global a,b
    a=600
    b=300
    print("Division of "+str(a)+"/"+str(b)+"="+str(a/b))
div(a, b)
print("global values changed after function called a="+str(a)+","+str("b=")+str(b))
#LEGB=(local,enclosed,global,builtin)variables.
#1st preference local variables
#2nd enclosed varibles. means with in function local variable declared
#global variables means we can access every where in the program. we changed values by using global keyword.
#builtin means automatically predefined values stored in python keyword values.
#pi=10
from math import pi
def outer():
    pi=20
    def inner():
        pi=30
        print("local variable:"+str(pi))#local variable
    inner()
    def extainner():
        nonlocal pi
        print("enclosed varible:"+str(pi))#enclosed variable
    extainner()
    def inn():
        global pi
        print("global varible:"+str(pi))#global variable
    inn()
outer()
print("Built in varible:"+str(pi))#By using built in variable

