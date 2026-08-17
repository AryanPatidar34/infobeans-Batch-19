'''
82Create a string from a character array.
 Char[] = {'h', 'i'}
 "hi"
'''
n=list(input("Enter character").split())
'''
arr=[]
for i in range(n):
    ch=input("Enter element")
    arr.append(ch)
print(arr)
'''
print(n)
res=""
for i in n:
    res+=i
print(res)