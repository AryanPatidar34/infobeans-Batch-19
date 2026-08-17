'''
7.
Factory Production – Factorial Expansion List

Problem Statement

A factory produces items where production capacity is defined using factorial growth.

Given a list of numbers, replace each number with its factorial value.

Then perform analysis on the resulting list.

Tasks:

Convert each element to factorial
Find sum of all factorial values
Find maximum factorial value
Count how many factorial values are even

Input:
A list of integers

Example 1

Input:
[3, 4, 5]

Processing:
3! = 6
4! = 24
5! = 120

Output:
[6, 24, 120]
Sum = 150
Max = 120
Even Count = 3
'''

n=list(map(int,input("Enter elements").split()))
Efact=0
sum=0
fac=[]
lar=0
print(n)
for i in n:
    fact=1
    for j in range(i,0,-1):
        fact=fact*j
    sum+=fact
    fac.append(fact)
    if fact>lar:
        lar=fact
    if fact%2==0:
        Efact+=1
print(fac)
print("Sum =",sum)
print("Max =",lar)
print("Even Count =",Efact)