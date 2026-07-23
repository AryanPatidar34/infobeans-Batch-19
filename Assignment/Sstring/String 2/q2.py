'''
2.
Mobile Number Digit Counter

A telecom company wants to count how many digits are present in a customer contact number entered with spaces or symbols.

Input:
Enter contact number: +91 98765-43210

Output:
Total digits: 12
'''

n=input("Enter your number")
count=0
for ch in n:
    if ch in '0123456789':
        count+=1
    elif ch==" ":
        continue
    elif ch=="-":
        continue
    else:
        break 
    

print("Total Digit :",count)
     

        