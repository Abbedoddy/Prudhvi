#Creating empty list and asking user how many elements to create list and inputs taken by user
a=[]
n=int(input("Enter number of elements required to create a list(Asking length of a list):"))
for i in range(0,n):
    e=int(input("Enter the value integers only:"))
    a.append(e)
print("The user entered list:",a)
#1.Program to print find the sum of elements in a user given list
'''sum=0
for i in range(len(a)):
    sum+=a[i]
print("sum of all elements in a user given list:",sum)'''
#2.program to print largest element in a user given list
'''largest=a[0]
for i in range(1,len(a)):
    if largest<a[i]:
        largest=a[i]
print("The largest element in a user given list:",largest)'''
#3.program to print smallest element in a user given list
'''smallest=a[0]
for i in range(1,len(a)):
    if smallest>a[i]:
        smallest=a[i]
print("The smallest element in a user given list:",smallest)'''
#4.program to print the average of all elements in a user given list
'''sum=0
for i in range(len(a)):
    sum+=a[i]
print("average of all elements in a user given list:",sum/len(a))'''
#5.program to print the median of all elements in a user given list
'''for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
median_index=int((len(a)-1)/2)
print("The given user list median is index",median_index,"and value is:",a[median_index])'''
#6.program to remove duplicates elements in a user given list
'''test=[]#taken empty list
for x in a:#itterating a values to x
    if x not in test:#conditional statement checking if x not present in a test list.appending list with x value
        test.append(x)
print("The removal of duplicates elements from user given list and printed final list without duplicate values:",test)'''
#7.program to sort a user given list in ascending order
'''for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
print("After sorting all elements in a asscending order from user given list:",a)'''
#8.program to sort a user given list in decending order
'''for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i]<a[j]:
            a[i],a[j]=a[j],a[i]
print("After sorting all elements in a descending order from user given list:",a)'''
#9.program to reverse a user given list
'''reverse=[]#Taken empty list
for i in range(len(a)):
    reverse.append(a[len(a)-i-1])#or we use reverse=a[::-1]
print("The reverse of a user list:",reverse)'''
#10.program to print second largest element in a user given list
'''for i in range(0,len(a)):#1st we have to sort() descending order in a user given list and printing second index value be the second largest.
    for j in range(i+1,len(a)):
        if a[i]<a[j]:
            a[i],a[j]=a[j],a[i]
print("After descending order of user given list:",a)
secondlargest=a[0]
for i in range(1,len(a)):
    if a[i]<secondlargest:
        print("The second largest number in a user given list:",a[i])
        break'''
#11.program to print second smallest number in a user given list
'''for i in range(0,len(a)):#1st we have to sort() asscending order in a user given list and printing second index value be the second smallest.
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
print("After asscending order of user given list:",a)
secondsmallest=a[0]
for i in range(1,len(a)):
    if a[i]>secondsmallest:
        print("The second smallest number in a user given list:",a[i])
        break'''
#12.Merging two given user lists and sort 
'''b=[]
n=int(input("Enter number of elements required to create a list(Asking length of a list):"))
for i in range(0,n):
    e=int(input("Enter the value integers only:"))
    b.append(e)
print("The user entered 2nd list:",b)
new=a+b
print("The merging two lists before sorting:",new)  
for i in range(0,len(new)):#1st we have to sort() asscending order in a user given list and printing second index value be the second smallest.
    for j in range(i+1,len(new)):
        if new[i]>new[j]:
            temp=new[i]
            new[i]=new[j]
            new[j]=temp
print("After sorting merging list:",new)'''
#13.program for checking the list is empty list or not
'''if len(a)!=0:print("The given list is not a empty list:",a)
else:print("The given list is a empty list:",a)'''
'''a.clear()#clearing all elements in a list
print("After clearing all elements by using clear():",a)
if len(a)==0:print("The list is a empty list:",a)'''
#14.Checking a given list is palindrome or not
'''reverse=a[::-1]
print(reverse)
if a==reverse:
    print("The given list is a polindrome:","reverse=",reverse,"orginal=",a,"Reverse and Orginal Both are same")
else:
    print("The given list is not a polindrome:","reverse=",reverse,"orginal=",a,"The Reverse and Orginal is not same")'''
#15.Removing a item in a list nth element in a given list
'''test=[]
n=int(input("Enter which element to remove in a given list:"))
for i in a:
    test.append(i)
    if i==n:
        a.pop(i-1)#To remove a nth element by using pop() using index value
if a==test:
    print("The given removing "+str(n)+"th element is not present in a list:",a)
else:
    print("After removing "+str(n)+"th element and final list is:",a)'''
