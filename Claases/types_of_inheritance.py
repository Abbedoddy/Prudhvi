# -*- coding: utf-8 -*-
"""Type of Inheritance.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XJW2NW6ITI7uNpUR_OITlZn3EsN0AZZB
"""

# SINGLE INHERITANCE

# class Fruits():
#   def __init__(self,color,size,taste):
#     self.color = color
#     self.size = size
#     self.taste = taste

#   def details(self):
#       print("Fruit details : ", self.color, self.size, self.taste)


# class sweet_fruits(Fruits):
#   def __init__(self,color,size,taste = "Sweet"):
#     self.color = color
#     self.size = size
#     self.taste = taste

# class sour_fruits(Fruits):
#   def __init__(self,color,size,taste = "Sour"):
#     self.color = color
#     self.size = size
#     self.taste = taste

# sw_obj = sweet_fruits("Mango", "Medium")
# sw_obj.details()

class Parent():
  def method1(self):
    print("This is Method 1 from Class Parent")

class Child(Parent):
  def method2(self):
    print("This is Method 2 from Class Child")


obj1 = Child()
obj1.method2()
obj1.method1()

# MULTILEVEL INHERITANCE

# class Parent(): # Company Name
#   def method1(self):
#     print("This is Method 1 from Class Parent")

# class Child(Parent): # Department
#   def method2(self):
#     print("This is Method 2 from Class Child")

# class SubChild(Child): # Employee 

#   def method3(self):
#     print("This is Method 3 from Class SubChild")

# obj1 = SubChild()
# obj1.method3()
# obj1.method2()
# obj1.method1()

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
dep_obj.method1()

# Multiple Inheritance

class Father(): 
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
obj1.method1()

# Hierarchical Inheritance

class Parent(): 
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
bro_obj.method1()

sis_obj.method2()