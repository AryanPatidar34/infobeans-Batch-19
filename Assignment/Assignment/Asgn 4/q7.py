"""
Assignment 7: Cricket Run Rate

In cricket, overs are given in decimal format (e.g., 48.3 means 48 overs and 3 balls). Convert overs into total balls and calculate run rate.

Input:
Total runs = 275
Overs = 48.3

Expected Output:
Total Balls = 291
Run Rate = 5.67
"""

runs = float(input("Enter total runs :  "))
overs = float(input("Enter total overs : "))
mul = overs*10
over = mul//10
ball = mul%10
total_ball = over*6+ball
ac_over = total_ball/6
run_rate  = runs/ac_over





print("Total balls :",(total_ball))
print("Run Rate :",(run_rate))