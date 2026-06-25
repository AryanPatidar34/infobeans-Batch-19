"""1. Insurance Claim Approval System

An insurance company processes claims based on policy age, claim amount, and accident type. The approval depends on multiple levels of verification to reduce fraud.

If the policy age is at least 2 years, then check the claim amount. If the claim amount is up to 50000, then check the accident type. If it is minor, approve the claim; otherwise, approve it with inspection. If the claim amount is between 50001 and 200000, then check the accident type. If it is major, approve with investigation; otherwise reject. If the claim amount exceeds 200000, reject. If the policy age is less than 2 years, then check accident type. If minor, reject; otherwise mark as pending review.

Input:
Policy Age = 3
Claim Amount = 120000
Accident Type = major

Output:
Claim Status = Approved with Investigation"""

age = int(input("Enter your age"))
amount = int(input("Enter amount"))
type = input("Enter type:(Major/Minor)").lower()

if age>=2:
    if amount<=50000:
        if type=="minor":
            print("approve the clam")
        else:
            print("approved it with inpection")
    elif amount>=50001 and amount<=200000:
        if type=="major":
            print("approved with investigation")
        else:
            print("rejected")
elif amount>200000:
    print("rejected")
elif age<2:
     if type=="minor":
         print("rejected")
     else:
         print("pending review")
    
        
