# Inheritance - Acquiring the properties from ancestors/parents
 # transfer of characteristics/properties from parent to child

# Variable/Attributes/properties - kindness, patience,the way of living
# Methods/behaviour - the way we are living by learning from them

# Types of Inheritance
# 1. Single Inheritance 
# 2. Multilevel
# 3. Multiple
# 4. Hierarchical
# 5. Hybrid

#1.Single Inheritance
#One Parent/Super/Base class and One Derived class present inherting properties of Base/Super/Parent Class.
'''class A:
  properties_of_parent="Land,Apartments,Cars"
  def display1(self):
    print("Father of only B")
class B(A):
  def display(self):
    print("child of A")
    print("The properties of parent:",self.properties_of_parent)
o1=B()
o1.display1()
o1.display()
print(o1.properties_of_parent)'''
#2.Multi Level Inheritance
'''class Parent(): # Company Name
    def method1(self):
      print("This is Method 1 from Class Parent")

class Child(Parent): # Department
  def method2(self):
    print("This is Method 2 from Class Child")

class SubChild(Child): # Employee 

  def method3(self):
    print("This is Method 3 from Class SubChild")

obj1 = SubChild()
obj1.method3()
obj1.method2()
obj1.method1()

class Company(): # Company Name
  def method1(self):
    print("This gives us Company Name & Details")

class Department(Company): # Department
  def method2(self):
    print("This gives us Department Name & Details")

class Employee(Department): # Employee 
  def method3(self):
    print("This gives us Employee Name & Details")

emp_obj = Employee()
emp_obj.method3()
emp_obj.method2()
emp_obj.method1()

dep_obj = Department()
# dep_obj.method3()
dep_obj.method2()
dep_obj.method1()'''

# Multiple Inheritance

'''class Father(): 
  def method1(self):
    print("This is Method 1 from Class Father")

class Mother():
  def method2(self):
    print("This is Method 2 from Class Mother")

class Child(Father,Mother):
  def method3(self):
    print("This is Method 3 from Class Child")


obj1 = Child()
obj1.method3()
obj1.method2()
obj1.method1()'''

# Hierarchical Inheritance

'''class Parent(): 
  def method1(self):
    print("This is Method 1 from Class Parent")

class Brother(Parent):
  def method2(self):
    print("This is Method 2 from Class Brother")

class Sister(Parent):
  def method3(self):
    print("This is Method 3 from Class Sister")

bro_obj = Brother()
sis_obj = Sister()

sis_obj.method1()
bro_obj.method1()'''

#sis_obj.method2()#We can't access brother properties / only we can acesss parent properties.'''
