
def read_file(filename):
    try:
        with open(filename,'r') as file:
            data=file.readlines()
            for i in range(len(data)):
                data[i]=data[i].rstrip().split(' ')
                for j in range(len(data[i])):
                    data[i][j]=int(data[i][j])

    except FileExistsError:
        print('error')

    return data

def check_top(data):
    tops = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            if i == 0:
                if data[i][j]>data[i][j+1] and data[i][j]>data[i][j-1] and data[i][j]>data[i+1][j+1] and data[i][j]>data[i+1][j-1] and data[i][j]>data[i+1][j]:
                    tops.append([data[i][j],i,j])
            elif j == 0:
                if data[i][j]>data[i+1][j] and data[i][j]>data[i-1][j] and data[i][j]>data[i+1][j+1] and data[i][j]>data[i+1][j-1] and data[i][j]>data[i+1][j]:
                    tops.append([data[i][j],i,j])
            elif i == len(data)-1:

            elif j == len(data[i])-1:

            else:



def main():



main()