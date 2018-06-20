//Krishan Sritharar

void setup() {
  fullScreen();
  noLoop();
  println("Width :", displayWidth);
  println("Height :", displayHeight);
}

void draw() {
  
    int coloumn = 80;
    int row = 60;
    int space = 10;
    int num_of_steps = 60;
    int num_of_walks = 50;
    int begin = 2;
    float Pright = 0.60;
    float Pleft = 0.00;
    float Pdown = 0.20;
    float Pup  = 0.20;
  
    grid(coloumn,row,space);// Coloumn, Row, space between each row/coloumn in pixels
    drawLines(num_of_steps,num_of_walks,coloumn,row,space,begin,Pright,Pleft,Pdown,Pup);//num of walks, num of steps
}

void grid(int col, int row, int len_th) {

  int x1 = (displayWidth/2)-((col/2)*len_th); // These two lines centre the grid
  int y1 = (displayHeight/2)-((row/2)*len_th);
  
  int x = x1;
  int y = y1;
  
  for (int i = 0; i < row; i++) { // These two for loops draw the grid
    for (int j = 0; j < col; j++) {
      stroke(0,0,0,255);// Sets the colour of the line and controls the transparancy of the line (0 is completely transparant, 255 is completely opaque)
      rect(x, y, len_th, len_th);
      x = x + len_th;
    }
    y = y + len_th;
    x = x1;
  }
}

void drawLines(int walknum,int stepnum,int col,int row,int len_th, int begin, float Pright, float Pleft, float Pdown, float Pup) {
  
  ArrayList<Integer> xaverage_array = new ArrayList<Integer>();
  ArrayList<Integer> yaverage_array = new ArrayList<Integer>();
  
  int x = 0;
  for (int num = 0; num < walknum; num++){
          
    if (begin == 1){
      x = (displayWidth / 2);      
    } else if (begin == 2){
      x = (displayWidth / 2) - ((col/2)*len_th);
    } else if (begin == 3){
      x = (displayWidth / 2) + ((col/2)*len_th);
    }
    
    int y = displayHeight / 2;

            
    for (int j = 0; j < stepnum; j++){
      
      ArrayList<Integer> numbers = new ArrayList<Integer>();
      numbers.add(0);
      numbers.add(1); 
      numbers.add(2); 
      numbers.add(3);
        
      if (( x == ((displayWidth/2) - ((col/2)*len_th))) && ( y == ((displayHeight/2) - ((row/2)*len_th)))){
        numbers.remove(1);
        numbers.remove(3);      
      } else if (( x == ((displayWidth/2) - ((col/2)*len_th))) && ( y == ((displayHeight/2) + ((row/2)*len_th)))){
        numbers.remove(1);
        numbers.remove(2);  
      } else if (( x == ((displayWidth/2) + ((col/2)*len_th))) && ( y == ((displayHeight/2) - ((row/2)*len_th)))){
        numbers.remove(0);
        numbers.remove(3);           
      } else if (( x == ((displayWidth/2) + ((col/2)*len_th))) && ( y == ((displayHeight/2) + ((row/2)*len_th)))){
        numbers.remove(0);
        numbers.remove(2);          
      } else if (x == ((displayWidth/2) - ((col/2)*len_th))) { 
        numbers.remove(1);   
      } else if (y == ((displayHeight/2) - ((row/2)*len_th))) {
        numbers.remove(3);    
      } else if (x == ((displayWidth/2) + ((col/2)*len_th))) {
        numbers.remove(0);
      } else if (y == ((displayHeight/2) + ((row/2)*len_th))) {
        numbers.remove(2);  
      }
      
      ArrayList<Integer> weights = new ArrayList<Integer>();
            
      for (int k = 0; k < numbers.size(); k++){
        if (numbers.get(k) == 0){
          for (int m = 0; m < Pright * 100; m++){
            weights.add(0);
          }          
        }
        if (numbers.get(k) == 1){
          for (int m = 0; m < Pleft * 100; m++){
            weights.add(1);
          }
        }
        if (numbers.get(k) == 2){
          for (int m = 0; m < Pdown * 100; m++){
            weights.add(2);
          }
        }
        if (numbers.get(k) == 3){
          for (int m = 0; m < Pup * 100; m++){
            weights.add(3);
          }      
        }
      }
            
      int index1 = int(random(weights.size()));
      int index2 = weights.get(index1);

      stroke(0);
      strokeWeight(3);
     
      if ((index2) == 0){
        line(x,y,x+len_th, y);
        x = x + len_th;
      } else if ((index2) == 1) {
        line(x,y,x-len_th,y);
        x = x - len_th;
      } else if ((index2) == 2) {
        line(x,y,x,y+len_th);
        y = y + len_th;
      } else if ((index2) == 3) {
        line(x,y,x,y-len_th);
        y = y - len_th;
      }
    }
  stroke(0);
  strokeWeight(3);
  point(x,y);
  xaverage_array.add(x);
  yaverage_array.add(y);

  fill(0);
  textSize(12);
  text(num+1,x,y);
    
}
int sum_of_x = 0;
int sum_of_y = 0;
   
for (int l = 0; l < xaverage_array.size(); l++){
  sum_of_x = sum_of_x + xaverage_array.get(l);
  sum_of_y = sum_of_y + yaverage_array.get(l);
}
     
int xaverage = sum_of_x / xaverage_array.size();
int yaverage = sum_of_y / yaverage_array.size();
 
stroke(255,0,0);
strokeWeight(4);

 int xpos = 0;
if (begin == 1){
  xpos = (displayWidth / 2);      
} else if (begin == 2){
  xpos = (displayWidth / 2) - ((col/2)*len_th);
} else if (begin == 3){
  xpos = (displayWidth / 2) + ((col/2)*len_th); 
}
  
line(xpos,(displayHeight/2),xaverage,yaverage);
}