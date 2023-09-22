import csv

def readfile(filename):
    foods = []
    with open(filename , 'r') as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            if i!=0:
                foods.append(row)
    return foods

def readfile2(filename):
    shops=[]
    with open(filename,'r') as file:
        shops = file.readlines()
        for i in range(len(shops)):
            shops[i] = shops[i].rstrip()
    return shops

def determine_cheapest(shop, food, foods):
    foods_filtered = list(filter(lambda x: x[2]==shop and x[3] == food and x[4] == 'E' , foods))
    foods_filtered.sort(key=lambda x: float(x[5]))
    return foods_filtered[0]

def main():
    filename = './1/NLFoodPricing.csv'
    filename2 = './1/shops.txt'
    foods = readfile(filename)
    foods_alpha_filtered = list(filter(lambda x: x[4] == 'E', foods))
    foods_alpha = list(map(lambda x: x[3], foods_alpha_filtered))
    foods_alpha = list(set(foods_alpha))
    foods_alpha.sort()
    print('Products:')
    for food in foods_alpha:
        print(f'- {food}')
    print('\n')
    
    shops = readfile2(filename2)
    shops.sort()

    for shop in shops:
        print(f'{shop}:')
        for food in foods_alpha:
            cheapest = determine_cheapest(shop, food, foods)
            print(f"- {food}: {cheapest[-1]} $/chilo")
        print('\n')
    
    prompt = input("Which food do you want to search for? (q to quit)\n")
    while prompt!='q':
        prompt_result = list(filter(lambda x:x[3] == prompt and x[4] == 'E' , foods))
        if len(prompt_result)!=0:
            prompt_result.sort(key=lambda x: float(x[5]))
            print(f"Minimum price: {prompt_result[0][-1]} $/kilo at {prompt_result[0][2]}")
        else:
            print("Product not available")
        prompt = input("Which food do you want to search for? (q to quit)\n")
    
    print("GoodBye")
    
    
main()