#Krishan Sritharar

#Random Walks 
import random
import turtle
from scipy import spatial
from Grid import *

pen = turtle.Turtle()
turtle.delay(0)
pen.ht()
turtle.colormode(255)
turtle.tracer(0,0)

def setup():
    fullScreen()
    noLoop()
    

def point(x,y):
    pen.up()
    pen.goto(x,y)
    pen.down()
    pen.dot()
    

def line(x1,y1,x2,y2):
    pen.up()
    pen.goto(x1,y1)
    pen.down()
    angle = pen.towards(x2,y2)
    distance = pen.distance(x2,y2)
    pen.seth(angle)
    pen.forward(distance)
    

def rect(x1,y1,len_th_1,len_th_2):
    pen.up()
    pen.goto(x1,y1)
    pen.down()
    for i in range(2):
        pen.forward(len_th_1)
        pen.right(90)
        pen.forward(len_th_2)
        pen.right(90)
    pen.up()
    

def traingle():
    pass

def stroke(r,g,b):
    col = (r,g,b)
    pen.pencolor(col)

def fill(r,g,b):
    col = (r,g,b)
    pen.fillcolor(col)

def drawLines(walk_num, step_num, col, row, len_th, mode, begin, Pright, Pleft, Pdown, Pup, Prightdown, Prightup, Pleftdown, Pleftup):
    
    xaverage_array = []
    yaverage_array = []
    avg = []
    
    if mode.lower() == "square":
        
        for num in range(walk_num):
            
            if begin == 1:#start at centre 
                x = (displayWidth/2)
    
            elif begin == 2:#start at left 
                x = (displayWidth/2) - ((col/2)*len_th)
            
            elif begin == 3: #start at right
                x = (displayWidth/2) + ((col/2)*len_th)
                
            xpos = x
            y = (displayHeight/2)
            
                    
            for j in range(step_num):
                
                if x == ((displayWidth/2) - ((col/2)*len_th)) and y == ((displayHeight/2) - ((row/2)*len_th)):#this prevent the line going off the grid
                    numbers = [0,2]
                elif x == ((displayWidth/2) - ((col/2)*len_th)) and y ==  ((displayHeight/2) + ((row/2)*len_th)):
                    numbers = [0,3]
                elif x == ((displayWidth/2) + ((col/2)*len_th)) and y == ((displayHeight/2) - ((row/2)*len_th)):#these are the corners
                    numbers = [1,2]
                elif x == ((displayWidth/2) + ((col/2)*len_th)) and y == ((displayHeight/2) + ((row/2)*len_th)):
                    numbers = [1,3]
                    
                elif x == ((displayWidth/2) - ((col/2)*len_th)):#these are the edges
                    numbers = [0,2,3]
                elif y == ((displayHeight/2) - ((row/2)*len_th)):
                    numbers = [0,1,2]
                elif x == ((displayWidth/2) + ((col/2)*len_th)):
                    numbers = [1,2,3]
                elif y == ((displayHeight/2) + ((row/2)*len_th)):
                    numbers = [0,1,3]
                else:
                    numbers = [0,1,2,3]
                
                weights = [] 
                
                for i in range(len(numbers)):
                    if numbers[i] == 0:
                        for k in range(int(Pright*100)):
                            weights.append(0)
                    if numbers[i] == 1:
                        for k in range(int(Pleft*100)):
                            weights.append(1)
                    if numbers[i] == 2:
                        for k in range(int(Pdown*100)):
                            weights.append(2)
                    if numbers[i] == 3:
                        for k in range(int(Pup*100)):
                            weights.append(3)
                    
                number = random.choice(weights)#generates a random number
                stroke(0)
                pen.pensize(2)(3)
                if number == 0:
                    line(x,y,x+len_th,y)#right
                    x += len_th
                elif number == 1:
                    line(x,y,x-len_th,y)#left
                    x -= len_th
                elif number == 2:
                    line(x,y,x,y+len_th)#down
                    y += len_th
                elif number == 3:
                    line(x,y,x,y-len_th)#up
                    y -= len_th

                avg.append([x,y])

            print("Average = ",avg)
            
            stroke(0)
            pen.pensize(2)(3)
            point(x,y)
            xaverage_array.append(x)
            yaverage_array.append(y)
    
