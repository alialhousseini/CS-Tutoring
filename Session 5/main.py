#https://t.me/+8Ejvr7CTBmIzZWY0

try:
    with open('actions-simple.txt','r') as file:
        data=file.readlines()
        for i in range(len(data)):
            data[i]=data[i].split()
            data[i]=[data[i][0],data[i][-1]]
    print(data)

except OSError:
    pass

n=2
boxes=[] #[ ['Apple',14], ['Banana',8],['Banana',8] ]

def find_box(boxes,obj):
    for index,box in enumerate(boxes):
        if obj in box:
            return index
    return None

def add_object(boxes,obj):
    index = find_box(boxes,obj)
    if index is None:
        if len(boxes)==n:
            print(f"Alice cannot add {obj}\n")
            return False
        else:
            boxes.append([obj,1])
    else:
        boxes[index][1]+=1

    return True

def take_object(boxes,obj):
    index= find_box(boxes,obj)
    if index is None:
        print(f"Alice cannot give carl {obj}\n")
        return False
    else:
        if boxes[index][1]==1:
            boxes.remove(boxes[index])
        else:
            boxes[index][1]-=1
    return True

for i in range(len(data)):
    object=data[i][1]
    if data[i][0] == "Bob":
        x = add_object(boxes,object)
        if x==False:
            break
    if data[i][0] == "Carl":
        x = take_object(boxes,object)
        if x==False:
            break

if x==True:
    print("All ok!")


