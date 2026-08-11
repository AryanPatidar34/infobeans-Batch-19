'''
70Compare the number of times 'the' and 'is' appear.
 S = "the cat is on the mat"
 the: 2, is: 1 (theis)
'''
s=input("Enter the string").split()
w1=input("Enter the word1")
w2=input("Enter the word2")
w1c=0
w2c=0
for i in s:
    if i==w1:
        w1c+=1
    elif i==w2:
        w2c+=1

print("the :",w1c,",","is :",w2c)