##            fill(0,0,0)
##            textSize(10)
##            text(num+1,x,y)#writes a number to link the line to the walk_num
    
    elif mode.lower() == "triangle":
        
        for num in range(walk_num):
            
            if begin == 1:#start at centre 
                x = (displayWidth/2)
    
            elif begin == 2:#start at left 
                x = (displayWidth/2) - ((col/2)*len_th)
            
            elif begin == 3: #start at right
                x = (displayWidth/2) + ((col/2)*len_th)
                
            xpos = x
            y = (displayHeight/2)
            
                    
            for j in range(step_num):
                
                if x == ((displayWidth/2) - ((col/2)*len_th)) and y == ((displayHeight/2) - ((row/2)*len_th)):#this prevent the line going off the grid
                    numbers = [0,2]#topleft
                elif x == ((displayWidth/2) - ((col/2)*len_th)) and y ==  ((displayHeight/2) + ((row/2)*len_th)):
                    numbers = [0,3]#bottomleft
                elif x == ((displayWidth/2) + ((col/2)*len_th)) and y == ((displayHeight/2) - ((row/2)*len_th)):#these are the corners
                    numbers = [1,4]#topright
                elif x == ((displayWidth/2) + ((col/2)*len_th)) and y == ((displayHeight/2) + ((row/2)*len_th)):
                    numbers = [1,5]#bottomright
                   
                elif x == ((displayWidth/2) - ((col/2)*len_th)) or x == ((displayWidth/2) - ((col/2)*len_th) + (len_th/2)):#these are the edges
                    numbers = [0,2,3]#left edge
                elif y == ((displayHeight/2) - ((row/2)*len_th)):
                    numbers = [0,1,2,4]#top edge
                elif x == ((displayWidth/2) + ((col/2)*len_th)) or x == ((displayWidth/2) + ((col/2)*len_th) - (len_th/2)):
                    numbers = [1,4,5]#right edge
                elif y == ((displayHeight/2) + ((row/2)*len_th)):
                    numbers = [0,1,3,5]#bottom edge
                else:
                    numbers = [0,1,2,3,4,5]
                
                weights = [] 
                
                for i in range(len(numbers)):
                    if numbers[i] == 0:
                        for k in range(int(Pright*100)):
                            weights.append(0)
                    if numbers[i] == 1:
                        for k in range(int(Pleft*100)):
                            weights.append(1)
                    if numbers[i] == 2:
                        for k in range(int(Prightdown*100)):
                            weights.append(2)
                    if numbers[i] == 3:
                        for k in range(int(Prightup*100)):
                            weights.append(3)
                    if numbers[i] == 4:
                        for k in range(int(Pleftdown*100)):
                            weights.append(4)
                    if numbers[i] == 5:
                        for k in range(int(Pleftup*100)):
                            weights.append(5)                    
                
                number = random.choice(weights)#generates a random number
                stroke(0)
                pen.pensize(2)(3)
                if number == 0:
                    line(x,y,x+len_th,y)#right
                    x += len_th
                elif number == 1:
                    line(x,y,x-len_th,y)#left
                    x -= len_th
                elif number == 2:
                    line(x,y,x+(len_th/2),y+len_th)#down right 
                    y += len_th
                    x += (len_th/2)
                elif number == 3:
                    line(x,y,x+(len_th/2),y-len_th)#up right
                    y -= len_th
                    x += (len_th/2)
                elif number == 4:
                    line(x,y,x-(len_th/2),y+len_th)#down left
                    y += len_th
                    x -= (len_th/2)
                elif number == 5:
                    line(x,y,x-(len_th/2),y-len_th)#up left
                    y -= len_th
                    x -= (len_th/2)
                avg.append([x,y])
            
            stroke(0)
            pen.pensize(2)(3)
            point(x,y)
            xaverage_array.append(x)
            yaverage_array.append(y)
    
            fill(0)
            textSize(10)
            text(num+1,x,y)#writes a number to link the line to the walk_num
            
    averageline1(xaverage_array,yaverage_array,xpos)
    averageline2(step_num,walk_num,avg,xpos)
    
    
    
