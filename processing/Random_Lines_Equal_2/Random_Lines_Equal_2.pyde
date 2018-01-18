'''Krishan Sritharar 21/01/2018'''

'''This is the first task of equal chance in all directions on Processing'''

import random 

def grid(col,row,len_th,step_num,walk_num):
    
    grid_size = [[1]*col for n in range(row)]
    w = len_th
    half_col, half_row = (col/2),(row/2)#Finds the centre of the grid
    print(grid_size)
    x,y = 0,0#This draws the grid
    for row_ in grid_size:
        for col_ in row_:
            rect(x,y,w,w)
            x += w
        y += w
        x = 0 
    

    for i in range(walk_num):
        x = half_col * w
        y = half_row * w#goes to the centre
#        print(x,y)
        
        lin_col = i % 3#sets different colours for lines
        if lin_col == 0:
            colour1, colour2, colour3 = 255,0,0#colour of line
        elif lin_col == 1:
            colour1, colour2, colour3 = 0,255,0
        elif lin_col == 2:
            colour1, colour2, colour3 = 0,0,255
        global colour1,colour2,colour3
#        print("This is lin_col:", lin_col)
                
        for j in range(step_num):
            
            if x == 0 and y == 0:#this prevent the line going off the grid
                numbers = [0,2]
            elif x == 0 and y == (row*len_th):
                numbers = [0,3]
            elif x == (col*len_th) and y == 0:#these are the corners
                numbers = [1,2]
            elif x == (col*len_th)and y == (row*len_th):
                numbers = [1,3]
                
            elif x == 0:#these are the edges
                numbers = [0,2,3]
            elif y == 0:
                numbers = [0,1,2]
            elif x == (col*len_th):
                numbers = [1,2,3]
            elif y == (row*len_th):
                numbers = [0,1,3]
            else:
                numbers = [0,1,2,3]

            
            number = random.choice(numbers)#generates a random number
#            print(x,y,numbers,number)        
            stroke(colour1,colour2,colour3)#colour of the line
            strokeWeight(3)#weight (i.e size) of the line's outline
            
            if number == 0:
                line(x,y,x+w,y)#right
                x += w
            elif number == 1:
                line(x,y,x-w,y)#left
                x -= w
            elif number == 2:
                line(x,y,x,y+w)#down
                y += w
            elif number == 3:
                line(x,y,x,y-w)#up
                y -= w
            print("X and Y are",x,y)

        fill(0)
        textSize(12)
        distx,disty = x,y#this is so the text is not displayed off the grid
        if x == (col*len_th):
            distx = x-10
        elif x == 0:
            distx = x+10
        if y == (row*len_th):
            disty = y-10
        elif y == 0:
            disty = y+10
        global distx, disty
        text(i+1,distx,disty)#writes a number to link the line to the walk_num
    
def setup():
    size(wid_th,hei_ght)
    grid(COLOUMN,ROW,LENGTH,STEPS,WALKS)#col,row,len_th,step_num,walk_num
    frameRate(1)
    noLoop()
    
'''THE INPUTS'''
COLOUMN = 21#col is the number of coloums
ROW = 21#row is the number of rows
LENGTH = 40#len_th is the size of the boxes, i.e the space between each row and coloumn
STEPS = 10#step_num is the number of steps
WALKS = 3#walk_num is the number of steps

'''This sets the size of the window'''
wid_th = COLOUMN * LENGTH # col * len_th 
hei_ght =  ROW * LENGTH# row * len_th
global wid_th, hei_ght



                      