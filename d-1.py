#finding the factorial of any given number using reccursive function
'''def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

num=int(input())
print(fact(num))

#sum of n natural numbers
def nat(n):
    if n==1:
        return 1
    else:
        return n + nat(n-1)

num=int(input())
print(nat(num))

#nth term of fibinacce series using reccursion #0 1 1 2 3 5 8
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
num=int(input())
print(fib(num))


#find the power of a number using reccursion
def power(a,b):
    if b==1:
        return a
    else:
        return a*(power(a,b-1))
base=int(input())
exp=int(input())
print(power(base,exp))'''

#nth term of fibinacce series using reccursion #0 1 1 2 3 5 8 and dP
def fib(n,dp):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif dp[n]!=-1:
        return dp[n]
    else:
        dp[n]=fib(n-1,dp)+fib(n-2,dp)
        return dp[n]

dp=[-1]*8
print(fib(4,dp))
print(dp)
print(fib(6,dp))
print(dp)

        
