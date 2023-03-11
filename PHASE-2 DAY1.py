#ENCAPSULATION
#protected
class encap:
    _a=10
    c=20
    def encapfunction(self):
        _b=200
        print("encap function-accessing protected")
        print(self._a+10)
obj=encap()
print(obj._a)
obj.encapfunction()
print(obj.c)

#private
class encap:
    __a=10
    print(__a)
    def encapfunction(self):
        print("encap function")
        print(self.__a)
obj=encap()
obj.encapfunction()
print(obj.__a)
#it will through error bcs a is a private cant
#acessed outside class

#extend
l=[1,2,3,4,5]
l.extend([10,20,30,])
print(l)

#index number
x=200
print(id(x))

#single linked list
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def display (self):
        if self.head is None:
            prinit("ll is empty")
        else:
            temp=self.head
            while(temp):
                print(temp.data,"==>",end=" ")
                temp=temp.next
obj=sll()
n1=node(100)
obj.head=n1
n2=node(200)
obj.head.next=n2
n3=node(300)
n2.next=n3
obj.display()

#insertion at begining in single linked list
class Node:
     def __init__(self,data):
         self.data=data
         self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def insert_begining(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head
        while temp:
            print(temp.data,"==>",end=" ")
            temp=temp.next
obj=singlelinkedlist()
n=Node(10)
obj.head=n
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
print(" before inserting 100")
obj.display()
print("")
print("after inserting100")
obj.insert_begining(100)
obj.display()
print(" ")
print("after inserting 555")
obj.insert_begining(555)
obj.display()

#insertion at end in single linked list 
class Node:
     def __init__(self,data):
         self.data=data
         self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def insert_end(self,data):
        ne=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=ne
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head
        while temp:
            print(temp.data,"==>",end=" ")
            temp=temp.next      
obj=singlelinkedlist()
n=Node(10)
obj.head=n
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
print(" before inserting 100")
obj.display()
print("")
print("after inserting100")
obj.insert_end(100)
obj.display()
print(" ")
print("after inserting 555")
obj.insert_end(555)
obj.display()
print(" ")
print("after inserting 11111")
obj.insert_end(11111)
obj.display()












