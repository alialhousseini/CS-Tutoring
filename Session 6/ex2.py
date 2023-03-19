
def readfile(filename):
    with open(filename,'r') as file:
        data=file.readlines()
        for i in range(len(data)):
            data[i]=data[i].rstrip()

    return data



def take_inputs():
    coords = input("Please, enter the coordinates (x,y): ")
    xs, ys = coords.split(',')
    x , y =int(xs), int(ys)
    size = int(input("Please, enter the square size: "))
    return x,y,size

def main():
    data = readfile('landscape.txt')
    #print(data)
    x,y,size = take_inputs()
    rows = len(data)
    columns = len(data[0])
    #print(x,y,size,rows,columns)

    #check dimensions
    if x<=0 or x >= columns-size or y<=0 or y>=rows-size:
        print("ERROR! The square is out of limits.")
        exit(1)

    stats = {}
    for r in range(y,y+size):
        for c in range(x,x+size):
            symbol = data[r][c]
            if symbol not in stats:
                stats[symbol]=0
            stats[symbol]+=1

    #print(stats)

    for s in sorted(stats,key=lambda x: stats[x],reverse=True):
        print(f"{s}-> {stats[s]/size/size*100}%")

if __name__ == '__main__':
    main()