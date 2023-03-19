def readfile(filename):
    try:
        with open(filename,'r') as file:
            data=file.readlines()
    except IOError or FileExistsError or FileNotFoundError:
        print("ERROR!\n")
        exit(1)
    return data

def printer(data,arguments):
    #data=[abc def,ghi jkl,mno pqr] args=[def,xyz,tro]
    for item in arguments:
        item = item.rstrip()
        for i in range(len(data)):
            data[i]=data[i].rstrip()
            if item in data[i]:
                return True
    return False

def main():
    murphy_txt = readfile('murphy_reads.txt')
    arguments = readfile('arguments.txt')
    #print(murphy_txt)
    data=[]
    for i in range(len(murphy_txt)):
        data.append(murphy_txt[i].rstrip())
        if murphy_txt[i]=='\n':
            if printer(data,arguments):
                s=''
                for j in range(1,len(data)):
                    s+=data[j]
                if len(s)<50:
                    print(data[0]+' - '+s)
                else:
                    print(data[0]+' - '+s[:50]+'...')

            data=[]




if __name__ == '__main__':
    main()