#sum of "n" numbers

#add all the digits in a number
'''num=int(input("enter number"))
i=s=0
while(num!=0):
    r=num%10
    s=s+r
    num=num//10
print(s)


#print all even numbers in given "N" numbers
num=int(input("enter number"))
i=0
while(i<=num):
    if i%2==0:
         print(i, end=  "\t")
    i=i+1

#sum of even numbers

num=int(input("enter even number"))
i=sum=0
while (i<=num):
    if i%2==0:
        sum=sum+i
    i=i+1
print(sum)

#print sum of even and od numbers separately
num=int(input("enter number"))
i=o=e=0
while(i<=num):
    if i%2==0:
        e=e+i
    else:
        o=o+i
    i=i+1
print("even sum is ",e)
print("odd sum is ",o)

#program to convert decimal number to binary number

dn=int(input("enter number"))
bn=0
i=0
while dn!=0:
    r=dn%2
    bn= bn+r*(10**i)
    dn=dn//2
    i+=1
print(bn)

#cLCULATE THE SUM OF NATURL NUMBERS AND FIND ITS AVERAGE:
for i in range(1,21,5):
    print(i,end="")
o/p=161116    

n=10
s=0
for i in range(1,n+1):
    s=s+i
    avg=s/n
print("sum of 10 natural number is ",2)
print("average of 10 natural number is ",avg)

#factorial of a number
n=int(input())
fact=1
for i in range (1,n+1):
    fact=fact*i
print("factorial value of ",n,"is",fact)


#find series 1+(1/2)^2+(1/2)^2+(1/3)^3.....+1/n n=10
n=int(input())
s=0
for i in range(1,n+1):
    s=s+1/i
print(s)

#series 1/2 + 2/3 + +3/4 +....n/(n+1) n=10

n=int(input())
sum=0
for i in range(1,n+1):
    sum=sum+(i/(i+1))
print(sum)

#print absolute diffferance of even and odd numbers in a number

n=int(input("enter a value:"))
E=0
O=0
i=0
while(n!=0):
    rem=n%10
    if(rem%2==0):
        E=rem+E
    else:
        O=rem+0
    n=n//10
print("diffeerance of terms is;",abs(0-E))
enter a value:3456
diffeerance of terms is; 10

#case1=input=1A,expected output=27,case2=input=23GF,expected output =10980

num=(str(input("enter a value :")))
print(int(num,17))
enter a value :17
24

#

abc=(1,2,3,4,5)
for i in abc:
    if i ==4:
        break
    print(i)

#continue

abc=(1,2,3,4,5,6)
for i in abc:
    if i ==4:
        continue
    print(i,end=" ")


#pass
for letter in 'neelima':
    print("pass:",letter)

#nth ternm of series 1,1,2,3,4,9,8,27,16,81,32,243,64,729,128,2187....
term=int(input("enter a term:"))
if term%2==0:
    print(3**(term-2))
else:
    print(2**(term-3))
 





    


















    






 
    


    
