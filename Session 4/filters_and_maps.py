world_cup=[["Italy",4],["France",2],["Brazil",6],["Argentina",2],["Uruguay",2],["Germany",4],["England",1],["Spain",1]]
world_cup.sort(key=lambda x: x[1],reverse=True)
print(world_cup)