'''
====================================================================
2. First Repeating Number
=========================

Scenario

A security system logs employee IDs.

Find the first ID that repeats in the list.

Requirements

* Read N and list elements from user
* Find the first repeating number
* If no repeating number exists, display an appropriate message

Test Case 1

Input:
[10, 5, 3, 4, 3, 5]

Output:
First Repeating Number = 3

Test Case 2

Input:
[1, 2, 3, 4]

Output:
No Repeating Number Found

---
'''
s=list(map(int,input("Enter elements").split()))
for i in s:
    if s.count(i)>1:
        print("First repeating character :",i)
        break
else:
     print("no repeating number found")