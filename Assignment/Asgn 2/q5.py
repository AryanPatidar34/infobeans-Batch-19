cart = float(input("Enter cart total amount: "))

tax = cart * 12 / 100
total = cart + tax

print("Tax = ₹", tax)
print("Total = ₹", total)