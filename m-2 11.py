#Write a python program to sum of the first n positive integers.
n=int(input("enter number : "))
sum=0
while 0<n:
    sum=sum+n
    print("sum : ",sum)
    n -= 1
