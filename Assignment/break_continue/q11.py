n= int(input("Enter the number"))
#1023
count=0
while n>0:
    d=n%10
    n=n//10
    if d==0: 
        print("duck number")  
        break 
    else:
         print(" not duck number")  