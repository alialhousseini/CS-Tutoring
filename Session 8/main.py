characters = []

# read the characters from the file and store them in the characters list
with open('characters.txt','r') as file:
    data = file.readlines()
    for i in range(1,len(data)):
        data[i]=data[i].rstrip().split(';')
        characters.append(data[i])

print(characters)

feature_indices = {"Name": 0, "Gender": 1, "Hair color": 2, "Hair length": 3, "Glasses": 4, "Hat": 5, "Mustache": 6, "Beard": 7, "Bald": 8}

# print("Game characters:")
# for c in characters:
#     print(f"{c[0]} - ", end='')
#     for feature, index in feature_indices.items():
#         if feature != "Name": # if index != 0
#             print(f"{feature}: {c[index]}, ", end='')
#     print()

with open('question2.txt','r') as file:
    questions=file.readlines()
    for i in range(len(questions)):
        questions[i]=questions[i].rstrip()
    for i, question in enumerate(questions):
        print(f"Step {i+1} - {question}")
        feature,value=question.split('=')
        feature=feature.strip()
        value=value.strip()
        index = feature_indices[feature]
        characters = list(filter(lambda x: x[index]==value,characters))
        for c in characters:
            print(f"{c[0]} - ", end='')
            for feature, index in feature_indices.items():
                if feature != "Name": # if index != 0
                    print(f"{feature}: {c[index]}, ", end='')
            print()
    if len(characters)==1:
        print('Congrats')
    else:
        print('you lose')
