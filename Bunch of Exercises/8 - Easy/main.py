import csv

def readfile(filename):
    alarms=[]
    with open(filename , 'r') as file:
        data = file.readlines()
        for i in range(1,len(data)):
            data[i]=data[i].rstrip().split(';')
            data[i][1]=int(data[i][1])
            alarms.append(data[i])
    return alarms

def main():
    filename='.\\8\\allarmi.csv'
    data = readfile(filename)
    
    ocurrences = {}
    for line in data:
        if line[0] not in ocurrences:
            ocurrences[line[0]]=0
        ocurrences[line[0]]+=1
    
    for s in sorted(ocurrences,key = lambda x: ocurrences[x], reverse=True):
        print(f"For robot {s}, {ocurrences[s]}  alarms have occured")
    
    print()
    
    print(f"The maximum severity level 10 was reached by the following robots:")
    max_sev = max(list(map(lambda x: x[1], data)))
    robots_max_sev = list(set(list(map(lambda x: x[0],list(filter(lambda x: x[1]==max_sev,data))))))
    for robot in robots_max_sev:
        print(f"{robot}")
    
main()