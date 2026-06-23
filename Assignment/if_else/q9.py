"""
9. Library Access System
   A library checks:

* If membership is active → Entry allowed
* If books issued < 3 → Can issue more books

Input:
Membership active (yes/no): yes
Books issued: 2

Output:
Entry allowed
Can issue more books
"""

membership  = input("your membership is active(yes/no)").lower()
issued = int(input("Enter issued books"))
if membership=="yes":
    print("Entry allowed")
    if issued<3:
        print("can isssue more books")
else:
     print("your membership has ended")
