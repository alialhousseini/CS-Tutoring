
def is_armstrong(num):
    sum_by_square = sum(list(map(lambda x: int(x)**len(str(num)),str(num))))
    return num == sum_by_square

try:
    with open("numbers.txt",'r') as file:
        nums=file.readlines()

except IOError:
    pass

try:
    with open("armstrong.txt",'w') as opt:
        for num in nums:
            if is_armstrong(int(num)):
                opt.write(num)
except IOError:
    pass

print("END!\n")