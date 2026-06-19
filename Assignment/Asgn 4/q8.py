"""
Assignment 8: Compound Interest

A person invests money in a bank that provides compound interest annually.

Input:
Principal = 10000
Rate = 5%
Time = 2 years

Expected Output:
Amount after interest = 11025.0
"""

principle = float(input("Enter principle : "))
rate =float(input("Enter rate : "))
time = float(input("Enter time : "))
amount = principle*((1+(rate/100))**time)
print("Amount after interest : ",(amount))