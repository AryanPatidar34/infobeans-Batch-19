"""
2. Student Performance Analyzer
   A school wants to evaluate students based on marks.

* If marks ≥ 40 → Pass
* If marks ≥ 75 → Distinction

Input:
Enter marks: 80

Output:
Pass
Distinction
"""



marks = int(input("Enter student marks"))
if marks>=40:
    print("pass")
    if marks>=75:
        print("Distinction")

else:
     print("fail")