#Krishan Sritharar

#Random Walks 

import random

def setup():
    fullScreen()
    noLoop()
    
def draw():
   
    coloumn = 80
    row = 60
    space = 10
    mode = "triangle"     #"square","triangle","random"
    num_of_steps = 120
    num_of_walks = 500
    begin = 2
    name = "triangle"
    Pdown = 0.00
    Pup  = 0.00
    Pright = 0.50
    Pleft = 0.10
    Prightdown = 0.10
    Prightup = 0.10
    Pleftdown = 0.10
    Pleftup = 0.10

    grid(coloumn,row,space,mode)
    drawLines(num_of_walks, num_of_steps, coloumn, row, space, mode, begin, Pright, Pleft, Pdown, Pup, Prightdown, Prightup, Pleftdown, Pleftup)
#    saveFrame("Walk_{}.png".format(name))

def clear_excess(col,row,len_th):
    stroke(205)
    strokeWeight(1)
    fill(205)
    rect(((displayWidth/2)+((col/2)*len_th)),((displayHeight/2)-((row/2)*len_th)),len_th*2,len_th*row)
    rect(((displayWidth/2)-((col/2)*len_th))-len_th*2,((displayHeight/2)-((row/2)*len_th)),len_th*2,len_th*row)
    stroke(0)
    line(((displayWidth/2)+((col/2)*len_th)),((displayHeight/2)-((row/2)*len_th)),((displayWidth/2)+((col/2)*len_th)),((displayHeight/2)+((row/2)*len_th)))
    line(((displayWidth/2)-((col/2)*len_th)),((displayHeight/2)-((row/2)*len_th)),((displayWidth/2)-((col/2)*len_th)),((displayHeight/2)+((row/2)*len_th)))

def grid(col, row, len_th, mode):
    
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

    
def drawLines(walk_num, step_num, col, row, len_th, mode, begin, Pright, Pleft, Pdown, Pup, Prightdown, Prightup, Pleftdown, Pleftup):
    
    xaverage_array = []
    yaverage_array = []
    
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
                elif x == ((displayWidth/2) + ((col/2)*len_th)):
                    numbers = [1,4,5]#left edge
                elif y == ((displayHeight/2) + ((row/2)*len_th)) or x == ((displayWidth/2) + ((col/2)*len_th) - (len_th/2)):
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
            
            stroke(0)
            strokeWeight(3)
            point(x,y)
            xaverage_array.append(x)
            yaverage_array.append(y)
    
            fill(0)
            textSize(10)
            text(num+1,x,y)#writes a number to link the line to the walk_num
    
    
    
    sum_of_x,sum_of_y = 0,0
    
    for l in range(len(xaverage_array)):
        sum_of_x += xaverage_array[l]
        sum_of_y += yaverage_array[l]
        
    xaverage = sum_of_x / len(xaverage_array)
    yaverage = sum_of_y / len(yaverage_array)
    
    stroke(255,0,0)
    strokeWeight(3)
    line(xpos,(displayHeight/2),xaverage,yaverage)