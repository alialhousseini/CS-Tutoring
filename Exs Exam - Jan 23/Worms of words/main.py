#a function that takes the input file as a parameters and returns a 2-D list of words
def readfile(filename):
    try:
        with open(filename,'r') as file:
            data = file.readlines()
            for i in range(len(data)):
                data[i]=data[i].strip().split(' ')

    except FileExistsError:
        print('error')

    return data

# a function that takes two words and the text (as a list) and prints the appropriate message
def distance(word1,word2,sequences):
    min_dist = 99
    index_min_dist = -1
    for i in range(len(sequences)):
        if word1 in sequences[i] and word2 in sequences[i]:
            for j in range(len(sequences[i])):
                for k in range(j+1,len(sequences[i])-1):
                    if (word1==sequences[i][j] and word2==sequences[i][k]) or (word1==sequences[i][k] and word2==sequences[i][j]):
                        if min_dist>=abs(j-k):
                            index_min_dist=i
                            min_dist=abs(j-k)

    if index_min_dist==-1:
        print(f"The two words never appear in the same sequence")
    else:
        print(f"Min distance: Sequence {index_min_dist+1} (distance = {min_dist})")


def main():
    seqences = readfile('seq.txt')
    print(seqences)
    word1=input('Enter the first word:')
    word2 =input('Enter the second word:')
    distance(word1,word2,seqences)

main()