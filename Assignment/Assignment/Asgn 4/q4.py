"""
Assignment 4: Travel Distance Calculation

A person is traveling at a constant speed. Time is given in hours and minutes. Convert total time into hours and calculate distance.

Input:
Speed = 60 km/hr
Time = 2 hours 30 minutes

Expected Output:
Total Time = 2.5 hours
Distance = 150.0 km
"""

speed = float(input("Enter speed in km/hr : "))
hours,min = map(int,input("Enter time in hr/min : ").split())
total_time = hours+min/60
print("Total time :",(total_time),"hours")
distance = speed*total_time
print("Distance : ",(distance))
