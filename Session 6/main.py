def readfile(filename):
    try:
        with open(filename,'r') as file:
            data=file.readlines()
            #for i in range(len(data)):
                #data[i]=data[i].rstrip()
    except FileExistsError:
        print('error')
    return data

def readfile2(filename):
    try:
        with open(filename,'r') as file:
            arguments=file.readlines()
            for i in range(len(arguments)):
                arguments[i]=arguments[i].rstrip()
    except FileExistsError:
        print('error')
    return arguments

def is_found(lst,arguments): #['abc def ghi','ccc ddd','xyz'] ['dsfs','def','sada']
    for word in arguments:
        for i in range(1,len(lst)):
            if word in lst[i]:
                return True
    return False

def main():
    data =readfile('murphy_reads.txt')
    print(data)
    args = readfile2('arguments.txt')
    print(args)
    lst=[]
    for i in range(len(data)):
        if data[i]!='\n':
            lst.append(data[i])
        if data[i]=='\n':
            if is_found(lst,args)==True:
                s=''
                for i in range(1,len(lst)):
                    s+=lst[i]
                if len(s)>50:
                    print(lst[0].rstrip()+'-'+s[0:51]+'...')
                if len(s)<50:
                    print(lst[0].rstrip()+'-'+s)
            lst=[]

main()