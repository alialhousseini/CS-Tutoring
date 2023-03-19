# Constants for the number of players needed for each role
GOALKEEPERS = 3
DEFENDERS = 8
MIDFIELDERS = 8
FORWARDS = 6

# Constants for the budget allocated for each role
GOALKEEPER_BUDGET = 20
DEFENDER_BUDGET = 40
MIDFIELDER_BUDGET = 80
FORWARD_BUDGET = 120

# Read players information from the file and store it in a list of dictionaries
players = []
with open('fantafoot.txt', 'r') as file:
    data=file.readlines()
    for i in range(len(data)):
        data[i]=data[i].rstrip().split(',')
        for j in range(len(data[i])):
            data[i][j]=data[i][j].strip()
            if j==3:
                data[i][j]=int(data[i][j])
        d=dict()
        d['name']=data[i][0]
        d['team']=data[i][1]
        d['role']=data[i][2]
        d['price']=data[i][3]
        players.append(d)


# Sort the players by price
players.sort(key=lambda x: int(x['price']), reverse=True)

print(players)
# Initialize the budget and number of players for each role
budget = {'goalkeeper': GOALKEEPER_BUDGET, 'defender': DEFENDER_BUDGET, 'midfielder': MIDFIELDER_BUDGET, 'forward': FORWARD_BUDGET}
players_needed = {'goalkeeper': GOALKEEPERS, 'defender': DEFENDERS, 'midfielder': MIDFIELDERS, 'forward': FORWARDS}

# Initialize the lists to store the purchased players for each role
purchased_players = {'goalkeeper': [], 'defender': [], 'midfielder': [], 'forward': []}

# Iterate through the list of players
for player in players:
    role = player['role']
    price = player['price']
    #print(role)
    if price <= budget[role] and budget[role] - price >= players_needed[role] -1:
        budget[role] -= price
        players_needed[role] -= 1
        purchased_players[role].append(player)
    if players_needed[role] == 0:
        players_needed[role]=0
        budget[role]=0
    if not players_needed or not budget:
        break

for role in purchased_players.keys():
    print(f"{role.capitalize()}: ",end=' ')
    for player in purchased_players[role]:
        print(f"{player['name']} {player['price']}",end=' ')
    print()
