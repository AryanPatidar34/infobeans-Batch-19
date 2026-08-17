'''
Find the first palindrome word.
 S = "this madam is here" 
"madam"
'''
s=input("Enter string").split()
#s=s.split()
for i in s:
   if i[::-1]==i:
       print(i)
       break
