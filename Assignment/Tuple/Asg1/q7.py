'''
7.

A cricket academy wants to analyze player performance. Each player's information is stored as a tuple.

Tuple Format:

(player_id, player_name, runs_scored)

Requirements:

Read N player records from the user and store them as tuples in a list.
Display all player records.
Find and display the player who scored the highest runs.
Find and display the player who scored the lowest runs.
Calculate and display the total runs scored by all players.
Calculate and display the average runs scored.
Display players who scored more than 50 runs.

Test Case:

Input:

Enter number of players: 5

101 Virat 82
102 Rohit 45
103 Gill 120
104 Hardik 38
105 SKY 76

Expected Output:

All Players:
(101, 'Virat', 82)
(102, 'Rohit', 45)
(103, 'Gill', 120)
(104, 'Hardik', 38)
(105, 'SKY', 76)

Highest Scorer:
(103, 'Gill', 120)

Lowest Scorer:
(104, 'Hardik', 38)

Total Runs:
361

Average Runs:
72.2

Players Scoring More Than 50 Runs:
(101, 'Virat', 82)
(103, 'Gill', 120)
(105, 'SKY', 76)

'''
n=int(input("Enter number of student : "))
arr=[]
for i in range(n):
    id=int(input("Enter the id of student"))
    name=input("Enter the name : ")
    marks=int(input("Enter marks : "))
    t=(id,name,marks)
    arr.append(t)
print("All palyers :")    
print(*arr)
print()
high=arr[0]
low=arr[0]
sum=0
for i in range(len(arr)):
    sum+=arr[i][2]
    if arr[i][2]>high[2]:
        high=arr[i]
    if arr[i][2]<low[2]:
        low=arr[i]
print("Highest marks :",high[0],high[1],high[2])
print()
print("Lowest marks :",low[0],low[1],low[2])
print()
print("Players Scoring More Than 50 runs :")
print("Average Runs :",sum/n)
print()
for i in range(len(arr)):
    if arr[i][2]>50:
        print(arr[i])
        
       