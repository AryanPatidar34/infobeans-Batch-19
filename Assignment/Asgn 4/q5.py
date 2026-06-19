"""
Assignment 5: Salary Breakdown

An employee wants to calculate salary per day and per hour.

Input:
Monthly salary = 36000
Working days = 24
Working hours per day = 8

Expected Output:
Salary per day = 1500.0
Salary per hour = 187.5
"""
salary = float(input("Enter monthly salary :"))
days = float(input("Enter days :"))
work = float(input("Enter working hours per day :"))
per_day = salary/days
per_hour = per_day/work
print("Salary Per Day : ",(per_day))
print("Salary Per Hour :" , (per_hour))

