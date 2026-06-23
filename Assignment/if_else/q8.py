"""
8. Number Property Checker
   A system evaluates number properties:

* If number % 2 == 0 → Even number
* If number % 5 == 0 → Divisible by 5

Input:
Enter number: 20

Output:
Even number
Divisible by 5
"""

number = int(input("Enter Number"))
if number%2==0:
    print("Even Number")
    if number%5==0:
        print("Divisible by 5")
else:
    print("not even number")