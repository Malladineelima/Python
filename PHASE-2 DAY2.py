#inserting new node at a given position in SLL
class Node:
     def __init__(self,data):
         self.data=data
         self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def insert_position(self,pos,data):
        np=Node(data)
        temp=self.head
        for i in range (pos-1):
            temp=temp.next
        #np.data=data
        np.next=temp.next
        temp.next=np
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
obj.display()
print()
obj.insert_position(2,1000)
obj.display()

#delete at the begining in SLL
class Node:
     def __init__(self,data):
         self.data=data
         self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def delete(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
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
#calling the function
obj.display()#it displays original data
print(" \n ")
obj.delete()
obj.display()#it displays after delete

#delete at the end in SLL
class Node:
     def __init__(self,data):
         self.data=data
         self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def delete_end(self):
        temp=self.head.next
        prev=self.head
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None#last but before node ne
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
obj.display()
print(" \n ")
obj.delete_end()
obj.display()

#deleting at a given position in SLL
class Node:
     def __init__(self,data):
         self.data=data
         self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def delete_position(self,pos):
        temp=self.head.next
        prev=self.head
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next=None
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
obj.display()
print("\n ")
obj.delete_position(3)
obj.display()

#double linked list implementation
class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"==>",end=" ")
                temp=temp.next
l=dll()
n1=Node(100)
l.head=n1
n2=Node(200)
n2.prev=n1
n1.next=n2
l.display()

#
import random
n=random.randrange(1,100)
guess=int(input("enter any number: "))
while n!=guess:
    if guess<n:
        print("too low")
        guess=int(input("enter number again: "))
    elif guess > n:
        print("too high")
        guess=int(input("enter number again: "))
    else:
        break
print("you guessed it right")


#insert at begining in double linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
    def insert_start(self):
         n=Node(300)
         temp=self.head
         temp.prev=n
         n.next=temp
         self.head=n
    def display(self):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"==>",end=" ")
                temp=temp.next
l=dll()
n1=Node(100)
l.head=n1
n2=Node(200)
n2.prev=n1
n1.next=n2
print(" before inserting ")
l.display()
print(" ")
print("after inserting")
l.insert_start()
l.display()

#insert at end in double linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
    def insert_end(self):
        n=Node(300)
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=n
        n.prev=temp
    def display(self):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"==>",end=" ")
                temp=temp.next
l=dll()
n1=Node(100)
l.head=n1
n2=Node(200)
n2.prev=n1
n1.next=n2
print("before insertion")
l.display()
print(" ")
print("after insertion")
l.insert_end()
l.display()

#inserting at given position in double linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
    def insert_pos(self,pos):
        n=Node(300)
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next
        n.prev=temp
        n.next=temp.next
        temp.next.prev=n
        temp.next=n
    def display(self):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"==>",end=" ")
                temp=temp.next
l=dll()
n1=Node(100)
l.head=n1
n2=Node(200)
n2.prev=n1
n1.next=n2
n3=Node(400)
n3.prev=n2
n2.next=n3
print(" before inserting ")
l.display()
print(" ")
print("after inserting")
l.insert_pos(3)
l.display()


#delete first node in DLL
class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
    def delete_start(self):
        temp=self.head
        temp.next.prev=None
        self.head=temp.next
        temp.next=None
    def display(self):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"==>",end=" ")
                temp=temp.next
l=dll()
n1=Node(100)
l.head=n1
n2=Node(200)
n2.prev=n1
n1.next=n2
print(" before delete ")
l.display()
print(" ")
print("after delete")
l.delete_start()
l.display()

#delete last node in DLL
class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
    def delete_end(self):
        temp=self.head.next
        prev=self.head
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None
    def display(self):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"==>",end=" ")
                temp=temp.next
l=dll()
n1=Node(100)
l.head=n1
n2=Node(200)
n2.prev=n1
n1.next=n2
n3=Node(400)
n3.prev=n2
n2.next=n3
print(" before delete ")
l.display()
print(" ")
print("after delete")
l.delete_end()
l.display()

#delete at given position in DLL
class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
    def delete_position(self,pos):
        temp=self.head.next
        prev=self.head
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next=None
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head
        while temp:
            print(temp.data,"==>",end=" ")
            temp=temp.next
l=dll()
n1=Node(100)
l.head=n1
n2=Node(200)
n2.prev=n1
n1.next=n2
n3=Node(400)
n3.prev=n2
n2.next=n3
print("before delete")
l.display()
print(" ")
print("after delete")
l.delete_position(2)
l.display()

















    
