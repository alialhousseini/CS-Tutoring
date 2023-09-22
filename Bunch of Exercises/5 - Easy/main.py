def readfile(filename):
    with open(filename,'r') as file:
        data = file.readlines()
        for i in range(len(data)):
            data[i]=data[i].rstrip().split(';')
            
    return data

def main():
    filename1 = '.\\5 - Easy\\database_atleti.txt'
    filename2 = '.\\5 - Easy\\risultati_gara.txt'
    
    players = readfile(filename1)
    results = readfile(filename2)
    
    #print(players)
    #print(results)
    
    for result in results:
        for player in players:
            if player[0] in result:
                result.append(player[1])
                
    #print(results)
    
    for result in results:
        pace = float(result[4])/10
        temp = round(pace - int(pace),2)
        #print(temp)
        if len(str(temp))-2 == 1:
            temp*=0.6
            pace = float(int(pace)) + temp
        result.append(pace)
        
    male = list(filter(lambda x: x[3]=='M',results))
    female = list(filter(lambda x: x[3]=='F', results))
    
    print("PARTICIPANTS RANKING\n")

    print("Category: M")
    for p in male:
        print(f"{p[0]} {p[1]}, {p[-1]} min/km")    

    print()
    
    print("Category: F")
    for p in female:
        print(f"{p[0]} {p[1]}, {p[-1]} min/km")
    
    print()
    
    print("ATHLETES WHO BEAT THEIR PERSONAL RECORD\n")
    
    for p in results:
        if float(p[-2])>p[-1]:
            print(f"{p[0]} {p[1]}")
            
        
    
main()