amount = int(input("Enter amount: "))

ten_rupee = amount // 10
remaining = amount % 10
five_rupee = remaining // 5

print("₹10 x", ten_rupee)
print("₹5 x", five_rupee)