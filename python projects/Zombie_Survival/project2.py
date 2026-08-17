import random
game=True
while game:
    
    print("+--------------------------------+")
    print("|   Welcome To Zombie Survival   |")   
    print("+--------------------------------+")
    print("                                  ")
    
        

    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    p_score=0
    z_score=0
    turn=0
    
    difficulty=int(input("Enter difficulty level : "))
    if difficulty == 1:
        p_health = 100
        z_health = 80
        medikit = 4

    elif difficulty == 2:
        p_health = 100
        z_health = 100
        medikit = 3

    elif difficulty == 3:
        p_health = 100
        z_health = 120
        medikit = 2
    while game:
        print("+---------------------+")
        print("|   Zombie Survival   |")   
        print("+---------------------+")
        print("                       ")

 
        print("1. Attack")
        print("2. Use Medikit")
        print("3. Check Status") 
        print("4. Score")
        print("5. Run Away")
        print("6. Exit")
        choice=int(input("Enter your choice : "))       
        match choice:
            case 1:
                 p_damage=random.randint(10,25)
                 z_damage=random.randint(15,30)
                 z_health=z_health-p_damage
                 p_score+=p_damage
                 z_score+=z_damage
                 turn+=1
                 p_health=p_health-z_damage
                 if z_health<=0:
                     print("+--------------------------+")
                     print("| Congratulations You Win! |")
                     print("+--------------------------+")
                    
                     x=input("do you want to continue(yes/no)").lower()
                     if x=="yes":
                         break
                     else:
                         game=False
                      
                     
                 
                 elif p_health<=0:
                    print(" +-----------------+ ")
                    print(" |   Zombie Won    | ")
                    print(" +-----------------+ ")
                    print("                    ")

                    print("******TRY AGAIN******")
                    x=input("do you want to continue(yes/no)")
                    if x=="yes":
                         break
                    else:
                         game=False
              
                 else:
                    print("Player Health :",p_health)
                    print("Zombie Health :",z_health)
                    print("=========================")
                    print("                         ")
                    
            case 2:
                  if medikit<=0:
                     print("no medikit Available")
                  else:
                     medikit=medikit-1
                     p_health+=25
                     print("player health after medikit :",p_health)

                     print("Remaining medikit are : ",medikit)
                  print("=========================")
                  print("                         ")
            case 3:
                  print("player helath :",p_health)
                  print("Zombie health :",z_health)
                  print("medikit left :",medikit)
                  if turn%2!=0:
                      print("current turn is :zombie ")
                  else:
                      print("current turn is : player")
                  #print("current turn :",turn)
                  print("=========================")
                  print("                         ")
            case 4:
                  print("Total damage from player side : ",p_score)
                  print("Total damage from zombie side : ",z_score)
                  print("=========================")
                  print("                         ")

            case 5:
                  print("you run away from zombie")
                  print("Zombie Wins!")
                  print("Game over......")
                  break
                  #game=False
                  
                 
            case 6:
                  print("exit the game")
                  print("Thank you for visiting")
                  game=False
                 
                  
   
     