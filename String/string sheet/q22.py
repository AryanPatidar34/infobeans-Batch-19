'''
22Find the last repeating character.
 S = "abracadabra"
 r'
'''
s=input("Enter the string")
i=len(s)-1
while i>=0:
   ch=s[i]
   c=s.count(ch)
   if c==2:
      print(ch)
      break
   i-=1


