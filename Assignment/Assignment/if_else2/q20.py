"""5. Smart Warehouse Dispatch System

A warehouse decides dispatch strategy based on stock availability, priority level, and delivery distance.

If stock is at least 100, then check priority. If high priority, then check distance. If distance is up to 200, dispatch immediately; otherwise use fast courier. If priority is not high, then check if stock is at least 300. If yes, bulk dispatch; otherwise normal dispatch. If stock is less than 100, then check if stock is at least 50. If yes, and priority is high, partially dispatch; otherwise hold. If stock is below 50, mark out of stock.

Input:
Stock = 120
Priority = high
Distance = 300

Output:
Dispatch Status = Dispatch via Fast Courier"""


stock = int(input("Enter stock"))
level =input("Enter Level:(high/low)").lower()
distance = int(input("Enter distance:"))

if stock>=100:
    if level=='high':
        if distance<=200:
            print(" Dispatch Status :dispatch immediately")
        else:
            print("Dispatch Status :fast courier")
    else:
        if stock>=360:
            print("Dispatch Status :bulk dispatch")
        else:
            print("Dispatch Status :normal dispatch")
elif stock>=50:
     if level=='high':
          print("Dispatch Status :partially dispatch")
     else:
          print("Dispatch Status :hold") 
else:
    print("Dispatch Status :out of stock") 
