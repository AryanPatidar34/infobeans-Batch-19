'''
6. Find Occurrence of a Word in a String

Product Review Analysis System

An e-commerce company wants to analyze customer reviews.

The company wants a Python program to count how many times a particular word appears in a review.

Input Sentence:


iphone is good and iphone battery is strong


Word:


iphone


Output:


2
'''
n=input("Enter sentence : ")
w=input("Enter word : ")
c=0
v=0
temp=""
for ch in n:
    v+=1
    if ch>='a' and ch<='z':
        temp+=ch
    if ch==" " or v==len(n):
            if w==temp:
                 c+=1
            temp=""


            

print("total count of word :",c)


       
        
    
