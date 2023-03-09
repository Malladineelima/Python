#inheritance-single level
class parent:
    name="parent class"
    def method_1(self):
        print("this is the method of class a")
class child(parent):
    pass
ob=child()
print(ob.name)
ob.method_1()

#multilevel inheritance
class father:
    def method1(self):
        print("father")
class son1(father):
    def method2(self):
        print("son1")
class son2(father):
    def method3(self):
        print("son2")
ob1=son1()
ob2=son2()
ob1.method2()
ob2.method3()

#multilevel inheritance example2
class a:
    var1="in class a"
class b(a):
    var2="in class b"
class c(b):
    var3="in class c"
class d(c):
    var4="in class d"
ob1=b()
ob2=c()
ob3=d()
print(ob1.var1)
print(ob3.var1)

#multilevel inheritance example3
class kindergarden:
    var1="in kindergarden"
class school(kindergarden):
    var2="in school"
class college(school):
    var3="in college"
class office(college):
    var4="in office"
ob1=school()
ob2=college()
ob3=office()
print(ob1.var1)
print(ob2.var2)
print(ob3.var3)

#hirarchical inheritance
class parent:
    def fun1(self):
        print("this function is in parent class")
class child1(parent):
    def fun2(self):
        print("this function is in child1")
class child2(parent):
    def fun3(self):
        print("this function is in child2")
ob1=child1()
ob2=child2()
ob1.fun1()
ob2.fun1()
ob1.fun2()
ob2.fun3()

#multiple inheritance
class school:
    def aim(self):
        print("motive is education")
class college:
    def aim(self):
        print("motive is job")
class office(school,college):
    pass
ob=office()
ob.aim()

#multiple inheritance example 2
class a:
    def m1(self):
        print("in class a")
class b:
    def m1(self):
        print("in class b")
class c(b,a):
    pass
ob=c()
ob.m1()

#abstract classes
from abc import ABC
class polygon(ABC):
    #abstract method
    def sides(self):
        pass
class triangle(polygon):
    def sides(self):
        print("triangle has 3 sides")
class pentagon(polygon):
    def sides(self):
        print("pentagon has 5 sides")
class hexagon(polygon):
    def sides(self):
        print("hexagon has 6 sides")
class square(polygon):
    def sides(self):
        print("square has 4 sides")

ob1=triangle()
ob1.sides()
ob2=pentagon()
ob2.sides()
ob3=hexagon()
ob3.sides()
ob4=square()
ob4.sides()

#polymorphism
class india():
    def capital(self):
        print("new delhi")
    def language(self):
        print("hindi")
class usa():
    def capital(self):
        print("washington,D.C")
    def language(self):
        print("english")
ob=india()
ob1=usa()
for country in (ob,ob1):
    country.capital()
    country.language()

















          

