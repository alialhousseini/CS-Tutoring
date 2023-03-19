list=[]

def read_elements(list):
    element = input("Enter a number, press enter to stop\n")
    while element != '':
        list.append(int(element))
        element = input("Enter a number, press enter to stop\n")
    return list

def alternate_sum(list):
    alternate_sum=0
    for i in range(len(list)):
        if i%2==0:
            alternate_sum+=list[i]
        else:
            alternate_sum-=list[i]
    print(f"The alternate sum is {alternate_sum}")

list=read_elements(list)
alternate_sum(list)
