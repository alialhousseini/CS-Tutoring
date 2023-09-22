def readfile(filename):
    with open(filename,'r') as file:
        data = file.readlines()
        for i in range(len(data)):
            data[i]=data[i].rstrip().split(';')
            data[i][-1]=int(data[i][-1])
            data[i][-2]=int(data[i][-2])
    return data

def readfile2(filename): 
    with open(filename,'r') as file:
        data = file.readlines()
        for i in range(len(data)):
            data[i]=data[i].rstrip()
    return data

def main():
    filename1='.\\7 - Easy\\comuni.csv'
    filename2='.\\7 - Easy\\province.txt'
    comuni = readfile(filename1)
    provinces = readfile2(filename2)
    filtered_comuni=list(filter(lambda x: x[2] ==provinces[0] or x[2] == provinces[1] ,comuni))

    print(filtered_comuni)        
main()