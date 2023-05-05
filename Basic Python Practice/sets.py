Countries={"India","America","Australia","Newzeland",1,True,0,False,"India","England","Sothafrica",1.2}#Unindexed,UnOrderd,Not allow duplicates,Unchanged,Data Container (int,Float,Strings,Complex,List,Tuple,Sets,Dict.)
print('Orginal Set Of Countries:',Countries)
for i in Countries: #You cannot access items in a set by referring to an index or a key.But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
    print(i) #Syntax (for variable in listname:) you can access items 
print("Southafrica" in Countries) #Check if "Southafrica" is present in the set if present it will print True Otherwise False
Countries.add("Pakisthan")#To add one item to a set use the add() method.Once a set is created, you cannot change its items, but you can add new items.
print('After add function Set Of Countries:',Countries)
print("Pakisthan" in Countries)
countries1={"Afganisthan","Srilanka","China"}#To add items from another set into the current set, use the update() method.
print('Orginal Set Of Countries1:',countries1)
Countries.update(countries1)#The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
print('After update function Set Of Countries:',Countries)
s={"apple","bannana","cherry"}
print('Orginal Set Of s:',s)
s.remove("apple")#If the item to remove does not exist, remove() will raise an error.
print('After remove fuction set of s:',s)
s.discard("apple")#If the item to remove does not exist, discard() will NOT raise an error.
s.add("apple")
x=s.pop()#Remove a random item by using the pop() method.Sets are unordered, so when using the pop() method, you do not know which item that gets removed.
print('Removed item when pop() function in set s:',s)
s.clear()#The clear() method empties the set
print('After clear function set of s:',s)
del s #The del keyword will delete the set completely
#print('After delete function set of s:',s) this throws error name 's' is not defined
set1={"a","b","c"}
set2={"a",1,2,3}
set3=set1.union(set2)#You can use the union() method that returns a new set containing all items from both sets, or the update() method that inserts all the items from one set into another
print(set3)
x={"apple","banana","cherry"}
y={"google","microsoft","apple"}
v=x.intersection_update(y)
print(x)
print(id(x))
p={"apple","banana","cherry"}
z=p.intersection(y)
print(z)
print(id(z))
x={"apple","banana","cherry"}
print(x)
print(y)
x.symmetric_difference_update(y)
print(x)
w=x.symmetric_difference(y)
print(w)
q=w.copy()#set.copy()
print(q)
set4=[]
    

