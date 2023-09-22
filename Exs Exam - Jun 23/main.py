def readfile1(filename1):
    map=[]
    try:
        with open(filename1,'r') as file:
            data= file.readlines()
            for i in range(len(data)):
                data[i]=data[i].strip()
                mapline=[]
                for j in range(len(data[i])):
                    if data[i][j]=='#':
                        mapline.append('#')
                    else:
                        mapline.append('-')
                map.append(mapline)
                        
    except IOError or FileExistsError:
        print("File not found")
        
    return map

def readfile2(filename2, relation):
    moves = []
    try:
        with open(filename2,'r') as file:
            data= file.readlines()
            for i in range(len(data)):
                data[i]=data[i].strip().split(',')
                move = [relation[data[i][0]], int(data[i][1])]
                moves.append(move)
    except IOError or FileExistsError:
        print("File not found")
        
    return moves

def count_ships(map):
    count=0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j]=='#':
                count+=1
    return count

def main():
    try:
        filename1=input("Enter the name of the file for the battle map (player 1): ")
        map1 = readfile1(filename1)
    except IOError or FileExistsError:
        print("File not found")
        
    try:
        filename2=input("Enter the name of the file for the battle map (player 2): ")
        map2 = readfile1(filename2)
    except IOError or FileExistsError:
        print("File not found")
        
        
    relation={'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9}
    relation2={0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F',6:'G', 7:'H', 8:'I', 9:'J'}
    try:
        filename3=input("Enter the name of the file for the moves: ")
        moves  = readfile2(filename3, relation)
    except IOError or FileExistsError:
        print("File not found")
        
    count1 = count_ships(map1)
    count2 = count_ships(map2)
    
            
    for i,move in enumerate(moves):
        if i%2==0:
            x,y = move
            if map1[x][y]=='#':
                map1[x][y]='*'
                count1-=1
                print(f"Player 1 shot {relation2[move[0]]},{move[1]}: hit")
            else:
                map1[x][y]='o'
                print(f"Player 1 shot {relation2[move[0]]},{move[1]}: miss") 
        if i%2!=0:
            x,y = move
            if map2[x][y]=='#':
                map2[x][y]='*'
                count2-=1
                print(f"Player 2 shot {relation2[move[0]]},{move[1]}: hit")
            else:
                map2[x][y]='o'
                print(f"Player 2 shot {relation2[move[0]]},{move[1]}: miss")
        if count1==0 or count2==0:
            break
    
    print()
    
    print(f"THe games has ended!")
    print(f"Player 1 map")
    for i in range(len(map1)):
        for j in range(len(map1[i])):
            print(map1[i][j], end='')
        print()
    
    print()
    
    print(f"Player 2 map")
    for i in range(len(map2)):
        for j in range(len(map2[i])):
            print(map2[i][j], end='')
        print()   
    
            
            
        
        
    
    
    
    
    
    
main()