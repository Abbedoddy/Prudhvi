# -*- coding: utf-8 -*-
"""Types of Polymorphism.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sVVYSMliOXd_MD9zBBrWAZQQdOEQbgUs
"""

# METHOD OVERLOADING
# def add(x,y):
#   print(x+y)

# def add(x,y,z):
#   print(x+y+z)

# add(3,4)
# add(2,3,4)

def concate(a,b):
	print(a+b)

def concate(a,b,c):
	print(a+b+c)


# concate("Python", "Programming")
#concate("Python", "Programming","Language","Orange")

# FUnction with Multiple Arguments
def concate(*args):
  s = ""
  for r in args:
    s += r
  print(s)

#METHOD OVERRIDING
total_company_worth = "5cr" # Sttaic Variable
class Company:
  dept = "HR"
  def __init__(self,name1,regnum,age1):
    self.compname = name1 #Instance Variables
    self.regnum = regnum
    self.compage = age1
  def display(self): # Instance Method
    print(self.compname, " is of ", self.compage, " years old registered with  ", self.regnum)

# comp_obj = Company("HCL")
# comp_obj.display()

class EmployeeDetails(Company):
  def __init__(self,name1,regnum, age1, name,age,location):
    super().__init__(name1,regnum,age1)
    self.name = name
    self.age = age
    self.location = location

  def display(self):
    super().display()
    print(self.name, " is of ", self.age, " years old living in ", self.location)

emp_obj1 = EmployeeDetails("HCL",3456,50, "Karthik", 25, "Hyderabad")
emp_obj1.display()

# Polymorphism with Inheritance
# METHOD RESOLUTION ORDER
class A:
  def display(self):
    print("Class A properties")

class B:
  def display(self):
    print("Class B properties")

class C(A,B):
  def display1(self):
    super().display()
    print("Class C properties")

obj = C()
obj.display()

# CLASS METHOD
class A:
 num = 9848022663 # Class Variable
 @classmethod
 def my_num(cls,name):
  print(f'{name} phone number is {cls.num}')
obj = A
A.my_num("Karthik")

A.num = 9949657890
A.my_num("Karthik")
print(A.num)
print(obj.num)


# STATIC METHOD
# class A:
#   @staticmethod
#   def add(x,y):
#     print(x+y)
# obj = A()
# obj.add(2,3)

class Employee:
  def display(self):
    print("Employee Details")


emp_obj1 = Employee()
emp_obj2 = Employee()
emp_obj3 = Employee()
emp_obj4 = Employee()
emp_obj5 = Employee()

emp_obj6 = Employee()
print(emp_obj6)
emp_obj6.display()