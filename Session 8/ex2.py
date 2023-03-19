def readfile(filename):
    try:
        appointments = []
        with open(filename,'r') as file:
            data = file.readlines()
            for i in range(len(data)):
                data[i]=data[i].rstrip().split(';')
                data[i][0]=int(data[i][0])
                data[i][1]=int(data[i][1])
                appointments.append(data[i])

    except FileExistsError:
        print('error')

    return appointments

def insert(event,appointments):
    filtered = list(filter(lambda x: x[0]==event[0] and x[1]==event[1],appointments))
    if len(filtered)==0:
        appointments.append(event)
        print("Appointment inserted correctly")
        print(f"day {event[0]} at {event[1]}: {event[2]}")
    else:
        print("Impossible to insert")

def visualize(day,appointments):
    for event in list(filter(lambda x:x[0]==day,appointments)):
        print(f"day {event[0]} at {event[1]}: {event[2]}")

def main():
    filename='agenda.txt'
    appointments= readfile(filename)
    try:
        with open('commands.txt','r') as file:
            commands = file.readlines()
            for i in range(len(commands)):
                commands[i]=commands[i].rstrip().split(' ',maxsplit=3)
                if commands[i][0]=='v':
                    visualize(int(commands[i][1]),appointments)
                if commands[i][0]=='i':
                    event = [int(commands[i][1]),int(commands[i][2]),commands[i][3]]
                    insert(event,appointments)

    except FileNotFoundError:
        print('error')

main()

