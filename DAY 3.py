#strings basic format

'''txt='neelima'
index=0
for i in txt:
    print("message[",index,"]=",i)
    index+=1
#0/p=
message[ 0 ]= n
message[ 1 ]= e
message[ 2 ]= e
message[ 3 ]= l
message[ 4 ]= i
message[ 5 ]= m
message[ 6 ]= a

#string function title
txt='the nun'
print(txt.title())
#0/p=The Nun

#upper
txt='the nun'
print(txt.upper())
o/p=THE NUN

#lower
txt='the nun'
print(txt.lower())
0/p=the nun

txt='6'
print(txt.zfill(4))
0/p=0006

txt='63625'
print(txt.lower())
0/p=63625

#
n=int(input())
s=0
while(n!=0):
    r=n%10
    s=(r*r*r)
    n=n//10
    s=(r*r*r)
print(s)
0/p=323
27

#string functions
#highest element
txt='hi students'
print(txt.zfill(4))
o/p=hi students

#
n=int(input("enter a number"))
s=0
while n!=0:
    r=n%10
    s=s+(r*r*r)
    n=n//10
if (s==n):
    print("armstrong ")
else:
    print("not")
0/p=enter a number10
not

#maximum value
txt="glucoz"
print(max(txt))
o/p=z

#minimum value
txt="neelima"
print(min(txt))
0/p=a

#replace
txt="ne ne ne ne"
print(txt.replace('n','a'))
0/p=ae ae ae ae

#swap txt
txt="suji my friend"
print(txt.swapcase())
o/p=SUJI MY FRIEND

#string separation
txt='abc,def,ghi,jkl'
print(txt.split(','))
0/p=['abc', 'def', 'ghi', 'jkl']

#join text
txt='neelima,is,a,good,girl'
print('-'.join(['neelima','is','a','good','girl']))
0/p=neelima-is-a-good-girl


txt='my name is neelima'
print(list(enumerate(txt)))
0/p=[(0, 'm'), (1, 'y'), (2, ' '), (3, 'n'), (4, 'a'), (5, 'm'), (6, 'e'), (7, ' '), (8, 'i'), (9, 's'), (10, ' '),
(11, 'n'), (12, 'e'), (13, 'e'), (14, 'l'), (15, 'i'), (16, 'm'), (17, 'a')]


#boolean functions
txt='malladineelima2003'
print(txt.isalpha())
print(txt.isnumeric())
print(txt.isupper())
0/p=False
False
False

#
txt=""
print(txt.isspace())
0/p=False
#
txt='malladineelima'
print(len(txt))
0/p=14
#
txt='neelima'
print(txt.ljust(10,'$'))
print(txt.rjust(10,'$'))
print(txt.center(20,'$'))
o/p=neelima$$$
$$$neelima
$$$$$$neelima$$$$$$$
#
txt='india is my country'
print(txt)
print(txt[1:5])
print(txt[:6])
print(txt[:])
print(txt[-4])
print(txt[::-1])
print(txt[::2])
0/p=india is my country
ndia
india 
india is my country
n
yrtnuoc ym si aidni
idai ycuty

#asky value of A
ch='A'
print(ord(ch))
0/p=65

#ord valu to character
print(chr(65))
0/p=A

#string
txt1='neeelima is great'
txt2='is'
if txt2 in txt1 :
    print("found")

else:
    print("not found")
0/p=found

txt1='neeelima is great'
txt2='id'
if txt2 in txt1 :
    print("found")

else:
    print("not found")
 0/p=not found

#

txt1='neeelima is great'
txt2=' i'
if txt2 in txt1 :
    print("found")

else:
    print("not found")
0/p=found

#

txt='neelima is great'
for i in txt:
    print(i,end='  ')
 0/p=n  e  e  l  i  m  a     i  s     g  r  e  a  t  

#
txt='neelima is great'
i=0
while i<len(txt):
    letter=txt[i]
    print(letter,end=" ")
    i+=1
0/p=n e e l i m a   i s   g r e a t 

#pattern programs

n=int(input())
for i in range (1,n+1):
    ch='A'
    print()
    for j in range(1,i+1):
        print(ch, end='  ')
        ch=chr(ord(ch)+1)

o/p=5
A  
A  B  
A  B  C  
A  B  C  D  
A  B  C  D  E  

#imp quest
message="danger"
i=0
while i<len(message):
    letter=message[i]
    print(chr(ord(letter)+2), end=' ')
    i+=1
o/p-f c p i g t 
          
#list
    
list=[1,2,3,4,5,6,7,8,9,10]
print(list)
print(list[9])
print(list[2:5])
print(list[::3])
print(list[::2])
print(list[1::3])
0/p=
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
10
[3, 4, 5]
[1, 4, 7, 10]
[1, 3, 5, 7, 9]
[2, 5, 8]

#

list=[1,2,3,4,5,6,7,8,9,10]
list[5]=100
print(list)
list.append(200)
print(list)
0/p=
[1, 2, 3, 4, 5, 100, 7, 8, 9, 10]
[1, 2, 3, 4, 5, 100, 7, 8, 9, 10, 200]'''































































