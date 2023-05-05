#1.The reverse of given number.
'''def rever(x):
    x=str(x)
    if x[0]=='-':
        a=x[::-1]
        return int(f"{x[0]}{a[:-1]}")
    else:
        return int(x[::-1])
n=int(input("Enter a number integer type only(+/-):"))
print("The reverse of a user given number:"+str(rever(n)),"\nType of reverse number is:"+str(type(rever(n))))
#2.write a function "Repeat" that takes an input string and return the output with each charecter repeated twice.
def Repeat(s):
    r=""
    for i in range(0,len(s)):
        r+=s[i]+s[i]
    return r
n=str(input("Enter a string:"))
print("Printing each charecter repeated twice in a user string is:"+str(Repeat(n)))'''
#Day-2
#3.Write a program to mask the first 12 digits of the credit card number with X and print only last 4 digits
#Ex : input = 2345678987656543, output = XXXXXXXXXXXX6543 and return the output
'''n=str(input("Enter your 16 digits credit card number..."))
for i in range(0,len(n)):
    if i<=11:
        print("x",end="")
    else:
        print(n[i],end="") 
print()'''
'''class Creditcard:
    def __init__(self,creditcardnumber):
        self.creditcardnumber=str(creditcardnumber)
        print("User given credit card number ending with last 4 digits:",end="")
        for i in range(0,len(self.creditcardnumber)):
            if i<=11:
                print("x",end="")
            else:
                print(self.creditcardnumber[i],end="") 
        print()
    def display(self):
        print("The user given full card number by accessing display function in class:"+str(self.creditcardnumber))
number=Creditcard(int(input("Enter your 16digits credit card number....")))
number.display()'''#if you want to see full credit card number
#4.Write a function "Ordered_List" that takes list of numbers as input and returns a ascending ordered list
#Ex : input = Ordered_List([45,67,98,25,81,8,0,2]), output = [0,2,8,25,45,67,81,98]
'''a=[]
n=int(input("Enter number of elements required to create a list(Asking length of a list):"))
for i in range(0,n):
    e=int(input("Enter the value integers only:"))
    a.append(e)
print("The user entered list:",a)
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
print("After sorting all elements in a asscending order from user given list:",a)'''
#Day3
#Removing duplicate elements in a list. By taking two usered entered list. printing unique elements in alist.
'''a=[]
n=int(input("Enter number of elements required to create a list(Asking length of a list):"))
for i in range(0,n):
    e=int(input("Enter the value integers only:"))
    a.append(e)
print("The user entered list:",a)
b=[]
n=int(input("Enter number of elements required to create a list(Asking length of a list):"))
for i in range(0,n):
    e=int(input("Enter the value integers only:"))
    b.append(e)
print("The user entered another list:",b)
for i in a:
        if i not in b:
            a.remove(i)
print("Removing elements not present in a another list:",a)
print(b)'''

'''a=[]
n=int(input("Enter number of elements required to create a list(Asking length of a list):"))
for i in range(0,n):
    e=int(input("Enter the value integer only:"))
    a.append(e)
print("The user entered list:",a)
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
print("After sorting all elements in a asscending order from user given list:",a)
c=int(a[0])
i=1
while (i<len(a)):
    if a[i]==c:
        a.pop(i)
    else:
        c=a[i]
        i+=1
print("Removing all occurances in a user given list and final list is:",a)'''
#Day4
'''n=str(input("Enter a string:"))
l=list(n)
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]
print("After sorting all elements in a asscending order from user given list:",l)
c=1
temp=l[0]
for i in range(1,len(l)):
    if l[i]==temp:
        c+=1 
    elif l[i]!=temp:
        print("The occurence of",temp,"in a given string is:"+str(c))
        temp=l[i]
        c=1
print("The occurence of",temp,"in a given string is:"+str(c))'''
'''s= input("Enter a string: ")
d={}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)'''
#Program to find FizzBuzz Numbers in given range by user input.
#Fizz=(number%3==0)
#Buzz=(number%5==0)
#FizzBuzz=(number%3==0 and number%5==0)
'''print("This is program to print FizzBuzz Numbers...")
n=int(input("Please enter range postive integer type only:"))
for i in range(1,n+1):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%5==0:
        print("Buzz")
    elif i%3==0:
        print("Fizz")
    else:
        print(i)'''
