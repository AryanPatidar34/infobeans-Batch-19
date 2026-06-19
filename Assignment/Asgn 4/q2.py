"""
Assignment 2: Mobile EMI Calculation

You purchased a mobile phone using EMI. After paying a down payment, the remaining amount includes interest and is divided into monthly installments.

Input:
Mobile price = 30000
Down payment = 5000
Interest rate = 10%
Months = 10

Expected Output:p
Remaining Amount = 25000
Total with Interest = 27500
Monthly EMI = 2750.0

"""


price = int(input("Enter mobile price : "))
down = int(input("Enter down payment : "))
rate = int(input("Enter rate interest : "))
time  = int(input("Enter time : "))
remaining = price-down
print("Remainnig Amount is : ",(remaining))
total_interest = remaining*rate/100
print("Total interest is : ",(total_interest))
total_price = remaining+total_interest
print("Monthly EMI : ",(total_price/time))