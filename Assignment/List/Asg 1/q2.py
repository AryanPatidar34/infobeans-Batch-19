'''
2.Employee Salary Processing
Store employee salaries in a List and calculate details.

Requirements:

Store salaries
Find average salary
Display salaries greater than average
Remove salaries below 15000

Test Cases:

Input: [10000, 20000, 30000] → Average = 20000, Above Average = 30000
Input: [15000, 15000, 15000] → Average = 15000
Input: [5000, 7000] → Remaining List = []
'''
s=list(map(int,input("Enter salary :").split()))
sum=sum(s)
avg=sum/len(s)
gre=[]
b15=[]
for i in s:
    if i>avg:
        gre.append(i)
    if i>15000:
        b15.append(i)
 

print("original salary : ",s)
print("Average Salary : ",avg)
print(" Greater Average  : ",gre)
print("above 15000 : ",b15)