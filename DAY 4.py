#LIST
#abcederian sseries

str1="ABCDEFGH"
str2="ate"
for l in str1:
    print((l+str2),end=" ")

#program to evaluate list of a cubes till the range of 10
cubes=[]
for i in range (11):
    cubes.append(i**3)
print(cubes)

#program to find the sum and mean of series 0-10'''

#sum and mean of list
abc=[1,2,3,4,5,6,7,8,9,10]
sum =0
for i in abc:
    sum+=i
print(sum)
print(sum/len(abc))

operations of list
length=len
repetition
in
not in
max
min

#predifined functions
a=[90,0,8,7]
print(max(a))
print(min(a))

a=[-9,-5,2]
print(min(a))

#sum
a=[1,2,3,4,5]
print(sum(a))

#all,any,list,sort
ab=[0,-99,99,231,86]
x=sorted(ab)
print(x)
#o/p=[-99, 0, 86, 99, 231]

#append
ab=[0,-99,99,231,86]
ab.append(10)
print(ab)


#count all numbers in a list
ab=[0,-99,99,231,86]
print(ab.count(4))

#insert
ab=[6,3,7,0,3,7,6,0]
ab.insert(3,99)
print(ab)

#remove
ab=[6,3,7,0,3,7,6,0]
ab.remove(0)
print(ab)

#
str=[1,2,3,4,5]
len(str)
print(str)

#sum of numbers in a list
num=[1,2,3,4,5,6,7,8,9,10]
print(sum(num))

#methods in a list:

num=[1,2,3,4,5,6,7,8,9,10]
num.reverse()
print(num)

#sort of elements
num=[10,-1,-9,2,8,5]
num.sort()
print(num)

#
num=['1','a','abc','2','B','Def']
num.sort()
print(num)


#delete elements in a list wrt index values
txt=['p','r','o','g','r','a','m']
txt[2:5]=[]
print(txt)


#cubes meethod 1
cubes=[]
for i in range(11):
    cubes.append(i**3)
print(cubes)
#method 2        
cubes=[i**3 for i in range(11)];print(cubes)


#
num=[1,2,3,4,5]
it=iter(num)
for i in range (len(num)):
    print("element at index",i,"is:",next(it))

#question
n=int(input())
if n==0:
    print("time estimated: 0 minutes")
elif n in range(1,2001):
    print ("time estimated:25 minutes")
elif n in range(2001,4001):
    print("time estimated:35 minutes")
elif n in range( 4001,7001):
    print("time estimated: 45 minutes")
else :
    print("invalid output")

#find fifteenth term and sixteenth term 0,0,7,6,14,12,21,......n
a=6
b=7
i=j=temp=1
list_=[]
n=int(input(" enter n:"))
while(temp<=n):
    if temp%2!=0:
        list_.append(a*(i-1))
        i+=1
else:
    list_.append(b*(j-i))
    temp+=1
print("the {} term is:{}".format (n,list_[n-1]))
         
































