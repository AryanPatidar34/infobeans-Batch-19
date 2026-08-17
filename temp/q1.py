
'''
peak element 
'''

n=int(input("Enter size"))
arr=[]
print("Enter element")
for i in range(n):
    arr.append(int(input()))
peakindex=-12
for i in range(n):
    if i==0:
        if n==1 or arr[i]>=arr[i+1]:
             peakindex=i
             break
    elif i==n-1:
        if arr[i]>=arr[i-1]:
            peakindex=i
            break
    else:
        if arr[i]>=arr[i-1] and arr[i]>=arr[i+1]:
            peakindex=i
            break
if peakindex!=-12:
    print("index",peakindex)
    print("value",arr[peakindex])
else:
    print(" no peak found")
        