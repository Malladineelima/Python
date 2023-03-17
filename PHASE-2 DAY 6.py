#DFS GRAPHS TRAVERSAL IMPLIMENTATION USING STACK
graph={
    '5': ['3','7'],
    '3': ['2','4'],
    '7': ['8'],
    '2':[],
    '4': ['8'],
    '8': []
    }

visited=set()#set to keep track of visited node
def dfs(visited,graph,node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited,graph,neighbour)

dfs(visited,graph, '5')


#BFS GRAPHS TRAVERSAL IMPLIMENTATION USING QUEUE
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

#BUBBLE SORT LIST
def bubblesort(list):
    for i in range(len(list)-1,0,-1):
        print("i value :")
        print(i)
        for j in range(i):
            print(j)
            if list[j]>list[j+1]:
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp
list=[10,5,-3,-2,0,100,10]
bubblesort(list)
print(list)

#INSERTION SORT
#swap the elements to arrange in order
def insertionSort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key< arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
arr=[12,11,13,5,6]
insertionSort(arr)
print("sorted array is :")
for i in range(len(arr)):
    print("%d" %arr[i])

#SELECTION SORT
b=[]
def ss(a):
    k=0
    for i in range(0,len(a)):
        k=min(a)
        b.append(k)
        a.remove(k)
a=[3,10,5,90,6]
ss(a)
print(b)


#SELECTION SORT ANOTHER CODE
def selection_sort(alist):
    for i in range(0,len(alist) -1):
        smallest=i
        for j in range(i+1,len(alist)):
            if alist[j] < alist[smallest]:
                smallest=3
            alist[i],alist[smallest]=alist[smallest],alist[i]
alist=input('enter the list of numbers: ').split()
alist=[int(x) for x in alist]
selection_sort(alist)
print(' Sorted list: ',end=' ')
print(alist)

#merge sort is divide and conquer algorithm it divides input array in two halves,calls itself
#for the two halves and merges 2 sorted halves.merge() function used to merge 2 halves
#MEERGE SORT 
def merge_sort(unsorted_list):
    if len(unsorted_list) <=1:
        return unsorted_list
#find the middle point and divide it
    middle=len(unsorted_list) // 2
    
    left_list=unsorted_list[:middle]
    right_list=unsorted_list[middle:]
    
    left_list=merge_sort(left_list)
    right_list=merge_sort(right_list)
    return list(merge(left_list,right_list))
#merge the sorted halves
def merge(left_half,right_half):
    res=[]
    while len(left_half) !=0 and len(right_half)!=0:
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])
    if len(left_half)==0:
            res=res+right_half
    else:
            res=res+left_half
    return res
unsorted_list=[64, 34, 25, 12, 22, 11, 90]
print(merge_sort(unsorted_list))
unsorted_list=[10, -6, 34, 2, 100]
print(merge_sort(unsorted_list))

#QUICK SORT
def partition(arr,low,high):
    i=(low-1)
    pivot=arr[high]#pivot element
    for j in range(low,high):
        #if current element is smaller
        if arr[j] <= pivot:
            #increment
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return(i+1)
#sort
def quickSort(arr,low,high):
    if low < high:
        #index
        pi=partition(arr,low,high)
        #sort the partitiions
        quickSort(arr,low,pi-1)
        quickSort(arr,pi+1,high)
#main
arr=[2,5,3,8,6,5,4,7]
n=len(arr)
quickSort(arr,0,n-1)
print("sorted array is : ")
for i in range(n):
    print(arr[i],end=" ")

#the globals()method returns a dictionary with all the global variables
#and symbols for the current program
#LINEAR SEARCH
pos=-1
def search(list,n):
    i=0;
    while i<len(list):
        if list[i]==n:
            globals()['pos']=i
            return True
        i=i+1
    return False

list=[100,40,20,10]
n=20
if search(list,n):
    print(" Found it at position",pos+1)
else:
    print("not found")

#BINARY SEARCH
pos=-1
def search(list,n):
    l=0
    u=len(list)-1
    while l<=u:
        mid=(l+u)//2
        if(list[mid])==n:
            globals()['pos']=mid
            return True
        else:
            if list[mid]<n:
                l=mid+1
            else:
                u=mid-1
    return False
list=[5,10,15,100]
n=100
if search(list,n):
    print("element is found at index : ",pos+1)
else:
    print("not found")

#JUMP SEARCH
import math
def jumpSearch(arr,x,n):
    #finding block size to be jumped
    step=math.sqrt(n)
    #finding the block where element is
    #present (if it is present)
    prev=0
    a=arr[int(min(step,n)-1)]
    print("a",a)
    while arr[int(min(step,n)-1)]<x:
        
        prev=step
        step+=math.sqrt(n)
        if prev>=n:
            return-1
#doing a linear search for x in
#block begining with prev
    while arr[int(prev)]< x:
        prev+=1
        #if we reached next block or end
        #of array,element is not present
        if prev ==min(step,n):
            return -1
    #if element is found
    if arr[int(prev)]==x:
        return prev
    return -1
arr=[0,1,1,2,4,5,9,13,21,34,55,89,144,300,377,710]
x=55
n=len(arr)
#find the index of 'x' using jump search
index=jumpSearch(arr, x, n)
#print the index where 'x' is located
print("Number", x, "is at index","%.0f" %index)




    


