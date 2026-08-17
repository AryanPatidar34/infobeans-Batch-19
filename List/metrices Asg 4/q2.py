'''
2.

=========================================================
            MATRIX ANALYSIS SYSTEM
=========================================================


A research laboratory stores experimental data in matrix form.
Scientists want a program that can analyze the matrix and provide
different statistics through a menu-driven application.

The application should allow the user to:

1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit

---------------------------------------------------------
Requirements
---------------------------------------------------------

1. Display the following menu repeatedly until the user selects Exit.

   1. Count Prime Numbers Row-wise
   2. Count Perfect Numbers Column-wise
   3. Display Row-wise Sum
   4. Exit

2. Read the number of rows and columns from the user.

3. Read all matrix elements from the user.

4. Based on the user's choice:

   Choice 1 - Count Prime Numbers Row-wise
   ---------------------------------------
   Count and display the number of prime numbers present
   in each row of the matrix.

5. Choice 2 - Count Perfect Numbers Column-wise
   --------------------------------------------
   Count and display the number of perfect numbers present
   in each column of the matrix.

   Note:
   A perfect number is a number that is equal to the sum
   of its proper divisors.

   Examples:
   6  = 1 + 2 + 3
   28 = 1 + 2 + 4 + 7 + 14

6. Choice 3 - Display Row-wise Sum
   --------------------------------
   Calculate and display the sum of each row.

7. Choice 4 - Exit
   --------------------------------
   Display:
   "Thank You for Using Matrix Analysis System"

---------------------------------------------------------
Sample Input/Output
---------------------------------------------------------

Menu
1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit

Enter your choice: 1

Enter rows: 3
Enter columns: 3

Enter matrix elements:
2 4 5
6 7 8
11 28 13

Output:
Row 1 Prime Count = 2
Row 2 Prime Count = 1
Row 3 Prime Count = 2

---------------------------------------------------------

Menu
1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit

Enter your choice: 2

Output:
Column 1 Perfect Number Count = 1
Column 2 Perfect Number Count = 1
Column 3 Perfect Number Count = 0

---------------------------------------------------------

Menu
1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit

Enter your choice: 3

Output:
Row 1 Sum = 11
Row 2 Sum = 21
Row 3 Sum = 52

---------------------------------------------------------

Menu
1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit

Enter your choice: 4

Output:
Thank You for Using Matrix Analysis System

=========================================================
'''

print("=========================================================")
print("           MATRIX ANALYSIS SYSTEM                        ")
print("=========================================================")
while True:
    print("1.Count Prime Numbers Row-wise")
    print("2.Count Perfect Numbers Column-wise")
    print("3.Display Row-wise Sum")
    print("4.Exit")
    choice=int(input("Enter your choice : "))
    match choice:
        case 1:
             r1=int(input("Enter number of rows :"))
             c1=int(input("Enter number of column :"))
             matrix1=[]
             for i in range(r1):
                 row=[]
                 for j in range(c1):
                     print("enter elements")
                     row.append(int(input()))
                 matrix1.append(row)
             print(matrix1)
             for i in range(r1):
                 c=0
                 for j in range(c1):
                     if matrix1[i][j]==1:
                              continue
                     elif matrix1[i][j]==2:
                               c+=1
                     else:
                         for k in range(2,matrix1[i][j]):
                             if matrix1[i][j]%k==0:
                                 print(k)
                                 break
                         else:
                             c+=1
                 print("row wise prime count :",i,"=",c) 
             print()
             print("---------------------------------------") 
        case 2:
             r1=int(input("Enter number of rows :"))
             c1=int(input("Enter number of column :"))
             matrix1=[]
             for i in range(r1):
                 row=[]
                 for j in range(c1):
                     print("enter elements")
                     row.append(int(input()))
                 matrix1.append(row)
             #print(matrix1)
             for i in range(c1):
                 c=0
                 for j in range(r1):
                     sum=0
                     for k in range(1,matrix1[j][i]):
                         if matrix1[j][i]%k==0:
                             sum+=k
                     if sum==matrix1[j][i]:
                         c+=1
                 print("row wise perfect count",c)
             print()
             print("---------------------------------------")     
        case 3:
             r1=int(input("Enter number of rows :"))
             c1=int(input("Enter number of column :"))
             matrix1=[]
             for i in range(r1):
                 row=[]
                 for j in range(c1):
                     print("enter elements")
                     row.append(int(input()))
                 matrix1.append(row)
             #print(matrix1)
             for i in range(r1):
                 sum=0
                 for j in range(c1):
                     sum+=matrix1[i][j]
                 print("row wise sum",sum)
             print()
             print("---------------------------------------") 
        case 4:
              print("Thank You for Using Matrix Analysis System") 
              break
              
 
                      
                              
             