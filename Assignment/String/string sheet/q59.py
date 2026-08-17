'''
59Rotate characters by 3 positions to the right. 
S = "abcde" 
"cdeab"
'''
s=input("Enter string")
res=""
n=int(input("how many times"))
#rot=s[len(s)-n:]
rot=s[:len(s)-n]
print("rot",rot)
#temp=s[:len(s)-n]
temp=s[len(s)-n:]
print("temp",temp)
#print(temp)
#res=rot+temp
res=temp+rot
print(res)



