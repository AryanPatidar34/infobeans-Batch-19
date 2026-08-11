'''
====================================================================
4. Longest Consecutive Sequence
===============================

Scenario

Find the longest sequence of consecutive numbers present in the list.

Requirements

* Read N and list elements from user
* Find the length of the longest consecutive sequence
* Display the sequence length

Test Case 1

Input:
[100, 4, 200, 1, 3, 2]

Output:
Longest Consecutive Length = 4

Explanation:
Sequence = 1, 2, 3, 4

Test Case 2

Input:
[10, 11, 12, 20]

Output:
Longest Consecutive Length = 3

---
'''
s=list(map(int,input("Enter elements").split()))
length=0
lar=0
for i in s:
     t=i+1
     if t in s:
         length+=1
         for j in range(1,len(s)):
            g=i+j
            
            if g in s:
                length+=1
            else:
                break
            j+=1
         if length>lar:
             lar=length
             length=0
        
             
     else:
         continue
        
print(lar)
