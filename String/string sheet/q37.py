'''
Reverse each word.
 S = "cat dog" 
"tac god"
'''
s=input("Enter string").split()
rev=""
for i in s:
    temp=i[::-1]
    rev+=temp+" "
print(rev)
