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
  
  drawLines(3,750,w);//num of walks, num of steps
}

void drawLines(int walknum, int stepnum, int w) {

  for (int i = 0; i < walknum; i++){
    
    int x = displayWidth / 2;
    int y = displayHeight / 2;
    
    int linecol = i % 3;
    int colour1 = 0;
    int colour2 = 0;
    int colour3 = 0;
    if (linecol == 0){
      colour1 = 255;    
    } else if (linecol == 1){
      colour2 = 255;
    } else if (linecol == 2){
      colour3 = 255;
    }
    
    for (int j = 0; j < stepnum; j++){
      int [] numbers = {0,1,2,3};
      int index = int(random(numbers.length));
      stroke(colour1, colour2, colour3);
      strokeWeight(3);
      if (numbers[index] == 0){
        line(x,y,x+w, y);
        x = x + w;
      } else if (numbers[index] == 1) {
        line(x,y,x-w,y);
        x = x - w;
      } else if (numbers[index] == 2) {
        line(x,y,x,y+w);
        y = y + w;
      } else if (numbers[index] == 3) {
        line(x,y,x,y-w);
        y = y - w;
      }
  }
  fill(0);
  textSize(12);
  text(i+1,x,y);
 }
}

//can do a dot at the final postion 