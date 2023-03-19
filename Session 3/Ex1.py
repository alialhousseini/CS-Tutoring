def rotate(lst, n):
    x = lst[n - 1]

    for i in range(n - 1, 0, -1):
        lst[i] = lst[i - 1]

    lst[0] = x
    return lst

lst=[1,7,6,3,0,4]
print(f"List before:{lst}")
print(f"List after:{rotate(lst,len(lst))}")