# A function that takes the file artists.txt and returns
# a data list that contains all songs along with the band code well structured
def read_artists(filename):
    try:
        with open(filename,'r') as file:
            data=file.readlines()
            for i in range(len(data)):
                data[i]=data[i].rstrip()
                data[i]=data[i].split(';')

    except FileExistsError or FileNotFoundError:
        print("ERROR IN FILE!")
        exit(0)

    return data

def work_on_data(data):
    list_of_all_songs = []
    for i in range(len(data)):
        code = data[i][0]
        file_of_songs = data[i][1]
        try:
            with open(file_of_songs, 'r') as inp:
                songs = inp.readlines()
                for i in range(len(songs)):
                    songs[i] = songs[i].rstrip()
                    songs[i] = songs[i].split(';')
                    songs[i].append(code)
                    list_of_all_songs.append(songs[i])

        except IOError or FileNotFoundError:
            print('ERROR!')
            exit(0)
    return list_of_all_songs

def main():
    filename='artists.txt'
    data=read_artists(filename)
    #print(data)
    songs=work_on_data(data)
    #print(songs)
    songs.sort(key=lambda x: int(x[0]))
    print(songs)


    i=0
    while i<=len(songs)-1:
        year=songs[i][0]
        print(songs[i][0]+':')
        while i<=len(songs)-1 and songs[i][0]==year: #very imppp
            print(songs[i][1]+'\t'+songs[i][2])
            i+=1

main()