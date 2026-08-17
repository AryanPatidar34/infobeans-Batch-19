'''
10
Trim leading, trailing, or extra spaces. 
S = "  hello  world  "
 "hello world"
'''
n=input("enter string")
clean=" ".join(n.split())
print(clean)