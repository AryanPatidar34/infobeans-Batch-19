'''
QNo 8:--
SMART TEXT PROCESSING SYSTEM

A software company is developing a Smart Text Processing System for
handling user messages. Different users require different text
transformations. To avoid creating separate applications, the company
wants a menu-driven program where users can select operations according
to their requirements.

The system should continue executing until the user selects Exit.

====================================================== MENU
======================================================

===== Smart Text Processing System =====

1.  Reverse Complete String
2.  Reverse Every Word
3.  Reverse Word Order
4.  Exit

====================================================== Choice 1 :

Conditions: - Reverse the complete string - Ignore extra spaces - Keep
special characters (@,#,$,%) in their original positions - Do not use
built-in reverse functions

Example: Input: ja@va#py

Output: yp@av#aj

Test Case 1: ab@cd#ef Output: fe@dc#ba

Test Case 2: py@th#on Output: no@ht#yp

Test Case 3: java@proOutput : orpa@vaj

====================================================== Choice 2 :

Conditions: - Reverse every word separately - Words containing digits
should not be reversed - Ignore extra spaces between words - First
letter of each reversed word should become uppercase

Example: Input: java is easy123 programming

Output: Avaj Si easy123 Gnimmargorp

Test Case 1: python full stack22 developer Output: Nohtyp Lluf stack22
Repoleved

Test Case 2: hello java99 world Output: Olleh java99 Dlrow

====================================================== Choice 3 :

Conditions: - Reverse order of words - Remove duplicate words - Ignore
case while checking duplicates - Keep only first occurrence

Example: Input: Java python Java react Python

Output: React Python Java

Test Case 1: HTML CSS HTML Java CSS Output: Java CSS HTML

Test Case 2: Python React Java Python React Output: Java React Python

====================================================== Choice 4
======================================================

Program Closed Successfully
'''
while True:
    print("=========Smart Processing System=========")
    print("                                         ")
    print("                                         ")
    print("1.  Reverse Complete String")
    print("2.  Reverse Every Word")
    print("3.  Reverse Word Order")
    print("4.  Exit")
    choice=int(input("Enter your choice"))
    match choice:
         case 1:
               n=input("Enter your string")
               temp=""
               rev="" 
               res=""
               for ch in n:
                   if ch>='a' and ch<='z' or ch>='A' and ch<='Z':
                        temp+=ch
               i=-1
               while i>=-len(temp):
                   ch=temp[i]
                   rev+=ch 
                   i-=1
             
               j=0
               while j<len(n):
                   ch=n[j]
                   if ch=='%' or ch=='#' or ch=='@' or ch=='$':
                       res+=ch
                   else:
                      if ch>='a' and ch<='z' or ch>='A' and ch<='Z':
                           res+=rev[j]
                           j+=1
                   i+=1
               
               print(res)
               print("                   ")
               print("                   ")
       
         case 2:
               n=input("Enter your sentence : ")
               words=n.split()
               final=""
               i=0
               while i<len(words):
                   w=words[i]

                   if (any(ch.isdigit() for ch in w)):
                           final=final+w+" "

                   elif w.isalpha():
                       res=""
                       j=-1
                       while j>=-len(w):
                           res=res+w[j]
                           j-=1
                       final+=res.capitalize()+" "
                   
                   i+=1
               print(final)
               

         case 3:
               n=input("Enter your String : ")
               words=n.split()
               res=""
               for i in range(0,len(words)-1):
                    w=words[i]
                    if w not in res:
                        res+=w+" "
               print(res)
                       
                                               
         case 4:
               print("Exit")
               break