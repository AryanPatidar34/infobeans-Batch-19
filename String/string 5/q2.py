'''
2.
Find the Most Frequently Occurring Word
News Channel Keyword Analyzer

A news agency analyzes breaking news headlines to identify the most repeated keyword in a report.

Write a Python program to find the word with the highest frequency.

Input:
india won the match and india created history
Output:
india

'''

n=input("Enter your string")
words=n.split()
count=0
i=0
while i<len(words):
    w=words[i]
    c=n.count(w)
    if c>count:
        count=c
        ch=words[i]
    i+=1

print(ch," ",count)


    
