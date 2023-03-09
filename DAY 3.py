#strings basic format

txt='neelima'
index=0
for i in txt:
    print("message[",index,"]=",i)
    index+=1

#string function title
txt='the nun'
print(txt.title())

#upper
txt='the nun'
print(txt.upper())

#lower
txt='the nun'
print(txt.lower())

txt='6'
print(txt.zfill(4))

txt='63625'
print(txt.lower())

#
n=int(input())
s=0
while(n!=0):
    r=n%10
    s=(r*r*r)
    n=n//10
    s=(r*r*r)
print(s)

#string functions
#highest element
txt='hi students'
print(txt.zfill(4))

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

#maximum value
txt="glucoz"
print(max(txt))

#minimum value
txt="neelima"
print(min(txt))

#replace
txt="ne ne ne ne"
print(txt.replace('n','a'))

#swap txt
txt="suji my friend"
print(txt.swapcase())

#string separation
txt='abc,def,ghi,jkl'
print(txt.split(','))

#join text
txt='neelima,is,a,good,girl'
print('-'.join(['neelima','is','a','good','girl']))

txt='my name is neelima'
print(list(enumerate(txt)))

#boolean functions
txt='malladineelima2003'
print(txt.isalpha())
print(txt.isnumeric())
print(txt.isupper())

#
txt=""
print(txt.isspace())

#
txt='malladineelima'
print(len(txt))

#
txt='neelima'
print(txt.ljust(10,'$'))
print(txt.rjust(10,'$'))
print(txt.center(20,'$'))

#
txt='india is my country'
print(txt)
print(txt[1:5])
print(txt[:6])
print(txt[:])
print(txt[-4])
print(txt[::-1])
print(txt[::2])

#asky value of A
ch='A'
print(ord(ch))

#ord valu to character
print(chr(65))

#string
txt1='neeelima is great'
txt2='is'
if txt2 in txt1 :
    print("found")

else:
    print("not found")

txt1='neeelima is great'
txt2='id'
if txt2 in txt1 :
    print("found")

else:
    print("not found")
#

txt='neelima is great'
for i in txt:
    print(i,end='  ')

#
txt='neelima is great'
i=0
while i<len(txt):
    letter=txt[i]
    print(letter,end=" ")
    i+=1


#pattern programs
n=int(input())
for i in range (1,n+1):
    ch='A'
    print()
    for j in range(1,i+1):
        print(ch, end='  ')
        ch=chr(ord(ch)+1)


#imp quest
message="danger"
i=0
while i<len(message):
    letter=message[i]
    print(chr(ord(letter)+2), end=' ')
    i+=1

          
#list
    
list=[1,2,3,4,5,6,7,8,9,10]
print(list)
print(list[9])
print(list[2:5])
print(list[::3])
print(list[::2])
print(list[1::3])

#
list=[1,2,3,4,5,6,7,8,9,10]
list[5]=100
print(list)
list.append(200)
print(list)































































