#sets
s={1,2,3,4,5}
print(s)

#string to integer
s="2003"
n=int(s)
print(n)

#string to list
s="2003"
n=list(s)
print(n)

#string to float
s="2003"
n=float(s)
print(n)

#list to set
a=[1,27,2003]
print(set(a))

#dictionaries
#program 1
abc={
    "key1":"high1",
    "key2":"medium2",
    "key3":"low3"
}
print(abc)

#program 2
student={
    "name":"student1",
    "age":20,
    "year":3,
    "branch":"civil"
}
print(student)

#replace and add new value in dictionary
student={
    "name":"student1",
    "age":20,
    "year":3,
    "section":'A'
}
student.update(
    {"name":"name1","age":15,"branch":"civil"}
)    
print(student)

#
student={
    "name":"student1",
    "age":20,
    "year":3,
    "section":'A'
}
student.update(
    {"name":0,"age":2,"year":3,"section":4}
)
print(student)

#
student={
    "name":"student1",
    "age":20,
    "year":3
}
print(student['age'])
print(student['name'])
print(student['year'])
print(student.keys())
print(student.values())
print(student.items())

#functions
def fun_name():
    print("neelima")
fun_name()

#
def fun_name(num1,num2):
    print("ans: ",num1*num2)
fun_name(10,20)

#
def fun_name(num1,num2,op):
    if op=="+":
        print(num1+num2)
    elif op=="-":
        print(num1-num2)
    elif op=="*":
        print(num1*num2)
fun_name(10,20,"*")

#sum of the array by using function
def fun_name(arr):
    sum=0
    for i in arr:
        sum=sum+i
        print(sum)
arr=[1,2,3,4,5]
fun_name(arr)
o/p=
1
3
6
10
15

#variable length function
def hellow(*variable):
    print(variable)
hellow(10,20)
hellow()

#VLF example 2
def add_num(*xyz):
    print(xyz)
add_num(10,20,30)
add_num(10)
add_num(10,20,30,"hello world",[10,2,5])

#keyword argument function
def add_num(a,b,c):
    print(a)
    print(b)
    print(c)
add_num(c=10,b=20,a=10)

#object oriented programming
class student:
    name="neelima"
    roll="le-103"
    def study(self):
        print("neelima is studying")
var1=student()
print(var1.name)
var1.study()

#packages
class A:
    val=10
    def say_hello(self):
        print("in class A")
class B:
    val=100
    def say_hello(self):
        print("in class B")
ob=A()
ob.say_hello()
ob2=B()
ob2.say_hello()

#
class pec:
    n="college"
    org="autonomous"
    y=2003
ob=pec()#call the class using ob
print(ob.org)#access the class variable

#
class happy:
    a=100
    def method(self):
        b=12
        print(self.a)
        print(b)
obj=happy()
print(obj.a)
obj.method()

#f format method
n="college"
org="autonomous"
y=2003
print(f"hello {n},org is {org},and  year is  {y}")
#string docs format method
name="college"
org="autonomous"
y=2003
print("hello {},org is {} and y is {}".format(name,org,y))

#
class person:
    n="pragati"
    age=20
    year=2023
    def print_detail(self):
        print(f"name:{self.n} and age:{self.age}")
ob=person()#call the object using ob
ob.print_detail()
#
class college:
    name="PEC"
    location="KKD"
    def aim(self):
        print(f"{self.name} is autonomous")
var1=college()
print(var1.name)
print(var1.location)
print(var1.aim())
#
class vehicle:
    n="bike"
    c="red"
    p="1 lakkh"
    m="bullet"
    def company_product(self):
        print(f"vehicle name is :{self.n}, bike colour is {self.c},  model is:{self.m}")
ob=vehicle()#call the class using ob
ob.company_product()

#constructor
class student:
    name="neelu"
    age=20

    def __init__(self):
        print(f"{self.name} is studying")

var1=student()
var2=student()













              
              
