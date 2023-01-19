#Write a Python program to get the Fibonacci series of given range.

num=int(input("enter number"))

a,b=0,1

for i in range(num+1):
    print(b)
    a,b=b,b+a
    
