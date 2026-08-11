"""14. Online Course Fee System

An online platform offers courses with fixed fees:

* Programming → ₹5000
* Design → ₹4000
* Marketing → ₹3000
  Discount is applied based on user type:
* Student → 20% discount
* Working Professional → 10% discount
* Others → No discount

Write a Python program to calculate final course fee.

Input:
Enter course category: Programming
Enter user type: Student

Output:
Final Course Fee: ₹4000"""


course =input("Enter course category :(Programmig/Design/Marketing)").lower()
type = input("Enter user type:(Student/working_professional/other)").lower()

if course=="programming":
    if type=="student":
        Fee=5000-(5000*0.20)
        print("Final Course Fee :",Fee)
    elif type=="working_professional":
        Fee =5000-(5000*0.10)
        print("Final Course Fee:",Fee)
    else:
        print("no discount")
elif course=="design":
      if type=="student":
          Fee=4000-(4000*0.20)
          print("Final Course Fee:",Fee)
      elif type=="working_professional":
           Fee=4000-(4000*0.10)
           print("Final Course Fee:",Fee)
      else:
          print("no discount")
else:
     if type=="student":
         Fee=3000-(3000*20)
         print("Final Course Fee:",Fee)
     elif type=="working_professional":
          Fee=3000-(3000*0.10)
          print("Final Course Fee:",Fee)
     else:
         print("no discount")