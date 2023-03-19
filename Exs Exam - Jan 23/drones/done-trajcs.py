import math

def euclidean_distance(cood1,cood2):
    x1, y1 = cood1
    x2, y2= cood2
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def read_drones(filename):
    drones={}
    with open(filename,'r') as file:
        data = file.readlines()
        for i in range(len(data)):
            data[i]=data[i].rstrip().split(':')
            drones[data[i][0]]=data[i][1].split(',')
    return drones

def read_coods(filename):
    coods={}
    with open(filename,'r') as file:
        data = file.readlines()
        for i in range(len(data)):
            data[i]=data[i].rstrip().split(':')
            data[i][1] = data[i][1].split(',')
            for j in range(len(data[i][1])):
                data[i][1][j]=int(data[i][1][j])
            coods[data[i][0]]=data[i][1]
    return coods


def find_drone_with_highest_battery_capacity(drones,coods):
    drone_distances={}
    for id, stops in drones.items():
        distance = 0.0
        for i in range(len(stops)-1):
            stop1 = coods[stops[i]]
            stop2 = coods[stops[i+1]]
            distance+=euclidean_distance(stop1,stop2)
        drone_distances[id]=distance

    
    long_drone = max(drone_distances,key=lambda x: drone_distances[x])
    long_distance = drone_distances[long_drone]
    return long_drone,long_distance



def main():
    drones = read_drones('drones.txt')
    coods = read_coods('stops.txt')
    print(drones)
    print(coods)
    dr,ds = find_drone_with_highest_battery_capacity(drones,coods)
    print(f"Highest battery capacity is for {dr}")
    print(f"Total distance = {ds}")
    print(f"Number of stops = {len(drones[dr])-1}")

main()