def find_box(boxes,obj):
    for index,box in enumerate(boxes):
        if obj in box:
            return index
    return None

def readfile(filename):
    actions=[]
    with open(filename,'r') as file:
        data=file.readlines()
        for i in range(len(data)):
            a,b,c,d = data[i].rstrip().split(' ')
            actions.append([a,d])

    return actions
def main():
    actions = readfile('actions.txt')
    print(actions)

    boxes=[] #[ ['Apple',4], ['banana',6]]
    flag = True
    for i in range(len(actions)):
        obj = actions[i][1]
        if actions[i][0] == 'Bob':
            index = find_box(boxes,obj)
            if index is None:
                if len(boxes)<=1:
                    boxes.append([obj,1])
                else:
                    print('ERROR!')
                    exit(0)
            else:
                boxes[index][1]+=1

        if actions[i][0] == 'Carl':
            index = find_box(boxes,obj)
            if index is None:
                print('ERROR')
                exit(0)
            else:
                num = boxes[index][1]
                if num == 1:
                    boxes.remove(boxes[index])
                if num !=1:
                    boxes[index][1]-=1
    if flag==True:
        print('OK')


main()