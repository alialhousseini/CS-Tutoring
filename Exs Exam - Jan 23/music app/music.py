# https://t.me/+ioeaOw89DgxjOTE8

def readfile(filename):
    try:
        with open(filename,'r') as file:
            data = file.readlines()
            for i in range(len(data)):
                data[i]=data[i].rstrip().split(';')
                for j in range(len(data[i])):
                    data[i][j]=data[i][j].strip()

    except FileExistsError or FileNotFoundError:
        print('error')

    return data

def main():
    songs = readfile('Music.dat')
    users = readfile('Users.dat')
    for i in range(len(users)):
        print(f"{users[i][0]}")
        filtered1 = list(filter(lambda x: users[i][1] in x,songs))
        mapped1 = list(map(lambda x: x[0],filtered1))
        filtered2 = list(filter(lambda x: users[i][2] in x,songs))
        mapped2 = list(map(lambda x: x[0],filtered2))
        for j in range(len(mapped1)):
            print(f"- {mapped1[j]}")
        for k in range(len(mapped2)):
            if mapped2[k] not in mapped1:
                print(f"- {mapped2[k]}")

main()