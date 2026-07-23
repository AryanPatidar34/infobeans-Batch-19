capacity=int(input("Enter Tank Capacity : "))
if capacity<0:
    print("please enter valid capacity")
else:
#cur_level=int(input("Enter Current Water Level : "))
    fill=0
    used=0
    total_fill=0
    total_used=0
    total_leakage=0
    total_overflow=0
    leak=0
    overflow=0
    count=0
    cur_level=0
    space=0
    while True:
        print("===================================")
        print("      WATER MANAGEMENT SYSTEM      ")
        print("===================================")
        print("                                   ")
        print("1. Fill the tank")
        print("2. use water from the tank")
        print("3. check water level")
        print("4. Tank status")
        print("5. leakage")
        print("6. daily report")
        print("7. Exit")


        choice=int(input("Enter your choice : "))
        print("                                ")
        if choice>7 or choice<0:
            print("* * * * * * * * * * * * * * * ")
            print("* Please Choose Valid Choice* ")
            print("* * * * * * * * * * * * * * * ")
            print("                              ")
            print("                              ")
        match choice:
            case 1:
                  fill=int(input("Enter the amount of water to fill in tank :"))
                  cur_level+=fill
                  total_fill+=fill
                  if cur_level>capacity:
                      overflow=cur_level-capacity
                      cur_level-=overflow
                      total_overflow+=overflow
                  print("Tank overflowed! :",overflow)
              
                  print(f"Current water level: {cur_level}")
                  if cur_level==capacity:
                      print("+--------------+")
                      print(" Tank is full! |")
                      print("+--------------+")

            case 2:
                   used=int(input("Enter the amount of water you used : "))
                   if used<0:
                        print("invalid input format !")
                   else:
                        if used<=cur_level:
                            cur_level=cur_level-used
                            total_used+=used
                            count+=1
                            print("Current Water Level : ",cur_level)
                        
                        else:
                            print("**********************")
                            print("* Insufficient Water *")
                            print("**********************")
            case 3: 
                  space=capacity-cur_level
                  print("Current Water Level :",cur_level)
                  print("Available space in tank :",space)

            case 4: 
                  if cur_level==capacity:
                       print("Tank is full!")
                  elif cur_level>=75*capacity/100:
                       print("Tank is almost full")
                  elif cur_level>=50*capacity/100:
                       print("Tank is half full")
                  elif cur_level>=25*capacity/100:
                       print("Low water warning!")
                  elif cur_level==0:
                       print("Tank is empty!")
                  else: 
                       if cur_level<25*capacity/100:
                          print("tank is almost empty")

            case 5:
                  leakage=int(input("Enter the water leakage amount :"))
                  if leakage>cur_level:
                       print("*****************************************")
                       print("* leakage amount is greater than water! *")
                       print("*****************************************")
                   
                  else:
                      cur_level=cur_level-leakage
                      total_leakage+=leakage
                      print("current water level after leakage :",cur_level)


            case 6:
                  print("=====   Daily Report   ======   ")
                  print("                                ")
                  print("Total Capacity :",capacity)
                  print("Current Water Level:",cur_level)
                  print("Available Sapce :",space)
                  print("Total water filled :",total_fill)
                  print("Total water used :",total_used)
                  print("Total water leaked :",total_leakage)
                  print("Total overflow water:",total_overflow)
                  print("Total no. of times you water used:",count)

            case 7:
                  print("Exit the program")
                  print(" ===Thank you for visiting===")
                  break
               

