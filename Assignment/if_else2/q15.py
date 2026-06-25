"""15. Smart Parking System

A smart parking system charges based on vehicle type and parking duration:

* Bike → ₹10/hour
* Car → ₹20/hour
* Bus → ₹50/hour
  If parking duration exceeds 5 hours, an additional ₹100 penalty is applied.

Write a Python program to calculate total parking fee.

Input:
Enter vehicle type: Car
Enter hours parked: 6

Output:
Total Parking Fee: ₹220"""

type = input("Enter vehicle type:(Bike/Car/Bus)").lower()
hours = int(input("Enter hours"))


Fee = 10*hours if type=="bike" else 20*hours if type=="car" else 50*hours 
if hours>5:
    print("Totsl Parking Fee",Fee+100)
else:
    print("Totsl Parking Fee",Fee)