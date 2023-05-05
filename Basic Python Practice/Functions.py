#Functions=A function is a block of code which only runs when it is called.You can pass data,knows as parameters,into function.A function can return data as a result.
#In Python a function is defined using the def keyword:
'''def my_function(fname,surname):
    return("hello"+" "+ surname+" "+fname)
print(my_function("Prudhvi Reddy","Abbedoddy"))
def my_function1(*name):
    for i in name:
        print(i)
my_function1("prudhvi","reddy","raghav","vikram")
def my_function1(*name):
    for i in name:
        return(i)
print(my_function1())#without passing aruguments its print none.
#The smallest number finding in a given list by using for lopp
l=[999,123,-1,1,-12,4,-15]
print(l)
smallest = l[0]
for i in range(1,len(l)): 
  if smallest > l[i]:
    smallest = l[i]
    print("iteration time : ",i, "Current smallest number : ", smallest)
  else:
    print("iteration time : ",i, "Current smallest number : ", smallest)
print("The smallest present in a given list is: ", smallest)
#By using def function to access smallest element in a lists
def minimum_number(a):
    s=a[0]
    for i in range(1,len(a)):
        if s>a[i]:
            s=a[i]
    return(s)
l1=[44,-888,1,4,5,7,-998]
print("l1:",l1)
l2=[440,-550,2,77,88,-777]
print("l2:",l2)
print("The smallest number in l1 by using user defined function():",minimum_number(l1))
print("The smallest number in l2 by using user defined function():",minimum_number(l2))
def maximum_number(b):
    h=b[0]
    for i in range(1,len(b)):
        if h<b[i]:
            h=b[i]
    return(h)
print("The highest number in l1 by using user defined function():",maximum_number(l1))
print("The highest number in l2 by using user defined function():",maximum_number(l2))
print("The lowest number in l1 using built in function min():",min(l1))#By using built in function
print("The largest number in l1 using built in function max():",max(l1))#By using built in function
def sum_numbers(c):
    d=c[0]
    for i in range(1,len(c)):
        d+=c[i]
    return(d)
print("The sum of all numbers in a list l1 by using user defined function():",sum_numbers(l1))
print("The sum of all numbers in a list l1 by using built in function sum():",sum(l1))
#Checking a list in every element it's odd or even number.printing sum of odd & even numbers in a list.
def even_number(e):
    u=0
    k,m=0,0
    p=[]
    q=[]
    for i in range(0,len(e)):
        u=e[i]
        if u%2==0:
            print("index",i,":",u,"is a even number")
            k+=u
            p.append(u)
        else:
            print("index",i,":",u,"is a odd number")
            m+=u
            q.append(u)
    print("The Even numbers in a list:",p)
    print("The Odd numbers in a list:",q)
    print("The sum of total even numbers in a list:",k)
    print("The sum of total odd numbers in a list:",m)
print("l1:",l1)
even_number(l1)
print("l2:",l2)
even_number(l2)'''
def cal(a,b,operation):
    if operation==1:
        return a+b
    elif operation==2:
        return a-b
    elif operation==3:
        return a*b
    elif operation==4:
        return a/b
    elif operation==5:
        m=0
        m+=a%b
        return m
    elif operation==6:
        x,y=0,0
        e=int(input("Please enter exponent value:"))
        x=a**e
        y=b**e
        return x,y
    elif operation==7:
        x,y=1,1
        for a in range(1,a+1):
            x*=a
        for b in range(1,b+1):
            y*=b
        return x,y
    else:
        print("The given operation not present please select valid input operation in a menu::")
num1=int(input("Please enter num1 value:"))
num2=int(input("Please enter num2 value:"))
operation=int(input("Please select one operation in below mentioned menu list to perform:\n1.Addition\n2.subraction\n3.Multiplication\n4.Divison\n5.Modlus Divison\n6.Exponential\n7.Factorial\nGive input according to above list menu:"))
print("The operation",operation,"performed of",num1,"&",num2,"is:",cal(num1,num2,operation))
