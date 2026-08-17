'''
3.
Replace Consecutive Duplicate Characters with Single Character
Data Compression System

A cloud storage company wants to reduce unnecessary repeated characters in text logs.

Write a Python program that replaces consecutive duplicate characters with a single occurrence.

Input:
aaabbbccccdddaa
Output:
abcda
'''

n=input("Enter your string")
temp=""
i=0
c=1
while i<len(n):
    ch=n[i] 
    cn=n[i-1]
    if ch!=cn or c==len(n):
       temp+=cn
    i+=1
    c+=1

print(temp)
    
   