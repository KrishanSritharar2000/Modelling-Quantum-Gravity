#Krishan Sritharar

#Random Walks 
import random

def setup():
    fullScreen()
    noLoop()
    
def draw():

    column = 32
    row = 24
    space = 30
    mode = "square"     #"square","triangle","random"
    num_of_steps = 60
    num_of_walks = 50
    begin = 2
    name = "Triangle Grid 5x5"
    Pdown = 0.20
    Pup  = 0.20
    Pright = 0.60
    Pleft = 0.00
    Prightdown = 0.10
    Prightup = 0.10
    Pleftdown = 0.10
    Pleftup = 0.10
    
    coordinates = []
    # coordinates_dict = NearestDict(2)
     
    grid(column,row,space,mode, coordinates) 
    drawPlanets(column,row,space) 
    if mode.lower() == "square" or mode.lower() == "triangle":
        drawLines(num_of_walks, num_of_steps, column, row, space, mode, begin, Pright, Pleft, Pdown, Pup, Prightdown, Prightup, Pleftdown, Pleftup)
    # elif mode.lower() == "random":
    #    drawLinesRandom(num_of_walks, num_of_steps, column, row, space, begin,coordinates, Pright, Pleft, Pdown, Pup)
    # saveFrame("Walk_{}.png".format(name))


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
    
    
    
def drawPlanets(col,row,len_th):
    
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
    
    # cornerPlanet_x = (displayWidth*0.5) - (col*0.125*len_th)    
    # cornerPlanet_y = (displayHeight*0.5) + (row*0.125*len_th)  
    # centrePlanet_x = (displayWidth*0.5)
    # centrePlanet_y = (displayHeight*0.5) + (int(row*0.25)*len_th)
    # space = len_th*0.5    
    # fill(255)
    # strokeWeight(1)
    # rect(cornerPlanet_x,cornerPlanet_y,(col*0.25)*len_th,(row*0.25)*len_th)
    # x,y = cornerPlanet_x,cornerPlanet_y
    # for i in range(int(0.5*row)):#30
    #     for j in range(int(0.5*col)):#40
    #         stroke(0,0,0,255)
    #         rect(x,y,space,space)
    #         x += space
    #     y += space
    #     x = cornerPlanet_x
        
    # cornerPlanet_x = (displayWidth*0.5) - (col*0.0625*len_th)    
    # cornerPlanet_y = (displayHeight*0.5) + (row*0.1875*len_th)  
    # space = len_th*0.25    
    # rect(cornerPlanet_x,cornerPlanet_y,(col*0.125)*len_th,(row*0.125)*len_th)
    # x,y = cornerPlanet_x,cornerPlanet_y
    # for i in range(int(0.5*row)):#30
    #     for j in range(int(0.5*col)):#40
    #         stroke(0,0,0,255)
    #         rect(x,y,space,space)
    #         x += space
    #     y += space
    #     x = cornerPlanet_x    

    # cornerPlanet_x = (displayWidth*0.5) - (col*(0.0625/2)*len_th)   
    # cornerPlanet_y = (displayHeight*0.5) + (row*(0.1875+(0.0625/2))*len_th)  

    # rect(cornerPlanet_x,cornerPlanet_y,(col*(0.125/2))*len_th,(row*0.0625)*len_th)






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
    min_dist_value = min(diagonal_dist)
    min_dist_index = diagonal_dist.index(min_dist_value)
    nearest_coord_x,nearest_coord_y = coord[min_dist_index][0],coord[min_dist_index][1]
    nearest_coord = (nearest_coord_x,nearest_coord_y,min_dist_index)
    return nearest_coord

def remove_from_coord(index,coord,col,row):
    x,y = coord[index][0],coord[index][1]
    for i in range(col*row):
        if coord[i][0] == x and coord[i][1] == y:
            coord[i].pop()
            coord[i].pop()
    coord = filter(None,coord)            
    return coord

    
