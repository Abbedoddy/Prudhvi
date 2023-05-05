# create basic data structure with properties(details) - CLASS
# using this basic structure we can create objects

"""Classes & Objects

Classes - blueprint of user defined data structure
Objects - Instance of the class

Init - a constructor which will be instantiated with the properties/attribute/variables defined when we create an object

self = its a parameter which refers to the current instance of class
"""

'''class EmployeeDetails:
  def __init__(self,name,age,location):
    self.name = name
    self.age = age
    self.location = location


  # Instance Method
  def display(self):
    print(self.name, " is of ", self.age, " years old living in ", self.location)

obj1 = EmployeeDetails("Charan", 26, "Hyderabad")
obj2 = EmployeeDetails("Arjun", 24, "Vijayawada")
print(obj1.name)
print(obj2.location)
obj1.display()
obj2.display()'''
'''class Userdata:
  def __init__(self,username,customerid,accountnumber,ifsccode):
      self.username=username
      self.customerid=customerid
      self.accountnumber=accountnumber
      self.ifsccode=ifsccode
      if ifsccode=="DBSS0IN0811":
        self.branch="HO,Mumbai"
      else:
        self.branch="Hitechcity,Hyderabad"
  def display(self):
    print("Welcome To The DBS Bank \nCustomer Id:",self.customerid)
    print("Account Holder Name:", self.username ,"\nAccountno:", self.accountnumber ,"\tBranch:",self.branch,"\tIfsc code:",self.ifsccode)

p=Userdata("Abbedoddy Prudhvidhar Reddy", 123143,9107899708046,"DBSS0IN0008")
q=Userdata("Theja",123144,917655523121,"DBSS0IN0012")
p.display()
q.display()
class A:
  def display(self):
    print("Father of C")
class B:      
  def display1(self):
    print("Mother of C")
class C(A,B):
  def display2(self):
    print("Child of A&B")
q=C()
q.display()
q.display1()
q.display2()'''
'''class Employee:
  dept = "Financial"
  company = "MNC"       # Type of variable - Class Variables
  def __init__(self,name,age,location):
    self.name = name # Type of variable -  Instance variables
    self.age = age
    self.location = location

 
  def display(self): # Type of method - Instance methods
    print(self.name, " is of ", self.age, " years old living in ", self.location)
  
  def dept_details(self): # Type of method - Static Methods
    print("This particular employee is from",self.dept,"dept")

class Company(Employee):
  pass

comp1 = Company("Pudhvi Reddy",30,"Hyderabad")
comp1.dept_details()
print(comp1.dept)
print(comp1.company)
comp1.display()'''
"""In OOPS Methodologies are of 4 types
1. Inheritance
2. Polymorphism
3. Encapsulation
4. Abstraction
"""