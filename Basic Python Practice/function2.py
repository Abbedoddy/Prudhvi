#Recursive functions=Recursive functions are functions that calls itself. It is always made up of 2 portions, the base case and the recursive case. The base case is the condition to stop the recursion. The recursive case is the part where the function calls on itself.
def factorial(a):
    if a==1:
        return 1
    else:
        return a*factorial(a-1)
print(factorial(5))
def fibonacci(a):
    if a<=1:
        return a
    else:
        return (fibonacci(a-1)+fibonacci(a-2))
f=int(input("Enter the value positive integer only:"))
print("Fibonacci sequence of",f,"terms is:")
for i in range(f):
    print(fibonacci(i))
'''def grater(a,b,c):
    if a==b==c:
        return a,b,c,"all3numbesaresamesamevalues" 
    if a>b and a>c:
        return a,"isgraterthanall3numbers"
    if b>c:
        return b,"isgraterthanall3numbers"
    else:
        return c,"isgraterthanallnumbers" '''
#lambda=A lambda function is a small anonymous function.A lambda function can take any number of arguments, but can only have one expression.
#lambda arguments : expression
'''x=lambda a,b:a*b
a=int(input("Enter value of a:"))
b=int(input("Enter value of b:"))
print("Multiplication of",str(a)+"*"+str(b),"is:"+str(x(a,b)))
def function(n):
    return lambda a:a*n#use the same function definition to make both functions, in the same program
my_doubler=function(2)
print(my_doubler(a))
my_tripler=function(3)
print(my_tripler(a))
#Using lambda function filter()
a=[]
n=int(input("Enter number of elements required to create a list(Asking length of a list):"))
for i in range(0,n):
    e=int(input("Enter the value integers only:"))
    a.append(e)
print("The user entered list:",a)
b=list(map(lambda a:a+a,a))
print("After adding each elemnt it's same value using map list:",b)
c=list(filter(lambda a:a%2==0,a))
print("filtering even numbers using given list:",c)
d=list(filter(lambda a:a%2!=0,a))
print("filtering odd numbers using given list:",d)
n=int(input("Enter the value:"))
f=list(filter(lambda a:a<n,a))
print("filtering lessthan",n,"elements in a given list:",f)
g=list(filter(lambda a:a>n,a))
print("filtering graterthan",n,"elements in a given list:",g)
h=list(map(lambda g:g*g,g))
print(h)'''
