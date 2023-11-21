#STACK IS LIFO-LASTIN FIRST OUT
stack=[]
'''def push():
    element=int(input("enter the element: "))
    stack.append(element)
    print(stack)
def pop_element():
    if not stack:
        print("stack is empty")
    else:
        e=stack.pop()
        print("removed element: ",e)
        print(stack)
while True:
    print("select operation 1.push 2.pop 3.quit")
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop_element()
    elif choice==3:
        break
    else:
        print("enter the correct operation")'''

#stack using single linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stack:
    def __init__(self):
        self.head=None
    def isempty(self):
        if self.head==None:
            return True
        else:
            return False
    def push(self,data):
        if self.head==None:
            self.head=Node(data)
        else:
            newnode=Node(data)
            newnode.next=self.head
            self.head=newnode
    def pop(self):
        if self.isempty():
            return None
        else:
            popednode=self.head
            self.head=self.head.next
            popednode.next=None
            return popednode.data
    def peek(self):
        if self.isempty():
            return None
        else:
            return self.head.data
    def display(self):
        t=self.head
        if self.isempty():
            print("stack underflow")
        else:
            while(t !=None):
                print(t.data,end=" ")
                t=t.next
                if(t !=None):
                    print(" -> ",end= "")
            return
if __name__=="__main__":
    s=stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.display()
    print(" ")
    print("peek",s.peek())
    s.pop()
    s.display()
    print(" ")
    print("peek",s.peek())
'''o/p=
4  -> 3  -> 2  -> 1  
peek 4
2  -> 1  
peek 2'''

