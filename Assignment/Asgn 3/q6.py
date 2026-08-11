total_amount =int(input("Enter total amount : "))
discount_perc = int(input("Enter discount : "))
discount = total_amount*discount_perc/100
final_price = total_amount-discount
print("Final value is : " , (final_price))