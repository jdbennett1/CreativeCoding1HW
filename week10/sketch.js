var x1 = 200;
var x2 = 140;

var y1 = 95;

var y = 75;
var y2 = 168;

var z1 = 132.5
var z2 = 210
var movement = 4;
var size = 22;
var count = 0;
var sizeDirection = 10;

function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220);
    ellipse(95,y1,75,67.5);
    ellipse(245,y2,75,67.5);
    square(95,135,75);
    square(170,135,75);
    circle(170,285,75);
    square(z1,z2,75);

    line(95,210,132.5,285);
    line(245,210,207.5,285);

    triangle(143,135,170,75,197,135);
    circle(170,60,60);
    circle(x1,y,18);
    circle(x2,y,18);
    square(140,60,60);

    point(x2,75);
    point(x1,75);
    circle(155,75,12);
    circle(185,75,12);
    point(185,75);
    point(155,75);
    
    if (x1 >= 400 || x1 <= 0) {
      movement *= -1;
    }
    x1 += movement;
  if (x2 >= 400 || x2 <= 0) {
      movement *= -1;
    }
    x2 += movement;
  
  if (y1 >= 400 || y1 <= 0) {
      movement *= -1;
    }
    y1 += movement;
  
  if (y2 >= 500 || y2 <= 0) {
      movement *= 1;
    }
    y2 -= movement;
  
  
  if (z1 >= 400 || z1 <= 0) {
      movement *= -1;
    }
    z1 += movement;
  if (z2 >= 400 || z2 <= 0) {
      movement *= -1;
    }
    z2 += movement;
  
  
   
  textSize(size);
    size+= sizeDirection;
    count++;
    if(count > 5)
    {
        sizeDirection *=-1;
        count = 0;
    }
    text("JD Bennett",130,360 );
    }
