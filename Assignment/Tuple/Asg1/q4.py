'''
=====================================================================
QUESTION 4: ONLINE SHOPPING ORDERS
==================================

An online shopping company stores customer orders using NamedTuple.

Fields:
order_id, customer_name, product_name, amount

Requirements:

1. Read N order records from the user and store them in a list of NamedTuples.

---

2. Display all order details.

---

3. Find and display the order having the highest amount.

---

4. Calculate and display total sales.

---

5. Count the number of orders whose amount is greater than ₹10,000.

---

Test Case:

Input:
Enter number of orders: 5

O101 Rahul Laptop 55000
O102 Priya Mouse 800
O103 Amit Mobile 25000
O104 Neha Keyboard 1500
O105 Rakesh TV 45000

Expected Output:
Highest Value Order:
O101 Rahul Laptop 55000

Total Sales:
127300

Orders Above ₹10,000:
3
'''
from collections import namedtuple
shopping=namedtuple("basic",["order_id","customer_name","product_name","amount"])
n=int(input("Enter number of items : "))
arr=[]
for i in range(n):
    id=input("Enter id : ")
    cusn=input("Enter name of customer : ")
    pn=input("Enter age of prod name : ")
    a=int(input("Enter amount : "))
    arr.append(shopping(id,cusn,pn,a))
max=arr[0]
sum=0
c=0
for i in arr:
   sum+=i.amount
   if i.amount>10000:
       c+=1
   if i.amount>max.amount:
      max=i
   print()
   print(i.order_id,i.customer_name,i.product_name,i.amount)
print("Highest Value Order :",max.order_id,max.customer_name,max.product_name,max.amount)
print("Total sales :",sum)
print("orders Above 10000 : ",c)


