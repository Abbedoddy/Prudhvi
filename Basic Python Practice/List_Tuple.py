#Lists(Orderd,Indexed,Changable,Collection of multiple items[],Allow duplicates)
'''f1=[35,"Phython Programming",54,63,"computer","memory",31.9,22.5,[98,"surpassing",67],(21,"allocation",11,33.4)]
print(f1)
print('lenth of given list f1:',len(f1))'''
#'print(f1[0:4])'#slicing
#print('1.',f1[1][14]+f1[1][13]+f1[4][3])#Printing Map From Given List
#print('2.',f1[4][3]+f1[8][1][7]+f1[8][1][8]+f1[8][1][9])#Printing Ping From Given List
#'''print(f1[4][3]+f1[8][1][7:10])'''#Ping to access another format
#print('3.',f1[4][3]+f1[1][1]+f1[1][5]+f1[1][6]+f1[4][6])#Print Phone From Given List
#'''print(f1[4][3]+f1[1][4:7]+f1[4][6])'''#Print Phone From Given List another format
#'''print(f1[5][0:4]+f1[0][0]+f1[5][4:7]+f1[0][1])'''#printing mem3ory5 This gets Error Because Integer & Float Not Possible Indexing
#'''print(f1[5][0:4]+'3'+f1[5][4:7]+'5')'''#printing mem3ory5 ByUsing Hardcore Values
#print('4.',f1[5][0:4]+str(f1[0])[0]+f1[5][4:7]+str(f1[0])[1])
#print('5.',f1[1][11:15]+str(f1[2])[::-1]+f1[1][3]+f1[9][1][5:2:-1])#printing gram45taco from given list'''
'''f1.append(("Charles Babbage","c programme author","low level language","Binarycode",123,2.1))#The append() method appends an element to the end of the list.
print('After append function f1:',f1)
print('After append length of f1:',len(f1))
f1.remove(f1[10])#The remove() method takes a single element as an argument and removes it from the list.If the element doesn't exist, it throws ValueError: list.remove(x): x not in list exception.
f2=f1.copy()#The copy() method returns a shallow copy of the list.The copy() method doesn't take any parameters.
print('After Copy of f1 value to f2 is:', f2)
f3="Charles Babbage",("c programme author","low level language"),["Binarycode",123,2.1],0.1
f2.extend(f3)#The extend() method adds all the elements of an iterable (list, tuple, string etc.) to the end of the list.
print('After extend function f2:',f2,'\n','After extend length of f2:',len(f2))
f2.clear()#The clear() method removes all items from the list.The clear() method doesn't take any parameters.
print('After clear function f2:',f2,'After clear length of f2:',len(f2))
f2.insert(0,'hello')#The insert() method inserts an element to the list at the specified index.list.insert(i, elem)
a=["your a python learner id is",1201]
f2.insert(1,a)
f2.remove("hello")
print(f2)
f2.insert(0,'hello')
print('After insert functions done f2:',f2)
removed=f2.pop(0)#The pop() method removes the item at the given index from the list and returns the removed item.
print('Removed index by using pop:',removed)#if index value not given it takes automatically index value of last
print('After pop orginal string f2:',f2)
f4=[5,4,3,2,1]
print('orginal string of f4:',f4)
f4.reverse()#The reverse() method reverses the elements of the list.The syntax of the reverse() method is:list.reverse() The reverse() method doesn't return any value. It updates the existing list.
print('After Reverse Function f4:',f4)
f4.sort(reverse=True)#The sort() method accepts a reverse parameter as an optional argument.Setting reverse = True sorts the list in the descending order.list.sort(reverse=True)
print('After Sort By Descending Order f4:',f4)
f4.sort()#No need give to pass arguments for asscending order sorting 
print('After Sorting By Asscending Order f4:',f4)
#Tuples Tuples are used to store multiple items in a single variable.(ordered,unchangeble and allow duplicates,Indexed,())
tuple1=("India","Australia","England","India",1,2,3)
print('tuple1=',tuple1)
print(tuple1[0])#We can access by using index values
print(tuple1[-1])
print(tuple1[::-1])#Tuple access in reverse 
print(tuple1[4:-1])
print(tuple1[-1:-8:-1])
if "Australia" in tuple1:
    print("yes,'Australia' in given tuple1")#This will print because given string present in tuple1
else:
    print("given,'Australia' not present in tuple1")
if "Southafrica" in tuple1: #itwill false then execute else statement
    print("Yes 'Southafrica' present")
else:
    print("Given 'Southafrica' Not present in tuple")
#Change Tuple Values
#Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
#But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
y=list(tuple1)#Tuple converted to list
y[6]="Southafrica"#update value to existing index
tuple1=tuple(y)#Then after type converstion to store updated tuple in existing tuple
print("Updated tuple1:",tuple1)
y=list(tuple1)
y.append("Pakisthan")#add value to tuple by using convert into list and we use append function 
tuple1=tuple(y)#After list convert into tuple and assign update value to existing tuple
print(tuple1)
#Adding tuple to tuple
tuple1=(1,2,3,4)
print(tuple1)
tuple2=(5,6,7)
print(tuple2)
tuple1+=tuple2#By Using tuple+=tuple1 '+' operator can add tuple to tuple
print(tuple1)
#Removing items in tuple 
x=list(tuple1)
print(x)
x.remove(5)#Removing 5 and back to tuple
tuple1=tuple(x)
print(tuple1)
del tuple1
#print(tuple1)#It throws error tuple1 is not defined
#Unpacking Tuples When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
#But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":
t1=("Balayababu","Megastar","Superstar","Powerstar")
print(t1)
(x,y,*z)=t1 #assigning variables to tuple values.
print(x)#Accesing "Balayababu" by using x varible
print(y)#"     "
print(z)#"By using *we can access values by end"
#You can loop through the tuple items by using a for loop.
for i in t1:
    print(i)
#Loop Through the Index Numbers
for i in range(len(t1)):
    print(t1[i])
t2=t1*2#By access twice in given tuple using'*' by add '+'
print(t2)
#Counting given value how many times present in a tuple
print("t1:",t1)
print("t2:",t2)
print("Printing how many times presnt 'Balayababu' in t1:",t1.count("Balayababu"))
print("Printing how many times presnt 'Balayababu' in t2:", t2.count("Balayababu"))
#Index value of specified value
q=t1.index("Megastar")
print(q)'''
