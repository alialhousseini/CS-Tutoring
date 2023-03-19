def readfile(filename):
    with open(filename,'r') as file:
        data = file.readlines()
        for i in range(len(data)):
            data[i]=data[i].rstrip()
    return data

def main():
    lines = readfile('interception.txt')
    #print(lines)
    indices=[]
    for i in range(len(lines)):
        if 'Bob' in lines[i] or 'Arctor' in lines[i]:
            indices.append(i-2)
            indices.append(i-1)
            indices.append(i)
            indices.append(i+1)

    indices=list(set(indices))

    indices = list(filter(lambda x: x>=0,indices))
    print(indices)
    filtered_lines=[]
    for i,line in enumerate(lines):
        if i not in indices:
            filtered_lines.append(line)
    print(filtered_lines)

    with open('censored.txt','w') as out:
        for line in filtered_lines:
            out.write(line+'\n')
main()