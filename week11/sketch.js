let shapes = [];
var x = 50;
var y = 50;
var diameter = 15;
rand = Math.floor(Math.random() * 4) + 1;
rand2 = Math.floor(Math.random() *10) + 1;

a = 100;
b = 100;
c = 300;
d = 300;

function setup() {
  createCanvas(800, 600);
}
function draw() {
  background(0);
  fill(24, 200, 29);
  // player setup
    player(x,y,diameter)
    if(keyIsDown(39))
      {
        x+=5;
      }
    if(keyIsDown(37))
      {
        x-=5;
      }
    if(keyIsDown(40))
      {
        y+=5;
      }
    if(keyIsDown(38))
      {
        y-=5;
      }
  if (x >=800){
    x= 0;
  }
  if (x<=0){
    x=800;
  }
  if (y>= 600){
    y=0;
  }
  if (y<=0){
    y=600;
  }
  //

  //first object
  fill(218, 66, 245);
 ellipse(a, b, (10*rand), (10*rand2)); 
  // Move randomly every 60 frames (~once per second). I used Chatgpt to find the framecount function
  if (frameCount % 30 === 0) {
    rando = Math.floor(Math.random() * 2) + 1;
    if (rando == 2){
      a += 10
      if(a>800){
        a=0;
      }
    }
    else{
      a -= 10
      if(a<0){
        a=800;
      }
    }
  }
  
  if (frameCount % 30 === 0) {
    rando = Math.floor(Math.random() * 2) + 1;
    if (rando == 2){
      b += 10
      if(b>800){
        b=0;
      }
    }
    else{
      b -= 10
      if(b<0){
        b=800;
      }
    }
  }
  
  //second object
  fill(145, 22, 57);
square(c, d, (10*rand2)); 
  if (frameCount % 30 === 0) {
    rando = Math.floor(Math.random() * 2) + 1;
    if (rando == 2){
      c += 10
    }
    else{
      c -= 10
    }
  }
  
  if (frameCount % 30 === 0) {
    rando = Math.floor(Math.random() * 2) + 1;
    if (rando == 2){
      d += 10
    }
    else{
      d -= 10
    }
  }

  // win box
  fill(24, 200, 29);
  square(750,550,50);
  if(x > 750 && y > 550){
  textSize(20);
  text("YOU WIN",300,300 ); 
  }

  for (let i = 0; i < shapes.length; i++) {
    let pos = shapes[i];
    fill('skyblue');
    stroke('black');
    strokeWeight(2);
    triangle(
      pos.x, pos.y - 30,
      pos.x - 25, pos.y + 20,
      pos.x + 25, pos.y + 20
    );
  }

  // you can also animate other stuff here!
}

function mousePressed() {
  shapes.push({ x: mouseX, y: mouseY });
}

function player(x,y,diameter){
  square(x,y,diameter);
    square(x,y+15,diameter);
    triangle(x+15, y, x+15, y+30, x+30, y+15);
}
