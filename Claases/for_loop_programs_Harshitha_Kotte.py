#1.To print multiplication table of a given number
'''n=int(input("Enter a number: "))
for i in range(1,11):
    print(str(n)+'X'+str(i)+'='+str(n*i))'''

#2.To print fibonacci series up to a given number using for loop
'''l1=[0,1]
k=0
l=1
n=int(input("Enter the number up to which you need fibonacci series: "))
for i in range(2,n):
    m=k+l
    if m<n:
        l1.append(m)
        
    else:
        break
    k=l
    l=m
print(l1)'''# will print all fibinocci series till n

#3.To print factorial of a given number using function
'''def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
    
x=int(input("Enter a positive number : "))
print(fact(x))'''

#4.To print  prime numbers
'''n=int(input("Enter n value: "))
if n==1:
    print("1 is not a prime number")
else: 
    for i in range(2,n):
        flg=0
        for j in range(2,i):
            if(i%j == 0):
                flg=1
                break
        if flg!=1:
            print(i)'''

#5.To print sum of natural numbers from 1 to n
'''n=int(input("Enter n value: "))
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)'''

#6.To print ASCII value of all the characters in a string
'''str1=input("Enter a string : ")
for i in range(len(str1)):
    print(str1[i],ord(str1[i]))'''

#7.To print squares of all the numbers in a list
'''l1=[]
l2=[]
n=int(input("Enter number values in list: "))
for i in range(0,n):
    a=int(input("Enter list element: "))
    l1.append(a)

print(l1)
b=lambda x:x*x
for j in range(0,n):
    l2.append(b(l1[j]))
print(l2)'''

#8.To print cubes of all the numbers in a list
'''l1=[]
l2=[]
n=int(input("Enter number values in list: "))
for i in range(0,n):
    a=int(input("Enter list element: "))
    l1.append(a)

print(l1)
b=lambda x:x**3
for j in range(0,n):
    l2.append(b(l1[j]))
print(l2)'''

#9.To print reverse of a string
'''s1=input("Enter a string : ")
print(s1[::-1])'''

#10.To print reverse of a list
'''l1=[]
l2=[]
n=int(input("Enter length of list: "))
for i in range(0,n):
    a=int(input())
    l1.append(a)

print(l1)
for j in range(0,n):
    l2.append(l1[n-j-1])
print(l2)'''

#11.Print prime numbers between a range 
'''start_range = int(input("Enter starting value: "))
end_range = int(input("Enter end value: "))
for i in range(start_range,end_range):
        flg=0
        for j in range(2,i):
            if(i%j == 0):
                flg=1
                break
        if flg!=1:
            print(i)'''
#12.Factorial using for loop
'''n=int(input("Enter the number : "))
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)'''

#13.Fibonacci series up to a given num using func
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
num = int(input("Enter number of terms : "))
l2=[]
l2=fibonacci(num)
print(l2)'''

#14.To find prime factors of a given number
'''n=int(input("Enter a number: "))
for i in range(2,n+1):
    if n%i == 0:
        flg=1
        for j in range(2,i//2+1):
            if i%j ==0:
                flg=0
                break
        if flg==1:
            print(i)'''

#15.To find Greatest common divisor of two given num
'''n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
if n1>n2:
    smaller = n2
else:
    smaller=n1
for i in range(1,smaller+1):
    if n1 % i == 0 and n2 % i == 0:
        gcd=i

print(gcd)'''

#16.To find least common multiple of two given num - smallest postive integer that is divisible by two numbers
'''n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
if n1>n2:
    greatest=n1
else:
    greatest=n2

while True:
    if greatest % n1 == 0 and greatest % n2 == 0:
        lcm=greatest
        break
    greatest+=1
print(lcm)'''


#17.Sum of all natural numbers up to a given num using for loop
'''n=int(input("Enter the natural number : "))
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)'''

#18.sum of all even numbers up to given num using for loop
'''n=int(input("Enter a number: "))
sum=0
for i in range(1,n+1):
    if i%2 == 0:
        sum+=i
print(sum)'''

#19.sum of all odd numbers up to given num using for loop
'''n=int(input("Enter a number: "))
sum=0
for i in range(1,n+1):
    if i%2 != 0:
        sum+=i
print(sum)'''

#20.sum of all numbers in given range of numbers using for loop
'''start_num=int(input("Enter starting num: "))
end_num=int(input("Enter end number: "))
sum=0
for i in range(start_num,end_num+1):
    sum+=i
print(sum)'''

#21.sum of all digits of a number using for loop
'''num=int(input("Enter a number: "))
s=str(num)
sum=0
for i in range(len(s)):
    sum+=int(s[i])
print(sum)'''

#22.reverse of a given num using for loop
'''n=int(input("Enter a number : "))
rev_num=0
while n > 0:
    rem=n%10
    rev_num=rev_num*10+rem
    n//=10

