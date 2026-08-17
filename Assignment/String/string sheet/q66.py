'''
66Count number of sentences in a paragraph. 
P = "This. Is. Test."
 3
'''
s=input("Enter string").split()
c=0
for i in s:
    if(i.endswith(".")):
        c+=1
print(c)