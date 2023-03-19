def readfile(filename):
    try:
        with open(filename,'r') as file:
            data= file.readlines()
            for i in range(len(data)):
                data[i]=data[i].rstrip().split(';')
                for j in range(len(data[i])):
                    if j>=2:
                        data[i][j]=int(data[i][j])

    except FileExistsError:
        print('error')

    return data

def main():
    scores=readfile('bowling.txt')
    for player in sorted(scores,key=lambda x: sum(x[2:]),reverse=True):
        print(f"{player[0]} {player[1]} {sum(player[2:])}")
    max_tens=max(scores,key=lambda x: x[2:].count(10))
    max_zeros = max(scores,key=lambda x: x[2:].count(0))
    print(f"{max_tens[0]} {max_tens[1]} has knocked down all the pins {max_tens.count(10)} times")
    print(f"{max_zeros[0]} {max_zeros[1]} has missed all the pins {max_zeros.count(0)} time")


main()