import turtle
import random

def go_right(step):
     turtle.setheading(0)
     turtle.forward(step)

def go_up(step):
     turtle.setheading(90)
     turtle.forward(step)


def go_left(step):
     turtle.setheading(180)
     turtle.forward(step)

def go_down(step):
     turtle.setheading(270)
     turtle.forward(step)

def make_random_walk(step_size, step_number):
    move_dict = {1: go_up,
                 2: go_right,
                 3: go_left,
                 4: go_down
                 }
    for i in range(step_number):
        move_in_a_direction = move_dict[random.randint(1, 4)]
        move_in_a_direction(step_size)

if __name__ == "__main__":
    turtle.hideturtle()
    turtle.speed("fastest")
    make_random_walk(15, 100)
