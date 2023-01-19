#Write a Python program to get a single string from two given strings,
#separated by a space and swap the first two characters of each string

s1=input("enter your first string: ")
s2=input("enter your second string: ")

print("separated by a space: ",s1+" "+s2)

x=s1[:2]+s2[2:]
y=s2[:2]+s1[2:]

print("swap first two charecter",x+" "+y)

