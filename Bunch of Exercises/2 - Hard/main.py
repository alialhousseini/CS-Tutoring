import csv

def readfile(filename):
    values = []
    labels=''
    with open(filename , 'r') as file:
        reader = csv.reader(file,delimiter=';')
        for i, row in enumerate(reader):
            if i==0:
                labels=row
            if i!=0:
                values.append(row)
    return values,labels

def metrics(date, data, labels):
    filtered_data = list(filter(lambda x: x[0][0]==date,data))
    average = {}
    maximum = {}
    minimum = {}
    for i, label in enumerate(labels):
        if i!=0:
            sum_label = sum(map(lambda x: float(x[i]),filtered_data))
            avg = sum_label / len(filtered_data)
            average[label] = avg
            
            max_label = max(map(lambda x: float(x[i]),filtered_data))
            maximum[label] = max_label
            
            min_label = min(map(lambda x: float(x[i]),filtered_data))
            minimum[label] = min_label
    
    return average, maximum, minimum

def main():
    filename = '.\\2 - Hard\\Torino.csv'
    title = filename[4:-4]
    #print(title)
    data, labels = readfile(filename)
    #print(labels)
    #print(data)
    for i in range(len(data)):
        data[i][0] = data[i][0].split(' ')
    #print(data)
    
    print(f"Report meteorologico per la stazione di {title}")
    for i, label in enumerate(labels):
        if i!=0:
            print(f"\t{label}",end = " ")
    print('\n')
    
    filtered_dates = list(map(lambda x: x[0][0], data))
    dates = list(set(filtered_dates))
    dates.sort()
    
    for date in dates:
        average, maximum, minimum = metrics(date, data, labels)
        print(date)
        print('average\t', end =' ')
        for n in average.values():
            print(f"\t{round(n,2)}", end=" ")
        print('\n')
        print('maximum\t', end =' ')
        for n in maximum.values():
            print(f"\t{round(n,2)}", end=" ")
        print('\n')
        print('minimum\t', end =' ')
        for n in minimum.values():
            print(f"\t{round(n,2)}", end=" ")
        print('\n')
            
    
    
    
    
    
    
main()