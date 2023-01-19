'''Write a Python program to add 'ing' at the end of a given string length 
should be at least 3. If the given string already ends with 'ing' then add 
'ly' instead if the string length of the given string is less than 3, leave it 
unchanged'''

s=input("enter your string")
x=print(int(len(s)))

if len(s)>=3:
    if s[-3:]=="ing":
        s +="ly"
    else:
        s +="ing"

print(s)
