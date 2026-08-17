'''
62Count vowels and consonants. 
S = "apple" Vowels: 2,
 Consonants: 3
'''
s=input("Enter string")
vol=0
con=0
for i in s:
    if i in 'aeiou':
        vol+=1
    else:
        con+=1
print("Vowel :",vol)
print("Consonants :",con)