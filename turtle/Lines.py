import turtle #imports the modules
import random

def go_right(step):#defines functions for every possible move
     turtle.setheading(0)#sets the angle of the turtle to EAST
     turtle.forward(step)#travels forward the specified direction

def go_up(step):
     turtle.setheading(90)#sets the angle of the turtle to NORTH
     turtle.forward(step)


def go_left(step):
     turtle.setheading(180)#sets the angle of the turtle to WEST
     turtle.forward(step)

def go_down(step):
     turtle.setheading(270)#sets the angle of the turtle to SOUTH
     turtle.forward(step)
  
def make_random_walk(step_size, step_number, file_number):#defines a function for generating a random move
     turtle.color('red')#sets the colour of the path to red to contrast with the black grid
     turtle.speed("fast")#sets the speed so that you can see the paths and the animation is not instantaneous
     move_dict = {1: go_up,#makes a dictionary storing each of the four moving functions
                 2: go_right,
                 3: go_left,
                 4: go_down
                 }
     file = "Result{}.txt".format(str(file_number))##defines the name for the textfile
     results = open(file, 'w')#opens a textfile to store the ressults of the position of the light after every move
     results.write("Move 0 coordinates: (0.00, 0.00)")#writes that the starting coordinates of the light is 0,0
     for i in range(step_number):#repeats the number of times specified (in this case 100)
          move_in_a_direction = move_dict[random.randint(1, 4)]#selects a random function from that dictionary
          move_in_a_direction(step_size)#calls the chosen function using the step_size specified
          position = turtle.position()#gets the current position of the turtle (the coordinates)
          results.write("\nMove {} coordinates: {}".format(i+1, position))#writes the coordinates to the textfile
     results.close()#closes the textfile
     turtle.dot(5)#generates a dot at the finishing point
     turtle.write(file_number, font=("arial",8,"normal"))#writes the number next to the dot to show which path it was
     turtle.hideturtle()#hides the turtle
####     file_name = "Results{}.eps".format(file_number)           #I was trying to save a screenshot of the grid but it didn't quite work
####     canvas = turtle.getscreen()
####     canvas.getcanvas().postscript(file=file_name)"""
     turtle.up()#lifts the pen up (so it doesnt make a mark on the interface)
     turtle.goto(0,0)#goes to the coordinates 0,0
     turtle.down()#puts the pen down

if __name__ == "__main__":#if the code is run from this page. This is to prevent this code [from here down] to be run when the module is imported.
     step_size = int(input("What step size do you want: "))#asks for each input
     step_number = int(input("How many random walks do you want: "))
     make_random_walk(step_size, step_number)#calls the function
