#Conditional Statements if,elif,else
'''print("Enter the value of a")
a=int(input())
print("a=",a)
print("Enter the value of b")
b=int(input())
print("b=",b)
print("Enter the value of c")
c=int(input())
print("c=",c)
if a>b:
    print(a,"is graeter than",b)
elif b>a:
    print(b,"is graeter than",a)
else:
    print(a,"=",b)
print(a,"is a even number") if a%2==0 else print(a,"is a odd number")#When we use single statements one for if, and one for else, you can put it all on the same line.
if a>b and a>c: #if we use and both statements are true give output.
    print(a,"is greater than",b,"&",c)
elif b>c:
    print(b,"is greater than",a,"&",c)
else:
    print(c,"is greater than",a,"&",b)
if a>b or a>c:#It gives output atleast one statement is true
    print("Atleast one of the statement is true")
else:
    print("both statements are false")
if not a>b:#The not keyword is a logical operator, and is used to reverse the result of the conditional statement
    print(a,"is not grater than",b)
#Loops concept
#while loop
print("Enter the value of d")
d=str(input())
print("d=",d)
i=0
while i<(len(d)):
    print("index",i,"=",d[i])
    i+=1
    pass
i=-1
while i>-len(d)-1:
    print("index",i,"=",d[i])
    i-=1
j=0
while j<=(len(d)):
    print(d[:j])
    j+=1
j=-1
while j>-len(d)-1:
    print(d[:j])
    j-=1
i=0
while i<len(d):
    if d[i]=="t":
        print(" ")
        i+=1
        pass
    else:
        print(d[i])
        i+=1
print("....This program for print table from given input from user....")
print("Enter the number what table you want...")
a=int(input())
print("Enter the value upto table will print...")
b=int(input())
print("The table of",a,"is up to ",b,"...")
i=1
while i<=b:
    e=a*i
    print(a,"*",i,"=",e)
    i+=1

print("....Printing natural numbers by using given input from user.... ")
n=int(input("Enter the 'n' value:"))
for i in range(1,n+1):
    print(i,end=" ")
print("\n The whole numbers...")
for i in range(0,n+1):
    print(i,end=" ")
print("\n Printing natural numbers in reverse...")
for i in range(n,0,-1):
    print(i,end=" ")
print("\n Printing whole numbers in reverse...")
for i in range(n,-1,-1):
    print(i,end=" ")
j=0
print("\n The sum of natural numbers...")
for i in range(1,n+1):
    j+=i
print(j)
print("The odd numbers from given length",n)
i,k,j=0,0,1
while(i<n):
    print(j,end=" ")
    k+=j
    j+=2
    i+=1
print("\nThe sum of printed odd numbers...",k)
i=1
for i in range(1,20,2):
    print(i)
i=0
for i in range(i,n+1,2):
    print(i)
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
for i in range(num1,num2+1):
  for j in range(1,11):
    print(str(i)+' X '+str(j)+" = "+str(i*j))'''



    


