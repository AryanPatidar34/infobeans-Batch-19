'''
.
Secure Password Analysis

A cybersecurity team wants to identify pairs of passwords having no common characters.

Problem Statement:

Given N strings, count the number of pairs that do not share any common character.

Example:

Input

N = 4
passwords[] = {"abc", "de", "fg", "ad"}

Output

3

Explanation

("abc","de")
("abc","fg")
("de","fg")
'''
n=int(input("Size of array"))
arr=[]
for i in range(n):
    arr.append(input("Enter string"))
#print(arr)
c=0
for i in range(n):
    for j in range(i,n):
            for ch in arr[i]:
                if ch in arr[j]:
                    break
            else:
                c+=1
                print(arr[i],arr[j])
print(c)
   