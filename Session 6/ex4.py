def readfile_and_filter(filename):
    try:
        with open(filename,'r') as file:
            data = file.readlines()
            for i in range(len(data)):
                data[i]=data[i].rstrip()
                data[i]=data[i].split()
            data = list(filter(lambda x: int(x[2])>=200,data))
    except IOError or OSError:
        print("SHIT\n")
    return data

def main():
    data=readfile_and_filter('glucometer.txt')
    #print(data)
    patients = dict()

    for i in range(len(data)):
        if data[i][0] not in patients:
            patients[data[i][0]] = 0
        patients[data[i][0]]+=1

    for patient in sorted(patients, key= lambda x: patients[x],reverse=True):
        for i in range(len(data)):
            if patient==data[i][0]:
                print(f"{data[i][0]} {data[i][1]} {data[i][2]}")
        print()

if __name__ == '__main__':
    main()