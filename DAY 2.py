#sum of "n" numbers

#add all the digits in a number
'''num=int(input("enter number"))
i=s=0
while(num!=0):
    r=num%10
    s=s+r
    num=num//10
print(s)
0/p=enter number152
8

#print all even numbers in given "N" numbers
num=int(input("enter number"))
i=0
while(i<=num):
    if i%2==0:
         print(i, end=  "\t")
    i=i+1
0/p=enter number10
0	2	4	6	8	10


#sum of even numbers

num=int(input("enter even number"))
i=sum=0
while (i<=num):
    if i%2==0:
        sum=sum+i
    i=i+1
print(sum)
o/p=enter even number10
30

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
o/p=enter number10
even sum is  30
odd sum is  25


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
o/p=enter number7
111

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
o/p=sum of 10 natural number is  2
average of 10 natural number is  5.5


#program for math table

n=int(input("enter from 1-10"))
print("multiplication table of ",n)
print("---------------")
for i in range(1,11):
    print(n,"X",i,"=",n*i)
0/p=enter from 1-105
multiplication table of  5
---------------
5 X 1 = 5
5 X 2 = 10
5 X 3 = 15
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
5 X 8 = 40
5 X 9 = 45
5 X 10 = 50

#factorial of a number
n=int(input())
fact=1
for i in range (1,n+1):
    fact=fact*i
print("factorial value of ",n,"is",fact)
0/p=5
factorial value of  5 is 120


#find series 1+(1/2)^2+(1/2)^2+(1/3)^3.....+1/n n=10
n=int(input())
s=0
for i in range(1,n+1):
    s=s+1/i
print(s)
0/p=10
2.9289682539682538

#series 1/2 + 2/3 + +3/4 +....n/(n+1) n=10

n=int(input())
sum=0
for i in range(1,n+1):
    sum=sum+(i/(i+1))
print(sum)
0/p=5
3.5500000000000003

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
o/p=
1
2
3

#continue

abc=(1,2,3,4,5,6)
for i in abc:
    if i ==4:
        continue
    print(i,end=" ")
o/p=1 2 3 5 6

#pass
for letter in 'neelima':
    print("pass:",letter)
o/p=
pass: n
pass: e
pass: e
pass: l
pass: i
pass: m
pass: a

#nth ternm of series 1,1,2,3,4,9,8,27,16,81,32,243,64,729,128,2187....
term=int(input("enter a term:"))
if term%2==0:
    print(3**(term-2))
else:
    print(2**(term-3))
 o/p=enter a term:10
6561

#Generating a calender

#calender

import calendar
y=int(input("enter the year="))
n=1
cal=calendar.TextCalendar(calendar.SUNDAY)
i=1
while i<=12:
    cal.prmonth(y,i)
    i+=1
o/p=
enter the year=2023
    January 2023
Su Mo Tu We Th Fr Sa
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30 31
   February 2023
Su Mo Tu We Th Fr Sa
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28
     March 2023
Su Mo Tu We Th Fr Sa
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30 31
     April 2023
Su Mo Tu We Th Fr Sa
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29
30
      May 2023
Su Mo Tu We Th Fr Sa
    1  2  3  4  5  6
 7  8  9 10 11 12 13
14 15 16 17 18 19 20
21 22 23 24 25 26 27
28 29 30 31
     June 2023
Su Mo Tu We Th Fr Sa
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30
     July 2023
Su Mo Tu We Th Fr Sa
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29
30 31
    August 2023
Su Mo Tu We Th Fr Sa
       1  2  3  4  5
 6  7  8  9 10 11 12
13 14 15 16 17 18 19
20 21 22 23 24 25 26
27 28 29 30 31
   September 2023
Su Mo Tu We Th Fr Sa
                1  2
 3  4  5  6  7  8  9
10 11 12 13 14 15 16
17 18 19 20 21 22 23
24 25 26 27 28 29 30
    October 2023
Su Mo Tu We Th Fr Sa
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30 31
   November 2023
Su Mo Tu We Th Fr Sa
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30
   December 2023
Su Mo Tu We Th Fr Sa
                1  2
 3  4  5  6  7  8  9
10 11 12 13 14 15 16
17 18 19 20 21 22 23
24 25 26 27 28 29 30
31'''





    


















    






 
    


    
