"""Assignment 12: Expression Evaluation

A gaming score system calculates bonus points using exponent and applies penalties using unary negative values and brackets.

Input:
100 - (20 * (3**2)) + (40 / (+5)) - (-3)
"""

Cal = input("Enter Expression : ")
res = eval(Cal)
print(res)