#Krishan Sritharar

#Random Walks 
import random
import time

def setup():
    fullScreen()
    noLoop()
    
def draw():

    column = 80
    row = 60
    space = 10
    mode = "square"     #"square","triangle","random"
    num_of_steps = 10
    num_of_walks = 1000
    begin = 2
    planet = False
    planet_position = 1
    name = "Square_Grid_PRight=0.7_10_Steps_ "
    Pdown = 0.15
    Pup  = 0.15
    Pright = 0.70
    Pleft = 0.0
    Prightdown = 0.10
    Prightup = 0.10
    Pleftdown = 0.10
    Pleftup = 0.10
    
    coordinates = []
    # coordinates_dict = NearestDict(2)
    
    for i in range(10):
        num_i = i+1
        print(num_i)
        start_ = time.time()
        grid(column,row,space,mode, coordinates) 
        if planet == True:
            drawPlanets(column,row,space,planet_position) 
        if mode.lower() == "square" or mode.lower() == "triangle":
            drawLines(num_of_walks, num_of_steps, column, row, space, mode, begin, planet, planet_position, Pright, Pleft, Pdown, Pup, Prightdown, Prightup, Pleftdown, Pleftup, name, num_i)
        elif mode.lower() == "random":
            drawLinesRandom(num_of_walks, num_of_steps, column, row, space, begin,coordinates, Pright, Pleft, Pdown, Pup)
        saveFrame("Walk_{}{}_BlueLine.png".format(name,num_i))
        end_ = time.time()
        print( "The total time taken to simulate was: ", round(end_-start_,2))


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
    
    
    
def drawPlanets(col,row,len_th,position):
    if position == 1:
        for i in range(2):
            if i == 0:
                size_x = 0.125
                size_y = 0.125
                space_multi = 0.5
            elif i == 1:
                size_x = 0.0625
                size_y = 0.1875
                space_multi = 0.25
            cornerPlanet_x = (displayWidth*0.5) - (col*size_x*len_th)    
            cornerPlanet_y = (displayHeight*0.5) + (row*size_y*len_th)  
            centrePlanet_x = (displayWidth*0.5)
            centrePlanet_y = (displayHeight*0.5) + (int(row*0.25)*len_th)
            space = len_th*space_multi    
            fill(255)
            strokeWeight(1)
            rect(cornerPlanet_x,cornerPlanet_y,(col*(space_multi/2))*len_th,(row*(space_multi/2))*len_th)
            x,y = cornerPlanet_x,cornerPlanet_y
            for i in range(int(0.5*row)):#30
                for j in range(int(0.5*col)):#40
                    stroke(0,0,0,255)
                    rect(x,y,space,space)
                    x += space
                y += space
                x = cornerPlanet_x
        cornerPlanet_x = (displayWidth*0.5) - (col*(0.0625/2)*len_th)   
        cornerPlanet_y = (displayHeight*0.5) + (row*(0.1875+(0.0625/2))*len_th)  
        rect(cornerPlanet_x,cornerPlanet_y,(col*(0.125/2))*len_th,(row*0.0625)*len_th)
    elif position == 2:
        for i in range(2):
            if i == 0:
                size_x = 0.125
                size_y = 0.125
                space_multi = 0.5
            elif i == 1:
                size_x = 0.0625
                size_y = 0.0625
                space_multi = 0.25
            cornerPlanet_x = (displayWidth*0.5) - (col*size_x*len_th)    
            cornerPlanet_y = (displayHeight*0.5) - (row*size_y*len_th)  
            centrePlanet_x = (displayWidth*0.5)
            centrePlanet_y = (displayHeight*0.5)
            space = len_th*space_multi    
            fill(255)
            strokeWeight(1)
            rect(cornerPlanet_x,cornerPlanet_y,(col*(space_multi/2))*len_th,(row*(space_multi/2))*len_th)
            x,y = cornerPlanet_x,cornerPlanet_y
            for i in range(int(0.5*row)):#30
                for j in range(int(0.5*col)):#40
                    stroke(0,0,0,255)
                    rect(x,y,space,space)
                    x += space
                y += space
                x = cornerPlanet_x
        cornerPlanet_x = (displayWidth*0.5) - (col*(0.0625/2)*len_th)   
        cornerPlanet_y = (displayHeight*0.5) - (row*(0.0625/2)*len_th)  
        rect(cornerPlanet_x,cornerPlanet_y,(col*0.0625)*len_th,(row*0.0625)*len_th)
    if position == 3:
        for i in range(2):
            if i == 0:
                size_x = 0.125
                size_y = 0.375
                space_multi = 0.5
            elif i == 1:
                size_x = 0.0625
                size_y = 0.3125
                space_multi = 0.25
            cornerPlanet_x = (displayWidth*0.5) - (col*size_x*len_th)    
            cornerPlanet_y = (displayHeight*0.5) - (row*size_y*len_th)  
            centrePlanet_x = (displayWidth*0.5)
            centrePlanet_y = (displayHeight*0.5) - (int(row*0.25)*len_th)
            space = len_th*space_multi    
            fill(255)
            strokeWeight(1)
            rect(cornerPlanet_x,cornerPlanet_y,(col*(space_multi/2))*len_th,(row*(space_multi/2))*len_th)
            x,y = cornerPlanet_x,cornerPlanet_y
            for i in range(int(0.5*row)):#30
                for j in range(int(0.5*col)):#40
                    stroke(0,0,0,255)
                    rect(x,y,space,space)
                    x += space
                y += space
                x = cornerPlanet_x
        cornerPlanet_x = (displayWidth*0.5) - (col*(0.0625/2)*len_th)   
        cornerPlanet_y = (displayHeight*0.5) - (row*(0.25+(0.0625/2))*len_th)  
        rect(cornerPlanet_x,cornerPlanet_y,(col*(0.125/2))*len_th,(row*0.0625)*len_th)

