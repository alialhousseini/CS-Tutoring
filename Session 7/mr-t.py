
def delta(player_1, player_2):
    return 1 / (1 + 2**((player_1 - player_2) / 100))

def read_players(filename):
    players={}
    try:
        with open(filename,'r') as file:
            data = file.readlines()
            for i in range(1,len(data)):
                data[i]=data[i].rstrip()
                data[i]=data[i].split(',')
                data[i][1]=int(data[i][1])
                players[data[i][0]]=data[i][1]
    except IOError:
        print('Error!')
        exit(0)

    return players

def perform_games(filename,players):
    try:
        with open(filename,'r') as file:
            data=file.readlines()
            for i in range(1,len(data)):
                data[i] = data[i].rstrip()
                data[i] = data[i].split(',')
                #now we start performing the games and change our results
                player1 = data[i][0]
                player2 = data[i][1]
                result = data[i][2]

                if player1 not in players:
                    players[player1]=1500
                if player2 not in players:
                    players[player2]=1500

                if result == '1-0':
                    d=delta(players[player1],players[player2])
                    players[player1] += round(d*200)
                    players[player2] -= round(d*200)

                if result == '0-1':
                    d=delta(players[player2],players[player1])
                    players[player1] -= round(d*200)
                    players[player2] += round(d*200)

    except IOError:
        print('Error!')
        exit(0)

    return players

def main():
    players = read_players('players-short.csv')
    players = perform_games('games-short.csv',players)
    #print(players)

    for s in sorted(players,key=lambda x: players[x],reverse=True):
        print(f"{s}: {players[s]}")

if __name__ == '__main__':
    main()