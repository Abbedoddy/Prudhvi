#2.Ploymorphisam
# POly = Many
# Morphism - Forms
# Default/ Basic Polymorphism
# print(3+5)
# print("Poly"+"Morphism")
# Inbuilt Function Polymorphism
#print(len("POlymorphism"))
#print(len(("POlymorphism", "Python")))
# User defined Function Polymorphism
'''def display(name,age,salary=10):
  print(f"{name} is of {age} years old earning a salary of {salary} lakhs")

display("Charan", 25, 8)
display("Ram", 26)

def add(a,b,c=0):
  print(a+b+c)

add(1,2,3)
add(1,2)'''


# # Class Method POlymorphism
# class EmployeeDetails:
#   def __init__(self,name,age,location):
#     self.name = name
#     self.age = age
#     self.location = location

#   # Instance Method
#   def display(self):
#     print(self.name, " is of ", self.age, " years old living in ", self.location)

# emp_obj1 = EmployeeDetails("Karthik", 25, "Hyderabad")
# emp_obj2 = EmployeeDetails("Charan", 26, "Vizag")
# print(emp_obj1)
# print(emp_obj2)
# emp_obj1.display()
# emp_obj2.display()


'''class Company:
  def __init__(self,name1,regnum,age1):
    self.compname = name1
    self.regnum = regnum
    self.compage = age1
  def display1(self):
    print(f"Name of the company is {self.compname}")

# comp_obj = Company("HCL")
# comp_obj.display()

class EmployeeDetails(Company):
  def __init__(self,name1,regnum, age1, name,age,location):
    self.compname = name1
    self.regnum = regnum
    self.compage = age1
    # super().__init__(name1,regnum,age1)
    # Company.__init__(self,name1,regnum,age1)
    self.name = name
    self.age = age
    self.location = location

  def display1(self):
    print(self.name, " is of ", self.age, " years old living in ", self.location, "working at " , self.compname, "which has history of", self.compage, "with registration number", self.regnum)

emp_obj1 = EmployeeDetails("HCL",3456,50, "Karthik", 25, "Hyderabad")
emp_obj1.display1()'''