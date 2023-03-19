def readPCs(filename):
    with open(filename,'r') as file:
        data = file.readlines()
        for i in range(len(data)):
            data[i]=data[i].rstrip()

    return data

def readRegistrations(filename):
    with open(filename,'r') as file:
        data = file.readlines()
        for i in range(len(data)):
            data[i]=data[i].rstrip().split(':')

    return data

def main():
    PCs = readPCs('parcoPC.txt')
    #print(PCs)
    registrations = readRegistrations('registrazioni.txt')
    #print(registrations)
    ongoing_loans=[]

    for pc in PCs:
        filtered = list(filter(lambda x: x[0]==pc,registrations))
        if len(filtered)%2 != 0:
            ongoing_loans.append(filtered[-1])

    print(f"List of ongoing loans:")
    ongoing_loans.sort(key=lambda x: int(x[1]))

    flag = True
    for i in range(len(ongoing_loans)):
        if flag == False:
            flag=True
            continue
        s = ongoing_loans[i][1]+": "+ongoing_loans[i][0]
        for j in range(i+1,len(ongoing_loans)-1):
            if ongoing_loans[i][1]==ongoing_loans[j][1]:
                s+=", "+ongoing_loans[j][0]
                flag=False
        print(s)

    ongoing_loans_pcs=list(map(lambda x: x[0],ongoing_loans))
    x = set(PCs).difference(set(ongoing_loans_pcs))
    s=''
    for pc in sorted(x):
        s+=pc +', '
    print(f"PCs available for loan: {s[:-2]}")

if __name__ == "__main__":
    main()
