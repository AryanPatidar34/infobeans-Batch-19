"""Assignment 10: Time Conversion

Convert total seconds into hours, minutes, and seconds.

Input:
Total seconds = 7384

Expected Output:
Hours = 2
Minutes = 3
Seconds = 4
"""
seconds = int(input("Enter seconds : "))
hour = seconds//3600
rem1  = seconds%3600
min = rem1//60
rem2 = rem1%60
sec  = rem2
print("Hours : ",(hour))
print("Minutes : ",(min))
print("Seconds : ",(sec))
