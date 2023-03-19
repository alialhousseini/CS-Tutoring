def read_order(filename):
    with open(filename,'r') as file:
        data = file.readlines()
        for i in range(len(data)):
            data[i]=data[i].rstrip().split(',')
            data[i][1]=int(data[i][1].strip())
    return data

def read_menu(filename):
    with open(filename,'r') as file:
        data = file.readlines()
        for i in range(len(data)):
            data[i]=data[i].rstrip().split(',')
            data[i][1] = data[i][1].strip()
            data[i][2]=float(data[i][2].strip())
            data[i][3]=float(data[i][3].strip())
    return data

def main():
    orders = read_order('ordine.txt')
    menu = read_menu('menu.txt')
    #print(orders)
    #print(menu)
    for item in menu:
        for order in orders:
            if item[0]==order[0]:
                order.append(item[1])
                order.append(item[2])
                order.append(item[3])

    orders.sort(key=lambda x: x[-1])
    print(orders)
    print("Receipt")
    sum=0
    tax_cost=0.0
    for i in range(len(orders)):
        sum+=orders[i][3]*orders[i][1]
        tax_cost+= (orders[i][3]*orders[i][1])/(1+(orders[i][-1]/100))
        print(f"{orders[i][1]}  {orders[i][2]}  {orders[i][3]*orders[i][1]} IVA {orders[i][-1]}%")

    print(f"Total: {sum} Euros.")
    print(f"In which IVA: {round(sum - tax_cost,2)} Euros.")


main()