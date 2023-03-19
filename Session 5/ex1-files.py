def read_data(filename):
    try:
        with open(filename,'r') as file:
            data = file.readlines()
            for i in range(len(data)):
                data[i]=data[i].rstrip().split(' ')
    except FileExistsError:
        print('errpr')

    return data


def main():
    products = read_data('products.txt')
    purchases = read_data('purchases.txt')
    print("Suspicious transactions list\n")
    for i in range(len(products)):
        product = products[i][0]
        reseller = products[i][1]
        sus_transaction = list(filter(lambda x: x[0] == product and x[1] != reseller, purchases))
        sus_transaction = list(map(lambda x: x[1], sus_transaction))
        if len(sus_transaction) != 0:
            print(f"Product code: {product}")
            print(f"Official dealer: {reseller}")
            print("Non official dealers: ", end=" ")
            for element in sus_transaction:
                print(element, end=" ")
            print('\n')


main()