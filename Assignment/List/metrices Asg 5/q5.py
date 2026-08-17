'''
5.

Rearrange the array in alternating positive and negative items
Given an unsorted array Arr of N positive and negative numbers.
Your task is to create an array of alternate positive and negative numbers
without changing the relative order of positive and negative numbers.
Note: Array should start with positive number.

Example 1:
Input:
N = 9
Arr[] = {9, 4, -2, -1, 5, 0, -5, -3, 2}
Output:
9 -2 4 -1 5 -5 0 -3 2
Example 2:
Input:
N = 10
Arr[] = {-5, -2, 5, 2, 4, 7, 1, 8, 0, -8}
Output:
5 -5 2 -2 4 -8 7 1 8 0
'''
arr=list(map(int,input("Enter elemnts :").split()))
neg=[]
pos=[]
for i in arr:
    if i<0:
        neg.append(i)
    else:
        pos.append(i)
#print(pos)
#print(neg)
l=min(len(pos),len(neg))
Arr=[]
for i in range(l):
    Arr.append(pos[i])
    Arr.append(neg[i])
if len(pos)>len(neg):
    for i in range(len(neg),len(pos)):
        Arr.append(pos[i])
else:
    for i in range(len(pos),len(neg)):
        Arr.append(neg[i])   
print(Arr)