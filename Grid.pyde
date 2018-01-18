#Krishan Sritharar

#Drawing the Grid 

def setup():
    fullScreen()
    frameRate(1)
    noLoop()
    
def draw():
    grid(80,60,10)# Coloumn, Row, space between each row/coloumn in pixels
    
def grid(col, row, len_th):
    
    x1 = (displayWidth/2)- ((col/2)*len_th)#These two lines centre the grid
    y1 = (displayHeight/2) - ((row/2)*len_th)

    x,y,w = x1,y1,len_th
    
    for i in range(row):# These two for loops draw the grid
        for j in range(col):
            stroke(0,0,0,255)# Sets the colour of the line and controls the transparancy of the line (0 is completely transparant, 255 is completely opaque)
            rect(x,y,w,w)
            x += w
        y += w
        x = x1
    