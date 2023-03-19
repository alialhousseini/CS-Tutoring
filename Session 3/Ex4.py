
def waveform(my_list):
    my_list.sort()

    for i in range(0, len(my_list) - 1, 2):
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

    return my_list

lst=[10,5,6,3,2,100,80]
lst2=[20,10,8,6,4,2]
print(f"Wave form of my list is {waveform(lst2)}")