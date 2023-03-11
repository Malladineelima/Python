#creating forest using dictionary
#dictionary (forest of 3 trees:)
Families={
          'charley':
                   {'sam':{'Boxy','Rosy'},
                    'Nila':{'Pepsi'}},
          'Devi':
                {'Tommy':{'Tony'},
                 'Timmy':{'Hamster'},
                 'Tammy':{'Hamster'}},
          'Carlos':
                  {'Diego':'cat','Ferret':'Fox'}
          }
for Parent,children in Families.items():
    print(f"{Parent} has {len(children)} kids(s): ")
    print(f"{',and '.join([str(child) for child in[*children]])}")


#BST-INSERTION
class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
def insert(root,key):
    if root is None:
        return Node(key)
    else:
        if root.val==key:
            return root
        elif root.val<key:
            root.right=insert(root.right,key)
        else:
            root.left=insert(root.left,key)
    return root
#inorder traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
#     50
#     /   \
#    30    70
#   /  \  /  \
# 20   40 60  80
r=Node(50)
r=insert(r,30)
r=insert(r,20)
r=insert(r,40)
r=insert(r,70)
r=insert(r,60)
r=insert(r,80)
inorder(r)
o/p=
20
30
40
50
60
70
80


#BST INSERTIN,DELETION AND INORDER:
class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key)
        inorder(root.right)
def insert(node,key):
    if node is None:
        return Node(key)
    if key<node.key:
        node.left=insert(node.left,key)
    else:
        node.right=insert(node.right,key)
    return node
def minValueNode(node):
    current=node
    while(current.left is not None):
        current = current.left
        return current
def deleteNode(root,key):
    if root is None:
        return root
    if key < root.key:
        root.left = deleteNode(root.left,key)
    elif key > root.key:
        root.right = deleteNode(root.right,key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp=root.left
            root=None
            return temp
            #node with two children
            #fet the inorder successer small value
        temp = minValueNode(root.right)
        root.key = temp.key
        root.right = deleteNode(root.right,temp.key)
    return root
root=None
root=insert(root,50)
root=insert(root,30)
root=insert(root,20)
root=insert(root,40)
root=insert(root,70)
root=insert(root,60)
root=insert(root,80)
print("Inorder traversal of the given tree")
inorder(root)
print("\nDelete 20")
root = deleteNode(root,20)
print("Inorder traversal of the modified tree")
inorder(root)
print("\nDelete 30")
root = deleteNode(root,30)
print("Inorder traversal of the modified tree")
inorder(root)
print("\nDelete 50")
root = deleteNode(root,50)
print("Inorder traversal of the modified tree")
inorder(root)


#implimentation of graph with dictionary using collection module
from collections import defaultdict
#add edge to graph : function
graph=defaultdict(list)
def addEdge(graph,u,v):
    graph[u].append(v)
#function description
def generate_edges(graph):
    edges=[]
    #for each node in graph
    for node in graph:
        #for each neighbour node of a single node
        for neighbour in graph[node]:
            #if edge exists the append
            edges.append((node,neighbour))
    return edges
addEdge(graph,'a','c')
addEdge(graph,'b','c')
addEdge(graph,'b','e')
addEdge(graph,'c','d')
addEdge(graph,'c','e')
addEdge(graph,'c','a')
addEdge(graph,'c','b')
addEdge(graph,'e','b')
addEdge(graph,'d','c')
addEdge(graph,'e','c')
#printing graph
print(generate_edges(graph))


#BFS GRAPH TRAVERSAL IMPLIMENTATION
g={'5':['3','7'],'3':['2','4'],'7':['8'],'2':[],'4':['8'],'8':[]}
visited=[]
q=[]
def bfs(visited,g,node):
    visited.append(node)
    q.append(node)
    while q:
        m=q.pop(0)
        print(m,end=" ")
        for neighbour in g[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                q.append(neighbour)
bfs(visited,g,'5')
o/p=5 3 7 2 4 8 











      
