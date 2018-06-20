//Krishan Sritharar

//Drawing the Grid 

void setup() {
  fullScreen();
  frameRate(1);
  noLoop();
  println("Width :", displayWidth);
  println("Height :", displayHeight);
}

void draw() {
  grid(80, 60, 10);// Coloumn, Row, space between each row/coloumn in pixels

}

void grid(int col, int row, int len_th) {

  int x1 = (displayWidth/2)-((col/2)*len_th); // These two lines centre the grid
  int y1 = (displayHeight/2)-((row/2)*len_th);
  
  int x = x1;
  int y = y1;
  int w = len_th;
  
  for (int i = 0; i < row; i++) { // These two for loops draw the grid
    for (int j = 0; j < col; j++) {
      stroke(0,0,0,255);// Sets the colour of the line and controls the transparancy of the line (0 is completely transparant, 255 is completely opaque)
      rect(x, y, w, w);
      x = x + w;
    }
    y = y + w;
    x = x1;
  }
  
}