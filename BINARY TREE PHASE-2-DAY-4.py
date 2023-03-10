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


o/p=
Root Node is:
50
left child of the node is :
20
right child of the node is :
45
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
o/p=Inorder traversal before insertion: 7 11 10 15 9 8 <class 'list'>
1
1
2

inorder traversal after insertion: 12 11 10 15 9 8 

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
o/p=
PRE-ORDER: 
1 2 4 5 3 

 IN-ORDER: 
4 2 5 1 3 

 POST-ORDER: 
4 5 2 3 1 




        

            
           

