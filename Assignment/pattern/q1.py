'''
WAP to find sum of all integer between 100 and 200 which are divisible by 9'''



x=int(input("Enter the number"))
y=int(input("Enter the number"))
sum=0
for i in range(x,y+1):
   if i%9==0:
       sum=sum+i
   else:
       continue
   i=i+1   
print(sum)