'''
6. Banking Fraud Detection System

A bank checks fraud risk based on transaction amount, location, device, and transaction count.

If amount is greater than or equal to 50000, then check location. If location is international, then check device. If device is new, then check transaction count. If transactions are more than 3, mark High Risk (Block); otherwise Medium Risk. If device is not new, mark Medium Risk.

If location is domestic, then check transaction count. If more than 5, mark Medium Risk; otherwise Low Risk.

If amount is less than 50000, then check unusual activity. If yes, then check device. If device is new, mark Medium Risk; otherwise Low Risk. If no unusual activity, mark Safe.

Input:
Amount = 70000
Location = international
Device = new
Transactions = 4

Output:
Risk Level = High Risk (Blocked)'''


amount=int(input("Enter the amount"))
loc=input("Enter your location (international/domestic)")
device=input("Enter your device (new/old)")
tns=int(input("Enter total transactions"))
act=input("Enter unusual activity (yes/no)").lower()


if amount>=50000:
    if loc=="international":
         if device=="new":
             if tns>3:
                 print("Risk Level =High Risk (Blocked)")
    else:
        if tns>5:
            print("Risk Level =medium risk")
        else:
            print("Risk Level =low risk")
else:
    if act=="yes":
         if device=="new":
             print("Risk Level : medium risk")
         else:
             print("low risk")
    else:
        print("mark safe")

    