#16.program to remove all occurrences of an element from a list.
'''for i in range(0,len(a)):#a.sort()#Sorting asscending order
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
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
#17. program to count the number of occurrences of an element in a list
for i in range(0,len(a)):#a.sort()#Sorting asscending order
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print("After sorting all elements in a asscending order from user given list:",a)
i=1
c=int(a[0])
count=int(1)
while (i<len(a)):
    if a[i]==c:
       count+=1
       i+=1
    else:
        print("Count of occurances of element",c,"in a given list is:",count)
        c=a[i]
        count=int(1)
        i+=1
print("Count of occurances of element",c,"in a given list is:",count)  #We are printing because the previous element end of the list and end of the list is same count will happen and loop will exit.
#18.Program to find the index of a element in a list
'''n=int(input("Please enter which number index value you want in a given list:"))
count=int(0)
for i in range(0,len(a)):
    if a[i]==n:
        count+=1
        print("The index value of given number",n,"is","index=",i)
if count==0:
    print("The given number",n,"not present in a given list.")'''
#19.Inserting an element in specific position in a given list
'''n=int(input("Please enter the element to insert in a given list:"))
x=int(input("Enter which position to add given number in a list:"))
for i in range(0,len(a)):
    if i==x-1:
        a.insert(i,n)
print("The given element inserted in specific position after list:",a)'''
#20.To remove all elemnts in a list except first and last element.
'''i=1
while (i<(len(a)-1)):
    a.pop(i)
print("After removing all items except first and last elements:",a)'''
#21.Refer to 1st Program(Sum of all elements in a given list)
#22.Program to find product of all elements in a list
'''product=1
for i in a:
    product*=i
print("The product of all elements in a given list:",product)'''
#23. program to find the maximum and minimum elements in a list. 
'''largest=a[0]
for i in range(1,len(a)):
    if largest<a[i]:
        largest=a[i]
print("The largest element in a user given list:",largest)
smallest=a[0]
for i in range(1,len(a)):
    if smallest>a[i]:
        smallest=a[i]
print("The smallest element in a user given list:",smallest)'''
#24.program to find the second largest and second smallest elements in a list
'''for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i]<a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print("After descending order of user given list:",a)
secondlargest=a[0]
for i in range(1,len(a)):
    if a[i]<secondlargest:
        print("The second largest number in a user given list:",a[i])
        break
secondsmallest=a[-1]      
for i in range(len(a)-1):
    if a[i+1]>secondsmallest:
        print("The second smallest number in a user given list:",a[i+1])    
        break'''
#25.Please refer 6th is same.(Removing all duplicates elements in a list)
#26.program to remove all elements from a list that are divisible by a given number
'''n=int(input("Enter a number to check all elements in a list is divisable or not:"))
for i in a:
    if i%n==0:
        print("Itteration time",i,"is divisible by",n)
        a.remove(i)
print("After removing",n,"is exactly divisble in a list items:",a)'''
#27.Remove all elements from a list that are less than a given number
'''n=int(input("Enter a number to check every element is less than or not:"))
i=0
while i in range(len(a)):
    if a[i]<n:
        a.remove(a[i])
        i=0
    else:
        i+=1
print("Removing less than",n,"all elements in a given list:",a)'''
#28.Remove all elements from a list that are less than a given number
'''n=int(input("Enter a number to check every element is grater than or not:"))
i=0
while i in range(len(a)):
    if a[i]>n:
        a.remove(a[i])
        i=0
    else:
        i+=1
print("Removing grater than",n,"all elements in a given list:",a)'''
#29.program to remove all elements from a list that are not in another list
'''b=[]
n=int(input("Enter number of elements required to create a list(Asking length of a list):"))
for i in range(0,n):
    e=int(input("Enter the value integers only:"))
    b.append(e)
print("The user entered another list:",b)
for i in a:
        if i not in b:
            a.remove(i)
print("Removing elements not present in a another list:",a)'''
#30.program to reverse a list using slicing
'''myreversed=a[::-1]#[-1::],
print("By using indexing printing reverse a list:",myreversed)
for i in reversed(a):#This is another way to access
    print(i)'''
#31.program to rotate a list by a given number of positions
'''n=int(input("How many times to rotate given list:"))
if n>len(a):
    n = int(n%len(a))
    print("The given number grater than length of list and we use n\'%'\length(list) and we rotate as per given result:",n)
a=(a[-n:] + a[:-n])
print("after rotating",n,"number of positions final list:",a)'''
#32.program to shuffle a list randomly
'''for i in range(len(a)-1, 0, -1):
    for j in range(0, i + 1):
        a[i],a[j]=a[j],a[i]
print("After rotating randomly list:",a)'''
#33.program to find the difference between two lists
'''n=int(input("Enter number of elements required to create a list(Asking length of a list):"))
b=[]
for i in range(0,n):
    e=int(input("Enter the value integers only:"))
    b.append(e)
print("The user entered another list:",b)
diff=[]
for i in a:
    if i not in b:
        diff.append(i)
for j in b:
    if j not in a:
        diff.append(j)
print("The orginal list1:",a)
print("The orginal list2:",b)
print("The difference two given lists is:",diff)'''