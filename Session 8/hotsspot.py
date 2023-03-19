def hot_spot(matrix, d):
    row, col = len(matrix), len(matrix[0])
    result = [[['-' for j in range(col)] for i in range(row)]]
    print(result)
    for i in range(row):
        for j in range(col):
            left = max(0, j - d)
            right = min(col - 1, j + d)
            up = max(0, i - d)
            down = min(row - 1, i + d)
            flag = True
            for x in range(up, down + 1):
                for y in range(left, right + 1):
                    if matrix[x][y] > matrix[i][j]:
                        flag = False
                        break
                if not flag:
                    break
            if flag:
                result[i][j] = str(matrix[i][j])
    return result

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(row))

def readfile(filename):
    with open(filename,'r') as file:
        data = file.readlines()
        for i in range(len(data)):
            data[i]=data[i].rstrip().split(' ')
            for j in range(len(data[i])):
                data[i][j]=int(data[i][j])

    return data


def main():
    hotspot=readfile('hotspot.txt')
    print(hotspot)
    D = 2
    result = hot_spot(hotspot,D)
    print_matrix(result)
    result = hot_spot


main()