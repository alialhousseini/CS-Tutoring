n=2

data=[]
# read data of file and put it in data list in the form [person,object]
with open('actions-simple.txt','r') as file:
    lines=file.readlines()
    for i in range(len(lines)):
        person, _, _, object = lines[i].split()
        x = [person, object]
        data.append(x)

print(data)
def find_box(boxes, obj):
    boxes_t=list(map(lambda x:x[0],boxes))
    for index, box in enumerate(boxes_t):
        if obj == box:
            return index
    return None

def take_object(boxes,list):
    object=list[1]
    index = find_box(boxes,object)
    if index is None:
        print(f"Alice doesn't have {object}\n")
        return False
    else:
        if boxes[index][1]==1:
            boxes.remove(boxes[index])
        else:
            boxes[index][1]-=1
    return True


def add_object(boxes,list):
    object=list[1]
    index = find_box(boxes,object)
    if len(boxes)==n and index is None:
        print(f"Can't add {object}\n")
        return False
    if index is None:
        boxes.append([object,1])
    else:
        boxes[index][1]+=1
    return True

boxes=[]
count=0
for i in range(len(data)):
    if data[i][0]=='Bob':
        x=add_object(boxes,data[i])
        if x==False:
            break
    if data[i][0]=='Carl':
        x=take_object(boxes,data[i])
        if x==False:
            break

print("End of program!\n")

