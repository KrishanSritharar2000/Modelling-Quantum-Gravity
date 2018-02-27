#Krishan Sritharar

#Random Walks 
import random

def setup():
    fullScreen()
    noLoop()
    
def draw():
    
    column = 80
    row = 60
    space = 10
    mode = "square"     #"square","triangle","random"
    num_of_steps = 30
    num_of_walks = 20
    begin = 1
    name = "Sqaure30"
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
    
    x1 = (displayWidth*0.5)- ((col*0.5)*len_th)#These two lines centre the grid
    y1 = (displayHeight*0.5) - ((row*0.5)*len_th)

    x,y = x1,y1
    fill(255)
    rect(x1,y1,(col*len_th),(row*len_th))#+len_th*0.5

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
                strokeWeight(1)
                stroke(0,0,0,225)# Sets the colour of the line and controls the transparancy of the line (0 is completely transparant, 255 is completely opaque)
                if mode.lower() == "square":
                    rect(x,y,len_th,len_th)
                elif mode.lower() == "triangle":
                    triangle(x,y,x+len_th,y,x+(len_th*0.5),y+len_th)
                x += len_th
            y += len_th
            if mode.lower() == "square":
                x = x1
            elif mode.lower() == "triangle":
                if j % 2:
                    x = x1
                else:
                    x = x1 - (len_th*0.5)
            
        clear_excess(col, row, len_th)

def clear_excess(col,row,len_th):
    stroke(205)
    # stroke(0,0,0,0)
    strokeWeight(1)

    fill(205)
    rect(((displayWidth*0.5)+((col*0.5)*len_th)),((displayHeight*0.5)-((row*0.5)*len_th)),len_th*2,len_th*row)
    rect(((displayWidth*0.5)-((col*0.5)*len_th))-len_th*2,((displayHeight*0.5)-((row*0.5)*len_th)),len_th*2,len_th*row)
    stroke(0)
    line(((displayWidth*0.5)+((col*0.5)*len_th)),((displayHeight*0.5)-((row*0.5)*len_th)),((displayWidth*0.5)+((col*0.5)*len_th)),((displayHeight*0.5)+((row*0.5)*len_th)))
    line(((displayWidth*0.5)-((col*0.5)*len_th)),((displayHeight*0.5)-((row*0.5)*len_th)),((displayWidth*0.5)-((col*0.5)*len_th)),((displayHeight*0.5)+((row*0.5)*len_th)))
    
