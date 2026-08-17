'''
3.

MATRIX PERFORMANCE EVALUATION SYSTEM

A company records the monthly performance scores of employees in a matrix format. Each row represents an employee and each column represents a month.

The HR department wants a menu-driven application to analyze employee performance.

Menu
1. Find Employee with Highest Total Score
2. Find Month with Lowest Average Score
3. Display Employee-wise Maximum Score
4. Exit
Requirements
Choice 1 – Find Employee with Highest Total Score
Calculate the sum of each row.
Display the employee number having the highest total score.
Choice 2 – Find Month with Lowest Average Score
Calculate the average of each column.
Display the month having the lowest average score.
Choice 3 – Display Employee-wise Maximum Score
Find and display the maximum value present in each row.
Sample Input
10 20 30
40 50 60
25 35 45
Output
Employee 2 has Highest Total Score = 150

Month 1 Average = 25
Month 2 Average = 35
Month 3 Average = 45

Employee 1 Max Score = 30
Employee 2 Max Score = 60
Employee 3 Max Score = 45
'''
while True:
    print("Menu")
    print("1. Find Employee with Highest Total Score")
    print("2. Find Month with Lowest Average Score")
    print("3. Display Employee-wise Maximum Score")
    print("4. Exit")
    choice=int(input("Enter your choice : "))
    match choice:
        case 1:
              emp=int(input("Enter no. of employee"))
              month=int(input("Enter no. of months"))
              matrix=[]
              for i in range(emp):
                  row=[]
                  for j in range(month):
                      row.append(int(input("Enter elemetns")))
                  matrix.append(row)
              print(matrix)
              hscore=0
              index=0
              for i in range(emp):
                  sum=0
                  for j in range(month):
                      sum+=matrix[i][j]
                  if sum>hscore:
                      hscore=sum
                      index=i
              print("Employee",index,"has highest Total score",hscore)
     
        case 2:
              emp=int(input("Enter no. of employee"))
              month=int(input("Enter no. of months"))
              matrix=[]
              for i in range(emp):
                  row=[]
                  for j in range(month):
                      row.append(int(input("Enter elemetns")))
                  matrix.append(row)
              #print(matrix)
              for i in range(month):
                  sum=0
                  for j in range(emp):
                      sum+=matrix[j][i]
                      avg=sum/month
                  print("Month",i+1,"Average",avg)
         
        case 3:
              emp=int(input("Enter no. of employee"))
              month=int(input("Enter no. of months"))
              matrix=[]
              for i in range(emp):
                  row=[]
                  for j in range(month):
                      row.append(int(input("Enter elemetns")))
                  matrix.append(row)
              #print(matrix)
              for i in range(month):
                  max=0
                  for j in range(emp):
                      if matrix[i][j]>max:
                         max=matrix[i][j]
                  print("Employee",i+1, "Max Score =",max)
         
        case 4:
              print("Exit")
              break      
    