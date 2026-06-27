'''
6. Banking Fraud Detection System

A bank monitors transactions based on amount, location, OTP verification, and account age.

If transaction amount is at least 10000, then check location. If international, then check OTP verification. If verified, allow; otherwise block. If location is domestic, then check if amount is at least 50000. If yes, check account age. If account age is at least 2 years, allow; otherwise flag. If amount is less than 50000, allow. If transaction amount is less than 10000, then check unusual activity. If yes, flag; otherwise allow.

Input:
Transaction Amount = 60000
Location = domestic
Account Age = 1

Output:
Transaction Status = Flagged'''


amount=int(input("Enter the amount"))
location=input("Enter the location : (international/domestic)")
age=int(input("Enter the age"))
verify=input("Enter the OTP verification done(yes/no)").lower()
activity=input("Enter unusual activity :(yes/no)")

if amount>=10000:
    if location=="international":
         if verify=="yes":
            print("Allow")
    else:
        if amount>=50000:
             if age>=2:
                 print("allow")
             else:
                 print("flag")
else:
    if activity=="yes":
        print("flag")
    else:
        print("Allow")