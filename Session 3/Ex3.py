def rotate(lst, n):
    x = lst[n - 1]

    for i in range(n - 1, 0, -1):
        lst[i] = lst[i - 1]

    lst[0] = x
    return lst

def maximumSum(lst,n):
    sum=[]
    for i in range(n):
        temp=0
        for j in range(n):
            temp+= lst[j]*j
        sum.append(temp)
        lst=rotate(lst,n)
    return max(sum)

list1=[8,3,1,2]
list2=[3,2,1]
print(f"Max of list1 is {maximumSum(list1,len(list1))}")
print(f"Max of list2 is {maximumSum(list2,len(list2))}")