def drawLines(walk_num, step_num, col, row, len_th, mode, begin, Pright, Pleft, Pdown, Pup, Prightdown, Prightup, Pleftdown, Pleftup):
    
    xaverage_array = []
    yaverage_array = []
    avg = []
    
    if mode.lower() == "square":
        
        for num in range(walk_num):
            
            if begin == 1:#start at centre 
                x = (displayWidth*0.5)
    
            elif begin == 2:#start at left 
                x = (displayWidth*0.5) - ((col*0.5)*len_th)
            
            elif begin == 3: #start at right
                x = (displayWidth*0.5) + ((col*0.5)*len_th)
                
            xpos = x
            y = (displayHeight*0.5)
            
                    
            for j in range(step_num):
                
                if x == ((displayWidth*0.5) - ((col*0.5)*len_th)) and y == ((displayHeight*0.5) - ((row*0.5)*len_th)):#this prevent the line going off the grid
                    numbers = [0,2]
                elif x == ((displayWidth*0.5) - ((col*0.5)*len_th)) and y ==  ((displayHeight*0.5) + ((row*0.5)*len_th)):
                    numbers = [0,3]
                elif x == ((displayWidth*0.5) + ((col*0.5)*len_th)) and y == ((displayHeight*0.5) - ((row*0.5)*len_th)):#these are the corners
                    numbers = [1,2]
                elif x == ((displayWidth*0.5) + ((col*0.5)*len_th)) and y == ((displayHeight*0.5) + ((row*0.5)*len_th)):
                    numbers = [1,3]
                    
                elif x == ((displayWidth*0.5) - ((col*0.5)*len_th)):#these are the edges
                    numbers = [0,2,3]
                elif y == ((displayHeight*0.5) - ((row*0.5)*len_th)):
                    numbers = [0,1,2]
                elif x == ((displayWidth*0.5) + ((col*0.5)*len_th)):
                    numbers = [1,2,3]
                elif y == ((displayHeight*0.5) + ((row*0.5)*len_th)):
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
                x = (displayWidth*0.5)
    
            elif begin == 2:#start at left 
                x = (displayWidth*0.5) - ((col*0.5)*len_th)
            
            elif begin == 3: #start at right
                x = (displayWidth*0.5) + ((col*0.5)*len_th)
                
            xpos = x
            y = (displayHeight*0.5)
            
                    
            for j in range(step_num):
                
                if x == ((displayWidth*0.5) - ((col*0.5)*len_th)) and y == ((displayHeight*0.5) - ((row*0.5)*len_th)):#this prevent the line going off the grid
                    numbers = [0,2]#topleft
                elif x == ((displayWidth*0.5) - ((col*0.5)*len_th)) and y ==  ((displayHeight*0.5) + ((row*0.5)*len_th)):
                    numbers = [0,3]#bottomleft
                elif x == ((displayWidth*0.5) + ((col*0.5)*len_th)) and y == ((displayHeight*0.5) - ((row*0.5)*len_th)):#these are the corners
                    numbers = [1,4]#topright
                elif x == ((displayWidth*0.5) + ((col*0.5)*len_th)) and y == ((displayHeight*0.5) + ((row*0.5)*len_th)):
                    numbers = [1,5]#bottomright
                   
                elif x == ((displayWidth*0.5) - ((col*0.5)*len_th)) or x == ((displayWidth*0.5) - ((col*0.5)*len_th) + (len_th*0.5)):#these are the edges
                    numbers = [0,2,3]#left edge
                elif y == ((displayHeight*0.5) - ((row*0.5)*len_th)):
                    numbers = [0,1,2,4]#top edge
                elif x == ((displayWidth*0.5) + ((col*0.5)*len_th)) or x == ((displayWidth*0.5) + ((col*0.5)*len_th) - (len_th*0.5)):
                    numbers = [1,4,5]#right edge
                elif y == ((displayHeight*0.5) + ((row*0.5)*len_th)):
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
                    line(x,y,x+(len_th*0.5),y+len_th)#down right 
                    y += len_th
                    x += (len_th*0.5)
                elif number == 3:
                    line(x,y,x+(len_th*0.5),y-len_th)#up right
                    y -= len_th
                    x += (len_th*0.5)
                elif number == 4:
                    line(x,y,x-(len_th*0.5),y+len_th)#down left
                    y += len_th
                    x -= (len_th*0.5)
                elif number == 5:
                    line(x,y,x-(len_th*0.5),y-len_th)#up left
                    y -= len_th
                    x -= (len_th*0.5)
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

    
def find_nearest_point(find_x,find_y,col,row,coord):
    find_coord = (find_x,find_y)
    dist_x,dist_y,diagonal_dist = [],[],[]
    for i in range(col*row):
        dist_x.append(abs(coord[i][0] - find_coord[0]))
        dist_y.append(abs(coord[i][1] - find_coord[1]))
        diagonal_dist.append(round(sqrt(dist_x[i]**2 + dist_y[i]**2),2))
    print("DistX", dist_x)
    print("Disty", dist_y)
    print("Diagonal dist", diagonal_dist )
    print("Coord",coord)
    min_dist_value = min(diagonal_dist)
    print("min_dist_value",min_dist_value)
    min_dist_index = diagonal_dist.index(min_dist_value)
    print("min_dist_index",min_dist_index)
    nearest_coord_x,nearest_coord_y = coord[min_dist_index][0],coord[min_dist_index][1]
    nearest_coord = (nearest_coord_x,nearest_coord_y)
    print(nearest_coord)
    return nearest_coord

                                
                                
            
    
    
def drawLinesRandom(walk_num, step_num, col, row, len_th, begin, coord, Pright, Pleft, Pdown, Pup):

    if begin == 1:#start at centre 
        x = (displayWidth*0.5)

    elif begin == 2:#start at left 
        x = (displayWidth*0.5) - ((col*0.5)*len_th)
    
    elif begin == 3: #start at right
        x = (displayWidth*0.5) + ((col*0.5)*len_th)
        
    xpos = x
    y = (displayHeight*0.5)
    nearest_coord = find_nearest_point(xpos,y,col,row,coord)
    stroke(0,0,0,100)
    line(xpos,y,nearest_coord[0],nearest_coord[1])
    print(xpos)
    print(y)
    
    
    
    
    
    
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
    line(xpos,(displayHeight*0.5),xaverage,yaverage)
    
    
def averageline2(step_num,walk_num,average_array,xpos):
    x = xpos
    y = (displayHeight*0.5)
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
