'''
4.
Employee ID Validator

A company wants to validate employee IDs before storing them in the database.

Conditions:
- ID must start with "EMP"
- Total length should be 8
- Remaining characters should be digits only

Input:
Enter Employee ID: EMP10234

Output:
Valid Employee ID
'''
'''
n=input("Enter your ID")
if len(n)<8 and len(n)>8:
    print("invalid ID")
else:
    if(n.startswith("EMP")):
    
        i=3
        while i<len(n):
            ch=n[i]
            if ch in '0123456789':
                pass
            else:
                print("invalid")
                break
            i+=1
        else:
            print("valid")
    else:
        print("invalid due to starting string")
  '''

n=input("Enter your ID")
if len!=8:
    print("invalid ID1")
else:
           if n[0]=="E" and n[1]=="M" and n[2]=="P":
               i=3
               while i<len(n):
                    ch=n[i]
                    if ch in '0123456789':
                       pass
                    else:
                        print("invalid2")
                        break
                    i+=1
               else:
                    print("valid")
           else:
                print("invalid due to starting string")  



    
    
    
         