def drawLinesRandom(walk_num, step_num, col, row, len_th, begin, coord, Pright, Pleft, Pdown, Pup):

    if begin == 1:#start at centre 
        x = (displayWidth/2)

    elif begin == 2:#start at left 
        x = (displayWidth/2) - ((col/2)*len_th)
    
    elif begin == 3: #start at right
        x = (displayWidth/2) + ((col/2)*len_th)
        
    xpos = x
    y = (displayHeight/2)
    xaverage_array = []
    yaverage_array = []
    avg = []
    print("Coord: ", coord)
    point_tree = scipy.spatial.cKDTree(coord)
    space = abs(len_th/(row*col))
    print("Points = ",point_tree.data[point_tree.query_ball_point([xpos,y],space)])
    
    # def getKeyX(item):
    #     return item[0]
    # def getKeyY(item):
    #     return item[1]
    # coord_x = sorted(coord, key=getKeyX)
    # coord_y = sorted(coord, key=getKeyY)
    # print()
    # print("Coord_x: ",coord_x)
    # print()
    # print("Coord_y: ",coord_y)    
    # print("Coordinate 1: ", coord)  
    # print("")    
    # print("Coordinates 2: ", coord2)
    
    # print("Nearest To beginning: ",coord2.nearest_key((xpos,y)))
    # temp = coord2.nearest_key((xpos,y))
    # print("Temp : ",temp)
    # temp_x = temp[0]
    # temp_y = temp[1]
    # print("Temp X :",temp[0])
    # print("Temp Y :",temp[1])
    # stroke(0,255,0)
    # line(temp_x,temp_y,displayWidth/2,y)

    # for num in range(walk_num):
                
    #     if begin == 1:#start at centre 
    #         x = (displayWidth/2)
    
    #     elif begin == 2:#start at left 
    #         x = (displayWidth/2) - ((col/2)*len_th)
        
    #     elif begin == 3: #start at right
    #         x = (displayWidth/2) + ((col/2)*len_th)
            
    #     xpos = x
    #     y = (displayHeight/2)
    #     prevx,prevy = x,y
    #     temp_coord_x = []
    #     temp_coord_y = []
                
        # space = abs(len_th/(row*col))
        # # space = 30
        # for j in range(step_num):
        #     while len(temp_coord_x) == 0:
        #         for i in range(len(coord_x)):
        #             temp_x = (coord_x[i][0])
        #             # print("Temp - space: ",(temp_x - space ))
        #             # print("Temp + space: ",(temp_x + space ))
        #             if (prevx - space ) <= temp_x <= (prevx + space):
        #                 temp_coord_x.append(coord_x[i])
        #         space += 2
        #     print("TempX",temp_coord_x)
        #     print("ABS",abs(len_th/(row*col)))
        #     print("new space", space)
        #     space = abs(len_th/(row*col))
        #     # space = 30
        #     while len(temp_coord_y) == 0:
        #         for i in range(len(coord_y)):
        #             temp_y = (coord_y[i][0])
        #             # print("Temp - space: ",(temp_y - space ))
        #             # print("Temp + space: ",(temp_y + space ))
        #             if (prevy - space ) <= temp_y <= (prevy + space):
        #                 temp_coord_y.append(coord_y[i])
        #         space += 2
        #     print("TempXY",temp_coord_y)
        #     print("ABS",abs(len_th/(row*col)))
        #     print("new space", space)
        #     for i in range(len(temp_coord_x)):
        #         stroke(255,0,0)
        #         strokeWeight(5)
        #         point(temp_coord_x[i][0], temp_coord_x[i][1])
        #         print("Donex")
        #     for i in range(len(temp_coord_y)):
        #         stroke(0,255,0)
        #         strokeWeight(5)
        #         point(temp_coord_y[i][0], temp_coord_y[i][1])

                
        # for j in range(step_num):
            
            # if x == ((displayWidth/2) - ((col/2)*len_th)) and y == ((displayHeight/2) - ((row/2)*len_th)):#this prevent the line going off the grid
            #     numbers = [0,2]
            # elif x == ((displayWidth/2) - ((col/2)*len_th)) and y ==  ((displayHeight/2) + ((row/2)*len_th)):
            #     numbers = [0,3]
            # elif x == ((displayWidth/2) + ((col/2)*len_th)) and y == ((displayHeight/2) - ((row/2)*len_th)):#these are the corners
            #     numbers = [1,2]
            # elif x == ((displayWidth/2) + ((col/2)*len_th)) and y == ((displayHeight/2) + ((row/2)*len_th)):
            #     numbers = [1,3]
                
            # elif x == ((displayWidth/2) - ((col/2)*len_th)):#these are the edges
            #     numbers = [0,2,3]
            # elif y == ((displayHeight/2) - ((row/2)*len_th)):
            #     numbers = [0,1,2]
            # elif x == ((displayWidth/2) + ((col/2)*len_th)):
            #     numbers = [1,2,3]
            # elif y == ((displayHeight/2) + ((row/2)*len_th)):
            #     numbers = [0,1,3]
            # else:
            #     numbers = [0,1,2,3]
            
            # weights = [] 
            
            # for i in range(len(numbers)):
            #     if numbers[i] == 0:
            #         for k in range(int(Pright*100)):
            #             weights.append(0)
            #     if numbers[i] == 1:
            #         for k in range(int(Pleft*100)):
            #             weights.append(1)
            #     if numbers[i] == 2:
            #         for k in range(int(Pdown*100)):
            #             weights.append(2)
            #     if numbers[i] == 3:
            #         for k in range(int(Pup*100)):
            #             weights.append(3)
                
            # number = random.choice(weights)#generates a random number
            # stroke(0)
            # strokeWeight(3)
        #     if number == 0:
        #         line(x,y,x+len_th,y)#right
        #         x += len_th
        #     elif number == 1:
        #         line(x,y,x-len_th,y)#left
        #         x -= len_th
        #     elif number == 2:
        #         line(x,y,x,y+len_th)#down
        #         y += len_th
        #     elif number == 3:
        #         line(x,y,x,y-len_th)#up
        #         y -= len_th

        #     avg.append([x,y])

        # print("Average = ",avg)
        
        # stroke(0)
        # strokeWeight(3)
        # point(x,y)
    #     xaverage_array.append(x)
    #     yaverage_array.append(y)

    #     fill(0)
    #     textSize(10)
    #     text(num+1,prevx,prevy)#writes a number to link the line to the walk_num 
    
    # averageline1(xaverage_array,yaverage_array,xpos)
    # averageline2(step_num,walk_num,avg,xpos)
    
    
    
    
    
    
    
