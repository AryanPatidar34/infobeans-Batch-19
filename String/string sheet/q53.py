'''
53Remove all punctuation characters.
 S = "Hello, world!" 
"Hello world"
'''
s=input("Enter string")
res=""
for i in s:
    if 'a'<=i<='z' or 'A'<=i<='Z':
        res=res+i
    else:
        continue

print(res) 
