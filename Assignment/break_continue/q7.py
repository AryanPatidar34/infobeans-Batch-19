'''
7. Duck Number Checker

A verification system is used by an e-commerce company to validate promotional coupon numbers. Coupon numbers containing at least one zero in between digits are considered special duck numbers. However, if the number starts with zero, it is rejected immediately.

A duck number is a number that contains at least one zero but does not start with zero.

Example:
1023

Write a program using loops to check whether the entered number is a Duck number.

Input:
1023

Output:
Duck Number'''


n=input("Enter the number")
sl=len(n)
nl=len(str(int(n)))
count=0
if sl!=nl:
    print("not duck number")
else:
    nt=int(n)
    while nt>0:
        d=nt%10
        nt=nt//10
        if d!=0:
           continue
        else:
           count+=1
        if count>1:
            break
    if count>=1:
        print("duck number")
    else:
        print("not a duck number")
    


