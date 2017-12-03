import random

def random_walk(n):
    x = 0
    y = 0
    for i in range(n):
        step = random.choice(['N', 'S', 'E', 'W'])
        if step == 'N':
            y = y + 1
        elif step == 'S':
            y = y - 1
        elif step == 'E':
            x = x +1
        else:
            x = x - 1
    return(x, y)

for i in range(5):
    for i in range(25):
        walk = random_walk(10)
        file = open('Results.txt', 'w')
        file.write("{} Distance from initial =  {} {}\n".format(walk, abs(walk[0]), abs(walk[1])))
        print(walk, "Distance from initial = ", abs(walk[0]) + abs(walk[1]))

