list1 = [5,4,7,3,8,9]
list2 = [1,2,3,4,1,1]
def sum_without_smallest(list):
    smallest=min(list)
    flag=False
    sum=0
    for i in range(len(list)):
        if list[i]==smallest:
            if flag:
                sum+=list[i]
            flag = True
        else:
            sum+=list[i]
    return sum

print(f"The sum without smallest of our list is {sum_without_smallest(list2)}\n")