#1.Remove duplicate elements in a user list (Without using in/notin)
'''a=[]
n=int(input("enter how many elements to create a list(asking length).."))
for i in range(0,n):
  x=int(input("Enter the value integer type only..."))
  a.append(x)
print("The user given list:",a)
b=[]
for i in a:
  if i not in b:
    b.append(i) 
print("Removing all duplictaes in user given list:",b)'''
#Minourity element in a list
'''a=[]
n=int(input("enter how many elements to create a list(asking length).."))
for i in range(0,n):
  x=int(input("Enter the value integer type only...."))
  a.append(x)
print("The user given list:",a)
t=a[0]
for i in range(1,len(a)):
  if t>a[i]:
    t=a[i] 
if t<len(a)/2:
    print("The minourity element in list less length of a list:",t)
else:
    print("The minourity element not present in list less than lenth of list")'''

#Polarisis matching target sum
'''def matching_paris(n,targetsum):
  b=[]
  for i in range(0,len(n)):
    for j in range(0,len(n)):
      if a[i]+a[j]==targetsum:
        b.append([i,j])
  return b
a=[]
n=int(input("enter how many elements to create a list(asking length).."))
for i in range(0,n):
  x=int(input("Enter the value integer type only..."))
  a.append(x)
print("The user given list:",a)
targetsum=int(input("Enter target sum:"))
print("The polarasis matching index given target sum in a user list",matching_paris(a,targetsum))'''
#perform a/b when b<a. other wise swap values a,b=b,a and perform a/b.
#1.Without Decor Function
'''def div(a,b):
  if b<a:
    print("The divison of a,b is:"+str(a/b))
  else:
    print("The value of b="+str(b),"is grater than a="+str(a))
    a,b=b,a
    print("After swapping a,b values:",a,b)
    print("The divison of a,b is:"+str(a/b))
a=int(input("Enter the value of a:"))
b=int(input("enter the value of b:"))
div(a,b)'''
#2.Using Decor fun()
'''def swap_dec(function):
  def div(a,b):
    if b<a:
        print("Without swapping values condition satisfy b<a...")
        return a/b
    else:
        return function(a,b)
  return div

@swap_dec
def swap(a,b):
    print("Swapping values condition doesn't satisfy b<a...")
    a,b=b,a
    print("After swapping a,b values:",a,b)
    return a/b 
a=int(input("Enter the value of a:"))
b=int(input("enter the value of b:"))
print("The divison of a/b is:",swap(a, b))'''

'''p="python"
print("p="+str(p))
if p[-0]==p[-6] and p[0]==p[-6]:
  print("p[-0]="+str(p[-0]))
  print("p[-6]="+str(p[-6]))
  print("p[0]="+str(p[0]))
  print("p[-6]="+str(p[-6]))
  print("The above both conditions p[-0]==p[-6] and p[0]==p[-6] is:"+str(bool(1 and 1)))
if p[-0]==p[-6]:
  print("p[-0]="+str(p[-0]))
  print("p[-6]="+str(p[-6]))
  print("The condition p[-0]==p[-6] is:"+str(bool(1 or 0)))
if p[0]==p[-6]:
  print("p[0]="+str(p[0]))
  print("p[-6]="+str(p[-6]))
  print("The condition p[0]==p[-6] is:"+str(bool(0 or 1)))
else:
  print("The both conditions p[-0]==p[-6] and p[0]==p[-6] is:"+str(bool(0 and 0)))'''
'''print(bool(1 and 1))
print(bool(1 and 0))
print(bool(0 and 0))
print(bool(0 and 1))
print(bool(0))
print(bool(1))
print(bool(1 or 1))
print(bool(1 or 0))
print(bool(0 or 0))
print(bool(0 or 1))'''
'''s=input("Enter a string (int/string) to test polindrome or not:")
t=s[::-1]
print("The user string:"+str(s))
print("The reverse of user string:"+str(t))
if s==t:
  print("The given string is polindrome:"+str(bool(1)))
else:
  print("The given string is polindrome:"+str(bool(0)))'''
