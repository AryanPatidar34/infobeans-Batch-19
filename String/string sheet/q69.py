'''
69Count how many times 'life' appears in a string. 
S = "life is life" 
2
'''
s=input("Enter the string").split()
w=input("Enter the word")
c=0
for i in s:
    if i==w:
        c+=1
print(c)