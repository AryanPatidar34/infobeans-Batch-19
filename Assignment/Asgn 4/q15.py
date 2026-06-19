"""Assignment 15: Expression Evaluation

An electricity billing system uses nested brackets, exponent-based scaling, and unary corrections.

Input:
60 + (12 * (2**3) // (+(4))) - (-(10 % 3))
"""
Cal = input("Enter Expression")
res =eval(Cal)
print(res)