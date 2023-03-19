n = 2 #change n to 42 when checking the big file
def get_actions(filename):
    try:
        with open(filename, "r") as file:
            data = file.readlines()
            for i in range(len(data)):
                data[i] = data[i].rstrip()
                data[i] = data[i].split()
    except FileExistsError:
        print("error")
        exit(0)
    return data

def proceed_acts(data):
    flag = False
    chcklst = {}
    maxim = []
    for i in range(len(data)):
        char = data[i][0]
        obj = data[i][3]
        gh = True
        if char == "Bob":
            if obj in chcklst:
                chcklst[obj] += 1
            elif obj not in chcklst:
                if len(chcklst) < n:
                    chcklst[obj] = 1
                else:
                    print("alice cant store: " + obj)
                    gh == False
                    exit(0)
                if gh == True and i == len(data):
                    print("NO ERRors occured")


        if char == "Carl":
            if obj in chcklst and chcklst[obj] > 1:
                chcklst[obj] -= 1
            if obj not in chcklst:
                print("alice cant give: " + obj)
                gh == False
                exit(0)

            if obj in chcklst and chcklst[obj] <= 1:
                del chcklst[obj]

            if gh==True and i == len(data):
                print("no errors occured")




    return chcklst

def main():
    act_lst = get_actions("actions-simple.txt")
    #print(act_lst)
    proceed_acts(act_lst)





main()

