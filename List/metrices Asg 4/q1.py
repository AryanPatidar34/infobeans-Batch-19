'''
1.
=========================================================
        MATRIX OPERATIONS MANAGEMENT SYSTEM
=========================================================


A data analysis company stores numerical information in matrix form.
To help employees perform matrix-related operations efficiently,
the company wants a menu-driven application.

The application should allow the user to:

1. Add Two Matrices
2. Subtract Two Matrices
3. Compare Two Matrices
4. Exit

The user must enter the number of rows, columns, and all matrix
elements. The program should perform the selected operation and
display the result.

---------------------------------------------------------
Requirements
---------------------------------------------------------

1. Display the following menu repeatedly until the user chooses Exit.

   1. Add Two Matrices
   2. Subtract Two Matrices
   3. Compare Two Matrices
   4. Exit

2. Read the number of rows and columns from the user.

3. Read all elements of Matrix A and Matrix B from the user whenever
   required.

4. Based on the user's choice:

   Choice 1 - Add Two Matrices
   --------------------------------
   Add corresponding elements of both matrices and display
   the resultant matrix.

5. Choice 2 - Subtract Two Matrices
   --------------------------------
   Subtract corresponding elements of Matrix B from Matrix A
   and display the resultant matrix.

6. Choice 3 - Compare Two Matrices
   --------------------------------
   Check whether both matrices are equal.

   Two matrices are considered equal if:
   - They have the same dimensions.
   - Corresponding elements are equal.

   Display:
   "Matrices are Equal"
   or
   "Matrices are Not Equal"

7. Choice 4 - Exit
   --------------------------------
   Display:
   "Thank You for Using Matrix Operations Management System"

---------------------------------------------------------
Sample Input/Output
---------------------------------------------------------

Menu
1. Add Two Matrices
2. Subtract Two Matrices
3. Compare Two Matrices
4. Exit

Enter your choice: 1

Enter number of rows: 2
Enter number of columns: 2

Enter Matrix A:
1 2
3 4

Enter Matrix B:
5 6
7 8

Result Matrix:
6 8
10 12

---------------------------------------------------------

Menu
1. Add Two Matrices
2. Subtract Two Matrices
3. Compare Two Matrices
4. Exit

Enter your choice: 3

Enter number of rows: 2
Enter number of columns: 2

Enter Matrix A:
1 2
3 4

Enter Matrix B:
1 2
3 4

Output:
Matrices are Equal

---------------------------------------------------------

Menu
1. Add Two Matrices
2. Subtract Two Matrices
3. Compare Two Matrices
4. Exit

Enter your choice: 4

Output:
Thank You for Using Matrix Operations Management System

===================================================
'''


print("=========================================================")
print("       MATRIX OPERATIONS MANAGEMENT SYSTEM               ")
print("=========================================================")


while True:
    print("Menu")
    print("1. Add Two Matrices")
    print("2. Subtract Two Matrices")
    print("3. Compare Two Matrices")
    print("4. Exit")

    choice=int(input("Enter your choice : "))
    match choice:
        case 1:
             row=int(input("Enter number of rows :"))
             col=int(input("Enter number of column :"))
             matrixA=[]
             for i in range(row):
                 row=[]
                 for j in range(col):
                     print("enter elements")
                     row.append(int(input()))
                 matrixA.append(row)
             print(matrixA)
             row2=int(input("Enter number of rows :"))
             col2=int(input("Enter number of column :"))
             matrixB=[]
             for i in range(row2):
                 row=[]
                 for j in range(col2):
                     print("enter elements")
                     row.append(int(input()))
                 matrixB.append(row)
             print(matrixB)
             res=[]
             for i in range(len(matrixA)):
                 row=[]
                 for j in range(len(matrixB)):
                      row.append(matrixA[i][j]+matrixB[i][j]) 
                 res.append(row)   
             print(res)
             print()
             print("---------------------------------------")  
        case 2:
             row=int(input("Enter number of rows :"))
             col=int(input("Enter number of column :"))
             matrixA=[]
             for i in range(row):
                 row=[]
                 for j in range(col):
                     print("enter elements")
                     row.append(int(input()))
                 matrixA.append(row)
             print(matrixA)
             row2=int(input("Enter number of rows :"))
             col2=int(input("Enter number of column :"))
             matrixB=[]
             for i in range(row2):
                 row=[]
                 for j in range(col2):
                     print("enter elements")
                     row.append(int(input()))
                 matrixB.append(row)
             print(matrixB)
             res=[]
             for i in range(len(matrixA)):
                 row=[]
                 for j in range(len(matrixB)):
                      row.append(matrixA[i][j]-matrixB[i][j]) 
                 res.append(row)   
             print(res)
             print()
             print("---------------------------------------")     
        case 3:
             row=int(input("Enter number of rows :"))
             col=int(input("Enter number of column :"))
             matrix1=[]
             for i in range(row):
                 row=[]
                 for j in range(col):
                     print("enter elements")
                     row.append(int(input()))
                 matrix1.append(row)
             #print(matrix1)
             row2=int(input("Enter number of rows :"))
             col2=int(input("Enter number of column :"))
             matrix2=[]
             for i in range(row2):
                 row=[]
                 for j in range(col2):
                     print("enter elements")
                     row.append(int(input()))
                 matrix2.append(row)
             #print(matrix2)
             if len(matrix1)!=len(matrix2):
                 print("matrices are not equal")
             else:
                 isequal=True
                 for i in range(len(matrix1)):
                     for j in range(len(matrix2)):
                          if matrix1[i][j]!=matrix2[i][j]:
                              isequal=False
                              break
                     if isequal==False:
                         print("Metrices are not equal")
                         break
                 else:
                      print("Metrices are equal")
             print()
             print("---------------------------------------")  
        case 4:
              print("Thank You for Using Matrix Operations Management System")
              print()
              print("===================================================")
              break