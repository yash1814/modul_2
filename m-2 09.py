#Write a Python program to sum of three given integers. However  if two values are equal sum will be zero

def sum(x,y,z):
    if x==y or y==z or x==z:
        sum=0
    else:
        sum=x+y+z
    return sum


x=float(input("enter x"))
y=float(input("enter y"))
z=float(input("enter z"))
print(sum(x, y, z))