def find_points(x,y,index,coord,col,row):
    print("x",x)
    print("y",y)
    print("Original coord",coord)

    print("Updated coord",coord)
    leftup,rightup,leftdown,rightdown = False,False,False,False
    leftup_count,rightup_count,leftdown_count,rightdown_count = 0,0,0,0
    leftup_array,rightup_array,leftdown_array,rightdown_array = [],[],[],[]
    max_count = int(round(sqrt(row*col)/2,0))
    dist_x,dist_y,diagonal_dist,numbers = [],[],[],[]
    # points_removed = 1
    for i in range(col*row-1):
        dist_x.append(abs(coord[i][0] - x))
        dist_y.append(abs(coord[i][1] - y))
        diagonal_dist.append(round(sqrt(dist_x[i]**2 + dist_y[i]**2),2))
    max_value = max(diagonal_dist)
    print("A",diagonal_dist)
    print("Maxcount",max_count)
    loops = 0
    while (leftup == False or rightup == False or leftdown == False or rightdown == False) and loops < (col*row*2):
        temp_min = min(diagonal_dist)
        print("tempmin",temp_min)
        temp_min_index = diagonal_dist.index(temp_min)
        print("tempminindex", temp_min_index)
        if leftup_count < max_count:
            if coord[temp_min_index][0] < x and coord[temp_min_index][1] < y:#to the left and up
                leftup = True
                leftup_count +=1
                print("leftup_count",leftup_count)
                leftup_array.append((coord[temp_min_index][0],coord[temp_min_index][1]))
                numbers.append(0)
                diagonal_dist.pop(temp_min_index)
                diagonal_dist.insert(temp_min_index,(max_value*1000))
        if rightup_count < max_count:
            if coord[temp_min_index][0] > x and coord[temp_min_index][1] < y:#to the left and up
                rightup = True
                rightup_count +=1
                print("rightup_count",rightup_count)
                rightup_array.append((coord[temp_min_index][0],coord[temp_min_index][1]))                
                numbers.append(1)
                diagonal_dist.pop(temp_min_index)   
                diagonal_dist.insert(temp_min_index,(max_value*1000))
        if leftdown_count < max_count:
            if coord[temp_min_index][0] < x and coord[temp_min_index][1] > y:#to the left and up
                leftdown = True
                leftdown_count +=1
                print("leftdown_count",leftdown_count)
                leftdown_array.append((coord[temp_min_index][0],coord[temp_min_index][1]))                
                numbers.append(2)
                diagonal_dist.pop(temp_min_index)
                diagonal_dist.insert(temp_min_index,(max_value*1000))
        if rightdown_count < max_count:
            if coord[temp_min_index][0] > x and coord[temp_min_index][1] > y:#to the left and up
                rightdown = True
                rightdown_count +=1
                print("rightdown_count",rightdown_count)
                rightdown_array.append((coord[temp_min_index][0],coord[temp_min_index][1]))                
                numbers.append(3)
                diagonal_dist.pop(temp_min_index)
                diagonal_dist.insert(temp_min_index,(max_value*1000))
        loops += 1
        print()
        print("New",diagonal_dist)
        print("Numbers",numbers, "loop",loops)
        print("leftup_array ",leftup_array)
        print("rightup_array ",rightup_array)
        print("leftdown_array ",leftdown_array)
        print("rightdown_array ",rightdown_array)
    if len(leftup_array) == 0:
        leftup_array = [()]
    if len(rightup_array) == 0:
        rightup_array = [()]
    if len(leftdown_array) == 0:
        leftdown_array = [()]
    if len(rightdown_array) == 0:
        rightdown_array = [()]
    # all_arrays = (leftup_array + rightup_array + leftdown_array + rightdown_array)
    print("all Arrays", all_arrays)

    # return all_arrays
    # global numbers,leftup_array,rightup_array,leftdown_array,rightdown_array    

    
    
