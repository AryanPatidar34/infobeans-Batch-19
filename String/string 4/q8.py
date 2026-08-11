'''
8.
Find the Second Highest Repeating Character in a String

Social Media Trend Analysis System

A social media company analyzes hashtags and user comments to identify trending character patterns.

The analytics team wants a Python program to find the character with the second highest frequency in a given string.

This helps detect secondary trending patterns in user activity.

Input:

aaabbbbccddeee

Output:

e

Explanation:

b occurs 4 times → highest
e occurs 3 times → second highest

Condition:

Program should work for both uppercase and lowercase letters.
Spaces should be ignored.
If no second highest frequency exists, print:
Second highest repeating character not found
'''

n=input("Enter your String").replace(" ","")      #aaabbbbccddeee
lar=""
sl=""
temp=""
i=0
slc=0
larc=0
while i<len(n):
    ch=n[i]
    if ch not in temp:  
       temp+=ch    #aaabbbccceeeeffff
       j=0
       c=0
       while j<len(n):
            cj=n[j]
            if ch==cj:
                c+=1
            j+=1
       if c>=larc:
             if c==larc:
                 lar=ch
                 larc=c
             else:
                 slc=larc
                 sl=lar
                 lar=ch
                 larc=c
            
                 
       else:
           if c>=slc and c<larc:
              slc=c
              sl=ch
    i+=1
    
print(lar,"occurs",larc,"times -> highest")
if slc==0:
    print("second highest no found")
else:
    print(sl,"occurs",slc,"times-> second highest")
