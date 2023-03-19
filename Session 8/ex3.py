# import libraries (not necessary but helpful)
import csv

# list to store the characters from the characters.txt file
characters = []

# read the characters from the file and store them in the characters list
with open('characters.txt','r') as file:
    data = file.readlines()
    for i in range(1,len(data)):
        data[i]=data[i].rstrip().split(';')
        characters.append(data[i])

print(characters)

feature_indices = {"Name": 0, "Gender": 1, "Hair color": 2, "Hair length": 3, "Glasses": 4, "Hat": 5, "Mustache": 6, "Beard": 7, "Bald": 8}

print("Game characters:")
for c in characters:
    print(f"{c[0]} - ", end='')
    for feature, index in feature_indices.items():
        if feature != "Name": # if index != 0
            print(f"{feature}: {c[index]}, ", end='')
    print()

print('\n')

# Read the user's questions from file
with open("question2.txt", "r") as f:
    questions = f.readlines()
    for i,question in enumerate(questions):
        question = question.strip()
        feature, value = question.split("=")
        feature = feature.strip()
        value = value.strip()
        index = feature_indices[feature]  # use the dictionary to get the index of the feature
        characters = list(filter(lambda x: x[index] == value, characters))
        print(f"Step {i+1} - question: {feature} = {value}")
        print("Selected characters:")
        for c in characters:
            print(
                f"{c[0]} - Gender: {c[1]}, Hair color: {c[2]}, Hair length: {c[3]}, Mustache: {c[4]}, Beard: {c[5]}, Bald: {c[6]}, Glasses: {c[7]}, Hat: {c[8]}")
        print()
    if len(characters) == 1:
        print("Congratulations, you win! Character selected:")
        print(f"{c[0]} - Gender: {c[1]}, Hair color: {c[2]}, Hair length: {c[3]}, Mustache: {c[4]}, Beard: {c[5]}, Bald: {c[6]}, Glasses: {c[7]}, Hat: {c[8]}")
    else:
        print("Too bad, you lose.")


# print the final result
