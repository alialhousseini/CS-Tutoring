
def readfile(filename):
    try:
        ingredients = {}
        with open(filename,'r') as file:
            data = file.readlines()
            for i in range(1,len(data)):
                if data[i]=='\n':
                    break
                data[i]=data[i].rstrip().split(';')
                data[i][1] = int(data[i][1])
                ingredients[data[i][0]]=data[i][1]

    except FileExistsError:
        print('error')

    return ingredients

def read_ing(filename):
    try:
        with open(filename,'r') as file:
            data = file.readlines()
            for i in range(len(data)):
                data[i]=data[i].rstrip().split(';')
                data[i][1]=float(data[i][1].strip())
                data[i][2] = float(data[i][2].strip())
    except FileExistsError:
        print('errpr')

    return data

def cost(k,ingredients):
    for i in range(len(ingredients)):
        if k==ingredients[i][0]:
            return ingredients[i][1]
    return 0

def calories(k,ingredients):
    for i in range(len(ingredients)):
        if k==ingredients[i][0]:
            return ingredients[i][2]
    return 0

def main():
    recipe_ing = readfile('recipe.txt')
    #print(recipe_ing)
    for element in recipe_ing.keys():
        print(f"{element} - {recipe_ing[element]}")
    ingredients = read_ing('foods.txt')
    #print(ingredients)
    print(f"Number of ingredients: {len(recipe_ing)}")
    total_cost=sum(list(map(lambda x: recipe_ing[x]*cost(x,ingredients),recipe_ing)))
    print(total_cost/1000)
    total_calories=sum(list(map(lambda x: recipe_ing[x]*calories(x,ingredients),recipe_ing)))
    print(total_calories/1000)
main()