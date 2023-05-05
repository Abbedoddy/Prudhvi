dict1={"name":["prudhvi","theja","marcus"],"age":[29,27,30],"designation":("python developer","ios developer","vmware Admin")}
print("dict1="+str(dict1))
#print(dict1["name"]) accesing value by using key
#1.program to print all the keys of a dictionary.
'''print("All keys in a given dictonary:") 
for keys,value in dict1.items():
    print(keys)'''
#2.program to print all the keys of a dictionary.
'''print("All values in a given dictonary:") 
for keys,values in dict1.items():
    print(values)'''
#3.program to print all items in a dictionary.
'''print("All keys&values in a given dictonary:")
for keys,values in dict1.items():
    print(keys+str("=")+str(values))'''
#4.program to find the length of a dictionary.
'''c=0
for i in dict1:c+=1
print("The length of dictonary:",c)''' #print(len(dict1)) also work
#5.program to check if a key is present in a dictionary
'''n=input(("Enter the key to check that key present or not in a given dictnory:"))
c=0
for keys,values in dict1.items():
    if keys==n:break
    else:c+=1
if c==len(dict1):print("The given key","'"+str(n)+"'","not present in a given list") 
else:print("The given key","'"+str(n)+"'","present in a given list")'''
#6.program to check if a value is present in a dictionary
'''c=0
n=str(input(("Enter the value to check that value present or not in a given dictnory:")))
for i in dict1.values():
    for j in range (0,len(i)):
        if str(i[j])==n:
            c+=1
            break
if c!=0:
    print("The given value","'"+str(n)+"'","is present in a given list")
else:
    print("The given value","'"+str(n)+"'","is not present in a given list")'''
#7.program to add a key-value pair to a dictionary
#dict1.update(place=("Hyderabad","Banglore","Chennai"))
#print("Updaated dict1:",dict1)
#The given method also work
#new_key="place"
#new_value=["Hyderabad","Banglore","Mumbai"]
#dict1.update({new_key:new_value})
#print("Updated dict1=",dict1)
'''print("Enter the how many keys you want add in existing dict:",end=" ")
n=int(input())
for i in range(n):
    new_key=(input("Enter the key to pair in dictonary:"))
    new_value=input("Enter the value to pair in given key:").split(",")
    dict1.update({new_key:new_value})
print("Updated dict1="+str(dict1))'''
#8.program to remove a key-value pair from a dictionary
'''n=(input("Enter the key to remove key-value pair in dictonary:"))
for i,j in dict1.items():
    if i==n:
        del dict1[i]
        break
print("After removing given"+"'"+str(n)+"'","key-value pair in dictnory=",dict1)'''
#9.program to clear a dictionary
'''dict2=dict1.copy()
print("copy of dict1 is dict2=",dict2)
dict2.clear()
print("After clear function dictnory of dict2=",dict2)'''
#10.program to copy a dictionary.
'''dict2={}
for i,j in dict1.items():
     dict2.update({i:j}) 
print("dict2=",dict2)
print("After copying checking two dictnaries are same or not:",dict1==dict2)'''
#11.program to get the value for a given key in a dictionary
'''n=(input("Enter the key to get value in dictonary:"))
for i,j in dict1.items():
    if i==n:
        print(str(i)+str("=")+str(j))
        break
else:
    print("The given key"+"'"+str(n)+"'","is not present in a dictonary")'''
#12.update the value for a given key in a dictionary.
'''n=(input("Enter the key to update value in dictonary:"))
for i,j in dict1.items():
    if i==n:
        c=1
        v=input(("Enter the key value to update in a existing dictonary:")).split(",")
        dict1.update({i:v})
        break
    else:
        c=0
if c==1:
    print("After updating key to value "+str(n)+str("=")+str(v)+"\nupdated dict1="+str(dict1))
else:
    print("The given key "+"'"+str(n)+"'","is not present dictnory")'''
#13.program to remove a key from a dictionary
'''n=(input("Enter the key to remove value in dictonary:"))
for i,j in dict1.items():
    if i==n:
        dict1.pop(i,j)
        break
print("After deleting key="+str(n)+"\ndict1=",dict1)'''
#14.program to sort a dictionary by key
'''print("After sorting dict1 by using keys:")
for key in sorted(dict1):
    print(key+str(":")+str(dict1[key]))'''
#15.program to sort a dictionary by value
'''print()
print("After sorting dict1 by using values:")
for key in dict1:
    print(key+str(":")+str(sorted(dict1[key])))'''
#16.program to find the largest value in a dictionary
'''c=[]
for key,values in dict1.items():
    for i in range(0,len(values)):
        c.append(str(values[i]))
c.sort()
check=c[0]
for i in range(1,len(c)):
    if len(check)<=len(c[i]):
        check=c[i]
print("The largest value in a dictnory is:",check)'''
#17.program to find the smallest value in a dictionary
'''c=[]
for key,values in dict1.items():
    for i in range(0,len(values)):
        c.append(str(values[i]))
c.sort()
check=c[0]
for i in range(1,len(c)):
    if len(check)>len(c[i]):
        check=c[i]
print("The smallest value in a dictnory is:",check)'''
#18.program to find the largest key in a dictionary.
'''c=[]
for i in dict1:
    c.append(str(i)) 
c.sort()
check=c[0]
for i in range(1,len(c)):
    if len(check)<len(c[i]):
        check=c[i]
print("The largest key in a dictonary is:",check)'''
#19.program to find the smallest key in a dictionary.
'''c=[]
for i in dict1:
    c.append(str(i)) 
c.sort()
check=c[0]
for i in range(1,len(c)):
    if len(check)>len(c[i]):
        check=c[i]
print("The smallest key in a dictonary is:",check)'''
#20.program to concatenate two dictionaries. 
'''dict2={"location":["Hyderabad","Banglore","Mumbai"],"id":["007","001","003"]}
print("dict2=",dict2)
#dict1.update(dict2)
#print("The concatenate of dict2 to dict1:",dict1)
for i in dict2:
    for j in range(len(dict1),len(dict1)+len(dict2)):
         dict1[i]=dict2[i]
print("The concatenate of dict2 to dict1:","\nupdated dict1=",dict1)'''