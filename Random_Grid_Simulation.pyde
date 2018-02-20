#Krishan Sritharar

#Random Walks 
import random
import scipy
import numpy

def setup():
    fullScreen()
    noLoop()
    
def draw():

    column = 4
    row = 4
    space = 80
    mode = "random"     #"square","triangle","random"
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
     
    grid(column,row,space,mode, coordinates)    
    if mode.lower() == "square" or mode.lower() == "triangle":
        drawLines(num_of_walks, num_of_steps, column, row, space, mode, begin, Pright, Pleft, Pdown, Pup, Prightdown, Prightup, Pleftdown, Pleftup)
    elif mode.lower() == "random":
       drawLinesRandom(num_of_walks, num_of_steps, column, row, space, begin,coordinates, Pright, Pleft, Pdown, Pup)
    saveFrame("Walk_{}.png".format(name))


def grid(col, row, len_th, mode, coordinates):
    
    x1 = (displayWidth/2)- ((col/2)*len_th)#These two lines centre the grid
    y1 = (displayHeight/2) - ((row/2)*len_th)

    x,y = x1,y1
    fill(255)
    rect(x1,y1,(col*len_th),(row*len_th))#+len_th/2
    
    if mode.lower() == "random":
        for i in range(col*row):
            x = random.randint(x1,x1+(col*len_th))
            y = random.randint(y1, y1+(row*len_th))
            strokeWeight(2)
            point(x,y)
            coordinates.append([x,y])
            # coordinates_dict[x,y] = i
        return coordinates
        # return coordinates_dict
    else:           
        for j in range(row):# These two for loops draw the grid
            for k in range(col+1):
                stroke(0,0,0,225)# Sets the colour of the line and controls the transparancy of the line (0 is completely transparant, 255 is completely opaque)
                if mode.lower() == "square":
                    rect(x,y,len_th,len_th)
                elif mode.lower() == "triangle":
                    triangle(x,y,x+len_th,y,x+(len_th/2),y+len_th)
                x += len_th
            y += len_th
            if mode.lower() == "square":
                x = x1
            elif mode.lower() == "triangle":
                if j % 2:
                    x = x1
                else:
                    x = x1 - (len_th/2)
            
        clear_excess(col, row, len_th)

def clear_excess(col,row,len_th):
    stroke(205)
    strokeWeight(1)
    fill(205)
    rect(((displayWidth/2)+((col/2)*len_th)),((displayHeight/2)-((row/2)*len_th)),len_th*2,len_th*row)
    rect(((displayWidth/2)-((col/2)*len_th))-len_th*2,((displayHeight/2)-((row/2)*len_th)),len_th*2,len_th*row)
    stroke(0)
    line(((displayWidth/2)+((col/2)*len_th)),((displayHeight/2)-((row/2)*len_th)),((displayWidth/2)+((col/2)*len_th)),((displayHeight/2)+((row/2)*len_th)))
    line(((displayWidth/2)-((col/2)*len_th)),((displayHeight/2)-((row/2)*len_th)),((displayWidth/2)-((col/2)*len_th)),((displayHeight/2)+((row/2)*len_th)))
    
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
                strokeWeight(3)
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
            strokeWeight(3)
            point(x,y)
            xaverage_array.append(x)
            yaverage_array.append(y)
    
            fill(0)
            textSize(10)
            text(num+1,x,y)#writes a number to link the line to the walk_num
    
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
                strokeWeight(3)
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
            strokeWeight(3)
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
    print(coord)
    def getKeyX(item):
        return item[0]
    def getKeyY(item):
        return item[1]
    coord_x = sorted(coord, key=getKeyX)
    coord_y = sorted(coord, key=getKeyY)
    print()
    print("Coord_x: ",coord_x)
    print()
    print("Coord_y: ",coord_y)    
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

    for num in range(walk_num):
                
        if begin == 1:#start at centre 
            x = (displayWidth/2)
    
        elif begin == 2:#start at left 
            x = (displayWidth/2) - ((col/2)*len_th)
        
        elif begin == 3: #start at right
            x = (displayWidth/2) + ((col/2)*len_th)
            
        xpos = x
        y = (displayHeight/2)
        prevx,prevy = x,y
        temp_coord_x = []
        temp_coord_y = []

        space = abs(len_th/(row*col))
        # space = 30
        for j in range(step_num):
            while len(temp_coord_x) == 0:
                for i in range(len(coord_x)):
                    temp_x = (coord_x[i][0])
                    # print("Temp - space: ",(temp_x - space ))
                    # print("Temp + space: ",(temp_x + space ))
                    if (prevx - space ) <= temp_x <= (prevx + space):
                        temp_coord_x.append(coord_x[i])
                space += 2
            print("TempX",temp_coord_x)
            print("ABS",abs(len_th/(row*col)))
            print("new space", space)
            space = abs(len_th/(row*col))
            # space = 30
            while len(temp_coord_y) == 0:
                for i in range(len(coord_y)):
                    temp_y = (coord_y[i][0])
                    # print("Temp - space: ",(temp_y - space ))
                    # print("Temp + space: ",(temp_y + space ))
                    if (prevy - space ) <= temp_y <= (prevy + space):
                        temp_coord_y.append(coord_y[i])
                space += 2
            print("TempXY",temp_coord_y)
            print("ABS",abs(len_th/(row*col)))
            print("new space", space)
            for i in range(len(temp_coord_x)):
                stroke(255,0,0)
                strokeWeight(5)
                point(temp_coord_x[i][0], temp_coord_x[i][1])
                print("Donex")
            for i in range(len(temp_coord_y)):
                stroke(0,255,0)
                strokeWeight(5)
                point(temp_coord_y[i][0], temp_coord_y[i][1])
                print("Done y")
        # temp_coord = coord2.nearest_key((xpos,y))
        # temp_coord_x = temp_coord[0]
        # temp_coord_y = temp_coord[1]
        # stroke(0)
        # strokeWeight(1)
        # line(prevx,prevy,temp_coord_x,temp_coord_y)
        # prevx = temp_coord_x
        # prevy = temp_coord_y
        # del coord2[temp_coord]
        # avg.append([prevx,prevy])
                
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

# class NearestDict(dict):
    
#     def __init__(self, ndims):
#         super(NearestDict, self).__init__()
#         self.ndims = ndims

#     # Enforce dimensionality
#     def __setitem__(self, key, val):
#         if not isinstance(key, tuple): key = (key,)
#         if len(key) != self.ndims: raise KeyError("key must be %d dimensions" % self.ndims)
#         super(NearestDict, self).__setitem__(key, val)

#     @staticmethod
#     def __dist(ka, kb):
#         assert len(ka) == len(kb)
#         return sum((ea-eb)**2 for (ea, eb) in zip(ka, kb))

#     # Helper method and might be of use
#     def nearest_key(self, key):
#         if not isinstance(key, tuple): key = (key,)
#         nk = min((k for k in self), key=lambda k: NearestDict.__dist(key, k))
#         return nk

#     def __missing__(self, key):
#         if not isinstance(key, tuple): key = (key,)
#         if len(key) != self.ndims: raise KeyError("key must be %d dimensions" % self.ndims)
#         return self[self.nearest_key(key)]    