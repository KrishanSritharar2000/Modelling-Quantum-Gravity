#Grid
import turtle
from Main2 import *

pen = turtle.Turtle()
turtle.delay(0)
pen.ht()
turtle.colormode(255)
turtle.tracer(0,0)

   
def grid(col, row, len_th, mode, coordinates):

    width = turtle.window_width()
    height = turtle.window_height()
    x1 = round((0)- ((col/2)*len_th),0)#These two lines centre the grid
    y1 = round((0) + ((row/2)*len_th),0)

    x,y = x1,y1
    print("X",x,"Y",y)
    print("X1",x1+(col*len_th),"Y1",y1+(col*len_th))

    pen.begin_fill()
    fill(255,255,255)
    rect(x1,y1,(col*len_th),(row*len_th))#+len_th/2
    pen.end_fill()
    
    if mode.lower() == "random":
        for i in range(col*row):
            x = random.randint(x1,x1+(col*len_th))
            y = random.randint(y1, y1+(row*len_th))
            pen.pensize(2)
            point(x,y)
            pen.pensize(1)
            coordinates.append([x,y])
            print("Done")
            # coordinates_dict[x,y] = i
        return coordinates
        # return coordinates_dict
    else:           
        for j in range(row):# These two for loops draw the grid
            for k in range(col+1):
                stroke(0,0,0)# Sets the colour of the line and controls the transparancy of the line (0 is completely transparant, 255 is completely opaque)
                if mode.lower() == "square":
                    rect(x,y,len_th,len_th)
                elif mode.lower() == "triangle":
                    triangle(x,y,x+len_th,y,x+(len_th/2),y+len_th)
                x += len_th
            y -= len_th
            if mode.lower() == "square":
                x = x1
            elif mode.lower() == "triangle":
                if j % 2:
                    x = x1
                else:
                    x = x1 - (len_th/2)
            
        clear_excess(col, row, len_th)
        turtle.update()

def clear_excess(col,row,len_th):
    colour = turtle.bgcolor()
    pen.pencolor(colour)
    pen.pensize(1)
    pen.begin_fill()
    pen.fillcolor(colour)
    rect(((0)-((col/2)*len_th))-len_th*2,((0)+((row/2)*len_th)),len_th*2,len_th*row)
    pen.end_fill()
    pen.begin_fill()
    pen.fillcolor(colour)
    rect(((0)+((col/2)*len_th)),((0)+((row/2)*len_th)),len_th*2,len_th*row)
    pen.end_fill()
    stroke(0,0,0)
##    line(((0)+((col/2)*len_th)),((0)-((row/2)*len_th)),((0)+((col/2)*len_th)),((1)+((row/2)*len_th)))
    stroke(0,0,0)
##    line(((0)-((col/2)*len_th)),((0)-((row/2)*len_th)),((0)-((col/2)*len_th)),((1)+((row/2)*len_th)))

if __name__ == "__main__":
    mode = "sqaure"
    coord = []
    grid(10,10,10,mode,coord)
