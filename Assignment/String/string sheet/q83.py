'''
83Create a string from a byte array. 
Byte[] = {72, 101, 108} (ASCII for H, e, l)
 "Hel"
'''
s=list(map(int,input("Enter elemetns").split()))
temp=""
for i in s:
    temp+=chr(i)
print(temp)