'''def calculateSq(n):
    for i in range(0,len(n)):
         n[i]=n[i]*n[i]
    return n
numbers = [2, 3, 4, 5]
result = map( calculateSq, numbers)
print(result)
print(calculateSq(numbers))
print(numbers)'''
#Day5
#Program to print largest difference between two numbers in a userlist.
'''a=[]
n=int(input("Enter number of elements required to create a list(Asking length of a list):"))
for i in range(0,n):
    e=int(input("Enter the value integers only:"))
    a.append(e)
print("The user entered list:",a)
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
print("After sorting all elements in asscending order from user given list:",a)
t1=a[len(a)-1]
t2=a[0]
print("The 1st largest difference between two numbers in a user list","[",str(t1)+str(",")+str(t2),"]","is:",t1-t2)
for i in range(1,len(a)):
    if a[i]!=t2:
        t2=a[i]
        print("The 2nd largest difference between two numbers in a user list","[",str(t1)+str(",")+str(t2),"]","is:",t1-t2)    
        break'''
#Febonacci series by using recurssive function
def fibonacci(a):
    if a<=1:
        return a
    else:
        return (fibonacci(a-1)+fibonacci(a-2))
f=int(input("Enter the value positive integer only:"))
print("Fibonacci sequence of",f,"terms is:")
for i in range(f):
    print(fibonacci(i))
#Factorial of numbers by using recurssive function
def factorial(a):
    if a==1:
        return 1
    else:
        return a*factorial(a-1)
n=int(input("Enter range to print factorial numbers upto..."))
if n<1:
    print(n)
else:
    for i in range(1,n+1):
        print(str(i)+str("!=")+str(factorial(i)))
#Day-6
#The additive sequence is a sequence of numbers where the sum of the first two numbers is equal to the third one.
#Sample additive sequence: 6, 6, 12, 18, 30
#In the above sequence 6 + 6 =12, 6 + 12 = 18, 12 + 18 = 30....
#Also, you can split a number into one or more digits to create an additive sequence.
#Sample additive sequence: 66121830
#In the above sequence 6 + 6 =12, 6 + 12 = 18, 12 + 18 = 30....
'''class Solution(object):
# DFS: iterative implement.
    def is_additive_number(self, num):
        length = len(num)
        for i in range(1, int(length/2+1)):
            for j in range(1, int((length-i)/2 + 1)):
                first, second, others = num[:i], num[i:i+j], num[i+j:]
                if self.isValid(first, second, others):
                    return True
        return False
    def isValid(self, first, second, others):
        if ((len(first) > 1 and first[0] == "0") or
                (len(second) > 1 and second[0] == "0")):
            return False
        sum_str = str(int(first) + int(second))
        if sum_str == others:
            return True
        elif others.startswith(sum_str):
            return self.isValid(second, sum_str, others[len(sum_str):])
        else:
            return False

if __name__ == "__main__":
    print(Solution().is_additive_number('66121830'))
    print(Solution().is_additive_number('51123'))
    print(Solution().is_additive_number('235813'))'''


'''def isAdditiveNumber(num):
   def add(prev,curr,index):
       if index==len(num):
           return 1
       total=str(int(prev)+int(curr))
       print(str(prev)+str("+")+str(curr)+str("=")+str(total))
       if total==num[index:index+len(total)]:
           return add(curr,total,index+len(total))
       else:
           return False
   for i in range(len(num)):
       if num[0]=='0' and i>0:
           break
       for j in range(i+1,len(num)):
           prev=num[0:i+1]
           curr=num[i+1:j+1]
           if curr[0]=='0' and len(curr)>1:
               break
           total=str(int(prev)+int(curr))
           print(str(prev)+str("+")+str(curr)+str("=")+str(total))
           if total==num[j+1:j+1+len(total)]:
               if  add(curr,total,j+1+len(total)):
                   return True
   return False
num=input("Enter a number...")
print("The probability checking given number is addictive sequence....")
p=isAdditiveNumber(num)
if p==True:
    print("The given number "+str(num)+" is in additive sequence")
else:
    print("After checking all the probability given number "+str(num)+" is not additive sequence")'''





















	