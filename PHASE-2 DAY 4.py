#taking multiple inputs in one line using map
a=list(map(int,input().split(' ')))
for i in a:
       print(i,end= ' ')
#adding numbers
a=list(map(int,input().split(' ')))
sum=0
for i in a:
       sum=sum+i
print(sum)
#multiplying numbers
a=list(map(int,input().split(' ')))
i=0
for i in a:
       print(i*i,end=" ")

#adding numbers by giving size
n=int(input("enter size"))
a=list(map(int,input().split(' ')))[n:]
sum=0
for i in a:
      #print(i,end=' ')
      sum=sum+i
print(sum)

#CIRCULAR QUEUE
#insert:rear=rear+1--we add new person at end of queue
#delete:front=front+1--fifo
class CircularQueue():
       def __init__(self,size):
              #initializing the class
              self.size=size
              #can use self.queue=[none]*size
              self.queue=[None for i in range(size)]
              self.front=self.rear=-1
       def enqueue(self,data):
              #condition if queue is full
              if ((self.rear+1) % self.size==self.front):#size 6 index from 0
                     print("Queue is Full\n")
              #condition for empty queue
              elif (self.front==-1):
                     self.front=0
                     self.rear=0
                     self.queue[self.rear]=data
                     #always add elements at tail place
              
              else:
                   #next position of rear
                   self.rear=(self.rear+1) % self.size
                   self.queue[self.rear]=data
       def dequeue(self):
              if (self.front == -1):#condition for empty queue
                     
                     print("Queue is Empty\n")
              #condition for only one element
              elif  (self.front ==self.rear):
                     temp=self.queue[self.front]
                     self.front= -1
                     self.rear= -1
                     return temp
              else:
                     temp=self.queue[self.front]
                     self.front=(self.front+1) % self.size
                     return temp
       def display(self):
              #condition for empty queue
              if self.front==-1:
                     print(" Queue is empty ")
              elif (self.rear >= self.front):
                     print("Elements in the circular queue:",end= " ")
                     for i in range(self.front,self.rear+1):
                           print(self.queue[i],end=" ")
                     print()
              else:
                     print("Elements in circular queue are:",end= " ")
                     for i in range (0,self.rear+1):
                            print(self.queue[i],end=" ")
                     
                     print()
              if((self.rear + 1) % self.size==self.front):
                     print("Queue is Full")
ob=CircularQueue(5)
ob.enqueue(14)
ob.enqueue(22)
ob.enqueue(13)
ob.enqueue(-6)
ob.display()
print("deleted value =",ob.dequeue())
print("deleted value =",ob.dequeue())
ob.display()
ob.enqueue(9)
ob.enqueue(20)
ob.enqueue(5)
ob.display()

#BINARY TREE IMPLIMENTATION
class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None
node1=BinaryTreeNode(50)
node2=BinaryTreeNode(20)
node3=BinaryTreeNode(45)
node4=BinaryTreeNode(11)
node5=BinaryTreeNode(15)
node6=BinaryTreeNode(30)
node7=BinaryTreeNode(78)

node1.leftChild =node2
node1.rightChild=node3
node2.leftChild=node4
node2.rightChild=node5
node3.leftChild=node6
node3.rightChild=node7

print("Root Node is:")
print(node1.data)
print("left child of the node is :")
print(node1.leftChild.data)
print("right child of the node is :")
print(node1.rightChild.data)


#insertion in binary tree
class newNode():
    def __init__(self,data):
        self.key=data
        self.left=None
        self.right=None
#inorder traversal of binary tree
def inorder(temp):
    if (not temp):
        return
    inorder(temp.left)
    print(temp.key,end=" ")
    inorder(temp.right)
def insert(temp,key):
    if not temp:
        root=newNode(key)
        return
    q=[]
    q.append(temp)
    print(type(q))
    print(len(q))
    while (len(q)):
        print(len(q))
        temp=q[0]
        q.pop(0)
        if (not temp.left):
            temp.left=newNode(key)
            break
        else:
            q.append(temp.left)
            
        if(not temp.right):
            temp.left=newNode(key)
            break
        else:
            q.append(temp.left)
if __name__=='__main__':
    root=newNode(10)
    root.left=newNode(11)
    root.left.left=newNode(7)
    root.right=newNode(9)
    root.right.left=newNode(15)
    root.right.right=newNode(8)
    print("Inorder traversal before insertion:",end=" ")
    inorder(root)
    key=12
    insert(root,key)
    print()
    print("inorder traversal after insertion:",end=" ")
    inorder(root)
#BINARY TREE WITH DIFF TRAVERSAL METHODS
class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
def printInorder(root):
    if root:
        #first recur on left child
        printInorder(root.left)
        #then print the data of node
        print(root.val,end= " " ),
        #now recur on right child
        printInorder(root.right)
def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.val,end= " "),
def printPreorder(root):
    if root:
        print(root.val,end= " "),
        printPreorder(root.left)
        printPreorder(root.right)
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
print("PRE-ORDER: ")
printPreorder(root)
print()
print("\n IN-ORDER: ")
printInorder(root)
print()
print("\n POST-ORDER: ")
printPostorder(root)
print()
                 
              
              
                     
