
def readfile(filename):
    with open(filename,'r') as file:
        data = file.readlines()
        for i in range(len(data)):
            data[i] = data[i].rstrip().split(',')
    
    return data

def main():
    filename1='.\\3 - Easy\\cfu.dati'
    filename2='.\\3 - Easy\\exams.log'
    cfu = readfile(filename1)
    exams = readfile(filename2)
    
    students = list(map(lambda x: x[0],exams))
    students = list(set(students))
    students.sort()
    
    for exam in exams:
        for cf in cfu:
            if exam[2]==cf[0]:
                exam.append(cf[1])
                exam.append(cf[2])
                
    for student in students:
        total = 0
        mandatory = 0
        avg = 1
        count = 0
        for exam in exams:
            if student in exam:
                if exam[3]!='A' and exam[3]!='R':
                    total += int(exam[4])
                    if exam[-1]=='1':
                        mandatory+=int(exam[4])
                    avg += (int(exam[3])*int(exam[4]))
                    count += int(exam[4])
        print(f"Student {student}")
        print(f" student with total {total} CFU; {mandatory} CFU mandatory, {round(avg/count,2)} of average", end = ' ')
        if total <=30:
            print('no graduation')
        print('\n')
    
main()