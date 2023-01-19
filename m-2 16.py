s=input("enter string : ")
char=0
space=0
world=1
num=0

for i in s:
    if i.isalpha():
        chare=char+1
    elif i.isspace():
        space=space+1
        world=world+1
    elif i.isnumeric():
        num=num+1

print("char : ",char)
print("space : ",space)
print("world : ",world)
print("num : ",num)
