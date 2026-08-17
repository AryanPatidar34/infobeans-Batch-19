'''

6.

NOTE: using tuple only
An electronics store wants to maintain product information. Since product details should not be modified accidentally,
 each product record is stored as a tuple.

Tuple Format:

(product_id, product_name, price)

Requirements:

Read N product details from the user and store them as tuples in a list.
Display all product details.
Find and display the costliest product.
Find and display the cheapest product.
Calculate and display the average price of all products.
Display all products whose price is greater than ₹50,000.

Test Case:

Input:

Enter number of products: 4

P101 Laptop 65000
P102 Mobile 25000
P103 Television 80000
P104 Tablet 30000

Expected Output:

All Products:
('P101', 'Laptop', 65000)
('P102', 'Mobile', 25000)
('P103', 'Television', 80000)
('P104', 'Tablet', 30000)

Costliest Product:
('P103', 'Television', 80000)

Cheapest Product:
('P102', 'Mobile', 25000)

Average Price:
50000.0

Products Above ₹50,000:
('P101', 'Laptop', 65000)
('P103', 'Television', 80000)
'''
n=int(input("Enter product size"))
arr=[]
for i in range(n):
    id=int(input("Enter id : "))
    name=input("Enter prod name : ")
    price=int(input("Enter price"))
    prod=(id,name,price)
    arr.append(prod)
max=arr[0]
min=arr[0]
sum=0
for i in range(len(arr)):
       sum+=arr[i][2]
       if arr[i][2]>max[2]:
           max=arr[i]
       if arr[i][2]<min[2]:
           min=arr[i]           
       print(arr[i])
print(max[0],max[1],max[2])
print(min[0],min[1],min[2])
print("AVG :",sum/n)
for i in range(len(arr)):
    if arr[i][2]>50000:
        print(arr[i])



    
    
