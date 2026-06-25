"""12. Restaurant Bill with GST System

A restaurant applies GST based on the total bill amount:

* Up to ₹1000 → 5% GST
* ₹1001 to ₹5000 → 12% GST
* Above ₹5000 → 18% GST
  Additionally, if the bill exceeds ₹3000, a service charge of ₹200 is added.

Write a Python program to calculate the final bill.

Input:
Enter bill amount: 4000

Output:
Final Bill Amount: ₹4680"""



bill = int(input("Enter bill"))
if bill<1000:
    bill = bill+(bill*0.05)
    print("Final Bill Amount :",bill)

elif bill>=1000 and bill<=5000:
     bill =  bill+(bill*0.12)
     if bill>3000:
         bill = bill+200
         print("Final Bill Amount :",bill)
     else:
         print("Final Bill Amount :",bill)

else:
     bill = bill*0.18
     print("Final Bill Amount :",bill)
    