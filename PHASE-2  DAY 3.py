#stack operations using list
#STACK IS LIFO-LAST IN FIRST OUT
#stack implimentation
stack=[]
def push():
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
        print("enter the correct operation")

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
    print("")
    print("peek",s.peek())
    s.pop()
    s.display()
    print("")
    print("peek",s.peek())

#STACK implimentation using lifo queue
from queue import LifoQueue
s=LifoQueue(maxsize=3)
print(s.qsize())
s.put('a')
s.put('b')
s.put('c')
print(s.full())
print(s.qsize())
print(s.get())
print(s.get())
print(s.get())
print(s.empty())

#QUEUE IMPLIMENTATION USING ARRAY OR LIST
queue=[]
def enqueue():
    element=input("enter element")
    queue.append(element)
    print(element,"is added in q")
def dequeue():
    if not queue:
        print("Q is empty")
    else:
        e=queue.pop(0)
        print("removed element",e)
def display():
    print(queue)
while True:
    print("select operation 1.add 2.remove 3.show 4.quit ")
    choice=int(input())
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        break

#QUEUE IMPLIMENTATION USING QUEUE MODULE
import queue
L=queue.Queue(maxsize=5)
L.put(10)
L.put(20)
print(type(L))
print(L.get())
print(L.get())

#create two stacks:
#define size of both stacks as 5:
#if your input is even number it has to pushed
#in stack_1 and other inputs has to be pushed
#in stack_2
#options: push/pop/display/_stack/quit
stack1=[]
stack2=[]
def push():
    for i in range (5):
         element=int(input("enter the element: "))
         if (element%2==0):
             stack1.append(element)
         else:
            stack2.append(element)
def pop_element():
    pop_what=input("1 or 2")
    if pop_what==" 1 ":

        if not stack1:
            print("stack is empty")
        else:
            e=stack1.pop()
            print("removed element: ",e)
            print(stack1)
        
    else:
        if not stack2:
            print("stack is empty")
        else:
            e=stack2.pop()
            print("removed element: ",e)
            print(stack2)
def show():
    what=input("1 or 2 ")
    if what==" 1 ":
        print(stack1)
    else:
        print(stack2)
while True:
    print("select operation 1.push 2.pop 3.show 4.quit")
    choice=int(input(" enter choice:"))
    if choice == 1:
        push()
    elif choice == 2:
        pop_element()
    elif choice == 3:
        show()
    elif choice == 4:
        break
    else:
        print("enter the correct operation")

#QUEUE IMPLIMENTATION USING LINKED LIST
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.head=None
        self.last=None
    def enqueue(self,data):
        if self.last is None:
            self.head=Node(data)
            self.last=self.head
        else:
            self.last.next=Node(data)
            self.last=self.last.next
    def dequeue(self):
        if self.head is None:
            return None
        else:
            to_return=self.head.data
            self.head=self.head.next
            return to_return
a_queue=Queue()
while True:
    print('enqueue <value>')
    print('dequeue')
    print('quit')
#by using spilt,do will become a list,spilt
#works with string
    do=input("what would you like to do?").split()
    operation=do[0].strip().lower()
    if operation =='enqueue':
        a_queue.enqueue(int(do[1]))
    elif operation=='dequeue':
        dequeued=a_queue.dequeue()
        if dequeued is None:
            print('queue is empty.')
        else:
            print('dequeue element:',int(dequeued))
    elif operation=='quit':
        break
 
