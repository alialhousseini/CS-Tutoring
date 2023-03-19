import csv

def read_journal(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        journals={}
        for i,row in enumerate(reader):
            if i!=0:
                journals[row[1]]=row[-1]
    for j in journals:
        if journals[j]=='N/A':
            journals[j]=0.0
        else:
            journals[j]=float(journals[j])

    return journals

def read_pubs(name):
    filename = name+'.csv'
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            pubs=[]
            for i,row in enumerate(reader):
                if i!=0:
                    if len(row[-1])==9:
                        pubs.append([row[-1],row[0]])
    except FileNotFoundError:
        print(f'File not found for author {name}')
        exit(0)
    return pubs

def main():
    journals = read_journal('journal_IF.csv')
    #print(journals)
    name = input("Enter the researcher's name: ")
    pubs = read_pubs(name)
    #print(pubs)

    sum=0
    for i in range(len(pubs)):
        if name in pubs[i][1]:
            sum+=journals[pubs[i][0]]

    print(f"Total IF for {name}: {round(sum,2)}")

    sum=0
    num=0
    for i in range(len(pubs)):
        if name in pubs[i][1].split(',')[0]:
            num+=1
            sum+=journals[pubs[i][0]]

    print(f"Total IF as first author: {round(sum, 2)} ({num} publications)")

    sum=0
    num=0
    for i in range(len(pubs)):
        if name in pubs[i][1].split(',')[-1]:
            num+=1
            sum+=journals[pubs[i][0]]

    print(f"Total IF as last author: {round(sum, 2)} ({num} publications)")



main()