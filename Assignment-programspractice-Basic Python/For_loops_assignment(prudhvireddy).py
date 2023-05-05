#1.program to print the multiplication table of a given number
'''print("....This program for print table from given input from user....")
print("Enter the number what table you want...",end=" ")
a=int(input())
print("Enter the value upto table will print...",end=" ")
b=int(input())
print("The table of",a,"is up to",b,"...")
i=1
while i<=b:
    e=a*i
    print(str(a)+str("*")+str(i)+str("=")+str(e))
    i+=1'''
#2.program to print the Fibonacci series up to a given number.
'''f=int(input("Enter the value positive integer only:"))
print("Fibonacci sequence of",f,"terms is:")
e=0
d=1
r=0
if f<=0:
    print("The requested fibonacci series of",f,"is:",f)
else:
    print(e)
    print(d)
for i in range(2,f):
    r=e+d
    print(r)
    e=d
    d=r'''
#3.program to find the factorial of a given number
'''n=int(input("Please enter a value postive number:"))
m=1
for i in range(1,n+1):
    m=m*i
print("The factorial of a given number",n,"is:"+str(m))'''
#4.program to print the first n prime numbers
'''n=int(input("Please enter a value postive number:"))
print("The prime numbers upto",n,"is:")
for i in range(0,n+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
             print(i,end=" ")
print()'''
#5.program to find the sum of all natural numbers from 1 to n.
'''n=int(input("Enter the value postive integer only:"))
c=0
print("The natural numbers upto",n,"is:")
for i in range(1,n+1):
    print(i,end=" ")
    c+=i
print("\nThe sum of above all natural is:",c)'''
#6.program to print the ASCII values of all the characters in a string. 
'''n=str(input("Enter a string to find ascii values of each charecter:"))
print("The given string is:",n)
ascii_values=[]
for i in range(0,len(n)):
    ascii_values.append(ord(n[i]))#ord() is the built in function to find ascii value given argument.
print("The Ascii values of each charecter in a above string is:",ascii_values)'''
#7.program to print the squares of all the numbers in a list.
'''l1=[]
l2=[]
n=int(input("Enter number values you want in a list: "))
for i in range(0,n):
    a=int(input("Enter list element integer type only: "))
    l1.append(a)
print("The user given list:",l1)
b=lambda x:x*x
for j in range(0,n):
    l2.append(b(l1[j]))
print("The square of each element in a user list is:",l2)'''
#8.program to print the cubes of all the numbers in a list. 
'''l1=[]
l2=[]
n=int(input("Enter number values you want in a list:"))
for i in range(0,n):
    a=int(input("Enter list element integer type only:"))
    l1.append(a)
print("The user given list:",l1)
b=lambda x:x**3
for j in range(0,n):
    l2.append(b(l1[j]))
print("The cube of each element in a user list is:",l2)'''
#9.program to print the reverse of a string. 
'''s1=str(input("Enter a string : "))
reverse_string=""
print("User given string is:",s1)
for i in s1:
    reverse_string=i+reverse_string
print("The reverse of user given string is:"+str(reverse_string))'''
#10.program to print the reverse of a list. 
'''l1=[]
l2=[]
n=int(input("Enter length of list: "))
for i in range(0,n):
    print("Enter the value integer only:",end=" ")
    a=int(input())
    l1.append(a)
print("The user given list:",l1)
for j in range(0,n):
    l2.append(l1[n-j-1])
print("The reverse of a user given list:",l2)'''
#11.program to find all the prime numbers between a given range using for loop.
'''start_range = int(input("Enter starting value: "))
end_range = int(input("Enter end value: "))
print("The prime numbers from",start_range,"to",end_range,"is:",end=" ")
for i in range(start_range,end_range):
        f=0
        for j in range(2,i):
            if(i%j == 0):
                f=1
                break
        if f!=1:
            print(i,end=" ")
print()'''
#12.program to find the factorial of a given number using for loop. 
'''n=int(input("Please enter a value postive number:"))
m=1
for i in range(1,n+1):
    m=m*i
print("The factorial of a given number",n,"is:"+str(m))'''
#13.program to find the Fibonacci series up to a given number using for loop. 
'''def fibonacci(n):
     k=0
     l=1
     l1=[0,1]
     for i in range(2,n):
         m=k+l
         l1.append(m)
         k=l
         l=m
     return l1
num = int(input("Enter number of terms fibonacci series you want: "))
l2=[]
l2=fibonacci(num)
print("The fibonacci series upto",num,"terms is:",l2)'''
#14.program to find the prime factors of a given number using for loop.
'''n=int(input("Enter the value postive integer only to find prime factors of a given number:"))
print("The prime factors of given number",n,"is:",end=" ")
for i in range(2,n+1):
    if n%i == 0:
        flg=1
        for j in range(2,i//2+1):
            if i%j ==0:
                flg=0
                break
        if flg==1:
            print(i,end=" ")
print()'''
#15.program to find the greatest common divisor of two given numbers using for loop. 
'''n1=int(input("Enter first number positive integer only: "))
n2=int(input("Enter second number positive integer only: "))
if n1>n2:
    smaller = n2
else:
    smaller=n1
for i in range(1,smaller+1):
    if n1 % i == 0 and n2 % i == 0:
        gcd=i
print("The greatest common divisor for "+str(n1)+str("&")+str(n2),"is:",gcd)'''
#16.program to find the least common multiple of two given numbers using for loop.
'''p = int (input ("Enter first number positive integer only:"))
q = int (input ("Enter second number positive integer only:"))
for i in range (1, p + 1):
	if i <= q:
		if p % i == 0 and q % i == 0:
			g = i
x = (p * q) / g
print ("The LCM of two positive numbers ", p, " & ", q, " is ", x, ".")'''
#17.program to find the sum of all natural numbers up to a given number using for loop.
'''n=int(input("Enter the natural number : "))
sum=0
print("The all natural numbers upto",n,"is:",end=" ")
for i in range(1,n+1):
    print(i,end=" ")
    sum+=i
print("\nThe sum of all above natural numbers is:",sum)'''
#18.program to find the sum of all even numbers up to a given number using for loop. 
'''n=int(input("Enter a number postive integer only: "))
sum=0
print("All even numbers upto",n,"is:",end=" ")
for i in range(1,n+1):
    if i%2 == 0:
        sum+=i
        print(i,end=" ")
print("\nThe sum of above all even numbers is:",sum)'''
#19.program to find the sum of all odd numbers up to a given number using for loop. 
'''n=int(input("Enter a number positive integer only: "))
sum=0
print("The odd numbers upto",n,"is:",end=" ")
for i in range(1,n+1):
    if i%2 != 0:
        print(i,end=" ")
        sum+=i
print("\nThe sum of all above odd nubers is:",sum)'''
#20.program to find the sum of all numbers in each range using for loop.
'''start_num=int(input("Enter starting num: "))
end_num=int(input("Enter end number: "))
sum=0
print("The values present in between "+str(start_num)+str("&")+str(end_num),"is:",end=" ")
for i in range(start_num,end_num+1):
    print(i,end=" ")
    sum+=i
print("\nThe sum of all elements from stating value",start_num,"to end value",end_num,"is:",sum)'''
#21.program to find the sum of all digits of a given number using for loop. 
'''num=int(input("Enter a number postive integer only: "))
s=str(num)
sum=0
for i in range(len(s)):
    sum+=int(s[i])
print("The sum of all digits in a given number is:",sum)'''
#22.program to find the reverse of a given number using for loop. 
'''n=int(input("Enter a number postive integer only:"))
#using while loop
rev_num=0
while n > 0:
    rem=n%10
    rev_num=rev_num*10+rem
    n//=10
print("The reverse of a given number is:",rev_num)
#using for loop
s=str(n)
reverse_s=""
for i in s:
    reverse_s=i+reverse_s
print("The reverse of a given number is:",rev_num)'''
#23.program to find the number of digits in each number using for loop. 
'''l1=[]
l2=[]
n=int(input("Enter number values in list: "))
for i in range(0,n):
    a=int(input("Enter the value postive integer only:"))
    l1.append(a)
for j in range(0,n):
    l2.append(len(str(l1[j])))
print("User entered numbers:",l1,"\nThe count of digits each number is:",l2)'''
#24.program to find the sum of digits of a given number until the sum becomes a single digit using for loop. 
'''def sumOfDigits(x):
    sum=0
    a=str(x)
    if len(a) == 1:
        return a
    else:
        for i in range(len(a)):
            sum+=int(a[i])
        return sumOfDigits(sum)
n=int(input("Enter a number positive integer only: "))
print("sum of digits of a given numbers",n,"and until sum becomes a single digit is:",sumOfDigits(n))'''
#25.program to find all the Armstrong numbers between a given range using for loop. 
'''n1=int(input("Enter starting range: "))
n2=int(input("Enter ending range: "))
print("The Armstrong numbers present in between "+str(n1)+str(" to ")+str(n2),"is:",end=" ")
for i in range(n1,n2+1):
    s=0
    temp=i
    while i>0:
        rem=i%10
        s=s+(rem**3)
        i//=10
    i=temp
    if temp == s:
        print(temp,end=" ")
print()'''
#26.program to find all the perfect numbers between a given range using for loop.
# for example 6: has divisors 1,2,3,6 => 1+2+3 = 6 which is the original num . so 6 is perfect num
# 18: divisors- 1,2,3,6,9,18 - excluding the number itself (18) we have to add remaining - 1+2+3+6+9 =21 != 18(original num) - so 18 is not perfect number
'''n1=int(input("Enter starting number: "))
n2=int(input("Enter ending number: "))
print("The perfect numbers in between "+str(n1)+str("&")+str(n2),"is:",end=" ")
for i in range(n1,n2+1):
    sum=0
    j=1
    while j<i:
        if i%j == 0:
            sum+=j
        j+=1
    if sum == i:
        print(sum,end=" ")
print()'''
#27.program to find all the abundant numbers between a given range using for loop. 
#if the sum of divisors of a number(excluding the number itself) is greater than the number then that num is called abundant
'''n1=int(input("Enter starting number: "))
n2=int(input("Enter ending number: "))
print("The abundant numbers in between "+str(n1)+str("&")+str(n2),"is:",end=" ")
for i in range(n1,n2+1):
    sum=0
    j=1
    while j<i:
        if i%j == 0:
            sum+=j
        j+=1
    if sum > i:
        print(i,end=" ")
print()'''
#28.program to find all the palindrome numbers between a given range using for loop. 
'''n1=int(input("Enter starting number: "))
n2=int(input("Enter ending number: "))
print("The palindrome numbers in between "+str(n1)+str("&")+str(n2),"is:",end=" ")
for i in range(n1,n2+1):
    temp=i
    rev=0
    while i>0:
        rem=i%10
        rev=rev*10+rem
        i//=10
    i=temp
    if temp==rev:
        print(rev,end=" ")
print()'''
#29.program to find all the strong numbers between a given range using for loop.
#sum of factorial of its digit is equal to the number --145 = 1! + 4! + 5! --- so 145 is strong number
'''n1=int(input("Enter starting number: "))
n2=int(input("Enter ending number: "))
print("The strong numbers in between "+str(n1)+str("&")+str(n2),"is:",end=" ")
for i in range(n1,n2+1):
    a=str(i)
    sum=0
    for j in range(len(a)):
        fact=1
        b=int(a[j])
        for k in range(1,b+1):
            fact=fact*k
        sum+=fact
    if sum == i:
        print(i,end=" ")
print()'''
#30.program to find all the happy numbers between a given range using for loop.
#A number is called happy if it leads to 1 after a sequence of steps where in each step number is replaced by the sum of squares of its digit that is if we start with Happy Number and keep replacing it with digits square sum, we reach 1.
'''def check_happy(n):
    r=object()
    h=0
    while(n>0):
        r=n%10
        h=h+(r*r)
        n=n//10
    return h
n1=int(input("Enter starting number: "))
n2=int(input("Enter ending number: "))
print("The happy numbers in between "+str(n1)+str("&")+str(n2),"is:",end=" ")
for i in range(n1,n2+1):
    h=i
    while(h!=1 and h!=4):
        h=check_happy(h)
    if(h==1):
        print(i,end=" ")
print()'''
#31.program to find all the Smith numbers between a given range using for loop. 
#A Smith number is a composite number, the sum of whose digits equals the sum of the digits of all its prime factors. The smallest Smith number is 4 = 2×2. The sum of the digits of 4 is 4, and The sum of digits of its prime factors is 2 + 2 = 4
#Function to calculate the number of digits in a number
'''def digCount(num):
    c = 0
    while num != 0:
        num = num//10
        c += 1
    return c
#Function to calculate the sum of digits of a number
def digSum(num):
    temp = num
    sum = 0
    for i in range(digCount(num)):
        sum+=num%10
        num//=10
    return sum
#Function to check whether a number is prime or not
def isPrime(num):
    for i in range(2,num):  
       if (num % i) == 0:  
           return False
       else:  
           continue
    return True       
 #Function to check whether a number is a Smith Number or not      
def isSmith(num):
    if(isPrime(num)):
        pass
    else:
        prime_factors = []
        temp = num
        c = 2
        while(temp>1):
            if(temp%c == 0 and isPrime(c)):
                prime_factors.append(c)
                temp/=c
            else:
                c+=1
                continue
        for i in range(0,len(prime_factors)):
            if(digCount(prime_factors[i])>1):
                while(digCount(prime_factors[i])>1):
                    prime_factors[i] = digSum(prime_factors[i])
        if(sum(prime_factors) == digSum(num)):
            return True
        else:
            return False
n1=int(input("Enter starting number: "))
n2=int(input("Enter ending number: "))
print("The smith numbers in between "+str(n1)+str("&")+str(n2),"is:",end=" ")
for i in range(n1,n2+1):
    if(isSmith(i)):
        print(i,end=" ")
print()'''
#32.program to find all the ugly numbers between a given range using for loop. 
'''def getugly(n):
    ugly_num=[0]*n
    ugly_num[0]=1
    c_2=c_3=c_5=0
    next_mul_of_2=2
    next_mul_of_3=3
    next_mul_of_5=5

    for i in range(1,n):
        ugly_num[i]=min(next_mul_of_2,next_mul_of_3,next_mul_of_5)

        if ugly_num[i]==next_mul_of_2:
            c_2+=1
            next_mul_of_2=ugly_num[c_2]*2
        if ugly_num[i]==next_mul_of_3:
            c_3+=1
            next_mul_of_3=ugly_num[c_3]*3
        if ugly_num[i]==next_mul_of_5:
            c_5+=1
            next_mul_of_5=ugly_num[c_5]*5 
    return ugly_num[-1] 
n1=int(input("Enter the number: "))
print("The ugly number is:",end=" ")
print(getugly(n1))
print()'''
#33.program to find all the abundant numbers between a given range using for loop
#please refer to #27 is same.
#34.program to find all the odd numbers between a given range using for loop.
'''n1=int(input("Enter the start range: "))
n2=int(input("Enter the end range: "))
print("The odd numbers in between "+str(n1)+str("&")+str(n2),"is:",end=" ")
for i in range(n1,n2+1):
    if i%2 !=0:
        print(i,end=" ")
print()'''
#35.program to find all the even numbers between a given range using for loop
'''n1=int(input("Enter the start range: "))
n2=int(input("Enter the end range: "))
print("The even numbers in between "+str(n1)+str("&")+str(n2),"is:",end=" ")
for i in range(n1,n2+1):
    if i%2==0:
        print(i,end=" ")
print()'''
#36.program to find all the perfect squares between a given range using for loop.
'''n1=int(input("Enter the start range: "))
n2=int(input("Enter the end range: "))
print("The perfect squares in between "+str(n1)+str("&")+str(n2),"is:",end=" ")
for i in range(n1,n2+1):
    for j in range(1,i//2+1):
        if j**2 == i:
            print(i,end=" ")
        j+=1
    j=1
print()'''
#37.program to find all the factors of a given number using for loop
'''n=int(input("Enter a number: "))
print("The all factors of a given number",n,"is:",end=" ")
for i in range(1,n+1):
    if n%i == 0:
        print(i,end=" ")
print()'''
#38.program to find all the divisors of a given number using for loop. 
'''n=int(input("Enter a number: "))
print("The all divisors of given number",n,"is:",end=" ")
for i in range(1,n+1):
    if n%i == 0:
        print(i,end=" ")
print()'''
#39.program to find all the common elements in two lists using for loop. 
'''l1=[1,2,3,4,6,5]
l2=[4,7,8,5,23,9,6]
l3=[]
print("l1:",l1)
print("l2:",l2)
for i in range(len(l1)):
    a=l1[i]
    for j in range(len(l2)):
        if l2[j]==a:
            l3.append(l2[j])
print("common elements in both list is:",l3)'''
#40.program to find all the unique elements in a list using for loop.
'''l1=[1,2,3,4,6,5]
l2=[4,7,8,5,23,9,6]
print("l1:",l1)
print("l2:",l2)
l3=l2.copy()#copying
for i in l1:
    if i not in l3:
        l3.append(i)
print("Unique elements:",l3)'''