def drawLinesRandom(walk_num, step_num, col, row, len_th, begin, coord, Prightdown, Prightup, Pleftdown, Pleftup):
    if begin == 1:#start at centre 
        x = (displayWidth*0.5)

    elif begin == 2:#start at left 
        x = (displayWidth*0.5) - ((col*0.5)*len_th)
    
    elif begin == 3: #start at right
        x = (displayWidth*0.5) + ((col*0.5)*len_th)
        
    xpos = x
    y = (displayHeight*0.5)        
    
    nearest_coord = find_nearest_point(xpos,y,col,row,coord)
    stroke(255,0,0,100)
    line(xpos,y,nearest_coord[0],nearest_coord[1])
    x,y,index = nearest_coord[0],nearest_coord[1],nearest_coord[2]
    # print(x,y,index)   
    coord = remove_from_coord(index,coord,col,row)

    xaverage_array = []
    yaverage_array = []    
    avg = []
        
    for num in range(walk_num):

        # result = find_points(x,y,index,coord,col,row)
        x,y = nearest_coord[0],nearest_coord[1]
        print("x",x)
        print("y",y)
        print("Original coord",coord)
    
        print("Updated coord",coord)
        leftup,rightup,leftdown,rightdown = False,False,False,False
        leftup_count,rightup_count,leftdown_count,rightdown_count = 0,0,0,0
        leftup_array,rightup_array,leftdown_array,rightdown_array = [],[],[],[]
        max_count = int(round(sqrt(row*col)/2,0))
        dist_x,dist_y,diagonal_dist,numbers = [],[],[],[]
        # points_removed = 1
        for i in range(col*row-1):
            dist_x.append(abs(coord[i][0] - x))
            dist_y.append(abs(coord[i][1] - y))
            diagonal_dist.append(round(sqrt(dist_x[i]**2 + dist_y[i]**2),2))
        max_value = max(diagonal_dist)
        print("A",diagonal_dist)
        print("Maxcount",max_count)
        loops = 0        
        multiple_numbers = []
                                
        for j in range(step_num):
            
            prevx,prevy = x,y
            
            
            while (leftup == False or rightup == False or leftdown == False or rightdown == False) and loops < (col*row*2):
                temp_min = min(diagonal_dist)
                print("tempmin",temp_min)
                temp_min_index = diagonal_dist.index(temp_min)
                print("tempminindex", temp_min_index)
                if leftup_count < max_count:
                    if coord[temp_min_index][0] < x and coord[temp_min_index][1] < y:#to the left and up
                        leftup = True
                        leftup_count +=1
                        print("leftup_count",leftup_count)
                        leftup_array.append((coord[temp_min_index][0],coord[temp_min_index][1]))
                        numbers.append(0)
                        diagonal_dist.pop(temp_min_index)
                        diagonal_dist.insert(temp_min_index,(max_value*1000))
                if rightup_count < max_count:
                    if coord[temp_min_index][0] > x and coord[temp_min_index][1] < y:#to the left and up
                        rightup = True
                        rightup_count +=1
                        print("rightup_count",rightup_count)
                        rightup_array.append((coord[temp_min_index][0],coord[temp_min_index][1]))                
                        numbers.append(1)
                        diagonal_dist.pop(temp_min_index)   
                        diagonal_dist.insert(temp_min_index,(max_value*1000))
                if leftdown_count < max_count:
                    if coord[temp_min_index][0] < x and coord[temp_min_index][1] > y:#to the left and up
                        leftdown = True
                        leftdown_count +=1
                        print("leftdown_count",leftdown_count)
                        leftdown_array.append((coord[temp_min_index][0],coord[temp_min_index][1]))                
                        numbers.append(2)
                        diagonal_dist.pop(temp_min_index)
                        diagonal_dist.insert(temp_min_index,(max_value*1000))
                if rightdown_count < max_count:
                    if coord[temp_min_index][0] > x and coord[temp_min_index][1] > y:#to the left and up
                        rightdown = True
                        rightdown_count +=1
                        print("rightdown_count",rightdown_count)
                        rightdown_array.append((coord[temp_min_index][0],coord[temp_min_index][1]))                
                        numbers.append(3)
                        diagonal_dist.pop(temp_min_index)
                        diagonal_dist.insert(temp_min_index,(max_value*1000))
                loops += 1
                print()
                print("New",diagonal_dist)
                print("Numbers",numbers, "loop",loops)
                print("leftup_array ",leftup_array)
                print("rightup_array ",rightup_array)
                print("leftdown_array ",leftdown_array)
                print("rightdown_array ",rightdown_array)
            if len(leftup_array) == 0:
                leftup_array = [()]
            if len(rightup_array) == 0:
                rightup_array = [()]
            if len(leftdown_array) == 0:
                leftdown_array = [()]
            if len(rightdown_array) == 0:
                rightdown_array = [()]
            # all_arrays = (leftup_array + rightup_array + leftdown_array + rightdown_array)
            # print("all Arrays", all_arrays)
        
            # return all_arrays
            # global numbers,leftup_array,rightup_array,leftdown_array,rightdown_array    
            
            # leftup_array,rightup_array,leftdown_array,rightdown_array =  result[0],result[1],result[2],result[3]
            print("leftup",leftup_array)
            print("rightup",rightup_array)
            print("leftdown",leftdown_array)
            print("rightdown",rightdown_array)
            
            for i in range(4):
                temp_count = numbers.count(i)
                print(i,"tempcount: ",temp_count)
                if temp_count > 1:
                    for j in range(temp_count-1):
                        multiple_numbers.append(i)
                        print("multi numbers",multiple_numbers)
                        numbers.remove(i)
                print("NumBers", numbers)
                print("multi numbers",multiple_numbers)
            weights = [] 
            
            for i in range(len(numbers)):
                if numbers[i] == 0:
                    for k in range(int(Pleftup*100)):
                        weights.append(0)
                if numbers[i] == 1:
                    for k in range(int(Prightup*100)):
                        weights.append(1)
                if numbers[i] == 2:
                    for k in range(int(Pleftdown*100)):
                        weights.append(2)
                if numbers[i] == 3:
                    for k in range(int(Prightdown*100)):
                        weights.append(3)
                
            
            number = random.choice(weights)#generates a random number
            stroke(0,0,0,105)
            strokeWeight(3)
            print("leftup",leftup_array)
            print("rightup",rightup_array)
            print("leftdown",leftdown_array)
            print("rightdown",rightdown_array)
            print("prevx",prevx)
            print("prevy", prevy)
            stroke(0,0,0,100)
            if len(numbers) == 0:
                temp_amount_random_number = int(random.randint(0, col*row-1))
                line(prevx,prevy,coord[temp_amount_random_number][0],coord[temp_amount_random_number][1])
            elif number == 0:#leftup
                if multiple_numbers.count(0) == 0:
                    # print("AAAAAA",prevx,prevy,leftup_array[0],leftup_array[1])
                    stroke(0,0,0,100)
                    line(prevx,prevy,leftup_array[0][0],leftup_array[0][1])
                    x,y = leftup_array[0][0],leftup_array[0][1]
                elif multiple_numbers.count(0) >= 1:
                    temp_amount = multiple_numbers.count(0)
                    temp_amount_random_number = int(random.randint(0, temp_amount))
                    stroke(0,0,0,100)
                    line(prevx,prevy,leftup_array[temp_amount_random_number][0],leftup_array[temp_amount_random_number][1])
                    x,y = leftup_array[temp_amount_random_number][0],leftup_array[temp_amount_random_number][1]            
            elif number == 1:#rightup
                if multiple_numbers.count(1) == 0:
                    # print("BBBBBB",prevx,prevy,rightup_array[0],rightup_array[1])
                    stroke(0,0,0,100)
                    line(prevx,prevy,rightup_array[0][0],rightup_array[0][1])
                    x,y = rightup_array[0][0],rightup_array[0][1]
                elif multiple_numbers.count(1) >= 1:
                    temp_amount = multiple_numbers.count(1)
                    temp_amount_random_number = int(random.randint(0, temp_amount))
                    stroke(0,0,0,100)
                    line(prevx,prevy,rightup_array[temp_amount_random_number][0],rightup_array[temp_amount_random_number][1])
                    x,y = rightup_array[temp_amount_random_number][0],rightup_array[temp_amount_random_number][1] 
            elif number == 2:#leftdown
                if multiple_numbers.count(2) == 0:
                    # print("CCCCCC",prevx,prevy,leftdown_array[0],leftdown_array[1])
                    stroke(0,0,0,100)
                    line(prevx,prevy,leftdown_array[0][0],leftdown_array[0][1])
                    x,y = leftdown_array[0][0],leftdown_array[0][1]
                elif multiple_numbers.count(2) >= 1:
                    temp_amount = multiple_numbers.count(2)
                    temp_amount_random_number = int(random.randint(0, temp_amount))
                    stroke(0,0,0,100)
                    line(prevx,prevy,leftdown_array[temp_amount_random_number][0],leftdown_array[temp_amount_random_number][1])
                    x,y = leftdown_array[temp_amount_random_number][0],leftdown_array[temp_amount_random_number][1] 
            elif number == 3:#rightdown
                if multiple_numbers.count(3) == 0:
                    # print("DDDDDDDD", prevx,prevy,rightdown_array[0],rightdown_array[1])
                    stroke(0,0,0,100)
                    line(prevx,prevy,rightdown_array[0][0],rightdown_array[0][1])
                    x,y = rightdown_array[0][0],rightdown_array[0][1]
                elif multiple_numbers.count(3) >= 1:
                    temp_amount = multiple_numbers.count(3)
                    temp_amount_random_number = int(random.randint(0, temp_amount))
                    stroke(0,0,0,100)
                    line(prevx,prevy,rightdown_array[temp_amount_random_number][0],rightdown_array[temp_amount_random_number][1])
                    x,y = rightdown_array[temp_amount_random_number][0],rightdown_array[temp_amount_random_number][1] 
                     
        avg.append([x,y])        
    xaverage_array.append(x)
    yaverage_array.append(y)

    fill(0)
    textSize(10)
    text(num+1,x,y)#writes a number to link the line to the walk_num
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