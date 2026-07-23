'''
1.
Find the Longest Substring Without Repeating Characters
Cybersecurity Session Tracking System

A cybersecurity company monitors user session IDs generated during secure login sessions.

To detect suspicious repeated patterns, the company wants a Python program that finds the longest substring containing no repeated characters.

Input:
abcabcbb
Output:
abc
'''

n=input("Enter string")
lar=""
i=0
while i<len(n):
    temp=""
    ch=n[i]
    temp+=ch
    
    j=i+1
    while j<len(n):
        if n[j] not in temp:
            temp+=n[j]
            j+=1
        else:
            break
    i+=1
    if len(temp)>len(lar):
        lar=temp
                    
   
print(lar)           