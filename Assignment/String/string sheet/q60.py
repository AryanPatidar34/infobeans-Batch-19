'''
60Append two strings but remove duplicate adjacent characters.
 S1 = "miss", S2 = "issippi"
 "misisipi"
'''
s=input("Enter the string")
s1=input("Enter the string 1")
res=""
temp=""
for i in s:
    if i!=temp:
        res+=i
        temp=i
for i in s1:
    if i!=temp:
        res+=i
        temp=i

print(res)    

