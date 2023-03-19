
data=[]
with open("test.txt","r") as file:
    data=file.readlines()
    for i in range(len(data)):
        data[i]=data[i].split(' ')
#
# maxxx=0.0
# index=0
# for i in range(len(data)):
#     for j in range(4,len(data[i])):
#         if float(data[i][j])>maxxx:
#             maxxx=float(data[i][j])
#             index=i
# print(f"The competitor {data[index][0]} has the highest score of {maxxx}\n")

def compute_score(list):
    for i in range(len(list)):
        list[i]=float(list[i])
    list.remove(min(list))
    list.remove(max(list))
    return sum(list)


countries= list(dict.fromkeys(
 list(map(lambda x: x[3],data))
))
print(countries)
for i in range(len(countries)):
    a=[countries[i],0]
    countries[i]=a

print(countries)
for i in range(len(data)):
    for j in range(len(countries)):
        if data[i][3]==countries[j][0]:
            countries[j][1]+=compute_score(data[i][4:])

print(countries)

countries.sort(key=lambda x: x[1],reverse=True)

print("Final ranking\n")
for i in range(3):
    print(f"{i+1}) {countries[i][0]} with score {countries[i][1]}")



#
# females=list(filter(lambda x: x[2]=='F',data))
# for i in range(len(females)):
#     females[i].append(compute_score(females[i][4:]))
# females.sort(key=lambda x: x[-1],reverse=True)
# print(females)
# print(f" the highest score is for {females[0][0]}\n")