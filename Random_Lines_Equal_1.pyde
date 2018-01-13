import random 
grid = [[1]*8 for n in range(8)]

w = 70

def setup():
    size(800,600)
    frameRate(1)
    noLoop()


def draw():
    x,y = 0,0
    for row in grid:
        for col in row:
            rect(x,y,w,w)
            x += w
        y += w
        x = 0
    x,y = 4*w,4*w
    for i in range(10):
        number = random.randint(0,3)
        print(number)
        stroke(255,0,0)
        if number == 0:
            line(x,y-20,x+w,y-20)
            x += w
        elif number == 1:
            line(x,y-20,x-w,y-20)
            x -= w
        elif number == 2:
            line(x,y-20,x,y+w-20)
            y += w
        elif number == 3:
            line(x,y-20,x,y-w-20)
            y -= w     


                      