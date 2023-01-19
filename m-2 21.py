#Write a Python function to reverses a string if its length is a multiple of 4.

s="technologys "
print("original string : ",s)
if len(s)%4==0:
    print("reversed string : ",s[::-1])
