Assignment 1: Restaurant Bill Split

A group of friends went to a restaurant. The restaurant adds GST and service charge to the bill, and then the total is divided equally.

Input:
Total bill amount = 2500
GST = 5%
Service charge = 10%
Number of friends = 4

Expected Output:
Final Bill = 2875.0
Each Person Pays = 718.75

---


Bill  = int(input("Enter total bill : "))
Gst_per = int(input("Enter gst on bill : "))
ser_charge =int(input("Enter charge: "))
friends = int(input("Enter total students : "))
charge_per =Gst_per+ser_charge 
total_charge= Bill*charge_per/100
total_bill = Bill+total_charge
per_person =total_bill/friends 
print("Every person pay : ",(per_person))


 