print(rev_num)'''

#23.find number of digits in a given number
'''l1=[]
l2=[]
n=int(input("Enter number values in list: "))
for i in range(0,n):
    a=int(input())
    l1.append(a)

for j in range(0,n):
    l2.append(len(str(l1[j])))

print(l2)'''

#24.find sum of digits of a given num until the sum becomes a single digit
'''def sumOfDigits(x):
    sum=0
    a=str(x)
    if len(a) == 1:
        return a
    else:
        for i in range(len(a)):
            sum+=int(a[i])
        return sumOfDigits(sum)

n=int(input("Enter a number: "))
print(sumOfDigits(n))'''

#25.To find armstrong numbers between given range - sum of the cubes of digits of a number is equal to the number
'''n1=int(input("Enter starting range: "))
n2=int(input("Enter ending range: "))
for i in range(n1,n2+1):
    s=0
    temp=i
    while i>0:
        rem=i%10
        s=s+(rem**3)
        i//=10
    i=temp
    if temp == s:
        print(temp)'''


#26.To find perfect numbers betwwen given range - a num is perfect number if sum of its divisors except the number itself is equat to the original num
# for example 6: has divisors 1,2,3,6 => 1+2+3 = 6 which is the original num . so 6 is perfect num
# 18: divisors- 1,2,3,6,9,18 - excluding the number itself (18) we have to add remaining - 1+2+3+6+9 =21 != 18(original num) - so 18 is not perfect number

'''n1=int(input("Enter starting number: "))
n2=int(input("Enter ending number: "))
for i in range(n1,n2+1):
    sum=0
    j=1
    while j<i:
        if i%j == 0:
            sum+=j
        j+=1
    if sum == i:
        print(sum)'''


#27.To find abundant numbers between given range
#if the sum of divisors of a number(excluding the number itself) is greater than the number then that num is called abundant
'''n1=int(input("Enter starting number: "))
n2=int(input("Enter ending number: "))
for i in range(n1,n2+1):
    sum=0
    j=1
    while j<i:
        if i%j == 0:
            sum+=j
        j+=1
    if sum > i:
        print(i)'''

#28.To find palindrome numbers between given range
'''n1=int(input("Enter starting number: "))
n2=int(input("Enter ending number: "))
for i in range(n1,n2+1):
    temp=i
    rev=0
    while i>0:
        rem=i%10
        rev=rev*10+rem
        i//=10
    i=temp
    if temp==rev:
        print(rev)'''

#29.To find all strong numbers betwwen given range
#sum of factorial of its digit is equal to the number --145 = 1! + 4! + 5! --- so 145 is strong number
'''n1=int(input("Enter starting number: "))
n2=int(input("Enter ending number: "))
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
        print(i)'''

#30.To find all happy numbers between given range
#number that can be replaced by the sum of the squares of its digit repeatedly and after some repetitions, it will yield the number 1.
#19 = 1**2 +9**2= 82 =>8**2+2**2=68=>6**2+8**2=100=>1 ----------> 19 is happy number

        



#31.To find all smith numbers between range

#32. To find all ugly numbers between range

#33.To find all abundant numbers between range

#34.To find all odd numbers between range
'''n1=int(input("Enter the start range: "))
n2=int(input("Enter the end range: "))
for i in range(n1,n2+1):
    if i%2 !=0:
        print(i,end=" ")'''


#35.To find all even numbers between range
'''n1=int(input("Enter the start range: "))
n2=int(input("Enter the end range: "))
for i in range(n1,n2+1):
    if i%2 ==0:
        print(i,end=" ")'''

#36.To find all perfect squares between range
'''n1=int(input("Enter the start range: "))
n2=int(input("Enter the end range: "))
for i in range(n1,n2+1):
    for j in range(1,i//2+1):
        if j**2 == i:
            print(i)
        j+=1
    j=1
    '''

        

#37.To find all factors of a given number
'''n=int(input("Enter a number: "))
for i in range(1,n+1):
    if n%i == 0:
        print(i,end=" ")'''

    

#38.To find all divisors of given number
'''n=int(input("Enter a number: "))
for i in range(1,n+1):
    if n%i == 0:
        print(i,end=" ")'''


#39.To find all common elements in two lists
'''l1=[1,2,3,4,6,5]
l2=[4,7,8,5,23,9,6]
l3=[]
for i in range(len(l1)):
    a=l1[i]
    for j in range(len(l2)):
        if l2[j]==a:
            l3.append(l2[j])
print("common elements:",l3)'''


#40.To find unique elements in list
'''for i in range(len(l3)):
    l1.remove(l3[i])
    l2.remove(l3[i])
print("unique elements:" ,l1,l2)'''


    


    