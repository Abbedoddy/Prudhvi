#Dictionaries are used to store data values in key:value pairs.A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
'''dict1={"Name":["Kia","Tata","Honda"],"Model":["Ey360","Nexon","City"]}
print("dict1:",dict1,"\n""Lentgh of dict1:",len(dict1))
print("Brand Lists:",dict1["Name"])#Print the key="Name" value of the dictionary
dict2={"Name":["Kia","Tata","Honda"],"Model":["Ey360","Nexon","City"],"Name":["BMW","Rangerover"]}
print(dict2)#Duplicates not allowed.Dictionaries cannot have two items with the same key.Duplicate values will overwrite existing values.
s1=dict(name="Prudhvi",age=30,district="Anantapur")#Using the dict() method to make a dictionary
print("Type of s1:",type(s1),"\n",s1)
#Accessing items by refering to its key name.inside saquare brackets.
x=s1["name"]
print(x)
y=s1["age"]
print(y)
print(x)
y=s1.keys()#The keys() method will return a list of all the keys in the dictionary
print("Before change of s1 keys:",y)
s1["qualification"]="B.TECH"#Updating key in s1
print("After change of s1 keys:",y)
print(s1.get("name"))#By using get() function will access values of given key.
print("The whole values present before updation s1:",s1.values())
s1["age"]=29
print("The whole values present after updation s1:",s1.values())
print("The total items of dict1:",dict1.items())#The items() method will return each item in a dictionary, as tuples in a list.
dict1["colour"]="white","black","blue"#Adding an item to the dictionary is done by using a new index key and assigning a value to it.
print("The total updated items of dict1:",dict1.items())
if "colour" in dict1:
    print("Yes,'colur' is one of the keys in the dict1 dictonary")
dict1.update({"location":["southkorea","india","usa"]})#The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.The argument must be a dictionary, or an iterable object with key:value pairs.
print("Updated dict1:",dict1)
dict1.popitem()#The popitem() method removes the last inserted item in a dictionary.
print("Removing last item by using dictionary.popitem() updated dict1:",dict1)
dict1.pop("Model")#The pop() method removes the item with the specified key name
print("After deleting Model by using pop() updated dict1:",dict1)
del dict1["colour"]#The del keyword removes the item with the specified key name
print("After deleting colour by using 'del' updated dict1:",dict1)
#del dict1 #The del keyword can also delete the dictionary completely
#print(dict1)#It shows error dict1 not defined 
dict1.clear()#The clear() method empties the dictionary
print("After 'clear' function dict1:",dict1)
#You can loop through a dictionary by using a for loop.
#When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.
print("All the keys present in dict2:")
for i in dict2:#Print all key names in the dictionary, one by one
    print(i)
print("All the values presnt in dict2:")
for i in dict2:#Print all values in the dictionary, one by one
    print(dict2[i])
print("All the keys and values in dict2:")
for i,j in dict2.items():
    print(i,j)
print("s1:",s1)
dict3=s1.copy()#Make a copy of a dictionary with the copy() method
print("dict3:",dict3)
print(id(dict3)==id(s1))
#we can use newdict=dict(existing dict) this also copy existing dict keys and values to new dict.
#Nested Dictionaries.A dictionary can contain dictionaries, this is called nested dictionaries.
myfamily={"child1":{"name":"prudhvi","age":30},"child2":{"name":"sankar","age":32},"child3":{"name":"pooja","age":27}}
print(myfamily)
print(myfamily["child1"])
print(myfamily["child2"]["name"])
ott1={"Name":"Hotstar","Purpose":"Sports"}
ott2={"Name":"Netflix","purpose":"Films"}
ott={"ott1":ott1,"ott2":ott2}
print(ott)
s={"a","b","c"}
t=1
dict4=dict.fromkeys(s,t)#The fromkeys() method returns a dictionary with the specified keys and the specified value.
print(dict4)#dict.fromkeys(keys, value)
dict5=dict.fromkeys(s)#Without give value takes none.
print(dict5)'''
#By using input values create dictonary
dict1={}
name=input("Enter employee name:")
designation=input("Enter employee designation:")
salary=input("Enter salary of employee:")
dict1["name:"]=name
dict1["designation:"]=designation
dict1["salary:"]=(int(salary))
dict1.update(name:="theja")
print(dict1)
print(dict1.keys(),"\n",dict1.values())
print(dict1.items())
'''v=c[0]
for i in range(1,len(c)):
    if v<c[i]:
        v=str(c[i])
print(v)'''
'''i,j,k=0,0,0
dict2={}
print("Enter the how many keys you want in dict:",end=" ")
n=int(input())
for i in range(0,n):
    new_key=(input("Enter the key to pair in dictonary:"))
    new_value=input("Enter the value to pair in given key:").split(",")
    dict2.update({new_key:new_value})
print("User given dictonary:",dict2)
print("The values in a user given dictonary:",end=" ")
for i in dict2.values():
    print(i,end=" ")
print("\nThe keys in a user given dictonary:",end=" ")
for i in dict2.keys():
    print(i,end=" ")'''
'''dict2={}
for i,j in dict1.items():
    for k in range(len(j)):
        print(i,"index"+str(k)+str("=")+str(j[k]),end=",")
        if j[k]=="prudhvi" or j[k]==27 or j[k]=="Vmware Admin":
            print("The given value matched with",i+str("=")+str(j[k]))
            dict2.update({i:j[k]})
        else:
            print()
if dict2!={}:
    print("The matched values appended in new dictnory:",dict2)
if dict2=={}:
    print("The given values not present in dictnory")'''