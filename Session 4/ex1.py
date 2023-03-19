def compute_score(list):
    for i in range(len(list)):
        list[i]=float(list[i])
    list.remove(max(list))
    list.remove(min(list))
    return sum(list)

data=[]
with open('test.txt','r') as file:
    data = file.readlines()
    for i in range(len(data)):
        data[i]=data[i].split(' ')

maxxx=0
index=0
for i in range(len(data)):
    for j in range(5):
        if float(data[i][j+4])>maxxx:
            maxxx=float(data[i][j+4])
            index=i
print(f"{data[index]} {maxxx}")

countries=list(map(lambda x:x[3],data))
print(list(dict.fromkeys(countries)))

# # Part 1 - Using keys and filters
# females=list(filter(lambda x: x[2]=='F',data))
# print(females)
# females.sort(key=lambda x: compute_score(x[4:]),reverse=True)
# print(females)
# print(f"Best female competitor:\n{females[0][0]} {females[0][1]}, {females[0][3]} - score: {compute_score(females[0][4:])}\n")

index=0
highest_score = 0
for i in range(len(data)):
    if data[i][2]=="F":
        if highest_score < compute_score(data[i][4:]):
            highest_score = compute_score(data[i][4:])
            index=i
print(f"Best female competitor:\n{data[index][0]} {data[index][1]}, {data[index][2]} - score: {highest_score}\n")

countries_with_scores = []

for i in range(len(data)):
    temp = [x[0] for x in countries_with_scores]
    if data[i][3] in temp :
        index = temp.index(data[i][3])
        countries_with_scores[index][1]+=compute_score(data[i][4:])
    else:
        countries_with_scores.append([data[i][3],compute_score(data[i][4:])])

countries_with_scores.sort(key=lambda x: x[1],reverse=True)


print(f"Final countries ranking:\n")
for i in range(3):
    print(f"{i+1}) {countries_with_scores[i][0]} - total score: {countries_with_scores[i][1]}")

# Part 2 - maps
# def get_country_and_score(element):
#     return [element[3],compute_score(element[4:])]
#
# countries_with_scores=list(map(lambda x: get_country_and_score(x), data))
# n=len(countries_with_scores)
# for i in range(n-2):
#     for j in range(i+1,n-1):
#         if countries_with_scores[i][0]==countries_with_scores[j][0]:
#             countries_with_scores[i][1]+=countries_with_scores[j][1]
#             countries_with_scores.remove(countries_with_scores[j])
#             n=n-1
#
# countries_with_scores.sort(key=lambda x:x[1],reverse=True)
# print(f"Final countries ranking:\n")
# for i in range(3):
#    print(f"{i+1}) {countries_with_scores[i][0]} - total score: {countries_with_scores[i][1]}")
#

# world_cup=[["Italy",4],["France",2],["Brazil",6],["Argentina",2],["Uruguay",2],["Germany",4],["England",1],["Spain",1]]
# a=list(filter(lambda y: y[1]>=3,world_cup))
# print(a)
# b=map(lambda x: str(x[0][0:3]).upper(),a)
# print(list(b))