def drawLines(walk_num, step_num, col, row, len_th, mode, begin, planet, position, Pright, Pleft, Pdown, Pup, Prightdown, Prightup, Pleftdown, Pleftup, name, num_i):
    
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
#            y = ((displayHeight*0.5) + (col*0.136*len_th))
            y = (displayHeight*0.5)
            ypos = y
            

            
            for j in range(step_num):
                
                Pright1 = Pright
                Pleft1 = Pleft
                Pup1 = Pup
                Pdown1 = Pdown
                space = len_th

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
                
                if planet == True:
                    if position == 1:
                        if (((displayWidth*0.5) - (col*0.125*len_th)) < x < ((displayWidth*0.5) + (col*0.125*len_th))):
                            if (((displayHeight*0.5) + (row*0.125*len_th)) < y < ((displayHeight*0.5) + (row*0.375*len_th))):
                                space = len_th*0.5
                                if y >= ((displayHeight*0.5) - (row*0.25*len_th)):
#                                    # Pright1 = Pright + (0.2*Pleft)
#                                   # Pleft1 =  (0.8*Pleft)
                                    Pup1 = (0.8*Pup)
                                    Pdown1 = Pdown + (0.2*Pup)
                                else:
#                                    # Pright1 = Pright + (0.2*Pleft)
#                                    # Pleft1 =  (0.8*Pleft)
                                    Pdown1 = (0.8*Pdown)
                                    Pup1 = Pup + (0.2*Pdown)
                                    
                        if (((displayWidth*0.5) - (col*0.0625*len_th)) < x < ((displayWidth*0.5) + (col*0.0625*len_th))):
                            if (((displayHeight*0.5) + (row*0.1875*len_th)) < y < ((displayHeight*0.5) + (row*0.325*len_th))):
                                space = len_th*0.25
                                if y >= ((displayHeight*0.5) - (row*0.25*len_th)):
 #                                   # Pright1 = Pright + (0.4*Pleft)
 #                                   # Pleft1 =  (0.6*Pleft)
                                    Pup1 = (0.6*Pup)
                                    Pdown1 = Pdown + (0.4*Pup)
                                else:
 #                                   # Pright1 = Pright + (0.4*Pleft)
 #                                   # Pleft1 =  (0.6*Pleft)
                                    Pdown1 = (0.6*Pdown)
                                    Pup1 = Pup + (0.4*Pdown)
                        if (((displayWidth*0.5) - (col*0.03125*len_th)) <= x <= ((displayWidth*0.5) + (col*0.03125*len_th))):
                            if (((displayHeight*0.5) + (row*0.21875*len_th)) <= y <= ((displayHeight*0.5) + (row*0.29375*len_th))):
                                space = 0

                    elif position == 2:
                        if (((displayWidth*0.5) - (col*0.125*len_th)) <= x <= ((displayWidth*0.5) + (col*0.125*len_th))) and (((displayHeight*0.5) - (row*0.125*len_th)) <= y <= ((displayHeight*0.5) + (row*0.125*len_th))):
                            space = len_th*0.5
                        if (((displayWidth*0.5) - (col*0.0625*len_th)) <= x <= ((displayWidth*0.5) + (col*0.0625*len_th))) and (((displayHeight*0.5) - (row*0.0625*len_th)) <= y <= ((displayHeight*0.5) + (row*0.0625*len_th))):
                            space = len_th*0.25
                        if (((displayWidth*0.5) - (col*(0.0625/2)*len_th)) <= x <= ((displayWidth*0.5) + (col*(0.0625/2)*len_th))) and (((displayHeight*0.5) - (row*(0.0625/2)*len_th)) <= y <= ((displayHeight*0.5) + (row*(0.0625/2)*len_th))):
                            space = 0
                    elif position == 3:
                        if (((displayWidth*0.5) - (col*0.125*len_th)) <= x <= ((displayWidth*0.5) + (col*0.125*len_th))) and (((displayHeight*0.5) - (row*0.125*len_th)) <= y <= ((displayHeight*0.5) + (row*0.125*len_th))):
                            space = len_th*0.5
                        if (((displayWidth*0.5) - (col*0.0625*len_th)) <= x <= ((displayWidth*0.5) + (col*0.0625*len_th))) and (((displayHeight*0.5) - (row*0.0625*len_th)) <= y <= ((displayHeight*0.5) + (row*0.0625*len_th))):
                            space = len_th*0.25
                        if (((displayWidth*0.5) - (col*(0.0625/2)*len_th)) <= x <= ((displayWidth*0.5) + (col*(0.0625/2)*len_th))) and (((displayHeight*0.5) - (row*0.25-(0.0625/2)*len_th)) <= y <= ((displayHeight*0.5) + (row*0.25+(0.0625/2)*len_th))):
                            space = 0
                weights = [] 
                
                for i in range(len(numbers)):
                    if numbers[i] == 0:
                        for k in range(int(Pright1*100)):
                            weights.append(0)
                    if numbers[i] == 1:
                        for k in range(int(Pleft1*100)):
                            weights.append(1)
                    if numbers[i] == 2:
                        for k in range(int(Pdown1*100)):
                            weights.append(2)
                    if numbers[i] == 3:
                        for k in range(int(Pup1*100)):
                            weights.append(3)
                number = random.choice(weights)#generates a random number
                stroke(0)
                strokeWeight(2)
                if number == 0:
                    line(x,y,x+space,y)#right
                    x += space
                elif number == 1:
                    line(x,y,x-space,y)#left
                    x -= space
                elif number == 2:
                    line(x,y,x,y+space)#down
                    y += space
                elif number == 3:
                    line(x,y,x,y-space)#up
                    y -= space

                avg.append([x,y])

            # print("Average = ",avg)
            
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
            
    averageline1(xaverage_array,yaverage_array,xpos,ypos,num_i)
    saveFrame("Walk_{}{}_RedLine.png".format(name,num_i))
    averageline2(step_num,walk_num,avg,xpos,ypos)

def averageline1(xaverage_array,yaverage_array,xpos,ypos,num_i): 
        
    sum_of_x,sum_of_y = 0,0
    
    for l in range(len(xaverage_array)):
        sum_of_x += xaverage_array[l]
        sum_of_y += yaverage_array[l]
        
    xaverage = sum_of_x / len(xaverage_array)
    yaverage = sum_of_y / len(yaverage_array)
    
    mean_distance = sqrt(((xaverage-xpos)**2)+((yaverage-ypos)**2))
    
    stroke(255,0,0)
    strokeWeight(3)
    line(xpos,ypos,xaverage,yaverage)
    print("The Mean Distance Full For Step ",num_i," Is:", mean_distance)
    print("The Mean Distance Rounded For Step ", num_i," Is:", round(mean_distance,4))
    
    
def averageline2(step_num,walk_num,average_array,xpos,ypos):
    x = xpos
    y = ypos
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
        # print("Xaverage_t:", xaverage_t)
        
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
    # print("This is the average_array", average_array)
