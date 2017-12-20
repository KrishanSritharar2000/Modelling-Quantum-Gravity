import turtle

def make_grid(angle1, angle2, angle3, grid_size, partition, length):
    for i in range(grid_size):
        pen.seth(angle1)
        pen.forward(partition)
        pen.seth(angle2)
        pen.forward(length)
        pen.seth(angle3)
        pen.forward(length)
pen = turtle.Turtle()
turtle.delay(0)
grid_size = (int(input("How many columns/rows in the grid: "))- 1)
turtle.tracer(0,0)
height = turtle.window_height()
centre = int(50*round(float(height / 2)/50))# rounds to nearest 50
pen.up()
pen.goto(-centre,centre)
pen.down()
for i in range(4):
    pen.forward(centre*2)
    pen.right(90)
length = centre * 2
partition = length/grid_size
make_grid(0, 270, 90, grid_size, partition, length)
pen.up()
pen.goto(-centre,centre)
pen.down()
make_grid(270, 0, 180, grid_size, partition, length)
pen.up()
pen.goto(0,0)
pen.down()
turtle.update()
