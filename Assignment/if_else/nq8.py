"""
8. A warehouse management system needs to identify the highest stock level among six different storage units to prioritize dispatch.
 The system should take the quantity of items stored in six units as input. It should compare all six values using nested conditions
 and determine which unit has the maximum stock. Display the highest stock value among all six units.

Input:
Unit1 = 120
Unit2 = 450
Unit3 = 300
Unit4 = 275
Unit5 = 500
Unit6 = 390

Output:
Highest Stock = 500
"""

U1 = int(input("Enter unit 1 "))
U2 = int(input("Enter unit 2 "))
U3 = int(input("Enter unit 3 "))
U4 = int(input("Enter unit 4 "))
U5 = int(input("Enter unit 5 "))
U6 = int(input("Enter unit 6 "))



if U1>U2:
    if U1>U3:
        if U1>U4:
            if U1>U5:
                if U1>U6:
                    print("Highest stock ",U1)
                else:
                    print("Highest stock ",U6)
            else:
                if U5>U6:
                    print("Highest stock ",U5)
                else:
                    print("Highest stock ",U6)
        else:
            if U4>U5:
                if U4>U6:
                    print("Highest stock ",U4)
                else:
                    print("Highest stock ",U6)
            else:
                if U5>U6:
                    print("Highest stock ",U5)
                else:
                    print("Highest stock ",U6)
    else:
         if U3>U4:
             if U3>U5:
                  if U3>U6:
                      print("Highest stock ",U3)
                  else:
                      print("Highest stock ",U6)
             else:
                 if U5>U6:
                         print("Highest stock ",U5)
                 else:
                     print("Highest stock ",U6)
         else:
              if U4>U5:
                  if U4>U6:
                      print("Highest stock ",U4)
                  else:
                      print("Highest stock ",U6)
              else:
                  if U5>U6:
                        print("Highest stock ",U5)
                  else:
                       print("Highest stock ",U6)
       
else:
     if U2>U3:
        if U2>U4:
            if U2>U5:
                if U2>U6:
                    print("Highest stock ",U2)
                else:
                    print("Highest stock ",U6)
            else:
                 if U5>U6:
                     print("Highest stock ",U5)
                 else:
                     print("Highest stock ",U6)
        else:
            if U4>U5:
                if U4>U6:
                    print("Highest stock ",U4)
                else:
                    print("Highest stock ",U6)
            else:
                if U5>U6:
                    print("Highest stock ",U5)
                else:
                    print("Highest stock ",U6)
     else:
          if U3>U4:
              if U3>U5:
                  if U3>U6:
                      print("Highest stock ",U3)
                  else:
                      print("Highest stock ",U6)
              else:
                  if U5>U6:
                      print("Highest stock ",U5)
          else:
              if U4>U5:
                  if U4>U6:
                      print("Highest stock ",U4)
                  else:
                      print("Highest stock ",U6)
              else:
                   if U5>U6:
                       print("Highest stock ",U5)
                   else:
                       print("Highest stock ",U6)

             
                


    