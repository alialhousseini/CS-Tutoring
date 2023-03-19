def readfile(filename):
    with open(filename,'r') as file:
        header=''
        data=[]
        info = file.readlines()
        for i in range(len(info)):
            if i==0:
                header=info[i]
            else:
                data.append(info[i])

    return header,data

def main():
    header,data1=readfile('first_session.csv')
    _,data2=readfile('second_session.csv')
    #print(header)
    for i in range(len(data1)):
        data1[i]=data1[i].rstrip().split(',')
        data1[i][2]=int(data1[i][2])
        data1[i][4]=float(data1[i][4])
    for i in range(len(data2)):
        data2[i] = data2[i].rstrip().split(',')
        data2[i][2] = int(data2[i][2])
        data2[i][4] = float(data2[i][4])
    data=data1+data2
    data.sort(key=lambda x: (x[2],x[1]))
    #print(data)
    with open('session.csv','w') as out:
        out.write(header)
        for i in range(len(data)):
            s=str(data[i][0])+','+str(data[i][1])+','+str(data[i][2])+','+str(data[i][3])+','+str(data[i][4])+'\n'
            out.write(s)
            s=''
    diff=0.0
    for i in range(-5,0,1):
        diff += data[i][2]-data[i][4]
    print(f"The average is {round(diff/5,2)}")
main()