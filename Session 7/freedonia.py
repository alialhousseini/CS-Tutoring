
def string_to_date(str):
    d,m,y = str.split('-')
    return [int(y),int(m),int(d)]

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

def read_rules(filename):
    rules=[]
    added=[]
    removed=[]
    try:
        with open(filename,'r') as file:
            data = file.readlines()
            for i in range(len(data)):
                data[i]=data[i].strip()
                date, rlist = data[i].split(':')
                date =  string_to_date(date)
                for r in rlist.lstrip().split(' '):
                    if r[0] == '+':
                        added.append(r[1:])
                    if r[1] == '-':
                        removed.append(r[1:])
                rules.append([date,added,removed])
    except IOError:
        print('ERROR')
        exit(0)
    return rules

def get_active_rules(rules,day):
    active = set()
    for d, ra, rr in rules:
        ra=set(ra)
        rr=set(rr)
        if is_before(d, day):
            active = active.union(ra)
            active -= rr
        else:
            break
    return active

def main():
    rules = read_rules('rules-example1.txt')
    try:
        with open('dates-example1.txt') as file:
            for date in file.readlines():
                date=date.rstrip()
                print(date+':')
                date=string_to_date(date)
                for r in get_active_rules(rules,date):
                    print(r)
                print()

    except IOError:
        pass


if __name__ == '__main__':
    main()
