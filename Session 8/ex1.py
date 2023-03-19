def convert_date(date): #27/11/1920 or 21/03 without a year
    return date[3:5]+date[0:2]

def readfile(filename):
    try:
        with open(filename,'r') as file:
            data = file.readlines()
            for i in range(len(data)):
                data[i]=data[i].rstrip().split(',')
                data[i][3] = convert_date(data[i][3])
    except FileExistsError:
        print('Error')

    return data

def read_zodiac(filename):
    try:
        goals = {}
        with open(filename,'r') as file:
            zodiac = file.readlines()
            for i in range(len(zodiac)):
                zodiac[i]=zodiac[i].rstrip().split(',')
                zodiac[i][1] = convert_date(zodiac[i][1])
                zodiac[i][2] = convert_date(zodiac[i][2])
                goals[zodiac[i][0]] = 0
    except FileExistsError:
        print('error')

    return zodiac,goals

def player_zodiac(date,zodiac):
    if date >= zodiac[1] and date<= zodiac[2]:
        return  True
    return False


def main():
    players = readfile('sportivi.txt')
    zodiac, goals = read_zodiac('zodiaco.txt')
    maxx=0
    for i in range(len(zodiac)):
        filtered = list(filter(lambda x:player_zodiac(x[3],zodiac[i]),players))
        sum_goals = sum(list(map(lambda x: int(x[1]),filtered)))
        if sum_goals>maxx:
            maxx=sum_goals
        goals[zodiac[i][0]]=sum_goals

    for s in sorted(goals,key=lambda x: goals[x],reverse=True):
        astrisks = '*' * int((50 * goals[s]) / maxx)
        print(f"{s} ({goals[s]}) {astrisks}")

main()