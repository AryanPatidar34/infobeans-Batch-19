'''
8. Smart Farming Irrigation System

A farming system decides irrigation based on soil moisture, temperature, crop type, and rainfall prediction.

If soil moisture is 30 or below, then check temperature. If temperature is at least 35, then check crop type. If wheat, high water supply; otherwise moderate supply. If temperature is less than 35, moderate supply. If moisture is above 30, then check if it is up to 60. If yes, then check rainfall. If rain expected, delay irrigation; otherwise light irrigation. If moisture is above 60, no irrigation.

Input:
Soil Moisture = 25
Temperature = 36
Crop = wheat

Output:
Irrigation = High Water Supply'''


moist=int(input("Enter the moisture"))
temp=int(input("Enter the temperature"))
crop=input("crop type wheat(yes/no)").lower()
rainfall=input("Enter rain expected :(yes/no)").lower()

if moist<=30:
     if temp>=35:
         if crop=="yes":
             if rainfall=="no":
                 print("high water supply")
             else:
                 print("moderate supply")
     else: 
         print("moderate supply")
elif moist>60:
    print("no irregation")
else:
    if moist>30 and moist<60:
        if rainfall=="yes":
            print("dealy irregation")
        else:
            print("light irregation")
    