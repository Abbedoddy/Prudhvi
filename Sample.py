#This is the first program 
print("This is the program to find a given string charecters present in a list or not")
a=""
b=[]
a=str(input("Enter a string integer type/string..."))
n=int(input("How elements to want create a list..."))
for i in range(0,n):
    print("Enter the",i+1,"element in a list int/string type only...",end="")
    x=input()
    b.append(x)
print("The user given string:",a)
print("The user given list:",b)
c=[]
for i in range(0,len(a)):
    for j in range(0,len(b)):
        if a[i]==b[j]:
            c.append(["indexmatch=",[i,j],["element=",[a[i]]]])
print("The matching index and charecter in a user string and list is:",c)