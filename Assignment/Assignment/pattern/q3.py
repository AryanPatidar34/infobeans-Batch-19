'''
WAP to find out all the leap years between two entered years'''

x=int(input("Enter the number"))
y=int(input("Enter the number"))


for i in range(x,y+1):
    if i%400==0:
        print(i)
    elif i%4==0:
        print(i)
    