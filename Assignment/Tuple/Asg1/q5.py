'''
=====================================================================
QUESTION 5: LIBRARY BOOK RECORDS
================================

A library maintains book information using NamedTuple.

Fields:
book_id, title, author, price

Requirements:

1. Read N book records from the user and store them in a list of NamedTuples.

---

2. Display all book details.

---

3. Find and display the most expensive book.

---

4. Search books by author name.

---

5. Calculate and display the average price of all books.

---

Test Case:

Input:
Enter number of books: 4

B101 Python Basics John 450
B102 Java Programming James 550
B103 Data Science John 700
B104 SQL Guide Smith 300

Enter Author Name: John

Expected Output:
Most Expensive Book:
B103 Data Science John 700

Average Book Price:
500.0

Books Written By John:
B101 Python Basics John 450
B103 Data Science John 700
'''
from collections import namedtuple
library=namedtuple("basic",["book_id","title","author","price"])
n=int(input("Enter number of books : "))
arr=[]
for i in range(n):
    id=input("Enter id : ")
    title=input("Enter title : ")
    a=input("Enter author name : ")
    p=int(input("Enter price : "))
    arr.append(library(id,title,a,p))
high=arr[0]
au=input("Enter author name")
sum=0
for i in arr:
    sum+=i.price
    if i.author==au:
        if i.price>high.price:
            high=i
    print(i.book_id,i.title,i.author,i.price)
print("Most Expensive Book :")
print(high.book_id,high.title,high.author,high.price)
print("Average book price :",sum/n)
for i in arr:
    if i.author==au:
        print(i.book_id,i.title,i.author,i.price)

