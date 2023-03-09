#single linked list creation
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

#single linked list insertion operations:
1.insertion
 a.inserting new node at the begining
  step1=create new node which you want to insert
  step2=make the new node point to current head node
  step3=make your new node as head node
 b.inserting new node at the end
 c.inserting new node at given position

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
