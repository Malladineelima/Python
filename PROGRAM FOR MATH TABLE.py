#program for math table

n=int(input("enter from 1-10"))
print("multiplication table of ",n)
print("---------------")
for i in range(1,11):
    print(n,"X",i,"=",n*i)
