def readrows(filename):
    rows=[]
    with open(filename,'r') as file:
        data = file.readlines()
        for i in range(len(data)):
            data[i]=data[i].strip().split(',')
            for j in range(len(data[i])):
                data[i][j]=int(data[i][j].strip())
            row = {}
            row['umbrellas']=data[i][0] 
            row['umbrella_cost']=data[i][1]
            row['chairs']=data[i][2]
            row['chair_cost']=data[i][3]  
            row['customers']=[]   
            rows.append(row)
    return rows

def readentries(filename):
    with open(filename,'r') as file:
        data = file.readlines()
        for i in range(len(data)):
            data[i]=data[i].strip().split(',')
            for j in range(1,len(data[i])):
                data[i][j]=int(data[i][j].strip())
    return data


def main():
    filename1= '.\\6 - Hard\\stabilimento.txt'
    filename2= '.\\6 - Hard\\ingressi-uscite.txt'
    
    rows = readrows(filename1)
    entries = readentries(filename2)
        
    print(rows)
    print(entries)

    total_earnings=0
    for entry in entries:
        name = entry[0]
        if len(entry) !=1:
            umb = entry[1]
            chrs = entry[2]
            budget = entry[3]
            flag=0
            for i, row in enumerate(rows):
                total_umb = umb*row['umbrella_cost']
                total_chrs = chrs*row['chair_cost']
                total_possible = total_chrs + total_umb
                if umb<=row['umbrellas'] and chrs<=row['chairs'] and total_possible<=budget:
                    flag=1
                    row['umbrellas']-=1
                    row['chairs']-=1
                    row['customers'].append(name)
                    total_earnings+=total_possible
                    print(f"Customer {name} is in row {i+1}")
                    break
            if flag==0:
                print(f"Customer {name} didn't find a spot")
                
        else:
            for i, row in enumerate(rows):
                if name in row['customers']:
                    row['customers'].remove(name)
                    print(f"Customer {name} has left")
                    break
    print(f"Today's earnings {total_earnings}")
            
    
main()
