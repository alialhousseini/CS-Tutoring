def string_to_date(date): # 01-02-2021
    d,m,y=date.split('-')
    d=int(d)
    m=int(m)
    y=int(y)
    return [y,m,d]

def is_before(d1,d2):
    if d1[0]<d2[0]:
        return True
    elif d1[0]>d2[0]:
        return False
    else:
        if d1[1] < d2[1]:
            return True
        elif d1[1] > d2[1]:
            return False
        else:
            if d1[2] < d2[2]:
                return True
            elif d1[2] > d2[2]:
                return False
    return True

def readfile(filename):
    try:
        rules=[]
        radded=[]
        rremoved=[]
        with open(filename,'r') as file:
            data=file.readlines()
            for i in range(len(data)):
                data[i]=data[i].rstrip().split(':')
                date = string_to_date(data[i][0])
                rlist = data[i][1].lstrip().split(' ')
                for r in rlist:
                    if r[0]=='+':
                        radded.append(r[1:])
                    if r[0]=='-':
                        rremoved.append(r[1:])
                rules.append([date,radded,rremoved])
    except FileExistsError:
        print('error')

    return rules

def get_active_rules(date,rules):
    active_rules=set()
    for d, ra, rr in rules:
        ra = set(ra)
        rr = set(rr)
        if is_before(d, date):
            active_rules = active_rules.union(ra)
            active_rules -= rr
        else:
            break
    return active_rules

def main():
    rules = readfile('rules-example1.txt')
    print(rules)
    try:
        with open('dates-example1.txt','r') as file:
            for date in file.readlines():
                print(date.rstrip()+':')
                day = string_to_date(date)
                for r in get_active_rules(day,rules):
                    print(r)


    except FileExistsError:
        print('error')
        


main()