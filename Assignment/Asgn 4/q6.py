"""
Assignment 6: Data Storage Conversion

A user wants to convert data from GB into MB and KB.

Input:
Data = 5 GB

Expected Output:
In MB = 5120.0
In KB = 5242880.0
"""

GB = float(input("Enter data in GB :"))
MB = GB*1024
KB = MB*1024
print("IN MB :",(MB))
print("IN KB :",(KB))
