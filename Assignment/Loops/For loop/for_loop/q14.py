'''14.Floor Movement System (Elevator)
An elevator system takes the current floor and destination floor as input.

If current floor < destination → move upward and display floors
If current floor > destination → move downward and display floors
If both are same → display "Already on the same floor"

Write a program using if-elif-else and loops to simulate elevator movement.

Input: 1, 5
Output: 1 → 2 → 3 → 4 → 5

Input: 7, 3
Output: 7 → 6 → 5 → 4 → 3

Input: 4, 4
Output: Already on the same floor'''
'''
#using for loop
a,b=map(int,input("Enter the nyumbers: ").split())
if a<b:
    for i in range(a,b+1):
        print(i,end=" ")
elif a>b:
    for i in range(a,b-1,-1):
        print(i,end=" ")
else:
    print("Already on the same floor")'''


#using while loop
a,b = map(int,input("Enter the number :").split())
if a<b:
    while a<=b:
          print(a,end=" ")
          a=a+1
elif a>b:
    while a>=b:
        print(a,end=" ")
        a-=1
else:
    print("Already on the same floor")
       