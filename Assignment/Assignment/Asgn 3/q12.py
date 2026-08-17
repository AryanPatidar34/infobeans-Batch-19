amount = int(input("Enter total amount : "))
note_100 = amount//100
amount_rem = amount%100
note_50 = amount_rem//50
amount_rem1 = amount_rem%50
note_10=amount_rem1//10
print("100 notes is  : ",(note_100),"50 notes is : ",(note_50),"10 note is : ",(note_10))
