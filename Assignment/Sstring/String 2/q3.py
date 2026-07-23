'''
3.
Word Counter in Complaint Message

A customer care system wants to count how many words are present in a complaint message.

Input:
Enter complaint: Delivery was delayed again today

Output:
Total words: 5
'''

n=input("Enter your sentance")
count=1
for ch in n:
    if ch>='a' and ch<='z' or ch>='A' and ch<='Z':
        continue
    elif ch==" ":
        count=count+1



print("Total words : ",count)
          
    
  