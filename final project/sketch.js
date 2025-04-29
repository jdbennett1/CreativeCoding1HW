let ball;

function setup() {
  createCanvas(windowWidth, windowHeight); // use p5.js canvas directly
  ball = new Sprite();
}

function draw() {
  background('black');

  ball.vel.x = 0;
  ball.vel.y = 0;

  if (keyIsDown(LEFT_ARROW)) {
    ball.vel.x = -5;
  }
  if (keyIsDown(RIGHT_ARROW)) {
    ball.vel.x = 5;
  }
  if (keyIsDown(UP_ARROW)) {
    ball.vel.y = -5;
  }
  if (keyIsDown(DOWN_ARROW)) {
    ball.vel.y = 5;
  }

  drawSprites();
}