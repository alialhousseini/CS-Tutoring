def read_food(filename):
    try:
        food=[]
        with open(filename,'r') as file:
            data=file.readlines()
            for i in range(len(data)):
                data[i]=data[i].strip().split(';')
                data[i][1]=float(data[i][1].strip())
                data[i][2] = float(data[i][2].strip())
                food.append(data[i])
    except FileExistsError:
        print('error')

    return food

def read_ingredients(filename):
    try:
        ingredients={}
        with open(filename,'r') as file:
           data = file.readlines()
           for i in range(1,len(data)):
                if data[i] == '\n':
                    break
                ingredient, quantity = data[i].split(';')
                ingredients[ingredient]=int(quantity.strip())


    except FileExistsError:
        print('error')

    return ingredients

def main():
    food = read_food('foods.txt')
    ingredients = read_ingredients('recipe.txt')
    for ing in ingredients.keys():
        print(f"{ing} - {ingredients[ing]}")
    print()
    print(food)
    print(ingredients)
    print(f"Number of ingredients: {len(ingredients)}")
    recipe_cost = sum(list(map(lambda x: ingredients.get(x[0],0)*x[1]/1000,food)))
    print(f"Recipe cost: {recipe_cost}")
    recipe_calories = sum(list(map(lambda x: ingredients.get(x[0],0) * x[2]/1000,food)))
    print(f"Recipe calories: {recipe_calories}")

main()