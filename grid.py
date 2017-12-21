import turtle, time #imports the module

def grid(grid_size_input):

    def make_grid(angle1, angle2, angle3, grid_size, partition, length):#defines a function for drwaing the lines of the grid
        for i in range(grid_size):#repeats for the number of coloums - 1
            pen.seth(angle1)#sets the turtle to the specified compass direction
            pen.forward(partition)#moves forward the specified amount
            pen.seth(angle2)#repeat
            pen.forward(length)
            pen.seth(angle3)
            pen.forward(length)
    pen = turtle.Turtle()#defines the varaiable
    time.sleep(20)
    turtle.delay(0)#sets the delay to 0 to make the animation quick
    grid_size = (grid_size_input - 1)#the size of the grid is provided as an arguement ot the function. Its -1 because for example for a 5x5 grid 4 lines going down need to be drawn
    turtle.speed("fastest")#sets the speed to the fastest
####    height = turtle.window_height()#gets the height of the window to make the grid as big as possible.
    centre = 300 #defines the overall size of the grid 
####    centre = int(50*round(float(height / 2)/50))# rounds this value to nearest 50 -- thats all it does
    pen.up()
    pen.goto(-centre,centre)#goes to the coordinate of the calculated value
    pen.down()
    for i in range(4):#draws a box 
        pen.forward(centre*2)
        pen.right(90)
    length = centre * 2#length of the side of the box
    partition = length/grid_size#length between every column
    make_grid(0, 270, 90, grid_size, partition, length)#calls the function
    pen.up()
    pen.goto(-centre,centre)#goes to the original point
    pen.down()
    make_grid(270, 0, 180, grid_size, partition, length)#calls the function
    pen.up()
    pen.goto(0,0)#goes to the centre
    pen.down()
    pen.hideturtle()

if __name__ == "__main__":#if the code is run in this module, without being imported
    grid(21)#this code will be run.
