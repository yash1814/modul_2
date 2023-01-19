'''Write a Python program to count the number of characters (character frequency) in a string'''

s=input("enter string : ")

ch=0

for i in s:
    if i.isalpha():
        ch=ch+1



print(ch)
