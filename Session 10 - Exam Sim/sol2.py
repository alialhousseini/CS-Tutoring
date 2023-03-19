with open("fantafoot.txt") as player:
    data= player.readlines()
    for i in range(len(data)):
        data[i] = data[i].rstrip()
        data[i] = data[i].split(",")
        for j in range(len(data[i])):
            data[i][j]=data[i][j].replace(" ","")


goalkepper = []
defender = []
midfielder = []
striker = []
finallist = []
for i in range(len(data)):
    if data[i][2] == "goalkeeper" :
        goalkepper.append(data[i])
    elif data[i][2] == "defender" :
        defender.append(data[i])
    elif data[i][2] == "midfielder" :
        midfielder.append(data[i])
    elif data[i][2] == "forward" :
        striker.append(data[i])

print(goalkepper)
goalkepper.sort(key = lambda x: x[3], reverse=True)
defender.sort(key = lambda x: x[3], reverse=True)
midfielder.sort(key = lambda x: x[3], reverse=True)
striker.sort(key = lambda x: x[3], reverse=True)

finalgoalkepper = []
finaldefender = []
finalmidfielder = []
finalstriker = []
def chosing(position, player, price):
    finallist =[]
    budget = price - player
    remaining = 0
    for i in range(len(position)):
        value = int(position[i][3])
        if  value <= budget and budget>0 and player>-1:
            finallist.append(position[i])
            budget = budget - value
            budget +=1
            player -=1
    print (f"{position}" + ": ")
    for i in range(len(finallist)):
        print(f"{finallist[i][0]}" + " " + f"{finallist[i][3]}")



chosing(goalkepper, 3, 20)
chosing(defender,8,80)
chosing(midfielder, 8, 80)
chosing(striker,6,120)