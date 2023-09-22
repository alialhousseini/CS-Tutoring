# Load the data from the file
def readfile(filename):
    with open(filename,'r') as file:
        data = file.readlines()
        for i in range(len(data)):
            data[i]=data[i].rstrip().split()
    return data


def overlaps(wheel1, wheel2, draws, date,freqs):
    draws_on = list(filter(lambda x: x[0]==date and (x[1]==wheel1 or x[1]==wheel2),draws))
    for i in range(2,len(draws_on[0])):
        if draws_on[0][i] in draws_on[1][2:]:
            print(f"Common number {draws_on[0][i]} on date {date}")
            if draws_on[0][i] not in freqs:
                freqs[draws_on[0][i]]=0
            freqs[draws_on[0][i]]+=1
            
# # Identify overlaps between two wheels
# def calculate_overlaps(draws, wheel1, wheel2):
#     overlaps = []
#     for key, numbers in draws.items():
#         date, wheel = key
#         if wheel == wheel1:
#             if (date, wheel2) in draws:
#                 common_numbers = numbers & draws[(date, wheel2)]
#                 for number in common_numbers:
#                     overlaps.append((number, date))
#     return overlaps

# # Calculate frequency of each number
# def calculate_frequency(overlaps):
#     frequency = {}
#     for number, _ in overlaps:
#         if number in frequency:
#             frequency[number] += 1
#         else:
#             frequency[number] = 1
#     # Sort the numbers by their frequency in descending order
#     sorted_numbers = sorted(frequency, key=frequency.get, reverse=True)
#     return [(number, frequency[number]) for number in sorted_numbers]

# Main function
def main():
    filename = ".\\4 - Medium\\storico01-oggi.txt"
    draws = readfile(filename)
    print("Available wheels",end= " ")
    cities = list(set(list(map(lambda x: x[1],draws))))
    cities.sort()
    for city in cities:
        print(f"{city}",end=' ')
    print()
    wheel1 = input("Enter the first wheel: ")
    wheel2 = input("Enter the second wheel: ")
    print()
    dates = list(set(list(map(lambda x: x[0],draws))))
    dates.sort()
    freqs = {}
    for date in dates:
        overlaps(wheel1,wheel2,draws,date,freqs)
    # print(freqs)
    
    print("\nNumber    Frequency")
    for s in sorted(freqs, key=lambda x: freqs[x], reverse=True):
        print(f"     {s}        {freqs[s]}")


if __name__ == "__main__":
    main()
