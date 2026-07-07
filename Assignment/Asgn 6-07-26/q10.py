'''
10.
Electricity Bill Processing System (Multi-House)

An electricity board processes bills for multiple houses in a society.

Write a program to:

- Read number of houses n
- For each house:
    - Read units consumed
    - Calculate bill using slab rates:

        First 100 units      → ₹5 per unit  
        Next 100 units      → ₹7 per unit  
        Above 200 units     → ₹10 per unit  

    - Apply conditions:
        - If bill > ₹2000 → add 10% surcharge  
        - If units < 50 → give ₹100 subsidy  

    - Print bill for each house

- After processing all houses:
    - Print total bill collected
    - Print highest bill

---

Input:
3
120
250
40

Output:
House 1 Bill = 640
House 2 Bill = 1700
House 3 Bill = 100

Total Collection = 2440
Highest Bill = 1700'''

highest=0
sum=0
n=int(input("Enter number of houses"))
for i in range(n):
    u=int(input("Unit : "))
    if u<=100:
        bill=u*5
    elif u<200:
        bill=(u-100)*7+100*5
    else:
        bill=((u-200)*10+100*5+100*7)
    
    if bill>2000:
        bill=bill+bill*10/100
    if u<50:
        bill=bill-100
    print("bill with subsidy :",bill)
    if bill>highest:
        highest=bill
    sum=sum+bill
print("Highest bill :",highest)
print("Total bill :",sum)    




    
    
