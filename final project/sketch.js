let ball;

function setup() {
  new Canvas(windowWidth, windowHeight); // if you're using p5play
  ball = new Sprite();
}

function draw() {
  background('black');
  
  // Reset velocity
  ball.vel.x = 0;
  ball.vel.y = 0;

  // Handle input
  if (kb.pressing('left')) {
    ball.vel.x = -5;
  }
  if (kb.pressing('right')) {
    ball.vel.x = 5;
  }
  if (kb.pressing('up')) {
    ball.vel.y = -5;
  }
  if (kb.pressing('down')) {
    ball.vel.y = 5;
  }

  drawSprites(); // IMPORTANT: draw all sprites
}