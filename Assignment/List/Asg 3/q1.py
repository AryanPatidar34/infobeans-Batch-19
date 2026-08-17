'''
NOTE: In all programs, read the length and list elements from the user.

====================================================================

1. First Non-Repeating Number
   ====================================================================

Scenario

An online voting system stores vote IDs in a list.

Find the first vote ID that appears only once.

Requirements

* Read N and list elements from user
* Find the first non-repeating number
* If no such number exists, display an appropriate message

Test Case 1

Input:
[4, 5, 1, 2, 1, 2, 4]

Output:
First Non-Repeating Number = 5

Test Case 2

Input:
[7, 7, 8, 8]

Output:
No Non-Repeating Number Found
'''

n=int(input("Enter size"))
arr=[]
vis=[]
for i in range(n):
    t=int(input())
    arr.append(t)

for i in arr:
    if i not in vis:
        vis+=str(i)
        if arr.count(i)==1:
            print("First non repeating character :",i)
            break
else:
    print("no non repeating character found")
  
    