def averageline1(xaverage_array,yaverage_array,xpos):
        
    sum_of_x,sum_of_y = 0,0
    
    for l in range(len(xaverage_array)):
        sum_of_x += xaverage_array[l]
        sum_of_y += yaverage_array[l]
        
    xaverage = sum_of_x / len(xaverage_array)
    yaverage = sum_of_y / len(yaverage_array)
    
    stroke(255,0,0)
    strokeWeight(3)
    line(xpos,(displayHeight/2),xaverage,yaverage)
    
    
def averageline2(step_num,walk_num,average_array,xpos):
    x = xpos
    y = (displayHeight/2)
    prevx = x
    prevy = y
    xaverage = []
    yaverage = []
    for i in range(step_num*walk_num):
        xaverage.append(average_array[i][0])
        yaverage.append(average_array[i][1])
        
    for j in range(step_num):
        xaverage_t = xaverage[j::step_num]
        yaverage_t = yaverage[j::step_num]
        print("Xaverage_t:", xaverage_t)
        
        sum_of_x,sum_of_y = 0,0

        for k in range(len(xaverage_t)):
            sum_of_x += xaverage_t[k]
            sum_of_y += yaverage_t[k]
        
        temp_xaverage = sum_of_x / len(xaverage_t)
        temp_yaverage = sum_of_y / len(yaverage_t)
        
        stroke(0,0,255)
        line(prevx,prevy,temp_xaverage,temp_yaverage)
        prevx = temp_xaverage
        prevy = temp_yaverage

def draw():
    
    column = 10
    row = 10
    space = 40
    mode = "square"     #"square","triangle","random"
    num_of_steps = 1
    num_of_walks = 1
    begin = 2
    name = "Sqaure with Second Average5"
    Pdown = 0.20
    Pup  = 0.20
    Pright = 0.30
    Pleft = 0.30
    Prightdown = 0.10
    Prightup = 0.10
    Pleftdown = 0.10
    Pleftup = 0.10
    
    coordinates = []
    # coordinates_dict = NearestDict(2)

    turtle.bgcolor("grey")
    grid(column,row,space,mode, coordinates)


##    if mode.lower() == "square" or mode.lower() == "triangle":
##        drawLines(num_of_walks, num_of_steps, column, row, space, mode, begin, Pright, Pleft, Pdown, Pup, Prightdown, Prightup, Pleftdown, Pleftup)
##    elif mode.lower() == "random":
##       drawLinesRandom(num_of_walks, num_of_steps, column, row, space, begin,coordinates, Pright, Pleft, Pdown, Pup)
##    saveFrame("Walk_{}.png".format(name))


if __name__ == "__main__":
    draw()
