'''#to check if a number is even 0r odd
num=int(input("enter a number"))
if num%2 == 0:
    print("number is even")
                  
else:
    print("number is odd")

#to check leap year
n=int(input("enter a number"))
if n%4==0 or n%100==0:
    
    print("leap year")
else:
    print("non leap year")
      
#largest among 3 numbers
a=int(input())
b=int(input())
c=int(input())
if a>b:
    if b>c:
        print("a is largest")
if b>c:
    if c>a:
        print("b is largest")
if c>a:
    if a>b:
        print("c is largest")

#to check prime number
n=int(input())
a=1
fc=0
while(a<=n):
    r=int(n%a)
    if (r==0):
        fc=fc+1
    a=a+1
if fc==2:
    print("prime number")
else:
    print("not a prime number")'''

#print al prime numbers in an interval
n=int(input())
for i in range(2,n+1):
    for j in range(2,i+1):
        if i%j==0:
            break
    if i==j:
        print(i,end='')

#to check armstrong number
'''n=int(input())
i=len(str(n))
flag=n
s=0
while n!=0:
    r=n%10
    s=s+r**i
    n=n//10
if flag==s:
    print(flag,"is armstrong")
else:
    print(flag,"not armstrong")'''




'''#multiplication table
n=int(input("enter a number"))
print("multiplication table of ",n)
i=0
for i in range(0,21):
    print(n,"X",i,"=",n*i)'''




            
            
            
